import random

# A list containing a dictionary for each MCQ
quiz_data = [
    {
        "question": "Which is the largest river in the world?",
        "options": ["Nile", "Amazon", "Mississippi", "Yangtze"],
        "answer": "Amazon"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": ["Atlantic", "Pacific", "Indian", "Arctic"],
        "answer": "Pacific"
    },
    {
        "question": "Which is the largest desert in the world?",
        "options": ["Sahara", "Gobi", "Kalahari", "Antarctica"],
        "answer": "Antarctica"
    },
    {
        "question": "Which is the largest mountain in the world?",
        "options": ["Everest", "K2", "Kangchenjunga", "Lhotse"],
        "answer": "Everest"
    },
    {
        "question": "Which is the largest island in the world?",
        "options": ["Greenland", "New Guinea", "Borneo", "Madagascar"],
        "answer": "Greenland"
    }   
]

# Initialize game state variables
score = 0
has_lifeline = True
prizes = [1000, 5000, 10000, 50000, 100000]
money_won = 0

print("Welcome to KBC!")
print("Answer these questions to win cash prizes.")
print("Type A, B, C, or D to answer. Type 50 to use the 50-50 lifeline.")
print("--------------------------------------------")

for i in range(len(quiz_data)):
    q = quiz_data[i]
    print(f"\nQuestion {i + 1}: {q['question']}")
    
    # Print the options
    print(f"A. {q['options'][0]}")
    print(f"B. {q['options'][1]}")
    print(f"C. {q['options'][2]}")
    print(f"D. {q['options'][3]}")
    
    # Get user input
    user_choice = input("Your answer (A/B/C/D or 50): ").strip().upper()
    
    # Check if they want to use 50-50 lifeline
    if user_choice == "50":
        if has_lifeline:
            has_lifeline = False
            print("\n--- 50-50 Lifeline! ---")
            
            correct_ans = q['answer']
            options = q['options']
            
            # Find the correct letter
            correct_letter = ""
            if options[0] == correct_ans: correct_letter = "A"
            elif options[1] == correct_ans: correct_letter = "B"
            elif options[2] == correct_ans: correct_letter = "C"
            elif options[3] == correct_ans: correct_letter = "D"
            
            # Pick one random wrong option to show alongside correct
            wrong_letters = [x for x in ["A", "B", "C", "D"] if x != correct_letter]
            random_wrong_letter = random.choice(wrong_letters)
            
            # Display remaining options in order
            print("Remaining options:")
            for letter in ["A", "B", "C", "D"]:
                if letter == correct_letter or letter == random_wrong_letter:
                    idx = ord(letter) - ord('A')
                    print(f"{letter}. {options[idx]}")
            
            # Ask again
            while True:
                user_choice = input(f"Enter choice ({correct_letter} or {random_wrong_letter}): ").strip().upper()
                if user_choice in [correct_letter, random_wrong_letter]:
                    break
                print("Invalid input. Choose from the remaining options.")
        else:
            print("You already used your 50-50 lifeline!")
            while True:
                user_choice = input("Your answer (A/B/C/D): ").strip().upper()
                if user_choice in ["A", "B", "C", "D"]:
                    break
                print("Please enter A, B, C, or D.")
                
    # Validate selection
    while user_choice not in ["A", "B", "C", "D"]:
        user_choice = input("Invalid choice! Enter A, B, C, or D: ").strip().upper()
        
    # Map selection back to option value
    selected_option = ""
    if user_choice == "A": selected_option = q['options'][0]
    elif user_choice == "B": selected_option = q['options'][1]
    elif user_choice == "C": selected_option = q['options'][2]
    elif user_choice == "D": selected_option = q['options'][3]

    # Check answer
    if selected_option == q['answer']:
        score += 1
        money_won = prizes[i]
        print(f"Correct! You won Rs. {money_won:,}")
    else:
        print(f"Wrong answer! The correct answer was: {q['answer']}")
        print(f"Game over! You scored {score}/5 and take home Rs. {money_won:,}")
        break
else:
    print("\n========================================")
    print("CONGRATULATIONS! You answered all questions correctly!")
    print(f"You won the grand prize of Rs. {money_won:,}!")
    print(f"Final Score: {score}/5")
    print("========================================")

