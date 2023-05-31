from classes.result import Result

class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
        
    def results(self, new_result=None):
        return [result for result in Result.all if result.game == self]
    
    def players(self, new_player=None):
        return {result.player for result in self.results()}
    
    def average_score(self, player):
        all_scores = [result.score for result in self.results() 
                        if result.player == player]
        if all_scores: return sum(all_scores) / len(all_scores)

    # Properties 
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if (not hasattr(self, "title")
            and type(title) == str
            and len(title)):
            self._title = title
        else: 
            raise Exception("Title must be a string and cannot be changed")