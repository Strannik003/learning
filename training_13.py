player = {
    "name": "Hero",
    "health": 100,
    "gold": 0,
    "level": 1,
    "xp": 0
}

def take_damage(amount):
    if amount < 0:
        return player["health"]
    if (player["health"]-amount) <= 0:
        player["health"] = 0
        return player["health"]
    
    player["health"]-=amount
    return player["health"]
        
    

def heal(amount):
    if amount < 0:
        return player["health"]
    if player["health"] == 0:
        return player["health"]
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
        return player["xp"], player["level"]
    calc = player["xp"]+amount + player["level"]*100
    player["level"] = calc // 100
    player["xp"]= calc % 100
    return player["xp"], player["level"]


def get_status():
     if player["health"]==0:
         return print(f"You are dead, your level was {player['level']}")
     return print(player)

if __name__ == "__main__":
    take_damage(150)
    heal(200)
    get_status()