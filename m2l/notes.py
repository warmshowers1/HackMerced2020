
rawBytes = [114, 114, 114]
song = []
#notes = ["a", "b", "c", "d", "e", "f", "g", "r"]
octaves = ["\'", "," ]
notes = [["a", "aes", "ais"],["b", "bes", "bis"],["c", "ces", "cis"],["d", "des", "dis"],["e", "ees", "eis"], ["f", "fes", "fis"], ["g", "ges", "gis"]]
amounts = [[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0], [0, 0, 0], [0, 0, 0]]

i
def lowOct3(note):
    if note <= 5 :
        song.append(notes[0] + octaves[1] + octaves[1] + octaves[1])
    elif note <= 10:
        song.append(notes[1] + octaves[1] + octaves[1] + octaves[1])
    elif note <= 15:
        song.append(notes[2] + octaves[1] + octaves[1] + octaves[1])
    elif note <= 20:
        song.append(notes[3] + octaves[1] + octaves[1] + octaves[1])
    elif note <= 25:
        song.append(notes[4] + octaves[1] + octaves[1] + octaves[1])
    elif note <= 30:
        song.append(notes[5] + octaves[1] + octaves[1] + octaves[1])
    else:
        song.append(notes[6] + octaves[1] + octaves[1] + octaves[1])

def lowOct2(note):
    if note <= 41:
        song.append(notes[0] + octaves[1] + octaves[1])
    elif note <= 46:
        song.append(notes[1] + octaves[1] + octaves[1])
    elif note <= 51:
        song.append(notes[2] + octaves[1] + octaves[1])
    elif note <= 56:
        song.append(notes[3] + octaves[1] + octaves[1])
    elif note <= 61:
        song.append(notes[4] + octaves[1] + octaves[1])
    elif note <= 66:
        song.append(notes[5] + octaves[1] + octaves[1])
    else:
        song.append(notes[6] + octaves[1] + octaves[1])


def lowOct1(note):
    if note <= 78:
        song.append(notes[0] + octaves[1])
    elif note <= 83:
        song.append(notes[1] + octaves[1])
    elif note <= 88:
        song.append(notes[2] + octaves[1])
    elif note <= 94:
        song.append(notes[3] + octaves[1])
    elif note <= 99:
        song.append(notes[4] + octaves[1])
    elif note <= 104:
        song.append(notes[5] + octaves[1])
    else:
        song.append(notes[6] + octaves[1])


def regOct(note):
    if note <= 115:
        song.append(notes[0])
    elif note <= 120:
        song.append(notes[1])
    elif note <= 125:
        song.append(notes[2])
    elif note <= 130:
        song.append(notes[3])
    elif note <= 135:
        song.append(notes[4])
    elif note <= 140:
        song.append(notes[5])
    else:
        song.append(notes[6])


def highOct1(note):
    if note <= 151:
        song.append(notes[0] + octaves[0])
    elif note <= 156:
        song.append(notes[1] + octaves[0])
    elif note <= 162:
        song.append(notes[2] + octaves[0])
    elif note <= 167:
        song.append(notes[3] + octaves[0])
    elif note <= 172:
        song.append(notes[4] + octaves[0])
    elif note <= 177:
        song.append(notes[5] + octaves[0])
    else:
        song.append(notes[6] + octaves[0])


def highOct2(note):
    if note <= 188:
        song.append(notes[0] + octaves[0] + octaves[0])
    elif note <= 194:
        song.append(notes[1] + octaves[0] + octaves[0])
    elif note <= 199:
        song.append(notes[2] + octaves[0] + octaves[0])
    elif note <= 204:
        song.append(notes[3] + octaves[0] + octaves[0])
    elif note <= 209:
        song.append(notes[4] + octaves[0] + octaves[0])
    elif note <= 214:
        song.append(notes[5] + octaves[0] + octaves[0])
    else:
        song.append(notes[6] + octaves[0] + octaves[0])

def highOct3(note):
    if note <= 225:
        song.append(notes[0] + octaves[0] + octaves[0] + octaves[0])
    elif note <= 230:
        song.append(notes[1] + octaves[0] + octaves[0] + octaves[0])
    elif note <= 235:
        song.append(notes[2] + octaves[0] + octaves[0] + octaves[0])
    elif note <= 240:
        song.append(notes[3] + octaves[0] + octaves[0] + octaves[0])
    elif note <= 245:
        song.append(notes[4] + octaves[0] + octaves[0] + octaves[0])
    elif note <= 250:
        song.append(notes[5] + octaves[0] + octaves[0] + octaves[0])
    else:
        song.append(notes[6] + octaves[0] + octaves[0] + octaves[0])




for i in rawBytes:
    if i == 0:
        song.append(notes[-1])
    if i > 0 and i <= 36:
        lowOct3(i)
    if i > 36 and i <= 73:
        lowOct2(i)
    if i > 73 and i <= 109:
        lowOct1(i)
    if i > 109 and i <= 146:
        regOct(i)
    if i > 146 and i <= 183:
        highOct1(i)
    if i > 183 and i <= 219:
        highOct2(i)
    if i > 219 and i <= 256:
        highOct3(i)
        
begin = """\\documentclass[a4paper]{article}
\\usepackage{lilypond}

\\begin{document}
\\begin{lilypond}
\\relative c'' {\n"""
end = """   }
\\end{lilypond}
\\end{document}"""

f = open("prod/song.tex","w+")

f.write(begin)
for i in range(3, len(song), 4):
    f.write(song[i-3] + " " + song[i-2] + " " + song[i-1] + " " + song[i] + "\n")
if len(song) % 4 == 3:
    f.write(song[-3] + " " + song[-2] + " " + song[-1] + "\n")
if len(song) % 4 == 2:
    f.write(song[-2] + " " + song[-1] + "\n")
if len(song) % 4 == 1:
    f.write(song[-1] + "\n")
f.write(end)

f.close()
