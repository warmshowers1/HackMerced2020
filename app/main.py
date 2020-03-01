from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy import fft
import os
import numpy as np


def get_freq(data, duration):
    maximum = 100
    minimum = 20
    f_data = fft(data)[int(minimum * duration): int(1000 * duration)]
    return np.where(f_data == np.amax(f_data))[0] / duration + minimum

def wav2freq(filename: str, time_interval: int, graph=False):
    """
    time_interval should be the time (in seconds) of one note
    """
    fs, data = wavfile.read(filename)
    duration = len(data) / fs
    l_data = [i for i in data]

    int_time = int(time_interval * fs)

    freq_data = [get_freq(l_data[cursor:cursor+int_time], int_time / fs) for cursor in range(0, len(l_data), int_time)]

    if graph:
        plt.scatter(range(len(freq_data)), freq_data)
        plt.show()

    return freq_data

def freq2note(freq: int):
    semitone = 2 ** (1/12)
    return int(np.log(freq / 440) / np.log(semitone))

if __name__ == '__main__':
    freqs = wav2freq("drumspiano.wav", 0.25)
    notes = [freq2note(f) for f in freqs]

song = []
#notes = ["a", "b", "c", "d", "e", "f", "g", "r"]
#notes = [["a", "aes"],["b", "bes"],["c", "cis"],["d", "des"],["e", "ees"], ["f", "fis"], ["g", "ges"]]
letters = ("a", "aes", "b", "bes", "c", "d", "des", "e", "ees", "f", "g", "ges")
# look to the letters array for reference as to which index correlates to which type of note.
amounts = [0 for i in range(12)]

for i in notes:
    b = i % 12
    song.append(letters[b])
    #if i >= -53 and i <= -44:
    #    song.append(letters[b])# + ",,, ")
    #if i > -44 and i <= -34:
    #    song.append(letters[b])# + ",, ")
    #if i > -34 and i <= -24:
    #    song.append(letters[b])# + ", ")
    #if i > -24 and i <= -14:
    #    song.append(letters[b])
    #if i > -14 and i <= -4:
    #    song.append(letters[b])# + "\' ")
    #if i > -4 and i <= 6:
    #    song.append(letters[b])# + "\'\' ")
    #if i > 6 and i <= 15:
    #    song.append(letters[b])# + "\'\'\' ")
    amounts[b] += 1

# These two indicies don't have relevant flat accidentals
amounts.remove(amounts[4])
amounts.remove(amounts[9])
key = 0
for i in range((len(amounts) - 2), -1, -2):
    if amounts[i+1] > amounts[i]:
        break
    else:
        key += 1

begin = """\\documentclass[a4paper]{article}
\\usepackage{lilypond}
\\usepackage[margin=0.25in]{geometry}
\\addtolength{\\textheight}{1in}

\\header{
    title = \"Drums and Piano\"
    composer = \"Bill from Craigslist\"
}

\\begin{document}
\\begin{lilypond}
"""
middle_start = """ \\relative c''{
\\clef \"treble\"
\\time 3/4
"""
middle = """}
{\\clef \"treble\"
\\time 3/4
"""
end = """   }
\\end{lilypond}
\\end{document}"""

'''
print(begin)
for i in range(3, len(song), 4):
    print(song[i-3] + " " + song[i-2] + " " + song[i-1] + " " + song[i] + "\n")
    if len(song) % 4 == 3:
        print(song[-3] + " " + song[-2] + " " + song[-1] + "\n")
    if len(song) % 4 == 2:
        print(song[-2] + " " + song[-1] + "\n")
    if len(song) % 4 == 1:
        print(song[-1] + "\n")
print(end)
'''

f = open("prod/song.tex","w+")
def key_finder(key: int):
    if key == 0:
        f.write("\\key des \major\n")
    elif key == 1:
        f.write("\\key aes \major\n")
    elif key == 2:
        f.write("\\key ees \major\n")
    elif key == 3:                 
        f.write("\\key ees \major\n")
    elif key == 4:
        f.write("\\key f \major\n")
    elif key == 5:               
        f.write("\\key c \major\n")

f.write(begin)
key_finder(key)

f.write(middle_start)
key_finder(key)
arr = [2, (len(song) / 3), 2*(len(song) / 3), len(song)]
for j in range(int(arr[0]),int(arr[1]) + 1, 3):
    f.write(song[j-2] + " " + song[j-1] + " " + song[j] + " | ")
if len(song) % 3 == 2:
    f.write(song[-2] + " " + song[-1] + " | ")
if len(song) % 3 == 1:
    f.write(song[-1] + " | ")
f.write(middle)
key_finder(key)
for j in range(int(arr[1]),int(arr[2]) + 1, 3):
    f.write(song[j-2] + " " + song[j-1] + " " + song[j] + " | ")
if len(song) % 3 == 2:
    f.write(song[-2] + " " + song[-1] + " | ")
if len(song) % 3 == 1:
    f.write(song[-1] + " | ")
f.write(middle)
key_finder(key)
for j in range(int(arr[2]), int(arr[3]), 3):
    f.write(song[j-2] + " " + song[j-1] + " " + song[j] + " | ")
if len(song) % 3 == 2:
    f.write(song[-2] + " " + song[-1] + " | ")
if len(song) % 3 == 1:
    f.write(song[-1] + " | ")

f.write(end)

f.close()

#os.system('lilypond-book --output=out --pdf prod/song.tex;')
