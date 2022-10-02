import math
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import time


do, re, mi, fa, sol, la, si, do_s, re_s, fa_s, sol_s, la_s = \
    261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 277.18, 311.13, 369.99, 415.30, 466.16
duration = 0.5
t_gen, x_gen, f_gen, my_gen = [], [], [], []


def play(note):
    """
    Play a note for a duration in seconds at a given frequency [note].
    :param note:
    :return: None
    """
    fs = 8000
    points_nfft = 1024
    t_arr = []
    x = []

    for t in range(int(duration * fs)):
        t_arr.append(t / fs)
        t_gen.append(t / fs)
        x.append(math.sin(2 * math.pi * note * t / fs))
        x_gen.append(math.sin(2 * math.pi * note * t / fs))

    # Take the FFT and populate with 0s to match the length of the signal
    y = np.fft.fft(x, points_nfft)
    y = y[1: points_nfft // 2]

    # Espectral potential
    my = np.abs(y) / (points_nfft / 2)
    my_gen.extend(my)

    # Frequential vector
    f_list = []
    for i in range(points_nfft // 2 - 1):
        f_list.append(i * fs / points_nfft)
        f_gen.append(i * fs / points_nfft)

    sd.play(x, fs)
    sd.wait()


def receive_play():
    """
    Receive an array input from the user and play the corresponding notes in the array
    :return: None
    """
    while True:
        notes = input("Enter a note: ").split(" ")
        freq = []

        for i in notes:
            if i == "do":
                play(do)
                freq.append(do)
            elif i == "re":
                play(re)
                freq.append(re)
            elif i == "mi":
                play(mi)
                freq.append(mi)
            elif i == "fa":
                play(fa)
                freq.append(fa)
            elif i == "sol":
                play(sol)
                freq.append(sol)
            elif i == "la":
                play(la)
                freq.append(la)
            elif i == "si":
                play(si)
                freq.append(si)
            elif i == "do_s":
                play(do_s)
                freq.append(do_s)
            elif i == "re_s":
                play(re_s)
                freq.append(re_s)
            elif i == "fa_s":
                play(fa_s)
                freq.append(fa_s)
            elif i == "sol_s":
                play(sol_s)
                freq.append(sol_s)
            elif i == "la_s":
                play(la_s)
                freq.append(la_s)
            elif i == "_":
                time.sleep(duration)
            else:
                print("Invalid note")

        plot_notes()


def plot_notes():
    """
    Plot the array of notes by frequency and power
    :param freq: 
    :param notes: array of notes
    :return: None
    """
    # Plot the signal
    plt.plot(t_gen, x_gen)
    plt.title("Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.show()

    # Plot the FFT
    plt.plot(f_gen, my_gen)
    plt.title("FFT")
    plt.xlabel("Frequency")
    plt.ylabel("Potential")
    plt.show()


def main():
    """
    Main function to run the program
    :return: None
    """
    receive_play()


if __name__ == "__main__":
    main()


# Twinkle Twinkle Little Star
# do do sol sol la la sol _ fa fa mi mi re re do _ sol sol fa fa mi mi re _ sol sol fa fa mi mi re
