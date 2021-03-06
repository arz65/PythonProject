#!/usr/bin/env python3

# Python Project : Python script to determine stoichiometric ratios of chemical reactions #1
# Handle imports

from chempy import balance_stoichiometry #importing stoichiometry function
from pprint import pprint # importing pretty print

# 1: Welcome to the tool. Is help required?

print('Hello aspiring chemist!')
print('Please input your reactants. Note: values are case sensitive.')
print('E.g. NH4ClO4, Al, H2O...')
reactants = input('Reactants: ')

print('Now please input your products. Note: values are case sensitive.')
products = input('Products: ')

print(reactants)
print(products) #reactants and products printed for verification

# 2 :determine stoichiometric coefficients of main reactions
reac, prod = balance_stoichiometry({'NH4ClO4', 'Al'}, {'Al2O3', 'AlCl3', 'H2O', 'N2'}) # rxn: ammonium perchlorate + aluminum

pprint(dict(reactants))
pprint(dict(products))
