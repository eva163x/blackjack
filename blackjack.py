#RULES- choice
account=100
choice=input("Would you like to hear the rules?(Y/N)")
if choice.upper()=='Y':
  print("First time in the casino? Worry not! We shall have you playing like a pro in no time.")
  print("Each player recieves TWO cards that are visible to everyone.")
  print("┌─────────┐",'',"┌─────────┐") #PLAYER CARD STRUCTURE
  print("| A       |",'',"| 8       |")
  print("│         |",'',"|         |")
  print("│         |",'',"|         |")
  print("│    ♠    |",'',"|    ♥    |")
  print("│         |",'',"|         |")
  print("│         |",'',"|         |")
  print("│        A|",'',"|        8|")
  print("└─────────┘",'',"└─────────┘")
  print("The dealer recieves two cards as well, but only one card is faceup, the other is facedown.")
  print("┌─────────┐",'',"┌─────────┐")  #DEALER CARD STRUCTURE
  print("|░░░░░░░░░|",'',"| 7       |")
  print("│░░░░░░░░░|",'',"|         |")
  print("│░░░░░░░░░|",'',"|         |")
  print("│░░░░░░░░░|",'',"|       ♦ |")
  print("│░░░░░░░░░|",'',"|         |")
  print("│░░░░░░░░░|",'',"|         |")
  print("│░░░░░░░░░|",'',"|        7|")
  print("└─────────┘",'',"└─────────┘")
  print("Now, the goal of the game is to make the sum of your cards closest to 21 without exceeding 21.")
  print("So, at your turn, you get to make two choices: HIT or STAND. If you STAND, it means you don’t wish to pick any cards and forego your turn or ‘PASS’.")
  print("If you HIT, you will receive a card from the deck. You can HIT as many times as you want during a turn but YOUR SUM SHOULD NOT EXCEED 21. If you exceed 21 you will go BUST and lose.")
  print("┌─────────┐",'',"┌─────────┐",'',"┌─────────┐") 
  print("| A       |",'',"| 8       |",'',"│ 3       |")
  print("│         |",'',"|         |",'',"│         │")
  print("│         |",'',"|         |",'',"│         │")
  print("│      ♠  |",'',"|       ♥ |",'',"│       ♦ │")
  print("│         |",'',"|         |",'',"│         │")
  print("│         |",'',"|         |",'',"│         │")
  print("│        A|",'',"|        8|",'',"│        3│")
  print("└─────────┘",'',"└─────────┘",'',"└─────────┘")
  print("When you finally STAND, your turn is over.")
  print()
  print("DEALER'S TURN: now the DEALER must HIT if his sum is below 17. Once his sum reaches 17 or above, he must STAND.")
  print()
  print("WINNING/LOSING: If you are closer to 21 than the dealer, you win, else, you lose. If, during your turn, you BUST, you lose.")
  print()
  print("BETTING: at the beginning of your turn, you place your bet (minimum 50 coins, maximum 100 coins).")
  print("If you WIN, the money you bet doubles. If you LOSE, you LOSE the money you bet. If it's a TIE, your money will remain as is.")
  print()
  print("SPECIAL CARDS: ACE: 1 or 11 (whatever you decide to keep it as)")
  print()
  print("JACK(J), KING(K),QUEEN(Q): all have a value 10")
  print()
  print("That's all you need to know to get started! Good luck to you and happy playing!")
elif choice=='N':
  print("Looks like we have a seasoned player on our hands! Not to worry, things will get hard soon.")
print()
print("If you're ready to start playing, press 'YES', if you wish to EXIT")
start=input("press any other key:")
if start.upper()=='YES':
  #Player info - name
  name=input("Enter your name:\n>")
  print(name+"'s account has", account,"points")
  #Card reveal
  from random import randint
  def card_deck():
    #sets the card types and values
    card_value = ['A ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10','J ','Q ','K ']
    card_type = ['♥','♠','♣','♦']
    deck = []
    #This iterates all 52 cards into a deck
    for i in card_type:
        for j in card_value:
            deck.append(j + ' of ' + i)
    return deck
  def card_value(card):
    #determine value of the card
    if card[:1] in ('J','Q','K','1'):
        return int(10)
    elif card[:1] in ('2','3','4','5','6','7','8','9'):
        return int(card[:1])
    elif card[:1] == 'A':
        print ("\n"+ str(card))
        num = input("Do you want this to be 1 or 11?\n>")
        while num !='1' or num !='11':
            if num == '1':
                return int(1)
            elif num == '11':
                return int(11)
            else:
                num = input("Do you want this to be 1 or 11?\n>")


def new_card(deck):
    return deck[randint(0,len(deck)-1)]

def remove_card(deck,card):
    return deck.remove(card)
def game():
  #rules
  acc=10
  print("You get 20 points for every right answer and minus 10 for a wrong one.\nWe'll start you off with an even 10 points and then we'll see!")
  print("There are 3 quizes...")
  menu={}
  menu['1']='Card trivia'
  menu['2']='Python quiz'
  menu['3']='Basic Biology quiz'
  d1={}
  d2={}
  d3={}
  #q/a card trivia
  d1['Q1 What is the probability of getting a black ace in a deck of cards?']='2/52'
  d1['Q2 How many one-eyed jacks are there in a deck?']='2'
  d1['Q3 If I were talking about a Suicide King, which king am I referring to?']='king of hearts'
  d1['Q4 Which is the only queen that faces right?']='queen of spades'
  d1['Q5 What name did Jacks previously go by?']='knave'
  #q/a CS quiz
  d2['Q1 What function is used to add elements at the end of a list?']='append'
  d2['Q2 Is tuple mutable or immutable?']='immutable'
  d2['Q3 What concept repeats whatever is inside it?']='loop'
  d2['Q4 Name the two types of loops.']='for and while'
  d2['Q5 What is the datatype of 6.4?']='float'
  #q/a basic bio quiz
  d3['Q1 What are the little pores at the bottom of a leaf?']='stomata'
  d3['Q2 What is a seed with two cotyledons called?']='dicot'
  d3['Q3 The central vein of the leaf is called...']='midrib'
  d3['Q4 What is the total number of bones in the adult human body?']='206'
  d3['Q5 What is the bone in your ear called?']='cartilage' 
  for i in menu:
      print(i, menu[i])
  select=input("Please select a quiz\n>")
  if select=='1':
      for j in d1:
          print(j)
          ans=input("Enter answer:\n>")
          if ans.lower()==d1[j]:
              print("Correct! You get 20 points!")
              acc+=20
              
          else:
              print("Wrong answer! The answer is", d1[j])
              print("You lose 10 points!")
              acc-=10
              
  elif select=='2':
      for j in d2:
          print(j)
          ans=input("Enter answer:\n>")
          if ans.lower()==d2[j]:
              print("Correct! You get 20 points!")
              acc+=20
          else:
              print("Wrong answer! The answer is", d2[j])
              print("You lose 10 points!")
              acc-=10
  elif select=='3':
      for j in d3:
          print(j)
          ans=input("Enter answer:\n>")
          if ans.lower()==d3[j]:
              print("Correct! You get 20 points!")
              acc+=20
          else:
              print("Wrong answer! The answer is", d3[j])
              print("You lose 10 points!")
              acc-=10
  else:
      select=input("Please re-enter your selection:\n>")
  print("You now have ",acc," points")
  return acc

play_again ='yes'
quiz = 'no'
while play_again.lower()=='yes' or quiz.lower()=='no':
  #Betting round
  print("Time to make your bets!")
  print()
  bet=int(input("Enter you bet (maximum 50, minimum 10):\n>"))
  if bet>50 or bet<10:
    while bet>50 or bet<10:
      print("Oops! Seems like your bet wasn't in the defined range.")
      bet=int(input("Please re-enter your bet:\n>"))
  elif bet>account:
    while bet>account:
      print("Sorry, your account doesn't have enough money!")
      bet=int(input("Please re-enter your bet:\n>"))
  #player's cards
  new_deck = card_deck()
  card1 = new_card(new_deck)
  remove_card(new_deck,card1)
  card2 = new_card(new_deck)
  remove_card(new_deck,card2)
  print ("\n\n\n\n" + card1 + " and " + card2)
  print("┌─────────┐",'',"┌─────────┐") #PLAYER CARD STRUCTURE
  print("|  "+card1[:2]+"     |",'',"| "+card2[:2]+"      |")
  print("│         |",'',"|         |")
  print("│         |",'',"|         |")
  print("│    "+card1[6]+"    |",'',"|    "+card2[6]+"    |")
  print("│         |",'',"|         |")
  print("│         |",'',"|         |")
  print("│       "+card1[:2]+"|",'',"|       "+card2[:2]+"|")
  print("└─────────┘",'',"└─────────┘")
  valu1 = card_value(card1)
  valu2 = card_value(card2)
  total = valu1 + valu2
  print("with a total of " + str(total) )

  #dealer's cards
  dealer_card1 = new_card(new_deck)
  remove_card(new_deck,dealer_card1)
  dealer_card2 = new_card(new_deck)
  remove_card(new_deck,dealer_card2)
  dealer_value1 = card_value(dealer_card1)
  dealer_value2 = card_value(dealer_card2)
  dealer_total = dealer_value1 + dealer_value2
  print ('\nThe Dealer deals himself a facedown card and a', dealer_card1)
  print("┌─────────┐",'',"┌─────────┐")  #DEALER CARD STRUCTURE
  print("|░░░░░░░░░|",'',"| "+dealer_card1[:2]+"      |")
  print("│░░░░░░░░░|",'',"|         |")
  print("│░░░░░░░░░|",'',"|         |")
  print("│░░░░░░░░░|",'',"|    "+dealer_card1[6]+"    |")
  print("│░░░░░░░░░|",'',"|         |")
  print("│░░░░░░░░░|",'',"|         |")
  print("│░░░░░░░░░|",'',"|       "+dealer_card1[:2]+"|")
  print("└─────────┘",'',"└─────────┘")
  if total == 21:
      print("Blackjack! You win!")
      account+=bet
      print("Your account now has", account)
  else:
      while total < 21: #not win or loss yet
          answer = input("Would you like to hit or stand?\n> ")
          if answer.lower() == 'hit':
              #more card creation, removal, and value added to total
              more_card = new_card(new_deck)
              remove_card(new_deck,more_card)
              more_value = card_value(more_card)
              total += int(more_value)
              print("┌─────────┐") #HIT CARD STRUCTURE
              print("|  "+more_card[:2]+"     |")
              print("│         |")
              print("│         |")
              print("│    "+more_card[6]+"    |")
              print("│         |")
              print("│         |")
              print("│       "+more_card[:2]+"|")
              print("└─────────┘")
              print (more_card + " for a new total of " + str(total))
              if total > 21: #lose condition
                  print("You LOSE!You went bust!")
                  account-=bet
                  print("Your account now has", account)
                  if account>10:
                    play_again = input("Would you like to continue? EXIT to leave\n")
                  else:
                    print("Looks like you're out of points!")
                    quiz=input("Would you like to play a quiz to earn more?\n>")
                    if quiz.lower()=='yes':
                      account=game()
                      play_again=input("Would you like to continue playing?\n>")
              elif total == 21: #winning condition
                  print("You WIN BIG!")
                  account+=bet
                  print("Your account now has", account)
                  if account>10:
                    play_again = input("Would you like to continue? EXIT to leave\n")
                  else:
                    print("Looks like you're out of points!")
                    quiz=input("Would you like to play a quiz to earn more?\n>")
                    if quiz.lower()=='yes':
                      account=game()
                      play_again=input("Would you like to continue playing?\n>")
                      play_again=input("Would you like to continue playing?\n>")
                      break
              else:
                  continue
          elif answer.lower() == 'stand':
              print("The dealer reveals his facedown card to be")
              print("a " + dealer_card2 + " for a total of " + str(dealer_total))
              print("┌─────────┐",'',"┌─────────┐") #DEALER CARD REVEAL STRUCTURE
              print("|  "+dealer_card2[:2]+"     |",'',"| "+dealer_card1[:2]+"      |")
              print("│         |",'',"|         |")
              print("│         |",'',"|         |")
              print("│    "+dealer_card2[6]+"    |",'',"|    "+dealer_card1[6]+"    |")
              print("│         |",'',"|         |")
              print("│         |",'',"|         |")
              print("│       "+dealer_card2[:2]+"|",'',"|       "+dealer_card1[:2]+"|")
              print("└─────────┘",'',"└─────────┘")
              if dealer_total < 17:
                  print("The Dealer HITS again.")
                  dealer_more = new_card(new_deck)
                  more_dealer_value = card_value(dealer_more)
                  print("The card is a " + str(dealer_more))
                  print("┌─────────┐") #DEALER HIT CARD STRUCTURE
                  print("|  "+dealer_more[:2]+"     |")
                  print("│         |")
                  print("│         |")
                  print("│    "+dealer_more[6]+"    |")
                  print("│         |")
                  print("│         |")
                  print("│       "+dealer_more[:2]+"|")
                  print("└─────────┘")
                  dealer_total += int(more_dealer_value)
                  if dealer_total > 21 and total <=21: #dealer bust
                      print("Dealer BUST! You win!")
                      account+=bet
                      print("Your account now has", account)
                  elif dealer_total < 21 and dealer_total > total:
                      print("Dealer has " + str(dealer_total) + " You lose!")#you lose
                      account-=bet
                      print("Your account now has", account)
                  else:
                      continue
              elif dealer_total == total:
                  print("Equal Deals, no winner")
                  print("Your account now has", account)
              elif dealer_total < total:
                  print("You win!")
                  account+=bet
                  print("Your account now has", account)
              else:
                  print("You Lose!")
                  account-=bet
                  print("Your account now has", account)
              if account>10:
                play_again = input("\nWould you like to continue? EXIT to leave\n")
              else:
                print("Looks like you're out of points!")
                quiz=input("Would you like to play a quiz to earn more?\n>")
                if quiz.lower()=='yes':
                  account=game()
                  play_again=input("Would you like to continue playing?\n>")
print("Thank you for Playing")

