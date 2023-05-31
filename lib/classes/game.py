class Game:
    def __init__(self, title):
        self.title = title
        
    def results(self):
        return [result for result in Result.all if result.game is self]
    
    def players(self):
        return list({result.player for result in self.results()})
    
    def average_score(self, player):
        all_scores = [result.score for result in self.results() 
                        if result.player is player]
        if all_scores: return sum(all_scores) / len(all_scores)

    # Properties 
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if (not hasattr(self, "_title")
            and isinstance(title, str)
            and len(title)):
            self._title = title
        else: 
            raise Exception("Title must be a string and cannot be changed")

from classes.result import Result