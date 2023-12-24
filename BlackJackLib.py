# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:46:10 2023

@author: Haida
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import random

def shuffle_deck(deck):
    l = list(deck.items())
    random.shuffle(l)
    deck = dict(l)
    return deck



class Deck:
    def __init__(self):
        deck_dict_1  = {"as_hearts":1, "two_hearts":2, "three_hearts":3, "four_hearts":4, "five_hearts":5, "six_hearts":6, "seven_hearts":7, "eight_hearts":8, 
 "nine_hearts":9, "ten_hearts":10, "jack_hearts":10, "queen_hearts":10, "king_hearts":10}

        deck_dict2 = {"as_diamonds":1, "two_diamonds":2, "three_diamonds":3, "four_diamonds":4, "five_diamonds":5, "six_diamonds":6, "seven_diamonds":7, "eight_diamonds":8, 
     "nine_diamonds":9, "ten_diamonds":10, "jack_diamonds":10, "queen_diamonds":10, "king_diamonds":10}

        deck_dict3 = {"as_spades":1, "two_spades":2, "three_spades":3, "four_spades":4, "five_spades":5, "six_spades":6, "seven_spades":7, "eight_spades":8, 
     "nine_spades":9, "ten_spades":10, "jack_spades":10, "queen_spades":10, "king_spades":10}

        deck_dict4 = {"as_clubs":1, "two_clubs":2, "three_clubs":3, "four_clubs":4, "five_clubs":5, "six_clubs_clubs":6, "seven_clubs":7, "eight_clubs":8, 
     "nine_clubs":9, "ten_clubs":10, "jack_clubs":10, "queen_clubs":10, "king_clubs":10}

        deck_dict_1.update(deck_dict2)
        deck_dict_1.update(deck_dict3)
        deck_dict_1.update(deck_dict4)
    
        self = shuffle_deck(deck_dict_1)
    

    
    def shuffle(self):
        l = list(self.items())
        random.shuffle(l)
        self = dict(l)
        return self
    
