import time

def quiz():
    score = 0

    print("🎮 Welcome to the Python Quiz! 🏆")
    time.sleep(1)

    # Question 1
    print("\n1. What keyword is used to define a function in Python?")
    print("a) func\nb) define\nc) def\nd) function")
    answer = input("Your answer: ").strip().lower()
    if answer == "c":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect! The correct answer is c) def.")

    # Question 2
    print("\n2. Which of these is used to output text in Python?")
    print("a) print()\nb) output()\nc) echo()\nd) write()")
    answer = input("Your answer: ").strip().lower()
    if answer == "a":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect! The correct answer is a) print().")

    # Question 3
    print("\n3. What is the correct file extension for Python files?")
    print("a) .py\nb) .python\nc) .pyt\nd) .pt")
    answer = input("Your answer: ").strip().lower()
    if answer == "a":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect! The correct answer is a) .py.")

    # Display final score
    print(f"\n🏁 Quiz Over! Your final score: {score}/3")

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        quiz()
    else:
        print("Thanks for playing! 🎉")

# Start the quiz
quiz()
