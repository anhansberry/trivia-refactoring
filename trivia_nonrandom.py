#!/usr/bin/env python3

class Game:
    def __init__(self): #works
        self.players = []

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

    def add(self, player_name): #works
        new_player = Player(player_name)
        self.players.append(new_player)
        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    def update_places(self, roll): #works
        current = self.players[self.current_player]
        current.places += roll
        if current.places > 11:
            current.places = current.places - 12
        print(str(current.name) + \
                    '\'s new location is ' + \
                    str(current.places)) 
        print("The category is %s" % self._current_category)
        self._ask_question()
        
    @property
    def how_many_players(self): #works
        return len(self.players)

    def roll(self, roll): #works
        current = self.players[self.current_player]
        print("%s is the current player" % current.name) #print current player
        print("They have rolled a %s" % roll) # what player rolled - some num from 1-5

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

    def _ask_question(self): #works
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    @property
    def _current_category(self): #works
        current = self.players[self.current_player]
        if current.places % 4 == 0: 
	        return 'Pop'
        elif current.places % 4 == 1:
	        return 'Science'
        elif current.places % 4 == 2:
	        return 'Sports'
        else:
	        return 'Rock'

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


from random import randrange 

class Player:
    def __init__(self, name):
        self.name = name
        self.places = 0
        self.purses = 0
        self.in_penalty_box = False

if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    dice = 1
    win = 0
    while True:
        game.roll(dice)
        dice+=1
        if dice > 5:
            dice = 1
        if win == 7: #0 - 8 
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()
        
        win = (win + 1) % 9
        if not not_a_winner: break
