# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:39:47 2019

@author: alecc

How it is played:
    Aces Low (execept royal flush)
    if two hands have the same order, highest card counts (even if not in set)
"""
import random as rd
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
colors = ['heart', 'diamonds', 'spades', 'clubs']
deck = [Card(value, color) for value in range(1, 14) for color in colors]
card1 = Card(1, "heart")
card2 = Card(2, "heart")
card3 = Card(3, "heart")
card4 = Card(13, "diamonds")
card5 = Card(5, "heart")
yourcolor = [card1.color,card2.color,card3.color,card4.color,card5.color]
yourval = [card1.value,card2.value,card3.value,card4.value,card5.value]
deck1 = deck
# This next section removes hand from deck, need to make more consice
for i, o in enumerate(deck1):
    if o.color == card1.color and o.value == card1.value:
        del deck1[i]
for i, o in enumerate(deck1):
    if o.color == card2.color and o.value == card2.value:
        del deck1[i]        
for i, o in enumerate(deck1):
    if o.color == card3.color and o.value == card3.value:
        del deck1[i]    
for i, o in enumerate(deck1):
    if o.color == card4.color and o.value == card4.value:
        del deck1[i]
for i, o in enumerate(deck1):
    if o.color == card5.color and o.value == card5.value:
        del deck1[i]
def handmake():
    rd.shuffle(deck1)
    hand = deck1[0:5]
    return(hand)

#hand1 = hand[0]
#hand2 = hand[1]
#hand3 = hand[2]
#hand4 = hand[3]
#hand5 = hand[4]

"""
Scoreing function: ranking is: Royal flush, straigt flush, 4k, full house, flush, straight, 3k 2p, 1p, hk
"""
from itertools import groupby

def score0(col,val):
#define scores of hands
    hk = 0
    onep = 1*14
    twop = 2*14
    threek = 3*14
    straight = 4*14
    flush = 5*14
    fullh = 6*14
    fourk = 7*14
    stfl = 8*14
    rf = 9*14

    scoref = 0
    sort = sorted(val)
    score = sort[-1]
    scoref = hk + score
    a = [len(list(group)) for key, group in groupby(val)] # defines a new matrix that is the occurence of each variable 
    if len(set(val)) == 2: #if only 2 unique values
      for i in a:
          if i == 4:
              scoref = score + fourk
          else:
              scoref = score + fullh
    if len(set(val)) == 3:
        for i in a:
            if i==3:
                scoref = threek+score
            else:
                scoref = twop + score
    if len(set(val)) == 4:
        scoref = onep + score
    if sort == [sort[0],sort[0]+1,sort[0]+2,sort[0]+3,sort[0]+4]:
            scoref = score + straight  
    if len(set(col)) <= 1:
        scoref = flush + score
        if sort == [sort[0],sort[0]+1,sort[0]+2,sort[0]+3,sort[0]+4]:
            scoref = score + stfl  
        if sorted(val) == [1,10,11,12,13]:
            scoref = score + rf      
    return(scoref)   
yours = score0(yourcolor,yourval)
i = 0
wins = 0
trials = 100000
while i < trials:
   i = i +1
   hand = handmake()
   """
   create two matrixes: one for color, one for value
   """
   hcol = [hand[0].color, hand[1].color, hand[2].color, hand[3].color, hand[4].color] 
   hval = [hand[1].value,hand[2].value,hand[3].value,hand[4].value,hand[0].value]
   theirs = score0(hcol,hval)
   if yours >= theirs:
       wins = wins + 1
print(wins/trials)      
print(yours)
    
