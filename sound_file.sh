#!/usr/bin/env zsh

curl https://mediadownloads.mlb.com/mlbam/2015/09/02/mlbtv_439507583_1800K.mp4 --output vin.mp4
ffmpeg -i vin.mp4 -vn -acodec copy vin.aac
ffmpeg -ss 6 -t 4 -i vin.aac short_vin.aac

~/Development/virtualenvs/sound_tattoo/bin/python3 sound_graph.py
