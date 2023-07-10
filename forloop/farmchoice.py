#!/usr/bin/env python3

#ask the user to pick a farm. Return the plants/animals that are raised on that farm.

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
farm_choice = input("Choose a farm (NE Farm, W Farm, or SE Farm): ")
for farm in farms:
    if farm["name"] == farm_choice:
        print(farm["agriculture"])
