# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

print(logo)


def find_highest_bidder(bidding_data):
    highest_bid = 0
    winner = ""

    for bidder in bidding_data:
        bid_amount = bidding_data[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    username = input("What is your name?\n").lower()
    bid_amount = int(input("What is your bid amount\n"))
    other_bids = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    bids[username] = bid_amount
    if other_bids != "yes":
        print("Let's find out who won!")
        continue_bidding = False
        find_highest_bidder(bids)
    elif other_bids == "yes":
        print("\n" * 20)
