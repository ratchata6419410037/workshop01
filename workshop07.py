def bingo_game(guess_number):
    target_number = 25

    if guess_number == target_number:
        print("Correct, You are the winner")
    else:
        print("Not Correct !!!")

# Input the guessed number
user_guess = int(input("ป้อนตัวเลขที่ต้องการทาย: "))

# Check the guessed number
bingo_game(user_guess)
