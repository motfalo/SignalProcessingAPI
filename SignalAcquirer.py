import pandas as pd
from tkinter import filedialog as tkFileDialog


class SignalAcquirer:
    @staticmethod
    def acquire_one_from_txt_file(delimiter='\n'):
        filename = tkFileDialog.askopenfilename()
        raw_signal = pd.read_csv(filename, delimiter=delimiter)
        return raw_signal.to_numpy(dtype=float)[:, 0]

    @staticmethod
    def acquire_many_from_txt_file(delimiter='\n'):
        filenames = tkFileDialog.askopenfilenames()
        raw_signals = []
        for filename in filenames:
            raw_signal = pd.read_csv(filename, delimiter=delimiter).to_numpy(dtype=float)[:, 0]
            raw_signals.append(raw_signal)
        return raw_signals
