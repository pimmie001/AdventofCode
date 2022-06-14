import itertools

# input
boss= [55, 8]    # hit points, damage
player = [50, 500] # hit points, mana


Strategies = ["Magic missile", "Drain", "Shield", "Poison", "Recharge"]
maxlen = 10


# ################  example input
# boss = [13 ,8]
# player = [10, 250]



possible_strategies= list( itertools.product(Strategies, repeat=maxlen ))


Mana = []
for s in possible_strategies:
    boss_stats = boss.copy()
    player_stats = player.copy()
    mana = 0
    player_turn = 1
    shield_effect = 0
    poison_effect = 0
    recharge_effect = 0
    i = 0
    while boss_stats[0] > 0 and player_stats[0] > 0:

        # Effects
        if shield_effect:
            shield_effect -= 1
        if poison_effect:
            boss_stats[0] -= 3 
            poison_effect -= 1
        if recharge_effect:
            player_stats[1] += 101
            recharge_effect -= 1

        if player_turn:
            if i >= len(s):
                player_stats[0] = 0
                continue
            strategy = s[i]
            i += 1

            if player_stats[1] < 0:
                player_stats[0] = 0
                continue

            if strategy == "Magic missile":
                player_stats[1] -= 53
                mana += 53
                boss_stats[0] -= 4
            elif strategy == "Drain":
                player_stats[1] -= 73
                mana += 73
                boss_stats[0] -= 2
                player_stats[0] += 2
            elif strategy == "Shield":
                if shield_effect:
                    player_stats[0] = 0
                    continue
                else:
                    player_stats[1] -= 113
                    mana += 113
                    shield_effect = 6
            elif strategy == "Poison":
                if poison_effect:
                    player_stats[0] = 0
                    continue
                else:
                    player_stats[1] -= 173
                    mana += 173
                    poison_effect = 6
            elif strategy == "Recharge":
                if recharge_effect:
                    player_stats[0] = 0
                    continue
                else:
                    player_stats[1] -= 229
                    mana += 229
                    recharge_effect = 5

            if player_stats[1] < 0:
                player_stats[0] = 0
                continue


        else: 
            if boss_stats[0] <= 0:
                continue

            if shield_effect:
                player_stats[0] -= max(1, boss_stats[0] - 7)
            else: 
                player_stats[0] -= boss_stats[1]

        player_turn = 1 - player_turn

    player_won = True if player_stats[0] > 0 else False
    if player_won:
        Mana.append(mana)
        

print(min(Mana))