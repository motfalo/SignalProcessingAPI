from tkinter import filedialog as tkFileDialog
import tkinter as tk
# TODO

class ArduinoConfigurationWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Konfiguracja arduino przy użyciu PyFirmata")
        self.root.geometry("550x500")
        self.set_widgets()

    def set_widgets(self):
        port_label = tk.Label(self.root, text="Nazwa portu")
        port_label.pack(padx=20, pady=20)
        self.port_entry = tk.Entry(self.root)
        self.port_entry.pack()
        input_pin_label = tk.Label(self.root, text="Pin wejściowy")
        input_pin_label.pack(padx=20, pady=20)
        self.input_pin_entry = tk.Entry(self.root)
        self.input_pin_entry.pack()
        digital_pin_label = tk.Label(self.root, text="Pin cyfrowy")
        digital_pin_label.pack(padx=20, pady=20)
        self.digital_pin_entry = tk.Entry(self.root)
        self.digital_pin_entry.pack()
        save_configuration_button = tk.Button(self.root, text="Zapisz", command=self.save)
        save_configuration_button.pack(side="left")
        exit_button = tk.Button(self.root, text="Wyjdź", command=self.quit_window)
        exit_button.pack(side="right")

    def save(self):
        with tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt") as filedialog:
            filedialog.write(self.port_entry.get() + '\n')
            filedialog.write(self.input_pin_entry.get() + '\n')
            filedialog.write(self.digital_pin_entry.get() + '\n')
        self.root.destroy()

    def quit_window(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()