from pyfirmata import Arduino, util
import time

# UNDO in future
PORT_NAME = "COM3"
INPUT_PIN = "a:0:i"
DIGITAL_PIN = "d:3:p"


class SignalAcquirer:
    def __init__(self):
        self.board = Arduino(PORT_NAME)
        self.iterator = util.Iterator(self.board)

    def acquire(self):
        self.iterator.start()
        Tv1 = self.board.get_pin(INPUT_PIN)
        H1 = self.board.get_pin(DIGITAL_PIN)
        time.sleep(1.0)
        # voltage
        # print(Tv1.read()*5000.0)

    def stop_acquiring(self):
        self.board.exit()