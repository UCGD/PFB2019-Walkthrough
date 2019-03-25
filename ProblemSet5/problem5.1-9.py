#!/usr/bin/env python3

import sys

fav = {
    'book' : 'The Road',
    'song' : 'Kurt Vile - Outlaw',
    'tree' : 'Palm'
}

for k in fav.keys():
    print(k)
viewItem = input("Enter which favorite item you want to see: ")
print(fav.get(viewItem))

addItem = input("Add another favorite item: (y/n)")
if addItem:
    itemKey = input("Favorate name: ")
    valueKey = input("Favorate thing: ")
    fav[itemKey] = valueKey

for k, v in fav.items():
    print(k, '--', v)

