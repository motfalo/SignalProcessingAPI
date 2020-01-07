import tkinter as tk
import DatabaseConfigurationWindow
import InDBSaver
import tkinter.filedialog as tkFileDialog
import SignalVisualizer
import ExternalProgramLauncher
import SignalAcquirer
import SignalProcessor
import pandas as pd
import CustomLinesProperty
import CustomTextProperty


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Przetwarzanie sygnałów API")
        self.root.geometry("400x750")
        self.initialize_buttons()
        self.initialize_menubar()
        self.initialize_processing_tools()

    def initialize_menubar(self):
        menubar = tk.Menu(self.root.master)
        self.root.config(menu=menubar)
        file_menu = tk.Menu(menubar)
        settings_menu = tk.Menu(menubar)
        menubar.add_cascade(label="Plik", menu=file_menu)
        file_menu.add_command(label="Wyjdź", command=self.quit_program)
        menubar.add_cascade(label="Ustawienia", menu=settings_menu)
        settings_menu.add_command(label="Konfiguracja serwera baz danych",
                                  command=self.open_database_configuration_window)

    def initialize_buttons(self):
        start_acquisition_button = tk.Button(self.root, text="Zacznij akwizycję", command=self.start_acquisition)
        start_acquisition_button.pack()
        process_and_visualize_signal_button = tk.Button(self.root, text="Przetwórz i wizualizuj z 1 pliku",
                                                        command=self.process_and_visualize_one)
        process_and_visualize_signal_button.pack()
        process_and_visualize_signals_button = tk.Button(self.root, text="Przetwórz i wizualizuj z wielu plików",
                                                         command=self.process_and_visualize_many)
        process_and_visualize_signals_button.pack()
        process_and_visualize_average_signal_button = tk.Button(self.root, text="Przetwórz i wizualizuj średni sygnał",
                                                                command=self.process_and_visualize_average_of_many)
        process_and_visualize_average_signal_button.pack()
        save_in_db_button = tk.Button(self.root, text="Zapisz w bazie danych", command=self.save_in_db)
        save_in_db_button.pack()

    def initialize_processing_tools(self):
        self.delimiter = tk.StringVar()
        self.signal_filename = tk.StringVar(value="signal")
        self.plot_title = tk.StringVar(value="Wykres")
        self.x_axis = tk.StringVar(value="Czas")
        self.y_axis = tk.StringVar(value="Wartości")
        self.scale_multiplier = tk.IntVar(value=1)
        self.step = tk.IntVar(value=1)
        self.is_convert = tk.BooleanVar(value=False)
        self.conversion_equation = tk.StringVar(value="sig")
        self.is_med_filter = tk.BooleanVar(value=False)
        self.window_size = tk.IntVar(value=251)
        self.is_normalize = tk.BooleanVar(value=False)
        self.is_custom_text = tk.BooleanVar(value=False)
        self.custom_text = tk.StringVar()
        self.custom_lines = tk.StringVar()
        self.signal_filename_label = tk.Label(self.root, text="Nazwa sygnału")
        self.signal_filename_label.pack()
        self.signal_filename_entry = tk.Entry(self.root, textvariable=self.signal_filename)
        self.signal_filename_entry.pack()
        self.plot_title_label = tk.Label(self.root, text="Tytuł wykresu")
        self.plot_title_label.pack()
        self.plot_title_entry = tk.Entry(self.root, textvariable=self.plot_title)
        self.plot_title_entry.pack()
        self.x_axis_label = tk.Label(self.root, text="Tytuł osi x")
        self.x_axis_label.pack()
        self.x_axis_entry = tk.Entry(self.root, textvariable=self.x_axis)
        self.x_axis_entry.pack()
        self.y_axis_label = tk.Label(self.root, text="Tytuł osi y")
        self.y_axis_label.pack()
        self.y_axis_entry = tk.Entry(self.root, textvariable=self.y_axis)
        self.y_axis_entry.pack()
        self.scale_multiplier_label = tk.Label(self.root, text="Mnożnik skali czasu")
        self.scale_multiplier_label.pack()
        self.scale_multiplier_entry = tk.Entry(self.root, textvariable=self.scale_multiplier)
        self.scale_multiplier_entry.pack()
        self.step_label = tk.Label(self.root, text="Wielkość kroku")
        self.step_label.pack()
        self.step_entry = tk.Entry(self.root, textvariable=self.step)
        self.step_entry.pack()
        self.is_convert_checkbox = tk.Checkbutton(self.root, text="Konwersja wartości", variable=self.is_convert)
        self.is_convert_checkbox.pack()
        conversion_equation_label = tk.Label(self.root, text="Działanie konwertujące")
        conversion_equation_label.pack()
        self.conversion_equation_entry = tk.Entry(self.root, textvariable=self.conversion_equation)
        self.conversion_equation_entry.pack()
        self.is_med_filter_checkbox = tk.Checkbutton(self.root, text="Filtr medianowy", variable=self.is_med_filter)
        self.is_med_filter_checkbox.pack()
        window_size_label = tk.Label(self.root, text="Wielkość okna")
        window_size_label.pack()
        self.window_size_entry = tk.Entry(self.root, textvariable=self.window_size)
        self.window_size_entry.pack()
        self.is_normalize_checkbox = tk.Checkbutton(self.root, text="Normalizacja wartości", variable=self.is_normalize)
        self.is_normalize_checkbox.pack()
        self.is_custom_text_checkbox = tk.Checkbutton(self.root, text="Dodaj tekst i linie do wykresu",
                                                      variable=self.is_custom_text)
        self.is_custom_text_checkbox.pack()
        self.custom_text_label = tk.Label(self.root, text="Format x, y, tekst;")
        self.custom_text_label.pack()
        self.custom_text_entry = tk.Entry(self.root, textvariable=self.custom_text)
        self.custom_text_entry.pack()
        self.custom_lines_label = tk.Label(self.root, text="Format x1, x2, y1, y2;")
        self.custom_lines_label.pack()
        self.custom_lines_entry = tk.Entry(self.root, textvariable=self.custom_lines)
        self.custom_lines_entry.pack()
        save_configuration_button = tk.Button(self.root, text="Zapisz konfigurację",
                                              command=self.save_processing_configuration)
        save_configuration_button.pack(side="left")
        load_configuration_button = tk.Button(self.root, text="Wczytaj konfigurację",
                                              command=self.load_processing_configuration)
        load_configuration_button.pack(side="right")

    def start_acquisition(self):
        external_program_launcher = ExternalProgramLauncher.ExternalProgramLauncher()
        external_program_launcher.run_external_program()

    def process_and_visualize_one(self):
        raw_signal = SignalAcquirer.SignalAcquirer.acquire_one_from_txt_file()
        signal_processor = SignalProcessor.SignalProcessor \
            (self.is_convert.get(), self.is_med_filter.get(), self.is_normalize.get(),
             self.window_size.get(), self.conversion_equation.get())
        sig = signal_processor.process_one(raw_signal)
        custom_lines_properties, custom_text_properties = self.get_properties()

        SignalVisualizer.SignalVisualizer.visualize_one \
            (sig, self.signal_filename.get(), self.plot_title.get(),
             self.x_axis.get(), self.y_axis.get(), self.scale_multiplier.get(), self.step.get(),
             custom_text_properties, custom_lines_properties)

    def get_properties(self):
        custom_lines_properties = []
        custom_text_properties = []
        if self.is_custom_text.get():
            custom_texts = self.custom_text.get().split(sep=';')
            for text in custom_texts:
                split_text = text.split(',')
                custom_text_property = CustomTextProperty.CustomTextProperty \
                    (split_text[0], split_text[1], split_text[2])
                custom_text_properties.append(custom_text_property)

            custom_lines = self.custom_lines.get().split(sep=';')
            for line in custom_lines:
                split_line = line.split(sep=',')
                custom_line_property = CustomLinesProperty.CustomLinesProperty \
                    (split_line[0], split_line[1], split_line[2], split_line[3])
                custom_lines_properties.append(custom_line_property)
        return custom_lines_properties, custom_text_properties

    def process_and_visualize_many(self):
        raw_signals = SignalAcquirer.SignalAcquirer.acquire_many_from_txt_file()
        signal_processor = SignalProcessor.SignalProcessor \
            (self.is_convert.get(), self.is_med_filter.get(), self.is_normalize.get(),
             self.window_size.get(), self.conversion_equation.get())
        sigs = signal_processor.process_many(raw_signals)
        if self.is_custom_text.get():
            pass

        SignalVisualizer.SignalVisualizer.visualize_many \
            (sigs, self.signal_filename.get(), self.plot_title.get(),
             self.x_axis.get(), self.y_axis.get(), self.scale_multiplier.get(), self.step.get())

    def process_and_visualize_average_of_many(self):
        raw_signals = SignalAcquirer.SignalAcquirer.acquire_many_from_txt_file()
        signal_processor = SignalProcessor.SignalProcessor \
            (self.is_convert.get(), self.is_med_filter.get(), self.is_normalize.get(),
             self.window_size.get(), self.conversion_equation.get())
        sig = signal_processor.process_many_to_one(raw_signals)
        if self.is_custom_text.get():
            pass

        SignalVisualizer.SignalVisualizer.visualize_one \
            (sig, self.signal_filename.get(), self.plot_title.get(),
             self.x_axis.get(), self.y_axis.get(), self.scale_multiplier.get(), self.step.get())

    def save_in_db(self):
        pass

    def open_database_configuration_window(self):
        database_configuration_window = DatabaseConfigurationWindow.DatabaseConfigurationWindow()
        database_configuration_window.run()

    def save_processing_configuration(self):
        configuration = {}
        configuration["signal_filename"] = self.signal_filename.get()
        configuration["plot_title"] = self.plot_title.get()
        configuration["x_axis"] = self.x_axis.get()
        configuration["y_axis"] = self.y_axis.get()
        configuration["scale_multiplier"] = self.scale_multiplier.get()
        configuration["step"] = self.step.get()
        configuration["is_convert"] = self.is_convert.get()
        configuration["conversion_equation"] = self.conversion_equation.get()
        configuration["is_med_filter"] = self.is_med_filter.get()
        configuration["window_size"] = self.window_size.get()
        configuration["is_normalize"] = self.is_normalize.get()
        index = [0]
        config_dataframe = pd.DataFrame(configuration, index=index)
        config_dataframe.to_csv("config.csv", index=False)

    def load_processing_configuration(self):
        config_filename = tkFileDialog.askopenfilename()
        config_dataframe = pd.read_csv(config_filename, index_col=False)
        configuration = config_dataframe.to_dict()

        self.signal_filename.set(configuration["signal_filename"])
        self.plot_title.set(configuration["plot_title"])
        self.x_axis.set(configuration["x_axis"])
        self.y_axis.set(configuration["y_axis"])
        self.scale_multiplier.set(configuration["scale_multiplier"])
        self.step.set(configuration["step"])
        self.is_convert.set(str(configuration["is_convert"]))
        self.conversion_equation.set(configuration["conversion_equation"])
        self.is_med_filter.set(str(configuration["is_med_filter"]))
        self.window_size.set(configuration["window_size"])
        self.is_normalize.set(str(configuration["is_normalize"]))

    def quit_program(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()
