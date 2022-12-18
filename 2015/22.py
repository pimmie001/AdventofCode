damage = 8 # input
inf = float('inf')

def play(state, memo={}, part2=False):
    if state in memo:
        return memo[state]

    manaspent, boss_hp, player_hp, mana, player_turn, shield_effect, poison_effect, recharge_effect = state


    #####
    if part2 and player_turn:
        player_hp -= 1 # extra line
    #####


    if player_hp <= 0:
        return inf


    ### effects
    if shield_effect:
        armor = True
        shield_effect -= 1
    else:
        armor = False

    if poison_effect:
        boss_hp -= 3
        poison_effect -= 1

    if recharge_effect:
        mana += 101
        recharge_effect -= 1


    if boss_hp <= 0:
        return manaspent


    if player_turn:
        options = []
        if mana < 53:
            return inf
        else:
            nstate = (manaspent+53, boss_hp-4, player_hp, mana-53, 1-player_turn, shield_effect, poison_effect, recharge_effect)
            options.append(nstate)
        if mana >= 73:
            nstate = (manaspent+73, boss_hp-2, player_hp+2, mana-73, 1-player_turn, shield_effect, poison_effect, recharge_effect)
            options.append(nstate)
        if mana >= 113 and shield_effect == 0:
            nstate = (manaspent+113, boss_hp, player_hp, mana-113, 1-player_turn, 6, poison_effect, recharge_effect)
            options.append(nstate)
        if mana >= 173 and poison_effect == 0:
            nstate = (manaspent+173, boss_hp, player_hp, mana-173, 1-player_turn, shield_effect, 6, recharge_effect)
            options.append(nstate)
        if mana >= 229 and recharge_effect == 0:
            nstate = (manaspent+229, boss_hp, player_hp, mana-229, 1-player_turn, shield_effect, poison_effect, 5)
            options.append(nstate)

        result = inf
        for option in options:
            result = min(result, play(option, memo, part2))
        memo[state] = result
        return result

    else: # boss turn
        if armor: 
            player_hp -= 1
        else:
            player_hp -= damage

        nstate = (manaspent, boss_hp, player_hp, mana, 1-player_turn, shield_effect, poison_effect, recharge_effect)
        result = play(nstate, memo, part2)
        memo[state] = result
        return result 


manaspent = 0
boss_hp = 55 # input
player_hp = 50
mana = 500
player_turn = 1
shield_effect = 0
poison_effect = 0
recharge_effect = 0

state = manaspent, boss_hp, player_hp, mana, player_turn, shield_effect, poison_effect, recharge_effect
print(play(state, {})) # 953
print(play(state, {}, part2=True)) # 1289
