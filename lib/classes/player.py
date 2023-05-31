class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        type(self).all.append(self)
        
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result): 
            self._results.append(new_result)
        return self._results
    
    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game): 
            self._games_played.append(new_game)
        return self._games_played 
    
    def played_game(self, game):
        return game in self._games_played
    
    def num_times_played(self, game):
        results = [r for r in self._results if r.game == game]
        return len(results)
    
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

        avg_scores = [game.average_score(player) for player in Player.all] 
        return max(avg_scores)
        
    # Properties 
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if type(username) == str and (2 <= len(username) <= 16):
            self._username = username
        else: 
            raise TypeError("Username must be a string of 2-16 characters")