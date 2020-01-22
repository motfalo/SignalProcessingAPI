import tkinter as tk
from tkinter import filedialog as tkFileDialog
from pymysql import cursors
import pandas as pd
from pymysql import connect


class InDBSaver:
    def __init__(self):
        # self.host = host
        # self.database = database
        # self.port = port
        # self.login = login
        # self.password = password
        self.get_connection_and_tablename_from_txt_file()

    def get_connection_and_tablename_from_txt_file(self):
        database_config_filename = tkFileDialog.askopenfilename()
        database_config_dataframe = pd.read_csv(database_config_filename, sep='|')
        self.connection = connect(
            host=database_config_dataframe["host"][0],
            user=database_config_dataframe["user"][0],
            password=database_config_dataframe["password"][0],
            db=database_config_dataframe["db"][0]
        )
        self.tablename = database_config_dataframe["tablename"][0]

    def store_signal_image(self):
        try:
            with self.connection.cursor as cursor:
                image_path = tkFileDialog.askopenfilename()
                binary_image = self.convert_to_binary_data(image_path)
                query = """INSERT INTO Signals VALUES %s"""
                cursor.execute(query, binary_image)
                self.connection.commit()
        except Exception:
            print(Exception)

    def convert_to_binary_data(self, filename):
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
