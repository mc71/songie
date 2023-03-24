import mido
from mido import Message, MidiFile, MidiTrack
import re

# Conversion from scientific pitch notation to MIDI note numbers
def spn_to_midi(spn):
    pitch_class = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
    match = re.match(r'([A-G])(\d)/(\d)', spn)
    note, octave, duration = match.groups()
    return pitch_class[note] + (int(octave) + 1) * 12, int(duration)

# Convert a list of notes in scientific pitch notation to MIDI events
def spn_to_midi_track(spn_list, track):
    for spn in spn_list:
        midi_note, duration = spn_to_midi(spn)
        track.append(Message('note_on', note=midi_note, velocity=64, time=0))
        track.append(Message('note_off', note=midi_note, velocity=64, time=duration * 240))

# Define the sections of the song
notation = {
    'Verse': [
        'C4/4', 'G4/4', 'A4/4', 'A4/4', 'G4/4', 'A4/4', 'B4/4', 'C5/2',
        'D5/4', 'C5/4', 'B4/4', 'A4/4', 'G4/4', 'A4/4', 'B4/4', 'C5/2'
    ],
    'Chorus': [
        'C5/4', 'C5/4', 'G4/4', 'A4/4', 'A4/4', 'G4/4', 'A4/4', 'B4/2',
        'C5/4', 'C5/4', 'G4/4', 'A4/4', 'A4/4', 'G4/4', 'A4/4', 'B4/2'
    ],
    'Bridge': [
        'E5/4', 'E5/4', 'F5/4', 'G5/4', 'A5/4', 'G5/4', 'F5/4', 'E5/2',
        'D5/4', 'D5/4', 'E5/4', 'F5/4', 'G5/4', 'F5/4', 'E5/4', 'D5/2'
    ]
}

# Create a new MIDI file and track
midi = MidiFile()
track = MidiTrack()
midi.tracks.append(track)

# Add the sections to the MIDI track
structure = ['Verse', 'Chorus', 'Verse', 'Bridge', 'Chorus', 'Verse', 'Bridge', 'Chorus']
for section in structure:
    spn_to_midi_track(notation[section], track)

# Save the MIDI file
midi.save('output.mid')
