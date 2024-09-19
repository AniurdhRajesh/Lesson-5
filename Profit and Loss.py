while True:
 buy=int(input("For how much are you buying oranges : \n"))
 sell=int(input("For how much are you going to sell the oranges for : \n"))
 if buy>sell:
    amount=buy-sell
 elif sell>buy:
    amount=sell-buy
 if buy>sell:
     print("Loss")
     print("You are losing ₹",amount)
 else:
     print("Profit")
     print("You are profiting by ₹",amount)