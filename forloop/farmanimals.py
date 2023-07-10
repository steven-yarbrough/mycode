#! usr/bin/env/ python3

#Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
farm_choice = input("Choose a farm (NE Farm, W Farm, or SE Farm): ")
for farm in farms:
    if farm["name"] == farm_choice:
        animals = [animal for animal in farm["agriculture"] if animal not in ["carrots", "celery"]]
        print(animals)
