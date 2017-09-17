#!usr/bin/env python3

import scipy.io.wavfile
import pydub
import numpy as np
import matplotlib
# sets the matplotlib backend at runtime to one that can use
# a Python virtualenv
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ORIG_VIN_FILE = 'short_vin.aac'
VIN_WAV = 'vin.wav'


def convert_to_wav(filepath):
    audio_file = pydub.AudioSegment.from_file(filepath, 'aac')
    audio_file.export(VIN_WAV, format='wav')


def read_wav(filepath):
    bitrate, audio_data = scipy.io.wavfile.read(filepath)

    return bitrate, audio_data


def plot_data(bitrate, data):
    time = np.arange(0, float(data.shape[0]), 1) / bitrate
    plt.figure(1)
    plt.subplot(211)
    plt.plot(time, data, linewidth=0.06, alpha=0.9, color='000000')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.savefig('vin.png', bbox_inches='tight')


def hi_everybody(filepath):
    convert_to_wav(filepath)
    bitrate, audio_data = read_wav(VIN_WAV)
    plot_data(bitrate, audio_data)


if __name__ == '__main__':
    hi_everybody(ORIG_VIN_FILE)
