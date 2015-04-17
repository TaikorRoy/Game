__author__ = 'OL'


import pylab
import player_baseClass, judge

player_a, player_b = player_baseClass.Player(), player_baseClass.Player()

judge = judge.Judge()

pl = list()

for i in range(100):

    player_a.think()

    player_b.think()

    judge.receive(player_a.move, player_b.move)

    result = judge.rulling()

    pl.append(result)

#print(result)

pylab.plot(pl,'ro')

pylab.show()