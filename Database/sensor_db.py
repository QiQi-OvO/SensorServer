
import sqlite3
import datetime

from Database.contract import DataEntry

#DB_NAME = 'senor2.db'
class DataTable:
    @classmethod
    def create_table(cls):
        """
        创建/连接到数据库
        :return:
        """
        conn = sqlite3.connect('senor2.db')
        cursor = conn.cursor()
        cursor.execute(
            f"CREATE TABLE {DataEntry.TABLE_NAME} ("
            f"{DataEntry.COLUMN_DATE} TEXT NOT NULL, "
            f"{DataEntry.COLUMN_TIME} TEXT NOT NULL, "
            f"{DataEntry.COLUMN_LIGHT} Double NOT NULL, "
            f"{DataEntry.COLUMN_MAGNETIC} Double NOT NULL, "
            f"{DataEntry.COLUMN_TEMP} Double NOT NULL); "
        )
        cursor.close()
        conn.close()
    @classmethod
    def insert(cls,light,temp,magnetic):
        """
        从手机端发送过来的数据进行插入
        :return:
        """
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        time = datetime.datetime.now().strftime('%H-%M')
        conn = sqlite3.connect('senor2.db')
        cursor = conn.cursor()
        sql = (
            f"INSERT INTO {DataEntry.TABLE_NAME} "
            f"({DataEntry.COLUMN_DATE}, {DataEntry.COLUMN_TIME},{DataEntry.COLUMN_LIGHT}, "
            f"{DataEntry.COLUMN_MAGNETIC}, {DataEntry.COLUMN_TEMP}) "
            f"VALUES ('{date}', '{time}', '{light}', '{magnetic}','{temp}');"
        )
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()
    @classmethod
    def query_all(cls):
        """

        :return:
        """
        conn = sqlite3.connect('senor2.db')
        cursor = conn.cursor()
        sql = (
            f"SELECT * FROM {DataEntry.TABLE_NAME} "
        )
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        conn.close()
        if not res:
            return None
        return res

if __name__ == "__main__":
    print(DataTable.query_all()[0][1])
    #pass