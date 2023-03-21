

import time
print("\n Welcome to the play game\n")
time.sleep(0.5)
name = input("Enter your name: ")
time.sleep(0.5)
start = input("Press The Enter To Select a Game: ")  # to start a game
time.sleep(0.5)
games_opt = print("Number Guessing Game[1]\n\nHangman[2]\n\nRock,Paper and Scissor[3]\n") # choose a game
game_num = int(input("Enter A Game number"))  # game name
time.sleep(0.5)
print("Hello " + name + "! All the Best!\n")
if game_num == 1:
    input1 = print(input("Press Enter Button To Start A Game")) # enter for start
    print(" You Have 5 Chances")  # number of chances
    chance = 5
    count = 0
    import random
    winning_num = random.randint(0, 100)  # wining number
    num_guess = int(input('GUESS A NUMBER(1 to 100):'))
    game_over = False
    while not game_over:
        for i in range(1, chance + 1):
            count = count + 1
            if winning_num == num_guess:
                print(f"COnGRATULATIONS!YOU WON\n You guessed number in {count} times")
                game_over = True
                break
            elif num_guess < winning_num:
                print("You guessed the LOW VALUE")
                print("==========================")
                num_guess = int(input("Guess Again"))
                break
            elif num_guess > winning_num:
                print("y\You guessed the HIGH")
                print("===========================")
                num_guess = int(input("Guess Again"))
                break
        if count == chance and num_guess != winning_num:
            print("GAME OVER YOU LOSS!")
elif game_num == 3:
    start = input("Press Enter Button To Start")
    print("YOU HAVE 5 CHANCES")
    user_count = 0
    comp_count = 0
    n = 5
    for i in range(1,n+1):
        import random
        options = ('rock', 'paper', 'scissor')
        computer = random.choice(options)
        print("==============================================")
        user = input("ENTER A CHOICE(rock,paper and scissor): ")

        while user not in options:
            user = input(" ENTER A CHOICE AGAIN : ")

        print("computer: " + computer)
        print("user: " + user)
        if computer == user:
            print("Its a Tie!")
        elif computer == "rock" and user == "paper":
            print("YOU WIN!")
            user_count = user_count+1
        elif computer == "paper" and user == "rock":
            print("YOU LOSS!")
            comp_count = comp_count+1
        elif computer == "rock" and user == "scissor":
            print("YOU LOSS")
            comp_count = comp_count + 1
        elif computer == "scissor" and user == "rock":
            print("YOU WIN!")
            user_count = user_count + 1
        elif computer == "scissor" and user == "paper":
            print("YOU LOSS")
            comp_count = comp_count + 1
        else:
            print("YOU WIN!")
            user_count = user_count + 1

    print("GAME OVER")
    print(f"YOUR SCORE: {user_count}")
    print(f"computer score: {comp_count}")
    if comp_count > user_count:
        print('computer win')
    elif comp_count == user_count:
        print("IT'S A TIE!!")
    else:
            print("CONGRATULATIONS!! YOU WIN THE GAME")
else:
    import random
    from hangman import hangman_parts
    print('WELLCOME! TO HANGMAN GAME')
    time.sleep(0.5)
    start = input("PRESS ENTER BUTTON TO START A GAME")
    time.sleep(0.5)
    print("CHOOSE A GENER: ")
    print("===============================")
    options = print("COUNTRIES NAME[1]\n\nMOVIES[2]\n\nFOOD NAMES[3]\n\nFLOWER NAME[4]")
    choice =int(input("Enter a option: "))
    if choice == 1:
        words = ['Afghanistan', 'Antarctica', 'Argentina', 'Australia', 'Austria','Bahamas',
              'Belgium', 'Belize', 'Canada', 'Chile', 'China', 'India', 'Japan', 'America', 'South Korea',
               'France', 'Poland', 'Russia''']
        word = random.choice(words)

        total_chances = 7
        guessed_word = "_"*len(word)
        while total_chances !=0:
            print("WORD: ", guessed_word)
            print("===========================")
            letter = input("Guess a letter: ").lower()
            if letter in word:
                for index in range(len(word)):
                    if word[index] == letter:
                        guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]

                if guessed_word == word :
                    print("CONGRATULATIONS YOU WON!!!")
                    print(f"THE WORD IS: {word}")
                    break
            else:
                total_chances -= 1
                print("Incorrect Guess")
                print("The remaining chances are: ",total_chances)
                from hangman import hangman_parts
                hangman_parts(total_chances)
        else:
            print("Game Over")
            print("You Lose")
            print("All The Chances Are Exhausted")
            print("The Correct Word Is:",word)

    elif choice == 2:
        words = ['Shershaah','URI','Dhoom','3 Idiots','Sultan','Dear Zindagi','Goodbye',
                 'Bhool Bhulaiya','Players','Dangal','Partner','Drishyam','Bodygaurd',
                 'Kesari','Chhichhore','Razi','Piku','Hindi Medium','English Medium']
        word = random.choice(words)

        total_chances = 7
        guessed_word = "_"*len(word)
        while total_chances !=0:
            print("WORD: ", guessed_word)
            print("==============================")
            letter = input("Guess a Letter: ").lower()
            if letter in word:
                for index in range(len(word)):
                    if word[index] == letter:
                        guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]

                if guessed_word == word :
                    print("Congratulations you won!!!")
                    print(f"THE WORD IS: {word}")
                    break
            else:
                total_chances -= 1
                print("Incorrect guess")
                print("the remaining chances are: ",total_chances)
                from hangman import hangman_parts
                hangman_parts(total_chances)
        else:
            print("Game Over")
            print("You Lose")
            print("All The Chances Are Exhausted")
            print("The Correct Word Is:",word)

    elif choice == 3:
        words = ['Sandwich','Bread','Steak','Rice','Spaghetti','Pizza','Hamburger','Eggs','Cheese'
                 'Sausages','Apple','Juice','Milk','Candy','Cookie','Pie','Cake','Cupcake']
        word = random.choice(words)

        total_chances = 7
        guessed_word = "_"*len(word)
        while total_chances != 0:
            print("WORD: ", guessed_word)
            print("==============================")
            letter = input("guess a letter: ").lower()
            if letter in word:
                for index in range(len(word)):
                    if word[index] == letter:
                        guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]

                if guessed_word == word:
                    print("congratulations you won!!!")
                    print(f"THE WORD IS: {word}")
                    break
            else:
                total_chances -= 1
                print("Incorrect guess")
                print("the remaining chances are: ", total_chances)
                from hangman import hangman_parts

                hangman_parts(total_chances)
        else:
            print("Game Over")
            print("You Lose")
            print("All The Chances Are Exhausted")
            print("The Correct Word Is:", word)
    else:
        words = ['Rose','Lotus','Jasmine','Sunflower','Daisy','Tupil','Lavender',
                 'Hibiscus','Balsam','Goldenshower','Aloevera','Lily','Cherryblosom',]
        word = random.choice(words)

        total_chances = 7
        guessed_word = "_"*len(word)
        while total_chances != 0:
            print("WORD: ", guessed_word)
            print("============================")
            letter = input("guess a letter: ").lower()
            if letter in word:
                for index in range(len(word)):
                    if word[index] == letter:
                        guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]

                if guessed_word == word:
                    print("Congratulations You Won!!!")
                    print(f"THE WORD IS: {word}")
                    break
            else:
                total_chances -= 1
                print("Incorrect guess")
                print("the remaining chances are: ", total_chances)
                from hangman import hangman_parts

                hangman_parts(total_chances)
        else:
            print("Game Over")
            print("You Lose")
            print("All The Chances Are Exhausted")
            print("The Correct Word Is:", word)

