# It's time for a new tattoo

It's not my first. So I wanted something a little different. Something code-related, but personal.

I'd taken the time to [learn to code](https://georgerede.wordpress.com/2017/08/23/a-writer-writes-always/) after spending years working in journalism and wanted to use it to create something special -- the basis for artwork I would be happy to wear.

I grew up listening to [Vin Scully](https://www.sbnation.com/longform/2014/6/2/5764256/vin-scully-career-retrospective-dodgers-broadcaster-profile). My parents grew up listening to Vin Scully. When I was little, I could grab my pillow and lay my head on one of the four steps leading down into the room I shared with my brother and hear him call the last few innings of whatever that night's Dodger game was. In my world, there were fewer more soothing sounds than that of Vin Scully's voice.

He retired last year after 67 seasons with the Dodgers, Brooklyn and Los Angeles. This season would be the first in almost literally the living memory of my family where Dodger games would not begin with a familiar "Hi, everybody, and a very pleasant good evening to you, wherever you may be."

Every game. Some version of that sentence. And I missed it. A lot.

So I found a source video floating around the internet -- one that contained Vin and his friendly greeting. I used `cURL` to download it, `ffmpeg` to strip out the video stream and cut it down to the subset of the audio I wanted, and then `Python 3.6` to turn that audio into something visual.

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

My goal was to make it so the whole thing could be run start to finish with one command, hence the bash script. Just running `zsh sound_file.sh` downloads the file, edits it, and calls the `Python` script to finish up all the fun.

And then we wind up with something like this:

![soundwave]

Now, a soundwave tattoo is a bit of a cliché. And I rather like a tattoo to be a collaborative process with the artist. I'm not the best visual or artistic thinker, and I know nothing about translating art-on-paper to another medium -- skin.

So I took this soundwave to [Matt "Octeel" Macri](https://www.instagram.com/octeeltattoo/) for some guidance. Looking through his drawings, I found some stylized flowers I liked. But I didn't want just any flower. So I sent him one with some significance to me: [gentiana dinarica](https://api.tela-botanica.org/img:000052354CRS.jpg). Italian distillers use its roots in traditional liqueurs I love. And it takes me back to a beautiful fall day in the Monti Sibillini looking for wild gentian while getting one of the craziest and best tours one can imagine.

It was his idea to blow up the soundwave and incorporate parts of it into striations on the flower's leaves. Which I thought was pretty cool. Thus empowered, he made this happen:

![tattoo]

And now I can carry those memories with me always, inside and out.

[soundwave]:https://raw.githubusercontent.com/thejqs/sound_tattoo/master/vin.png
[tattoo]:https://github.com/thejqs/sound_tattoo/blob/master/av_files/tattoo.jpg
