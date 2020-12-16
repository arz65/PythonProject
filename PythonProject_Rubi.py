#!/usr/bin/env python3

# Python Project : Python script to determine stoichiometric ratios of chemical reactions

# Imports
from chempy import balance_stoichiometry
from pprint import pprint

# 1: Welcome to the tool.

answer = input('Hello aspiring chemist. Would you like help balancing a chemical reaction? (yes/no)')
if answer == "yes":
    print('Okay!! Happy to help.')
elif answer == "no":
    print('Okay, bye!')
    # Need to input way to quit tool
else:
    print('Please enter yes/no')
    # Need to input a way to not move forward

print('Please input your reactants. Note: values are case sensitive.')
print('E.g. NH4ClO4, Al, H2O...')
reac = input('Reactants: ')

print('Now please input your products. Note: values are case sensitive.')
prod = input('Products: ')

# 2 :determine stoichiometric coefficients of main reactions

reac, prod = balance_stoichiometry({'NH4ClO4', 'Al'}, {'Al2O3', 'AlCl3', 'H2O', 'N2'}) # rxn: ammonium perchlorate + aluminum

pprint(dict(reac))
pprint(dict(prod))

