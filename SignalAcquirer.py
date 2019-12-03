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

    # TODO or UNDO
    def acquire(self):
        self.iterator.start()
        Tv1 = self.board.get_pin(INPUT_PIN)
        H1 = self.board.get_pin(DIGITAL_PIN)
        time.sleep(1.0)
        # voltage
        while True:
            print(Tv1.read())
            time.sleep(0.5)

    def stop_acquiring(self):
        self.board.exit()
