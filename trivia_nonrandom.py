#!/usr/bin/env python3

class Game:  #add new player class - inside initialize for game - throw player in there
    def __init__(self):
        list_size = 6
        self.players = []
        self.places = [0] * list_size #list of 6 0's
        self.purses = [0] * list_size
        self.in_penalty_box = [0] * list_size

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.out_penalty_box = False

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0  #needs to stay - places and purses initialized for player at 0.
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False #new player added is not in penalty box

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True
    def update_places(self, roll):
        self.places[self.current_player] = self.places[self.current_player] + roll #whatever is rolled is added to the places
        if self.places[self.current_player] > 11: # capped at 11 - goes back to about 0 after give or take a few.
            self.places[self.current_player] = self.places[self.current_player] - 12

        print(self.players[self.current_player] + \
                    '\'s new location is ' + \
                    str(self.places[self.current_player]))
        print("The category is %s" % self._current_category)
        self._ask_question()
        
    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player]) #print current player
        print("They have rolled a %s" % roll) # what player rolled - some num from 1-5

        if self.in_penalty_box[self.current_player]:#this implies if in_penalty_box[] = true
            if roll % 2 != 0:
                self.out_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self.update_places(roll)
                
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.out_penalty_box = False
        else:
            self.update_places(roll)

    def _ask_question(self):
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    @property
    def _current_category(self): #good
        if self.places[self.current_player] % 4 == 0: 
	        return 'Pop'
        elif self.places[self.current_player] % 4 == 1:
	        return 'Science'
        elif self.places[self.current_player] % 4 == 2:
	        return 'Sports'
        else:
	        return 'Rock'


    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]: #if in penalty box is true
            if self.out_penalty_box: #if out of pen box is true
                print('Answer was correct!!!!')
                self.purses[self.current_player] += 1
                print(self.players[self.current_player] + \
                    ' now has ' + \
                    str(self.purses[self.current_player]) + \
                    ' Gold Coins.')

                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True



        else:

            print("Answer was correct!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + \
                ' now has ' + \
                str(self.purses[self.current_player]) + \
                ' Gold Coins.')

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0

            return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)


from random import randrange #test without randomness

if __name__ == '__main__': #is this line necessary?
    not_a_winner = False #huh?

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    dice = 1
    win = 0

    while True:
        game.roll(dice)  #answer is always correct. - 1-5
        dice+=1
        if dice > 5:
            dice = 1
        if win == 7: #0 - 8 
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()
        
        win = (win + 1) % 9
        if not not_a_winner: break
