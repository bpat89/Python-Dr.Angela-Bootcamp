import os

import art

print(art.logo)

# create an empty dictionary inside a list of dictionaries
bid_list = {}

# create into a function to keep adding a person and loop until the final bidder
biding_finished = False


# finding highest bidder
def find_highest_bidder(bid_record):
    highest_bidder = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"{winner} {highest_bidder}")


while not biding_finished:
    # name and price inputs
    name = input("please enter you name :\n")
    price = int(input("please enter you bid :\n$"))
    bid_list[name] = price
    more_bids = input("Are there any more to bid ? :\n")
    if more_bids != "yes":
        biding_finished = True
        find_highest_bidder(bid_list)
    elif more_bids == "yes":

        os.system('cls')




