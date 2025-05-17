#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import Counter
import operator

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]


def _wine_cheese_score(wine: str, cheese: str) -> float:
    if cheese not in CHEESES:
        raise ValueError
    if not (wine in RED_WINES or wine in WHITE_WINES or wine in SPARKLING_WINES):
        raise ValueError

    wine_letters = Counter()
    for c in wine:
        wine_letters[c.lower()] += 1

    cheese_letters = Counter()
    for c in cheese:
        cheese_letters[c.lower()] += 1

    intersection_sum = 0
    for c, num in wine_letters.items():
        intersection_sum += min(wine_letters[c], cheese_letters[c])

    return intersection_sum / (1 + pow(len(wine) - len(cheese), 2))


def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    all_wines = []
    if wine_type == "red" or wine_type == "all":
        all_wines.append(RED_WINES)
    if wine_type == "white" or wine_type == "all":
        all_wines.append(WHITE_WINES)
    if wine_type == "sparkling" or wine_type == "all":
        all_wines.append(SPARKLING_WINES)
    if len(all_wines) == 0:
        raise ValueError

    best_wines_cheeses = []
    for wine_list in all_wines:
        wines_cheeses = []
        for wine in wine_list:
            for cheese in CHEESES:
                wines_cheeses.append((wine, cheese, _wine_cheese_score(wine, cheese)))
        best_wines_cheeses.append(sorted(wines_cheeses, key=lambda tup: tup[2])[-1])

    return sorted(best_wines_cheeses, key=lambda tup: tup[2])[-1]


def match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """
    all_wines_5cheeses = []
    for wine_list in [WHITE_WINES, RED_WINES, SPARKLING_WINES]:
        for wine in wine_list:
            scored_cheeses = []
            for cheese in CHEESES:
                scored_cheeses.append((cheese, _wine_cheese_score(wine, cheese)))

            scored_cheeses = [cheese[0] for cheese in sorted(scored_cheeses, key=lambda tup: (-tup[1], tup[0]))][:5]
            all_wines_5cheeses.append((wine, scored_cheeses))
    return sorted(all_wines_5cheeses, key=lambda tup: tup[0])


if __name__ == "__main__":
    print(match_wine_5cheeses())