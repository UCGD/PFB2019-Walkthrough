#!/usr/bin/env python3

taxa = "sapiens, erectus, neanderthalensis"

print(taxa)
print("Printing taxa[1]: ", taxa[1])
print("what type: ", type(taxa))

species = taxa.split(", ")
print(species)

print("species 1: ", species[1])
print("what type: ", type(species[1]))
print("Sorted: ", sorted(species))

## Sort the list by length of each string and print
sorted([len(name) for name in species])
print("Sorted based on len: ", species)
print("Sorted based on using key function: ", sorted(species, key=len))
