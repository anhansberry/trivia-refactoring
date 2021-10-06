#!/usr/bin/env python3
import question, player
class Game:
    max_players = 6 
    def __init__(self):
        self.questions = question.Question()
        max_players = 6 
        self.players = [] #add each player from created in Player class??
        #self.num_players = [0] * max_players
        self.current_player = 0
    
    
    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        """
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.num_players[self.how_many_players] = False
        """
        new_player = player.Player(player_name)
        self.players.append(new_player)
        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    def select_category(self): # second change
        current_player = self.players[self.current_player]
        if current_player.places % 4 == 0: 
            self.questions.current_category = "Pop"
        elif current_player.places % 5 == 1: 
            self.questions.current_category = "Science"
        elif current_player.places % 6 == 2:
            self.questions.current_category = "Sports"
        else:
            self.questions.current_category = "Rock"

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        current_player = self.players[self.current_player]
        print("%s is the current player" % current_player.name)
        print("They have rolled a %s" % roll)

        if current_player.status == True :
            if roll % 2 != 0:
                current_player.status = False
               
                print("%s is getting out of the penalty box" % current_player.name)
                current_player.places = current_player.places + roll
                if current_player.places > 11:
                    current_player.places =current_player.places - 12

                print(current_player.name + \
                            '\'s new location is ' + \
                            str(current_player.places))
                print("The category is %s" % self._current_category)
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % current_player.name)
                current_player.status = False
        else:
            current_player.places = current_player.places + roll
            if current_player.places > 11:
                current_player.places = current_player.places - 12

            print(current_player.name + \
                        '\'s new location is ' + \
                        str(current_player.places))
            print("The category is %s" % self.questions.current_category)
            self.questions._ask_question()

    def was_correctly_answered(self):
        current_player = self.players[self.current_player]
        if current_player.status == False:
            print('Answer was correct!!!!')
            current_player.purse += 1
            print(current_player.name + \
                ' now has ' + \
                str(current_player.purse) + \
                ' Gold Coins.')
            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0
            return winner

        else:
            self.current_player += 1
            if self.current_player == len(self.players): 
                self.current_player = 0
            return True

    def wrong_answer(self):
        print('Question was incorrectly answered')
        current_player = self.players[self.current_player]
        print(current_player.name + " was sent to the penalty box")

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        current_player = self.players[self.current_player]
        return not (current_player.purse == 6)


from random import randrange

if __name__ == '__main__':#when ths file is ran
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    dice = 0
    win_num = 0 

    while True:
        game.roll(dice +1 )
        dice = ( dice +1)%5
        if win_num == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()
            
        win_num = (win_num + 1)%9
        if not not_a_winner: break
