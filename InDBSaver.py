import tkinter as tk
from tkinter import filedialog as tkFileDialog
import pymysql.cursors


class InDBSaver:
    def __init__(self, connection, table_name):
        # self.host = host
        # self.database = database
        # self.port = port
        # self.login = login
        # self.password = password
        self.connection = connection

    # TODO
    def store_signal(self, signal):
        try:
            with self.connection.cursor as cursor:
                # for value in signal:
                query = """INSERT INTO %s VALUES (%s)""" % signal
                cursor.execute(query)
                self.connection.commit()
        except Exception:
            print(Exception)
