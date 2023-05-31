class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    # Properties 
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if (isinstance(score, int)
            and 1 <= score <= 5000):
            self._score = score
        else: 
            raise Exception("Score must be an integer between 1 and 5000")
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else: 
            raise Exception("Player must be of instance Player")
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else: 
            raise Exception("Game must be of instance Game")

from classes.player import Player 
from classes.game import Game 
