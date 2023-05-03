import musicalbeeps
import random
import argparse


SCALES = {
    "IONIAN": [0, 2, 4, 5, 7, 9, 11],
    "DORIAN": [0, 2, 3, 5, 7, 9, 10],
    "PHRYGIAN": [0, 1, 3, 5, 7, 8, 10],
    "PHRYGIAN DOMINANT": [0, 1, 4, 5, 7, 8, 10],
    "LYDIAN": [0, 2, 4, 6, 7, 9, 11],
    "MIXOLYDIAN": [0, 2, 4, 5, 9, 9, 10],
    "AEOLIAN": [0, 2, 3, 5, 7, 8, 10],
    "HARMONIC MINOR SCALE": [0, 2, 3, 5, 7, 8, 11],
    "LOCRIAN": [0, 1, 3, 5, 6, 8, 10],    
    "PANTATONIC": [0, 2, 4, 7, 9],
    "HEXATONIC": [0, 3, 5, 6, 7, 10],
    "HEPTATONIC": [0, 2, 3, 5, 6, 9, 10]
}

CHORDS = {
    # TRIADS
    "MAJOR": ["1", "3", "5"],
    "MINOR": ["1", "b3", "5"],
    "DIMINISHED": ["1", "b3", "b5"],
    "AUGMENTED": ["1", "3", "#5"],

    # 7ths    
    "MAJOR 7th": ["1", "3", "5", "7"],
    "MINOR 7th": ["1", "b3", "5", "b7"],
    "DOMINANT 7th": ["1", "3", "5", "b7"],
    "HALF-DIMINISHED 7th": ["1", "b3", "b5", "b7"],
    "DIMINISHED 7th": ["1", "b3", "b5", "bb7"],
    "MINOR-MAJOR 7th": ["1", "b3", "5", "7"],
    "AUGMENTED 7th": ["1", "3", "#5", "7"],
    "AUGMENTED DOMINANT 7th": ["1", "3", "#5", "b7"],
     
    # 9ths
    "MAJOR 9th": ["1", "3", "5", "7", "9"],
    "MINOR 9th": ["1", "b3", "5", "b7", "9"],
    "DOMINANT 9th": ["1", "3", "5", "b7", "9"],

    # 11ths
    "MAJOR 11th": ["1", "3", "5", "7", "9", "11"],
    "MINOR 11th": ["1", "b3", "5", "b7", "9", "11"],
    "DOMINANT 11th": ["1", "3", "5", "b7", "9", "11"],

    # 13ths
    "MAJOR 13th": ["1", "3", "5", "7", "9", "11", "13"],
    "MINOR 13th": ["1", "b3", "5", "b7", "9", "11", "13"],
    "DOMINANT 13th": ["1", "3", "5", "b7", "9", "11", "13"],
    
}

CHROMATIC_SCALE = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def relative_pitch_to_absolute_note(key_idx: int, mode: list):
    return [CHROMATIC_SCALE[(key_idx+interval) % 12] for interval in mode]

def generate_riff(avail_pitches: list, total_secs: int):
    player = musicalbeeps.Player(volume = 0.3, mute_output = False)

    num_notes = random.randint(10, 50)
    riff = [random.choice(avail_pitches) for _ in range(num_notes)]
    lengths = [random.randint(0, 50) for _ in range(num_notes)]
    lengths = [max(0.4, val / sum(lengths) * total_secs) for val in lengths]

    print("[RIFF]")
    print(riff)
    print("[Length]")
    print(lengths)
    for (note, length) in zip(riff, lengths):
        player.play_note(note, length)

# TODO
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sec", type=int, default=8)
parser.add_argument("-b", "--bar", type=int, default=4)
parser.add_argument("-k", "--key", type=str, default="C")
parser.add_argument("-m", "--mode", type=str, default="IONIAN")
args = parser.parse_args()

if args.mode not in SCALES:
    raise RuntimeError(f"[ERROR] Invalid mode {args.mode} specified. Supported modes are: {SCALES.keys()}")
if args.key not in CHROMATIC_SCALE:
    raise RuntimeError(f"[ERROR] Invalid key {args.key} specified. Supported modes are: {CHROMATIC_SCALE}")

key_idx = CHROMATIC_SCALE.index(args.key)
avail_pitchs_in_mode = relative_pitch_to_absolute_note(key_idx, SCALES[args.mode]) + ["pause"]




sec_per_bar = args.sec / args.bar



player = musicalbeeps.Player(volume = 0.3, mute_output = False)

OCTAVE = range(3, 5)

generate_riff(avail_pitchs_in_mode, args.sec)



