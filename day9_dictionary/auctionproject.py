from hammer import logo

print(logo)

def findhighestbidder(bidding_record): #bidding record disini adalah dictionary
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        amount = bidding_record[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}

testing = True
while testing:
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n $"))
    bids[name] = price
    response = input("Any other bidders?\ntype 'yes' or 'no'\n")
    if response == "no":
        testing = False
        findhighestbidder(bids)

        #print("Goodbye")
    #elif response == "yes":
        #clear()

    

