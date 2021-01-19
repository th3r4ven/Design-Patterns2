from pymysql import install_as_MySQLdb
install_as_MySQLdb()
import MySQLdb


def do_connection():
    return MySQLdb.connect(
        host="localhost",
        user="root",
        passwd='',
        db='intern01'
    )
