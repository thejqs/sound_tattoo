#!usr/bin/env python3

'''
Having used curl to download the file and ffmpeg to edit it, this script
is the last step in making a soundwave graph I can use
as the basis for the artwork
'''

import scipy.io.wavfile
import pydub
import numpy as np
import matplotlib
# sets the matplotlib backend at runtime to one that can use
# a Python virtualenv
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ORIG_VIN_FILE = 'av_files/short_vin.aac'
VIN_WAV = 'av_files/vin.wav'


def convert_to_wav(filepath):
    '''
    given a source audio file in aac format, converts it to an uncompressed wav

    args:
    string, a filepath

    returns:
    none, just leaves the output file in a predictable place
    '''
    audio_file = pydub.AudioSegment.from_file(filepath, 'aac')
    audio_file.export(VIN_WAV, format='wav')


def read_wav(filepath):
    '''
    reads the uncompressed wav file for basic data we'll need to plot the image

    args:
    string, the path to the wav file

    returns:
    a tuple, the file's bitrate and the audio data
    '''
    bitrate, audio_data = scipy.io.wavfile.read(filepath)

    return bitrate, audio_data


def plot_data(bitrate, data):
    '''
    given the file data, creates a plot and saves the resulting image

    args:
    int, the bitrate
    obj, a scipy object with the audio data

    returns:
    none; terminates with the writing out of the image file
    '''
    time = np.arange(0, float(data.shape[0]), 1) / bitrate
    # set the type of plot to use in matplotlib's near-inscrutable weirdness
    plt.figure(1)
    plt.subplot(211)
    # plot the data
    plt.plot(time, data, linewidth=0.06, alpha=0.9, color='000000')
    # label the chart
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    # bring it to life
    plt.savefig('vin.png', bbox_inches='tight')


def hi_everybody(filepath):
    '''
    runs the jewels
    runs the jewels fast
    '''
    convert_to_wav(filepath)
    bitrate, audio_data = read_wav(VIN_WAV)
    plot_data(bitrate, audio_data)


if __name__ == '__main__':
    hi_everybody(ORIG_VIN_FILE)
