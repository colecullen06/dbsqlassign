import database

MENU_PROMPT = """ - - Menu App - -

Please choose one of these options

1) Add a new menu item
2) See all menu items
3) Find an item by name
4) See an item's type
5) See an item's cost
6) See which option is cheapest
7) See which option is most expensive
8) Sort menu by price: Ascending
9) sort menu by price: Descending
10) Empty DB
11) Exit

Your Selection: """


def menu():
    connection = database.connect()
    database.create_tables(connection)
    while (user_input := input(MENU_PROMPT)) != "11":
        if user_input == "1":
            prompt_add_new_item(connection)
        elif user_input == "2":
            prompt_see_all_items(connection)
        elif user_input == "3":
            prompt_get_food_by_name(connection)
        elif user_input == "4":
            prompt_get_food_type(connection)
        elif user_input == "5":
            prompt_find_food_cost(connection)
        elif user_input == "6":
            prompt_get_cheapest_option(connection)
        elif user_input == "7":
            prompt_get_expensive_option(connection)
        elif user_input == "8":
            prompt_get_price_asc(connection)
        elif user_input == "9":
            prompt_get_price_desc(connection)
        elif user_input == "10":
            prompt_clear_db(connection)
        else:
            print("Invalid input, please try again")


def prompt_add_new_item(connection):
    name = input("Enter item name: ")
    food_type = input("Enter item type (sandwich, side, poutine, etc.): ")
    size = input("Enter item size (small, medium, large): ")
    cost = int(input("How much does the item cost: "))

    database.add_product(connection, name, food_type, size, cost)


def prompt_see_all_items(connection):
    food_menu = database.get_all_items(connection)

    for food in food_menu:
        print(f"{food[1]}  {food[2]}  {food[3]}  ${food[4]}")


def prompt_get_food_by_name(connection):
    name = input("Enter item name to find: ")
    food_menu = database.get_food_by_name(connection, name)

    for food in food_menu:
        print(f"{food[1]}, {food[3]} {food[2]}, ${food[4]}")


def prompt_find_food_cost(connection):
    name = input("Enter item name to find the cost of: ")
    food_menu = database.get_food_by_name(connection, name)

    for food in food_menu:
        print(f" The {name} costs ${food[4]}")


def prompt_get_food_type(connection):
    name = input("Enter an item to find the type of: ")
    food_menu = database.get_food_by_name(connection, name)

    for food in food_menu:
        print(f" {name}'s type is: {food[2]}")


def prompt_get_cheapest_option(connection):
    f_type = input("Enter a type to get the cheapest version of: ")
    cheapest_option = database.get_cheapest_option(connection, f_type,)
    print(f"The cheapest option of type {f_type} is the {cheapest_option[3]} {cheapest_option[1]} {cheapest_option[2]}, which costs ${cheapest_option[4]}.")


def prompt_get_expensive_option(connection):
    f_type = input("Enter a type to get the most expensive version of: ")
    expensive_option = database.get_expensive_option(connection, f_type,)
    print(f"The most expensive option of type {f_type} is the {expensive_option[3]} {expensive_option[1]} {expensive_option[2]}, which costs ${expensive_option[4]}.")


def prompt_get_price_asc(connection):
    menu_by_asc = database.get_menu_by_asc(connection)

    for food in menu_by_asc:
        print(f"{food[1]}  {food[2]}  {food[3]}  ${food[4]}")


def prompt_get_price_desc(connection):
    menu_by_desc = database.get_menu_by_desc(connection)

    for food in menu_by_desc:
        print(f"{food[1]}  {food[2]}  {food[3]}  ${food[4]}")


# I researched this, and got it to work with your help
def prompt_clear_db(connection):
    decision = input("Are you sure that you want to clear the DB (1 - yes, 2 - no): ")
    if decision == "1":
        database.clear_db(connection)
    else:
        pass


# def sort_by_price_asc(connection):
#    name =

menu()

