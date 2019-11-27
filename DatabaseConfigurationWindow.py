import tkinter as tk
import pymysql.cursors
from tkinter import filedialog as tkFileDialog


class DatabaseConfigurationWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Konfiguracja serwera baz danych")
        self.root.geometry("550x500")
        self.set_widgets()

    def set_widgets(self):
        host_label = tk.Label(self.root, text="Host")
        host_label.pack(padx=20, pady=20)
        self.host_entry = tk.Entry(self.root)
        self.host_entry.pack()
        database_label = tk.Label(self.root, text="Baza danych")
        database_label.pack(padx=20, pady=20)
        self.database_entry = tk.Entry(self.root)
        self.database_entry.pack()
        port_label = tk.Label(self.root, text="Port")
        port_label.pack(padx=20, pady=20)
        self.port_entry = tk.Entry(self.root)
        self.port_entry.pack()
        login_label = tk.Label(self.root, text="Login")
        login_label.pack(padx=20, pady=20)
        self.login_entry = tk.Entry(self.root)
        self.login_entry.pack()
        password_label = tk.Label(self.root, text="Hasło")
        password_label.pack(padx=20, pady=20)
        self.password_entry = tk.Entry(self.root)
        self.password_entry.pack()
        save_configuration_button = tk.Button(self.root, text="Zapisz", command=self.save)
        save_configuration_button.pack(side="left")
        exit_button = tk.Button(self.root, text="Wyjdź", command=self.quit_window)
        exit_button.pack(side="right")

    def quit_window(self):
        self.root.destroy()

    def save(self):
        with tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt") as filedialog:
            filedialog.write(self.host_entry.get() + '\n')
            filedialog.write(self.database_entry.get() + '\n')
            filedialog.write(self.port_entry.get() + '\n')
            filedialog.write(self.login_entry.get() + '\n')
            filedialog.write(self.password_entry.get())
        self.root.destroy()

    def run(self):
        self.root.mainloop()
