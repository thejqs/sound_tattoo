#!/usr/bin/env zsh

# grabs the target video file
curl https://mediadownloads.mlb.com/mlbam/2015/09/02/mlbtv_439507583_1800K.mp4 --output av_files/vin.mp4
# copies only the audio stream
ffmpeg -i av_files/vin.mp4 -vn -acodec copy av_files/vin.aac
# edits it down to the snippet we need -- four seconds beginning
# at the sixth second
ffmpeg -ss 6 -t 4 -i av_files/vin.aac av_files/short_vin.aac

# fires up the Python script to turn that snippet into an image
~/Development/virtualenvs/sound_tattoo/bin/python3 sound_graph.py
