import tkinter as tk
import DatabaseConfigurationWindow
import InDBSaver
import tkinter.filedialog as tkFileDialog
import SignalAcquirer
import ArduinoConfigurationWindow


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Przetwarzanie sygnałów REST API")
        self.root.geometry("500x300")
        self.initialize_buttons()
        self.initialize_menubar()

    def initialize_menubar(self):
        menubar = tk.Menu(self.root.master)
        self.root.config(menu=menubar)
        file_menu = tk.Menu(menubar)
        settings_menu = tk.Menu(menubar)
        menubar.add_cascade(label="Plik", menu=file_menu)
        file_menu.add_command(label="Wyjdź", command=self.quit_program)
        menubar.add_cascade(label="Ustawienia", menu=settings_menu)
        settings_menu.add_command(label="Konfiguracja serwera baz danych", command=self.open_database_configuration_window)
        settings_menu.add_command(label="Konfiguracja platformy pomiarowej arduino", command=self.open_arduino_configuration_window)

    def initialize_buttons(self):
        start_acquisition_button = tk.Button(self.root, text="Zacznij akwizycję", command=self.start_acquisition)
        start_acquisition_button.pack()
        stop_acquisition_button = tk.Button(self.root, text="Przerwij akwizycję", command=self.stop_acquisition)
        stop_acquisition_button.pack()
        visualize_signal_button = tk.Button(self.root, text="Przetwórz i wizualizuj", command=self.visualize)
        visualize_signal_button.pack()
        save_in_db_button = tk.Button(self.root, text="Zapisz w bazie danych", command=self.save_in_db)
        save_in_db_button.pack()
        save_on_device_button = tk.Button(self.root, text="Zapisz na urządzeniu", command=self.save_on_device)
        save_on_device_button.pack()

    def start_acquisition(self):
        self.signal_acquirer = SignalAcquirer.SignalAcquirer()
        self.signal_acquirer.acquire()

    def stop_acquisition(self):
        self.signal_acquirer.stop_acquiring()

    def visualize(self):
        pass

    def save_in_db(self):
        pass

    def save_on_device(self):
        with tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt") as filedialog:
            pass

    def open_database_configuration_window(self):
        database_configuration_window = DatabaseConfigurationWindow.DatabaseConfigurationWindow()
        database_configuration_window.run()

    def open_arduino_configuration_window(self):
        arduino_configuration_window = ArduinoConfigurationWindow.ArduinoConfigurationWindow()
        arduino_configuration_window.run()

    def quit_program(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()
