def quiz_game():

    questions = ("1. How many elements are in the periodic table?: ",
            "2. Which animal lays the largest eggs?: ",
            "3. What is the most abundant gas in the Earth's atmosphere?: ",
            "4. How many bones are in the human body?: ",
            "5. Which planet in the solar system is the hottest?: ") # Tuple of questions

    options = (("A. 116", "B. 117", "C. 118", "D. 119"),
            ("A. Whale", "B. Giant Squid", "C. Wholly Mammoth", "D. Ostrich"),
            ("A. Nitrogen", "B. Hydrogen", "C. Carbon-Dioxide", "D. Oxygen"),
            ("A. 116", "B. 117", "C. 118", "D. 119"),
            ("A. Mercury", "B. Venus", "C. Jupiter", "D. Mars")) # 2-D tuple(a tuple containing tuples)

    answers = ("C", "D", "A", "B", "B") # Tuple of correct answers

    guesses = [] # A list of guesses
    score = 0  # Keeping track of score
    question_num = 0  # For moving along the questions

    print("***************************QUIZ GAME***************************")

    for question in questions:  # Iterate over question elements in tuple using the IN keyword
        print()
        print(question)
        for option in options[question_num]:  # Add index operator to access option at index of question_num
            print(option)

        guess = input("Enter A, B, C, D: ").upper()
        guesses.append(guess)  # Append guess into the list of guesses
        if guess == answers[question_num]:  # If guess equal to answer at the index of the question_num
            score = score + 1  # Increment score by 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")
        question_num = question_num + 1  # Increment question num by 1 to move onto the next question_num

    print("*******************RESULTS*************************")
    print("Answers: ", end=" ")
    for answer in answers:  # Same as for x in answers: print(x)
        print(answer, end=" ")
    print()

    print("Guesses: ", end=" ")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)  # Formula to calculate percentage
    print(f"Your score is: {score}%")
    return None

quiz_game()