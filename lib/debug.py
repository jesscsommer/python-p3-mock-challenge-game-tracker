#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    g1 = Game("Scrabble")
    g2 = Game("Wingspan")
    g3 = Game("Here to Slay")

    p1 = Player("jess_sayin")
    p2 = Player("awrox")
    p3 = Player("hermywermy")

    r1 = Result(p1, g1, 150)
    r2 = Result(p1, g2, 135)
    r3 = Result(p1, g2, 120)
    r4 = Result(p2, g1, 95)
    r5 = Result(p2, g2, 157)

    sc = Player.highest_scored(g1)
    wc = Player.highest_scored(g2)

    ipdb.set_trace()
