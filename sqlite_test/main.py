import sqlite3

def show_all_tables(table):

    connection = sqlite3.connect(table)

    sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""

    cursor = connection.cursor()

    cursor.execute(sql_query)

    print(cursor.fetchall())

    connection.close()

def gta():

    connection = sqlite3.connect("gta.db")
    cursor = connection.cursor()
    sql_query = """CREATE TABLE gta (release_year integer, release_name text, city text);"""
    cursor.execute(sql_query)

    release_list = [
        (1997, "Grand Theft Auto", "State of New Guernsey"),
        (1999, "Grand Theft Auto 2", "Anywhere, USA"),
        (2001, "Grand Theft Auto III", "Liberty City"),
        (2004, "Grand Theft Auto: Vice City", "Vice City"),
        (2004, "Grand Theft Auto: San Andreas", "State of San Andreas"),
        (2004, "Grand Theft Auto IV", "Liberty City"),
        (2008, "Grand Theft Auto V", "Los Santos")
    ]

    cursor.executemany("INSERT INTO gta values (?,?,?);", release_list)

    connection.commit()

    connection.close()

def print_all_rows():
    connection = sqlite3.connect("gta.db")
    cursor = connection.cursor()
    for row in cursor.execute("select * from gta"):
        print(row)
    connection.close()

def print_all_one_row():
    connection = sqlite3.connect("gta.db")
    cursor = connection.cursor()
    cursor.execute("select * from gta where city=:c", {"c": "Liberty City"})
    gta_search = cursor.fetchall()
    print(gta_search)
    connection.close()

# gta()
# show_all_tables("gta.db")
# print_all_rows()
print_all_one_row()


print
print('-----')
print('TEST')
print('-----')