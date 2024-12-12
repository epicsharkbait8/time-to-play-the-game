print("Time to play the game!")
print("Welcome player, to Blackjack, you know how to play so ill start you off with a card")

def gamble():
  import random
  card1 = random.randint(1,10)
  card2 = random.randint(1,10)
  newcard = random.randint(1,10)
  dealers_show = random.randint(1,10)
  dealers_hidden = random.randint(1,10)
  total = card1 + card2
  dtotal = dealers_show + dealers_hidden

  print("dealer has a", dealers_show)
  print("Your cards are", card1, "and", card2, ",you're total is",       total)
  if total =="21":
    print("well played")
  if total > 21:
    print("you lose, and no refunds")
  while total < 21:
    print("would you like to hit or stand?")
    answer = input()
    if answer == "hit":
      newcard = random.randint(1,10)
      total = total + newcard
      print("your new total is", total)
      if total > 21:
        print("you lose, and no refunds")
        break
    if answer == "stand":
      print("dealers hidden card is", dealers_hidden)
      while dtotal < 15:
        print("Dealer must hit")
        print("dealers total is", dtotal + newcard)
        if dtotal + newcard > total:
            print("dealer stands")        
        break
gamble()