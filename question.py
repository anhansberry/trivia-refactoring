class Question:
    def __init__(self, pop, rock, sports, science):
        self.pop = []
        self.science = []
        self.sports = []
        self.rock = []
        types = [self.pop, self.rock, self.sports, self.science]
        type_name = ["pop","rock","sports","science"]
    
    def create_question(self,types, type_name):
        for x in range(4):
            for i in range(50):
                self.types[x].append(self.type_name[x], "Question" , i)
    
    def select_category(self): # second change
            if self.places[self.current_player]% 4 == 0: 
                return 'Pop'
            elif self.places[self.current_player]% 5 == 1: 
                return 'Science'
            elif self.places[self.current_player]% 6 == 2:
                return 'Sports'
            else:
                return 'Rock'