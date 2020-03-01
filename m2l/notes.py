
rawBytes = [114, 114, 114]
song = []
#notes = ["a", "b", "c", "d", "e", "f", "g", "r"]
octaves = ["\'", "," ]
notes = [["a", "aes"],["b", "bes"],["c", "cis"],["d", "des"],["e", "ees"], ["f", "fis"], ["g", "ges"]]
#c and f are sharps, all other notes are flats
amounts = [[0, 0],[0, 0],[0, 0],[0, 0],[0, 0], [0, 0], [0, 0]]

def lowOct3:

def lowOct2:

def lowOct1:

def regOct:

def highOct1:

def highOct2:

def highOct3:


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
