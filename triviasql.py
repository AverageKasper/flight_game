import mysql.connector
import random
from utilities import anim_print
from utilities import conn

def trivia_game():
    try:
        
        cursor = conn.cursor()

        #creating the table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS trivia_questions (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            question VARCHAR(255) NOT NULL,
                            option1 VARCHAR(255) NOT NULL,
                            option2 VARCHAR(255) NOT NULL,
                            option3 VARCHAR(255) NOT NULL,
                            option4 VARCHAR(255) NOT NULL,
                            correct_option INT NOT NULL
                        )''')
        conn.commit()

        # Step 2: Clear the trivia_questions table to avoid duplicate data
        cursor.execute("TRUNCATE TABLE trivia_questions")

        # Step 3: Check if trivia questions already exist and insert new ones if necessary
        cursor.execute("SELECT COUNT(*) FROM trivia_questions")
        count = cursor.fetchone()[0]

        
            # Sample trivia questions
        questions = [
            ("What is the capital of France?", "Berlin", "London", "Paris", "Madrid", 3),
            ("Who wrote 'Hamlet'?", "Mark Twain", "William Shakespeare", "Charles Dickens", "Leo Tolstoy", 2),
            ("What is the largest planet in our solar system?", "Earth", "Jupiter", "Saturn", "Mars", 2),
            ("What is the chemical symbol for water?", "H20", "H2O2", "HO2", "H2O", 4),
            ("Which year did World War I begin?", "1914", "1918", "1939", "1945", 1),
            ("Which year did world war 2 end?", "1963", "1945", "1933", "1943", 2),
            ("What is the name of the volcano located near Tokyo, Japan called?", "Mount Fuji", "Mount Yari", "Mount Kita", "Mount Aino", 1),
            ("Who sang the title song for the latest Bond film, No Time to Die?", "Adele", "Sam Smith", "Billie Eilish", "Michael Jackson", 3),
            ("Which flies a green, white, and orange (in that order) tricolor flag? ", "ireland", "Ivory Coast", "Italy", "India", 1),
            ("What company makes the Xperia model of smartphone?", "samsung", "sony", "Nokia", "Apple", 2),
            ("Which city is home to the Brandenburg Gate?", "Vienna", "Zurich", "Berlin", "Frankfurt", 3),
            ("Which of the following is NOT a fruit?", "Rhubarb", "Tomatoes", "Avocados", "Potatoes", 1),
            ("Where was the first example of paper money used?", "China", "Turkey", "Greece", "Japan", 1),
            ("Who is generally considered the inventor of the motor car?", "Henry Ford", "Karl Benz", "Henry M. Leland", "Gottlieb Daimler", 2),
            ("If you were looking at Iguazu Falls, on what continent would you be?", "Asia", "Africa", "South America", "North America", 3),
            ("What number was the Apollo mission that successfully put a man on the moon for the first time in human history?", "Apollo 12", "Apollo 11", "Apollo 13", "Apollo 9", 2),
            ("Which of the following languages has the longest alphabet?", "Greek", "Russian", "Arabic", "Chinese", 2),
            ("Who was the lead singer of the band The Who?", "Roger Daltrey", "Don Henley", "Robert Plant", "Bob Geldof", 1),
            ("What spirit is used in making a Tom Collins?", "Vodka", "Rum", "Gin", "tequila", 3),
            ("The fear of insects is known as what?", "Entomophobia", "Arachnophobia", "Ailurophobia", "Arachibutyrophobia", 1),
            ("What was the name of the Franco-British supersonic commercial plane that operated from 1976-2003?", "Accord", "Mirage", "Concorde", "The Voyager", 3),
            ("Which horoscope sign is a fish?", "Seahorse", "Aquarius", "Cancer", "Pisces", 4),
            ("What is the largest US state (by landmass)?", "Texas", "California", "Florida", "Alaska", 4),
            ("Which app has the most total users?", "Tik Tok", "Snapchat", "Instagram", "Facebook", 3),
            ("Which Game of Thrones character is known as the Young Wolf?", "Robb Stark", "Arya Stark", "Sansa Stark", "Bran Stark", 1),
            ("What city hosted the 2002 Olympic Games?", "Tokyo", "Paris", "Beijing", "Sydney", 4),
            ("How many plays do people (generally) believe that Shakespeare wrote?", "47", "27", "57", "37", 4),
            ]

            # Insert trivia questions into the 'trivia_questions' table
        cursor.executemany('''INSERT INTO trivia_questions (question, option1, option2, option3, option4, correct_option)
                                  VALUES (%s, %s, %s, %s, %s, %s)''', questions)

        conn.commit()
            
        

        cursor.execute("SELECT * FROM trivia_questions")
        questions = cursor.fetchall()

        if not questions:
            print("No trivia questions found in the database.")
            return

        # mixi mixi the questions
        random.shuffle(questions)

        score = 0
        total_questions = len(questions)

        # Set a limit on questions asked
        question_limit = min(3, total_questions)  # Change the number 3 to your desired limit

        # Loop through each question and present to the player
        for i, question in enumerate(questions[:question_limit], start=1):
            q_id, question_text, option1, option2, option3, option4, correct_option = question
            anim_print(f"\nQuestion {i}: {question_text}")
            anim_print(f"\n1. {option1}")
            anim_print(f"\n2. {option2}")
            anim_print(f"\n3. {option3}")
            anim_print(f"\n4. {option4}")

            # Get the user's answer
            user_answer = input(anim_print("\nYour answer (1-4) or 'q' to quit: "))

            if user_answer.lower() == 'q':
                anim_print("You chose to quit the game.")
                break

            # Validate the answer and update the score
            if user_answer.isdigit() and int(user_answer) == correct_option:
                anim_print("Correct!")
                score += 1
            else:
                anim_print(f"Wrong! The correct answer was option {correct_option}.")

        # print the final score
        anim_print(f"\nYour final score is {score} out of {i} questions.")
    except mysql.connector.Error as err:
        anim_print(f"Error: {err}")
    finally:
        conn.close()
        return score
