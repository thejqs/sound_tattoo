# It's time for a new tattoo

It's not my first. So I wanted something a little different. Something code-related, but personal.

I'd taken the time to [learn code](https://georgerede.wordpress.com/2017/08/23/a-writer-writes-always/) after spending years working in journalism and wanted to use it to create something special -- the basis for artwork I would be happy to wear.

I grew up listening to [Vin Scully](https://www.sbnation.com/longform/2014/6/2/5764256/vin-scully-career-retrospective-dodgers-broadcaster-profile). My parents grew up listening to Vin Scully. When I was little, I could grab my pillow and lay my head on one of the four steps leading down into the room I shared with my brother and hear him call the last few innings of whatever that night's Dodger game was. In my world, there were fewer more soothing sounds than that of Vin Scully's voice.

He retired last year after 67 seasons with the Dodgers, Brooklyn and Los Angeles. This season would be the first in almost literally the living memory of my family where Dodger games would not begin with a familiar "Hi, everybody, and a very pleasant good evening to you, wherever you may be."

Every game. Some version of that sentence. And I missed it

So found a source video floating around the internet -- one that contained Vin and his friendly greeting. I used `cURL` to download it, `ffmpeg` to strip out the video stream and cut it down to the subset of the auio I wanted, and then Python to turn that audio into something visual.

```python
def hi_everybody(filepath):
    '''
    runs the jewels
    runs the jewels fast
    '''
    convert_to_wav(filepath)
    bitrate, audio_data = read_wav(VIN_WAV)
    plot_data(bitrate, audio_data)
```

And then we wind up with something like this:

![soundwave]

Some Sundays are more fun than other Sundays.

[soundwave]:https://raw.githubusercontent.com/thejqs/sound_tattoo/master/vin.png 

