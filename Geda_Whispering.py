import re
import time
import socketserver
import sys
import io

# Read in flag from file
with open('flag.txt', 'r') as f:
    flag = f.read().strip()

secret_intro = '''Geda legacy awakened, echoes of the past,
In the circle of wisdom, traditions hold fast.
Guardians of honor, with courage we steer,
Within these ancient verses, your flag draws near.
''' + flag + '\n'

song_geda = secret_intro + '''
[REFRAIN]
We are the keepers of Geda, voices in the gale,
Ancient rulings and timeless tales.
Every challenge embraced, our honor reclaimed,
The spirit of tradition forever untamed.
CROWD (Join the chant!);
RETURN

[VERSE1]
In the realm of ancestors where history is alive,
Ethiopian hearts with the strength to survive.
The Geda system echoes with wisdom profound,
Decipher these verses where your flag is found.
With unity and valor, traverse this test,
Reveal the hidden truth, prove you are the best.

REFRAIN;

Through the corridors of time and lore so deep,
Every clue is a promise, a secret to keep.
Within the ancient council, let truth be your guide,
Geda calls the brave—let honor reside.

REFRAIN;

In these coded lines, find the sacred decree,
Where Geda’s spirit shines with clarity.
Reverse each challenge, let the old ways chime,
Unlock the flag, in rhythm and time.

REFRAIN;

END;
'''

MAX_LINES = 100  #this is max_lines

def reader(song, startLabel, iinput, iprint):
    lip = 0
    start = 0
    refrain = 0
    refrain_return = 0
    finished = False

    # Split the song into individual lines i add some thing
    song_lines = song.splitlines()

    # Identify the start label, refrain marker, and RETURN line index
    for i in range(len(song_lines)):
        if song_lines[i] == startLabel:
            start = i + 1
        elif song_lines[i] == '[REFRAIN]':
            refrain = i + 1
        elif song_lines[i] == 'RETURN':
            refrain_return = i












    line_count = 0
    lip = start
    while not finished and line_count < MAX_LINES:
        line_count += 1
        for line in song_lines[lip].split(';'):
            if line == '' and song_lines[lip] != '':
                continue
            if line == 'REFRAIN':
                # Set a jump marker for the refrain
                song_lines[refrain_return] = 'RETURN ' + str(lip + 1)
                lip = refrain
            elif re.match(r"CROWD.*", line):
                crowd = iinput('Crowd: ')
                song_lines[lip] = 'Crowd: ' + crowd
                lip += 1
            elif re.match(r"RETURN [0-9]+", line):
                lip = int(line.split()[1])
            elif line == 'END':
                finished = True
            else:
                iprint(line)
                time.sleep(0.5)
                lip += 1

reader(song_geda, '[VERSE1]')


















