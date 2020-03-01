
rawBytes = [-17, -12, -22, -34, 10, 2, -6, 0]
song = []
#notes = ["a", "b", "c", "d", "e", "f", "g", "r"]
#notes = [["a", "aes"],["b", "bes"],["c", "cis"],["d", "des"],["e", "ees"], ["f", "fis"], ["g", "ges"]]
notes = ["a", "aes", "b", "bes", "c", "d", "des", "e", "ees" "f", "g", "ges"]
#c and f are sharps, all other notes are flats
amounts = [[0, 0],[0, 0],[0, 0],[0, 0],[0, 0], [0, 0], [0, 0]]

for i in rawBytes:
    if i >= -53 and i <= -44:
        song.append(notes[i % 12] + ",,, ")
    if i > -44 and i <= -34:
        song.append(notes[i % 12] + ",,")
    if i > -34 and i <= -24:
        song.append(notes[i % 12] + ",")
    if i > -24 and i <= -14:
        song.append(notes[i % 12])
    if i > -14 and i <= -4:
        song.append(notes[i % 12] + "\' ")
    if i > -4 and i <= 6:
        song.append(notes[i % 12] + "\'\' ")
    if i > 6 and i <= 15:
        song.append(notes[i % 12] + "\'\'\' ")
        
begin = """\\documentclass[a4paper]{article}
\\usepackage{lilypond}

\\begin{document}
\\begin{lilypond}
\\relative c'' {\n"""
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
