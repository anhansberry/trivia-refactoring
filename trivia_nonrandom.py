#!/usr/bin/env python3

class Game:  #add new player class - inside initialize for game - throw player in there
    def __init__(self):
        self.players = []
        # list_size = 6
        # self.players = []
        # self.places = [0] * list_size #list of 6 0's
        # self.purses = [0] * list_size
        # self.in_penalty_box = [0] * list_size

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
        # self.players.append(player_name)
        # self.places[self.how_many_players] = 0  #needs to stay - places and purses initialized for player at 0.
        # self.purses[self.how_many_players] = 0
        # self.in_penalty_box[self.how_many_players] = False #new player added is not in penalty box
        new_player = Player(player_name)
        self.players.append(new_player)
        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True
    def update_places(self, roll):
        current = self.players[self.current_player]
        current.places += roll
        # self.places[self.current_player] = self.places[self.current_player] + roll #whatever is rolled is added to the places
        # if self.places[self.current_player] > 11: # capped at 11 - goes back to about 0 after give or take a few.
        if current.places > 11:
            current.places = current.places - 12
# i made current a str in line below
        print(str(current.name) + \
                    '\'s new location is ' + \
                    str(current.places)) 
        print("The category is %s" % self._current_category)
        self._ask_question()
        
    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        current = self.players[self.current_player]
        print("%s is the current player" % current.name) #print current player
        print("They have rolled a %s" % roll) # what player rolled - some num from 1-5

        # if self.in_penalty_box[self.current_player]:#this implies if in_penalty_box[] = true
        if current.in_penalty_box:
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
        current = self.players[self.current_player]
        if current.places % 4 == 0: 
	        return 'Pop'
        elif current.places % 4 == 1:
	        return 'Science'
        elif current.places % 4 == 2:
	        return 'Sports'
        else:
	        return 'Rock'
        # if self.places[self.current_player] % 4 == 0: 
	    #     return 'Pop'
        # elif self.places[self.current_player] % 4 == 1:
	    #     return 'Science'
        # elif self.places[self.current_player] % 4 == 2:
	    #     return 'Sports'
        # else:
	    #     return 'Rock'

    def correct_answer_str(self):
        current = self.players[self.current_player]
        print('Answer was correct!!!!')
        current.purses += 1
        print(current.name + \
                    ' now has ' + \
                    str(current.purses) + \
                    ' Gold Coins.')

        winner = self._did_player_win()
        self.current_player += 1 # could prob just put after conditional
        if self.current_player == len(self.players):
            self.current_player = 0
        return winner

    def was_correctly_answered(self):
        current = self.players[self.current_player]
        if current.in_penalty_box: #if in penalty box is true
            if self.out_penalty_box: #if out of pen box is true 
                self.correct_answer_str()
            else:
                self.current_player += 1 # merge w this one
                if self.current_player == len(self.players): self.current_player = 0
                return True
        else:
            self.correct_answer_str()
    
    def wrong_answer(self):
        current = self.players[self.current_player]
        print('Question was incorrectly answered')
        print(current.name + " was sent to the penalty box")
        current.in_penalty_box = True

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self): 
        current = self.players[self.current_player]
        return not (current.purses == 6)


from random import randrange #test without randomness

class Player:
    def __init__(self, name):
        self.name = name
        self.places = 0
        self.purses = 0
        self.in_penalty_box = False

# class Questions:
#     def __init__(self): #pop_questions, science_questions, sports_questions, rock_questions
#         self.pop_questions = 0
#         self.science_questions = 0
#         self.sports_questions = 0
#         self.rock_questions = 0

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
