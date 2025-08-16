# dependencies
# 1. ffmpeg
# 1. libavcodec-extra

import sys
from ffpyplayer.player import MediaPlayer
import ffmpeg

player = MediaPlayer("pipe:")

# run echo audio:
# ffmpeg -f alsa -i default -f mp3 - | python3 main.py

# pipe audio recording to stdout
# ffmpeg -f alsa -i default -f mp3 -

# set volume
# amixer -D pulse sset Master 0% 

# TODO:
# [x] Audio play
# [x] Audio record
# [ ] openAI API interaction
# [ ] wake word detection

while True:
    frame, val = player.get_frame()
    if val == "eof":
        break
