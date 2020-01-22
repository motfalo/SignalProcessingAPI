import numpy as np
import plotly.graph_objects as go
from plotly import offline
from typing import Sequence, List
from tkinter import filedialog as tkFileDialog
import pandas as pd
import CustomTextProperty
import CustomLinesProperty


class SignalVisualizer:
    @staticmethod
    def visualize_one(sig, filename, plot_title, x_axis, y_axis,
                      scale_multiplier, step,
                      custom_text_properties,
                      custom_lines_properties,
                      custom_x_axis_properties):

        samples = len(sig)
        time = np.arange(0, samples*scale_multiplier, step=step)
        trace = go.Scatter(
            x=time,
            y=sig,
            mode="lines",
            name=plot_title
        )

        layout = go.Layout()
        figure = go.Figure(data=trace, layout=layout)

        if custom_text_properties:
            x_vals = [text_property.x for text_property in custom_text_properties]
            y_vals = [text_property.y for text_property in custom_text_properties]
            text_vals = [text_property.text for text_property in custom_text_properties]
            # print(x_vals)
            # print(y_vals)
            # print(text_vals)

            figure.add_trace(go.Scatter(
                x= x_vals,
                y= y_vals,
                text=text_vals,
                mode="text"
            ))

        for line_property in custom_lines_properties:
            figure.add_shape(
                go.layout.Shape(
                    type="line",
                    x0=line_property.x1,
                    y0=line_property.y1,
                    x1=line_property.x2,
                    y1=line_property.y2,
                    line=dict(
                        width=1,
                        dash="dashdot",
                    ),
                ))

        if custom_x_axis_properties:
            text_vals = [x_axis_property.text for x_axis_property in custom_x_axis_properties]
            x_vals = [x_axis_property.x for x_axis_property in custom_x_axis_properties]

            figure.update_xaxes(
                ticktext=text_vals,
                tickvals=x_vals,
            )

        figure.update_layout(
            xaxis_title=x_axis,
            yaxis_title=y_axis,
            showlegend=False
        )

        offline.plot(figure, auto_open=True, filename=f"signals\\{filename}.html")

    @staticmethod
    def visualize_many(signals, filename_core, plot_title, x_axis, y_axis,
                       scale_multiplier, step,
                       custom_text_properties,
                       custom_lines_properties,
                        custom_x_axis_properties):
        for i, sig in enumerate(signals, 1):
            filename = f"{filename_core}{i}"
            print(filename)
            SignalVisualizer.visualize_one(sig, filename, plot_title, x_axis, y_axis,
                                           scale_multiplier, step,
                                           custom_text_properties,
                                           custom_lines_properties,
                                           custom_x_axis_properties)
