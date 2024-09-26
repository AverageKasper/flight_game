import mysql.connector
import random

# Step 1: Connect to the existing flight_game database and create the trivia table
def setup_database():
    conn = mysql.connector.connect(
        host='localhost',
        database='flight_game',
        user='root',
        password='K1rahV1!',
        autocommit=True,
        collation="utf8mb4_general_ci"
    )
    cursor = conn.cursor()

    # Create the 'trivia_questions' table if it doesn't exist
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
    conn.close()

# Step 2: Add trivia questions to the 'trivia_questions' table
def insert_questions():
    conn = mysql.connector.connect(
        host='localhost',
        database='flight_game',
        user='root',
        password='K1rahV1!',
        autocommit=True,
        collation="utf8mb4_general_ci"
    )
    cursor = conn.cursor()

    # Sample trivia questions
    questions = [
        ("What is the capital of France?", "Berlin", "London", "Paris", "Madrid", 3),
        ("Who wrote 'Hamlet'?", "Mark Twain", "William Shakespeare", "Charles Dickens", "Leo Tolstoy", 2),
        ("What is the largest planet in our solar system?", "Earth", "Jupiter", "Saturn", "Mars", 2),
        ("What is the chemical symbol for water?", "H20", "H2O2", "HO2", "H2O", 4),
        ("Which year did World War I begin?", "1914", "1918", "1939", "1945", 1)
    ]

    # Insert the trivia questions into the 'trivia_questions' table
    cursor.executemany('''INSERT INTO trivia_questions (question, option1, option2, option3, option4, correct_option)
                          VALUES (%s, %s, %s, %s, %s, %s)''', questions)

    conn.commit()
    conn.close()

# Step 3: Retrieve questions from the 'trivia_questions' table and run the trivia game
def run_trivia_game():
    conn = mysql.connector.connect(
        host='localhost',
        database='flight_game',
        user='root',
        password='K1rahV1!',
        autocommit=True,
        collation="utf8mb4_general_ci"
    )
    cursor = conn.cursor()

    # Retrieve all trivia questions
    cursor.execute("SELECT * FROM trivia_questions")
    questions = cursor.fetchall()

    # Shuffle the questions for randomness
    random.shuffle(questions)

    score = 0
    total_questions = len(questions)

    # Loop through each question and present to the player
    for question in questions:
        q_id, question_text, option1, option2, option3, option4, correct_option = question
        print(f"\n{question_text}")
        print(f"1. {option1}")
        print(f"2. {option2}")
        print(f"3. {option3}")
        print(f"4. {option4}")

        # Get the user's answer
        user_answer = input("Your answer (1-4): ")

        # Validate the answer and update the score
        if user_answer.isdigit() and int(user_answer) == correct_option:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was option {correct_option}.")

    # Display the final score
    print(f"\nYour final score is {score} out of {total_questions}.")
    conn.close()

# Main function to set up the database and run the game
def main():
    setup_database()

    insert_questions()

    run_trivia_game()

if __name__ == "__main__":
    main()
