import random


def trivia_game():
    # List of 100 questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
            "answer": "A"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A) Charles Dickens", "B) J.K. Rowling", "C) William Shakespeare", "D) Leo Tolstoy"],
            "answer": "C"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
            "answer": "B"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["A) Oxygen", "B) Gold", "C) Silver", "D) Iron"],
            "answer": "A"
        },
        {
            "question": "What is the tallest mountain in the world?",
            "options": ["A) K2", "B) Mount Everest", "C) Mount Kilimanjaro", "D) Mount Elbrus"],
            "answer": "B"
        },
        {
            "question": "In which year did World War I begin?",
            "options": ["A) 1914", "B) 1918", "C) 1939", "D) 1945"],
            "answer": "A"
        },
        {
            "question": "What is the speed of light?",
            "options": ["A) 300,000 km/s", "B) 150,000 km/s", "C) 450,000 km/s", "D) 600,000 km/s"],
            "answer": "A"
        },
        {
            "question": "Which country hosted the 2016 Summer Olympics?",
            "options": ["A) China", "B) Brazil", "C) UK", "D) USA"],
            "answer": "B"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A) Leonardo da Vinci", "B) Michelangelo", "C) Pablo Picasso", "D) Vincent van Gogh"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Venus", "B) Mars", "C) Mercury", "D) Saturn"],
            "answer": "B"
        },

    ]




    # Randomly select 3 questions from the pool of 100
    selected_questions = random.sample(questions, 3)

    score = 0  # Keep track of the player's score

    # Iterate over each selected question
    for i, question in enumerate(selected_questions, 1):
        print(f"Question {i}: {question['question']}")
        for option in question["options"]:
            print(option)

        # Get the user's answer
        user_answer = input("Your answer (A/B/C/D): ").upper()

        # Validate user input
        while user_answer not in ['A', 'B', 'C', 'D']:
            user_answer = input("Invalid input! Please enter A, B, C, or D: ").upper()

        # Check if the answer is correct
        if user_answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}\n")

    # Display the final score
    print(f"Your final score: {score}/3")
    if score == 3:
        print("Congratulations! You got all the answers right!")
    elif score > 1:
        print("Good job! You scored above average.")
    else:
        print("Better luck next time!")
    return score


