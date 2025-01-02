import random
import logo 

def generate_final_results(human_hand, computer_hand):
    human_final = f"Your final hand: {human_hand}, final score: {sum(human_hand)}"
    computer_final = f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}"
    return human_final, computer_final

def check_for_blackjack(human_hand, computer_hand):
    if len(human_hand) == 2 and sum(human_hand) == 21:
        print(f"You win, you have a Blackjack hand 😱")
        return generate_final_results(human_hand, computer_hand)
    elif len(computer_hand) == 2 and sum(computer_hand) == 21:
        print(f"Computer wins with a Blackjack 😱")
        return generate_final_results(human_hand, computer_hand)
    return None


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

startGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n")
game = startGame == 'y'

while game:

    humanHand = []
    computerHand = []


    while len(humanHand) < 2:
        humanHand.append(random.choice(cards))
    while len(computerHand) < 2:
        computerHand.append(random.choice(cards))

    print(f"Your cards: {humanHand}, current score: {sum(humanHand)}")
    print(f"Computer's first card: {computerHand[0]}")

    # Check for Blackjack
    result = check_for_blackjack(humanHand, computerHand)
    if result:
        print(result[0])
        print(result[1])
        break

    # Player's turn
    game_over = False
    while not game_over:
        choice = input("Type 'y' to get another card, type 'n' to pass:\n")

        if choice == 'y':
            humanHand.append(random.choice(cards))
            print(f"Your cards: {humanHand}, current score: {sum(humanHand)}")

            if sum(humanHand) > 21:
                print("You went over. You lose 😭")
                # Display final results
                human_final, computer_final = generate_final_results(humanHand, computerHand)
                print(human_final)
                print(computer_final)

                game_over = True
        elif choice == 'n':
            print("You chose to pass.")
            game_over = True
        else:
            print("Invalid input. Please type 'y' or 'n'.")


    if sum(humanHand) <= 21:
        while sum(computerHand) < 17:
            computerHand.append(random.choice(cards))


        if sum(computerHand) > 21:
            print("Computer went over. You win 🎉")
        elif sum(humanHand) > sum(computerHand):
            print("You win 🎉")
        elif sum(humanHand) < sum(computerHand):
            print("Computer wins 😭")
        else:
            print("It's a draw 🤪")

        #Display final results
        human_final, computer_final = generate_final_results(humanHand, computerHand)
        print(human_final)
        print(computer_final)


    play_again = input("Do you want to play again? Type 'y' or 'n':\n")
    if play_again != 'y':
        game = False

print("Thanks for playing Blackjack!")

