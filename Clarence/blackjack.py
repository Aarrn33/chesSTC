import time
from random import*
cardgame=[2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi", "as"]
bank=[]
bankp=[]
p1=[]
p1p=[]
end=0
#need to continue the testing regarding the p1p and bankp addition + changing 11 to 1 if needed
#no problem seen for now
#the main code can be considered as finish
#Next step would be to add a gambling system and a quick replay

def piocher_bank(): #add one card to the bank from 2 to 11
    global x 
    x=cardgame[randint(0,12)] #choose a random card
    if x == "valet" : #if card = str converting it in int
            bankp.append(x)
            x=10
            bank.append(x)
    elif x == "dame" :
            bankp.append(x)
            x=10
            bank.append(x)
    elif x == "roi" :
            bankp.append(x)
            x=10
            bank.append(x)
    elif x == "as" : #bank will always take an As as eleven as long as it can
            bankp.append(x)
            if sum(bank)<= 10:
                x=11
                bank.append(x)
            else :
                x=1
                bank.append(x)
    else :
        bankp.append(x) 
        bank.append(x)

def piocher_p1(): #sames as bank but for the player
    global x
    x=cardgame[randint(0,12)]
    if x == "valet" :
            p1p.append(x)
            x=10
            p1.append(x)
    elif x == "dame" :
            p1p.append(x)
            x=10
            p1.append(x)
    elif x == "roi" :
            p1p.append(x)
            x=10
            p1.append(x)
    elif x == "as" : #here the player can choose the value of the "As"
            print("p1=", p1p)
            print("As égal à 1 ou 11 ?")
            rep=input()
            if rep=="11":
                p1p.append(x)
                x=11
                p1.append(x)
            else :
                p1p.append(x)
                x=1
                p1.append(x)
    else :
        p1p.append(x)
        p1.append(x)

def blackjack(): 
    global bank
    global bankp
    global p1
    global p1p
    bank=[]
    bankp=[]
    p1=[]
    p1p=[]
    end=0
    for i in range (0,2): #add 2 random cards to the two packs
        piocher_p1()
    for i in range (0,2):
        piocher_bank()
    print("p1=", p1p)
    print("Piocher ou Passer ?") #ask the player if he wants to take a card or pass
    while input()=="Piocher" or "piocher" :
            piocher_p1()
            time.sleep(1)
            if sum(p1) > 21 : #if the player has more than 21 he lost
                if 11 in p1:
                    p1.remove(11)
                    p1.append(1)
                    print("p1=", p1p)
                else :
                    print("p1=", p1p)
                    print("Perdu")
                    end=end+1 #value that helps to not do the rest of the code for nothing
                    break
            else : 
                print("p1=", p1p)
                print("Piocher ou Passer ?")
    if end==0 : #if the player hasn't already lost the code continues
        while sum(bank) <= 17 :
            piocher_bank()
            if sum(bank) > 21: #if the bank has more than 21 the player wins
                if 11 in bank:
                    bank.remove(11)
                    bank.append(1)
                else :
                    print("p1=", p1p, "bank=", bankp)
                    print("Gagné")
                end=end+1 #the same as before
        if end==0 : #Here the code will determine who won and who lost 
                    #or if it's a draw by comparing the values if they don't exceed 21
            if sum(bank) < sum(p1) : 
                print("p1=", p1p, "bank=", bankp)
                print("Gagné")
            elif sum(p1) < sum(bank) :
                print("p1=", p1p, "bank=", bankp)
                print("Perdu")
            elif sum(p1) == sum(bank) :
                print("p1=", p1p, "bank=", bankp)
                print("Draw")

blackjack() #start the code for test/fun