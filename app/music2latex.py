from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy import fft
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
    csv = open('results.csv', 'w')
    for i in notes:
        csv.write(str(i) + ', ')
    csv.write('\n' + str(min(notes)) + ', ' + str(max(notes)))
    csv.close()
    print(notes)
