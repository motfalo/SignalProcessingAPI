import tkinter as tk
from tkinter import filedialog as tkFileDialog
from pymysql import cursors
import pandas as pd


class InDBSaver:
    def __init__(self, connection, table_name):
        # self.host = host
        # self.database = database
        # self.port = port
        # self.login = login
        # self.password = password
        self.connection = self.get_connection_from_txt_file()

    def get_connection_from_txt_file(self):
        # connection =
        # return connection
        pass

    # TODO
    def store_signal(self, sig_html):
        try:
            with self.connection.cursor as cursor:
                # for value in signal:
                query = """INSERT INTO %s VALUES (%s)""" % sig_html
                cursor.execute(query)
                self.connection.commit()
        except Exception:
            print(Exception)
