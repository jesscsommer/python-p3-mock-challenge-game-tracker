from classes.result import Result

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        type(self).all.append(self)
        
    def results(self, new_result=None):
        return [result for result in Result.all if result.player == self]
    
    def games_played(self, new_game=None):
        return {result.game for result in self.results()}
    
    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        all_plays = [result for result in self.results() if result.game == game]
        return len(all_plays)
    
    @classmethod
    def highest_scored(cls, game):
        high_score = 0
        best_player = None
        for player in cls.all: 
            avg = game.average_score(player)
            if avg and avg > high_score: 
                high_score = avg
                best_player = player
        return best_player
        

    # Properties 
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if (type(username) == str 
            and 2 <= len(username) <= 16):
            self._username = username 
        else: 
            raise Exception("Username must be a string between 2 and 16 chars")