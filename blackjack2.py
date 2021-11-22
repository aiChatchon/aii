from random import shuffle
class Deck:
    def __init__(self):
        self.card_face=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.card_type=['Spades','Diamonds','Hearts','Clubs']
        self.playing_deck=[]
        for i in self.card_type:
            for j in self.card_face:
                self.playing_deck.append(j + ' of ' + i)
    def shuffle_cards(self):
        shuffle(self.playing_deck)
        return self.playing_deck
class Dealer():
    def __init__(self,deck):
        self.playing_deck=deck
    def deal_cards(self):
        self.dealed_cards=self.playing_deck[0:2]
        del(self.playing_deck[0:2])
        return self.dealed_cards
    def draw(self):
        self.drawn_cards=self.playing_deck[0]
        del(self.playing_deck[0])
        return self.drawn_cards
    def gameResult(self):
        print("Dealer got",bot.cal_score())
        print("Player 1 got",player.cal_score())
        if bot.cal_score()>player.cal_score():
            print("Dealer won")
            quit()
        if bot.cal_score()<player.cal_score():
            print("You won")
            quit()          
        if bot.cal_score()==player.cal_score():
            print("Tie game")
            quit()
    def dealer_show(self):
        self.hide_housecard=True
        if self.hide_housecard==False:
            print(self.player_hand)
        if self.hide_housecard==True:
            print("First card of the Dealer is")
            print(self.player_hand[0])
            self.hide_housecard=False
    def dealer_play(self):
        if self.hand_value<17:
            return ("H")
        else:
            return ("S")

class Player(Dealer):
    def __init__(self,hand,player_team):
        self.player_hand=hand       
        self.player_team=player_team
        self.askforValue=True
    def show_hand(self):
        print(self.player_team,"'s hand")
        print(self.player_hand)
    def hitorstand(self,response):
        self.user_response=response
        if self.user_response=="H":
            self.player_hand.append(dealer.draw())
            print(self.player_hand)
        elif self.user_response=="S":
            print( self.player_team,"'s final hand is")
            print(self.player_hand)
            return False
    def cal_score(self):
        self.hand_value=0
        self.ace=False
        for i in (self.player_hand):
            if i[:1] in ["1","J","Q","K"]:
                self.hand_value+=10
            elif i[:1]in ['2','3','4','5','6','7','8','9',]:
                self.hand_value+=int(i[0])
            elif i[:1]=="A":              
                if self.askforValue==True:
                    self.ace_value=input("An ace!-value=11 or 1:  ")
                    self.askforValue=False
                self.hand_value+=int(self.ace_value)
        return(self.hand_value)
    def check_bust(self):
        if self.hand_value>21:
            if self.ace==True:
                self.hand_value-=10
            else:
                print(self.player_team,"Busted")
                quit()
    def check_blackjack(self):
        if self.hand_value==21:
            print(self.player_team,"Got Blackjack")
            print("Game is over")
            quit()   



deck=Deck()
deck.shuffle_cards()
dealer=Dealer(deck.shuffle_cards())
player=Player(dealer.deal_cards(),"Player")
bot=Player(dealer.deal_cards(),"Dealer")
bot.dealer_show()
player.show_hand()
player.cal_score()
player.check_blackjack()
while True:
    if player.hitorstand(input("Enter H for Hit and S for Stand:   "))==False:
        break
    player.cal_score()
    player.check_bust()
bot.dealer_show()
bot.show_hand()
bot.cal_score()
bot.check_blackjack()
while True:
    if bot.hitorstand(bot.dealer_play())==False:
        break
    bot.cal_score()
    bot.check_bust()
dealer.gameResult()



