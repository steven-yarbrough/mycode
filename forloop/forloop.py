#!/usr/bin/env python3

#for  loop that prins the contents of the list,dictionary

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
for farm in farms:
    if farm["name"] == "NE Farm":
        print(farm["agriculture"])
