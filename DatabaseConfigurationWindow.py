import tkinter as tk
import pymysql.cursors
from tkinter import filedialog as tkFileDialog
import pandas as pd


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
        tablename_label = tk.Label(self.root, text="Tabela")
        tablename_label.pack(padx=20, pady=20)
        self.tablename_entry = tk.Entry(self.root)
        self.tablename_entry.pack()
        save_configuration_button = tk.Button(self.root, text="Zapisz", command=self.save)
        save_configuration_button.pack(side="left")
        exit_button = tk.Button(self.root, text="Wyjdź", command=self.quit_window)
        exit_button.pack(side="right")

    def quit_window(self):
        self.root.destroy()

    def save(self):
        config_dataframe = pd.DataFrame(
            {
                "host": [self.host_entry.get()],
                "db": [self.database_entry.get()],
                "port": [self.port_entry.get()],
                "user": [self.login_entry.get()],
                "password": [self.password_entry.get()],
                "tablename": [self.tablename_entry.get()]
            }
        )
        # filepath = tkFileDialog.asksaveasfilename(defaultextension=".txt")
        config_dataframe.to_csv("database_config.txt", sep='|', header=True, index=False)
        self.root.destroy()

    def run(self):
        self.root.mainloop()
