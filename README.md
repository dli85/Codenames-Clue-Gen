# Codenames-Clue-Gen

## Codenames Overview

Codenames ia a party game that in which two teams of 4-8 players face off against each other. The "board" consists of 25 cards where each card has a word on one side and a color on the other side. The game starts with all 25 cards with the word side face up. Of the 25 cards, 9 are red, 8 are blue, 1 is black, and the rest are yellow. The goal of each team is to flip over all of the cards of their color using clues. Each team has one spymaster whose goal is to help their team flip over all of their colored-cards by giving clues. The first team to flip over all of their cards wins.

During a team's turn, the spymaster will give a clue that consists of a word and a number. For instance, "Nature 3". This means that there are 3 cards on the board which, in some way, relate to the word "nature" that are of that team's color. The team can then flip over a total of 4 cards. If the team flips over a yellow card, their turn will end. If the team flips over a card with the opposing team's color, their turn will end AND the card will stay flipped over for the opposing team. If the team flips over the black card, they will instantly lose the game.

## Clue Generator overview

The goal of this program is the find a one word clue that can relate two or more words while avoiding 2 or more words. For instance, if I wanted to give a clue that would help my team get the words "phone" and "smoothie" while avoiding the word "orange", the generator should come up with the word "Blackberry" as blackberry was a phone and smoothies are most commonly thought of to contain berries.
