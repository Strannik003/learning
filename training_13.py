player = {
    "name": "Hero",
    "health": 100,
    "gold": 0,
    "level": 1,
    "xp": 0
}

def take_damage(amount):
    if amount < 0:
        return "Amount can not be negative"
    if (player["health"]-amount) <= 0:
        player["health"] = 0
        return "You are dead"
    
    player["health"]-=amount
    return player["health"]
        
    

def heal(amount):
    if amount < 0:
        return "Amount can not be negative"
    if player["health"] == 0:
        return "You are already dead, you can not heal yourself"
    elif (player["health"]+amount) > 100:
        player["health"]=100
        return player["health"]
    else:
        player["health"]+=amount
        return player["health"]

def add_gold(amount):
    if (player["gold"]+amount) <= 0:
        player["gold"] = 0
        return player["gold"]
    player["gold"] += amount
    return player["gold"]

def add_xp(amount):
    if amount < 0:
        return "Amount can not be negative"
    calc = player["xp"]+amount + player["level"]*100
    player["level"] = calc // 100
    player["xp"]= calc % 100
    return player["xp"], player["level"]


def get_status():
     return player


take_damage(50)
heal(20000)
add_xp(135)
get_status()