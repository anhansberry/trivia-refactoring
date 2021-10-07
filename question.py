class Question:
    def __init__(self):
        self.pop = []
        self.science = []
        self.sports = []
        self.rock = []
        self.types = [self.pop, self.rock, self.sports, self.science]
        self.type_name = ["pop","rock","sports","science"]
        self.current_category = ""
    
    def create_question(self,types, type_name):
        for x in range(4):
            for i in range(50):
                self.types[x].append(self.type_name[x], "Question" , i)
    

    
    def _ask_question(self):
        if self.current_category == 'Pop': print(self.pop_questions.pop(0))
        if self.current_category == 'Science': print(self.science_questions.pop(0))
        if self.current_category == 'Sports': print(self.sports_questions.pop(0))
        if self.current_category == 'Rock': print(self.rock_questions.pop(0))
