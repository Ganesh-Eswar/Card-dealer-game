# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 07:29:27 2022

@author: mmanivan
"""
from typing import Optional,List

def get_deck_of_cards(deck_name: Optional[str] ='blue',num_jokers: Optional[int]=2)-> List[str]:
    """
    Request a neatly arranged deck of cards

    Parameters
    ----------
    deck_name : str, optional
        The name of the deck of cards. The default is 'blue'
    num_jokers : int, optional
        The number of jokers. The default is 2.

    Returns
    -------
    list[str] : 
        The deck of cards will be listed as shown in this example
        ['blue_ace_hearts','blue_2_hearts','blue_3_hearts'.....,
         'blue_ace_spades','blue_2_spades','blue_3_spades'.....,
         'blue_ace_clubs','blue_2_clubs','blue_3_clubs'.......,
         'blue_ace_diamonds','blue_2_diamonds','blue_3_diamonds',
         'blue_joker_1','blue_joker_2']

    """
    
    ranks=['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
    suites=['hearts','spades','clubs','diamonds']
    deck=[]
    
    for suite in suites:
        for card in ranks:
            deck.append("_".join([deck_name,card,suite]))
    
    if(num_jokers > 0):
        for iind in range(num_jokers):
            deck.append("_".join([deck_name,'joker',str(iind+1)]))
        
    return deck


def shuffle_deck(decks:List[str]) -> List[str]:
    """
    Takes a list of cards and shuffles them returns the list back
    
    ***
    Students need to write this function
    Hint: "https://www.w3schools.com/python/ref_random_shuffle.asp"
    or build your own shuffler
    ***
    
    Parameters
    ----------
    decks : List[str]
        a list of cards

    Returns
    -------
    List[str]
        a shuffled list of cards.

    """
    
    
def deal_cards(decks:List[str],num_players:int,num_cards_per_player:int)-> List[List[str]]:
    """
    
    ***
    Students need to write this function
    ***

    Parameters
    ----------
    decks : List[str]
        List of cards
    num_players : int
        number of players in the game
    num_cards_per_player : int
        number of cards to be dealt to the player

    Returns
    -------
    List[List[str]]
        list of lists of cards, 
        one list per player and the remaining list of cards if present
    """

if __name__ == "__main__":
    
    # Get Murugan Deck of Cards
    murugan_deck=get_deck_of_cards('Murugan',2)
    
    # Get Kuruvi Deck of Cards
    kuruvi_deck=get_deck_of_cards('Kuruvi',2)
    
    # Merge the Deck of Cards
    # Students need to write this code
    merged_deck=[]
    
    # Shuffle the Deck of Cards
    shuffle_deck(merged_deck)
    
    number_of_players = 6
    
    number_of_cards_per_player = 6
    
    # Deal the deck of cards
    [player1_cards,player2_cards,
     player3_cards,player4_cards,
     player5_cards,player6_cards,
     remaining_cards]=deal_cards(merged_deck,6,6)
    
    #Print each players cards