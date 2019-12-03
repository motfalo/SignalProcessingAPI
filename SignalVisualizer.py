import numpy as np
import plotly.graph_objects as go
from plotly import offline
from tkinter import filedialog as tkFileDialog


class SignalVisualizer:
    def __init__(self):
        self.y = self.get_signal_values_from_file()
        self.samples_number = len(self.y)
        # self.x = np.linspace(0, 5*self.samples_number, self.samples_number)
        self.x = np.arange(0, 5*self.samples_number, step=5)

    @staticmethod
    def get_signal_values_from_file():
        with tkFileDialog.askopenfile(mode='r') as filedialog:
            values = filedialog.readlines()
            print(len(values))
            return values

    def visualize(self):
        trace = go.Scatter(
            x=self.x,
            y=self.y,
            mode="markers+lines",
            name="Wykres zależności GSR od czasu"
        )
        layout = go.Layout()
        figure = go.Figure(data=trace, layout=layout)
        offline.plot(figure, auto_open=True, filename="signal.html")

