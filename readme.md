I used chatGPT to create a song, it would only output in scientific pitch notation (at the time of creation), I needed a way to use it so I created this script.

1. To create a MIDI file from scientific pitch notation we use the the mido library in Python.
2. First install mido with `pip install mido`
3. Modify the songie.py script with your scientific pitch notation
4. Then run `python songie.py` to convert the notation to a MIDI file. This script creates a MIDI file called output.mid with the provided structure and scientific pitch notation. You can then play the MIDI file with any compatible software or further edit it with a digital audio workstation.

I've included an example output.mid file, and a quick garage band file using this midi file.
