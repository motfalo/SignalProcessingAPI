import numpy as np
import plotly.graph_objects as go
from plotly import offline
from tkinter import filedialog as tkFileDialog
import pandas as pd


class SignalVisualizer:
    # def __init__(self):
    #     pass
        # self.y = self.get_signal_values_from_file()
        # self.samples_number = len(self.y)
        # self.x = np.arange(0, 5*self.samples_number, step=5)

    # @staticmethod
    # def get_signal_values_from_file():
    #     filename = tkFileDialog.askopenfilename()
    #     values = pd.read_csv(filename, delimiter='\n')
    #     return values.to_numpy(dtype=int)[:, 0]
    @staticmethod
    def visualize_one(sig, filename, plot_title, x_axis, y_axis, scale_multiplier, step):
        samples = len(sig)
        time = np.arange(0, samples*scale_multiplier, step=step)
        trace = go.Scatter(
            x=time,
            y=sig,
            # mode="markers+lines",
            mode="lines",
            name=plot_title
        )
        layout = go.Layout()
        figure = go.Figure(data=trace, layout=layout)
        offline.plot(figure, auto_open=True, filename=f"signals\\{filename}.html")

    @staticmethod
    def visualize_many(signals, filename_core, plot_title, x_axis, y_axis, scale_multiplier, step):
        for i, sig in enumerate(signals, 1):
            filename = f"{filename_core}{i}"
            print(filename)
            SignalVisualizer.visualize_one(sig, filename, plot_title, x_axis, y_axis, scale_multiplier, step)
