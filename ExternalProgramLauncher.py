import subprocess
from tkinter import filedialog as tkFileDialog


class ExternalProgramLauncher:
    def __init__(self):
        self.path = self.get_path_to_external_program()

    @staticmethod
    def get_path_to_external_program():
        path = tkFileDialog.askopenfilename()
        return path

    def run_external_program(self):
        subprocess.call(self.path, shell=True)