bid_participants={}
def bid():
    user_name=str(input("What is your name?:  ")).lower()
    user_bid=int(input("How much are you willing to bid?:  $ "))
    bid_participants[user_name]=user_bid
    user_decision=str(input("Are there any other bidders? Type 'yes or 'no:'\n")).lower()
    if user_decision=="yes":
        print(f"\n"*50)
        bid()
    elif user_decision=="no":
        highest=max(bid_participants,key=bid_participants.get)
        value = bid_participants[highest] 
        print(f"The winner is {highest} with a bid of {value} ")
    else:
        print=("Invalid input")
bid()