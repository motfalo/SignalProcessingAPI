import numpy as np
from scipy import signal


class SignalProcessor:
    def __init__(self, is_convert, is_med_filter, is_normalize, window_size=251, conversion_equation="sig"):
        self.is_convert: bool = is_convert
        self.is_med_filter: bool = is_med_filter
        self.is_normalize: bool = is_normalize
        self.window_size: int = window_size
        self.conversion_equation: str = conversion_equation

    def process_one(self, sig):
        if self.is_convert:
            sig = eval(self.conversion_equation)
        if self.is_med_filter:
            sig = signal.medfilt(sig, self.window_size)
        if self.is_normalize:
            min_sig = np.min(sig)
            max_sig = np.max(sig)
            sig = (sig - min_sig) / (max_sig - min_sig)
        return sig

    def process_many(self, raw_signals):
        signals = []
        for sig in raw_signals:
            sig = self.process_one(sig)
            signals.append(sig)
        return signals

    def process_many_to_one(self, raw_signals):
        signals_sum = np.zeros_like(raw_signals[0])
        result_sig = np.zeros_like(raw_signals[0])
        for sig in raw_signals:
            sig = self.process_one(sig)
            signals_sum += sig

        if self.is_normalize:
            min_sig = np.min(signals_sum)
            max_sig = np.max(signals_sum)
            result_sig =(signals_sum - min_sig) / (max_sig - min_sig)
        else:
            result_sig = signals_sum / len(raw_signals)

        return result_sig
