import mysql.connector

con = mysql.connector.connect(
                host='localhost',
                database='flight_game',
                user='kasper',
                password='Monkey',
                autocommit=True,
                collation="utf8mb4_general_ci"
                )

def current_airport(code):
    sql = f"select name from airport where ident = '{code}'"
    cursor = con.cursor()
    cursor.execute(sql)
    name = cursor.fetchall()
    return name[0][0]

def gambling():
    pass

command = ""
while command != "end":
    command = input("Select command (move,gamble,trivia,end): ")
    if command == "move":
        next_airport = input("What airport do you want to go to now(ICAO): ").upper()
        airport = current_airport(next_airport)
        print(f"You are at {airport} ")
    elif command == "gamble":
        pass
