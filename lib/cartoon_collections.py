def roll_call_dwarves(dwarf_names):
    index = 1
    for dwarf_name in dwarf_names:
        print(f"{index}. {dwarf_name}")
        index +=1
    pass

def summon_captain_planet(planeteer_calls):
    return [element.capitalize() + "!" for element in planeteer_calls]
    pass

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)
    pass

def find_the_cheese(ingredients):
    snacks = ["cheddar", "gouda", "comembert"]
    for ingredient in ingredients:
        if ingredient in snacks:
            return ingredient
    return None 
    pass
