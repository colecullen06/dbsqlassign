import sqlite3


CREATE_FOOD_MENU_TABLE = "CREATE TABLE IF NOT EXISTS food_menu (id INTEGER PRIMARY KEY, name TEXT, food_type TEXT, size TEXT, cost Integer);"

INSERT_FOOD = "INSERT INTO food_menu (name, food_type, size, cost) VAlUES (?, ?, ?, ?)"

GET_ALL_FOOD = "SELECT * FROM food_menu;"
GET_FOOD_BY_NAME = " SELECT * FROM food_menu WHERE name = ?;"

GET_FOOD_COST = "SELECT * FROM food_menu WHERE name = ?;"
GET_FOOD_SIZE = "SELECT * FROM food_menu WHERE size = ?;"
GET_CHEAPEST_OPTION = """
SELECT * FROM food_menu
WHERE food_type = ?
ORDER BY cost ASC
LIMIT 1; """

GET_EXPENSIVE_OPTION = """
SELECT * FROM food_menu
WHERE food_type = ?
ORDER BY cost DESC
LIMIT 1; """


GET_MENU_BY_ASC = """
SELECT * FROM food_menu
ORDER BY cost ASC; """


GET_MENU_BY_DESC = """
SELECT * FROM food_menu
ORDER BY cost DESC; """


DELETE_THE_DB = "DELETE FROM food_menu;"


DELETE_FROM_DB = """
DELETE FROM food_menu
WHERE name LIKE ?;
"""


def connect():
    return sqlite3.connect("data.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_FOOD_MENU_TABLE)


def add_product(connection, name, food_type, size, cost):
    with connection:
        connection.execute(INSERT_FOOD, (name, food_type, size, cost))


def get_all_items(connection):
    with connection:
        return connection.execute(GET_ALL_FOOD).fetchall()


def get_food_by_name(connection, name):
    with connection:
        return connection.execute(GET_FOOD_BY_NAME, (name,)).fetchall()


def get_food_cost(connection, name):
    with connection:
        return connection.execute(GET_FOOD_COST, (name, )).fetchone()


def get_food_size(connection, name):
    with connection:
        return connection.execute(GET_FOOD_SIZE, (name, )).fetchone()


def get_cheapest_option(connection, food_type):
    with connection:
        return connection.execute(GET_CHEAPEST_OPTION, (food_type, )).fetchone()


def get_expensive_option(connection, food_type,):
    with connection:
        return connection.execute(GET_EXPENSIVE_OPTION, (food_type, )).fetchone()


def get_menu_by_asc(connection):
    with connection:
        return connection.execute(GET_MENU_BY_ASC).fetchall()


def get_menu_by_desc(connection):
    with connection:
        return connection.execute(GET_MENU_BY_DESC).fetchall()


def delete_from_db(connection, name):
    with connection:
        all_items = connection.execute(GET_ALL_FOOD).fetchall()
        names_in_db= []
        for food in all_items:
            names_in_db.append(food[1])
        if name in names_in_db:
            print("Item deleted")
            return connection.execute(DELETE_FROM_DB, (name, )).fetchall()
        else:
            print(f"{name} is NOT in the database... why are you trying to delete it????")




def clear_db(connection, ):
    with connection:
        return connection.execute(DELETE_THE_DB, ).fetchall()

