class Player:

    all = []

    def __init__(self, username):
        self.username = username
        type(self).all.append(self)
        
    def results(self):
        return [result for result in Result.all if result.player is self]
    
    def games_played(self):
        return list({result.game for result in self.results()})
    
    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        all_plays = [result for result in self.results() if result.game is game]
        return len(all_plays)
    
    @classmethod
    def highest_scored(cls, game):
        if isinstance(game, Game) and game.results(): 
            avgs = [(player, game.average_score(player)) for player in cls.all]
            avgs.sort(key=lambda t: t[1], reverse = True)
            return avgs[0][0]

    # Properties 
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if (isinstance(username, str)
            and 2 <= len(username) <= 16):
            self._username = username 
        else: 
            raise Exception("Username must be a string between 2 and 16 chars")

from classes.result import Result
from classes.game import Game