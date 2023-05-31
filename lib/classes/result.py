class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        type(self).all.append(self)

        player.results(self)
        player.games_played(game)

        game.results(self)
        game.players(player)

    # Properties 
    @property
    def score(self): 
        return self._score
    
    @score.setter
    def score(self, score):
        if type(score) == int and (1 <= score <= 5000):
            self._score = score
        else: 
            raise TypeError("Score must be an integer between 1 and 5000")
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        from .player import Player
        if isinstance(player, Player):
            self._player = player 
        else: 
            raise Exception 
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        from .game import Game 
        if isinstance(game, Game):
            self._game = game 
        else: 
            raise Exception 
    