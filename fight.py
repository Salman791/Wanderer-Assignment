from random import *



def fight(hero, villain, villains, villains_movement):
    hero.get_villain_stat(villain)


    if villains_movement:
        attacker = villain
        defender = hero

    else:
        attacker = hero
        defender = villain

    hero.fighting = True

    while hero.attack:

        hero.attack = False

        attacker_sv = randint(1, 6) * 2 + attacker.SP
        defender_sv = randint(1, 6) * 2 + defender.SP

        if attacker_sv > defender.DP:

            defender.HP = defender.HP - (attacker_sv - defender.DP)

            if defender.HP <= 0:
                defender.dead()
                hero.fighting = False

        if defender_sv > attacker.DP and hero.fighting:

            attacker.HP = attacker.HP - (defender_sv - attacker.DP)

            if attacker.HP <= 0:
                attacker.dead()
                hero.fighting = False


    if not hero.fighting:


        if not villain.alive:

            hero.level_up()
            if not villains.villains[0].alive and not villains.villains[1].alive:

                villains.next_level()
                hero.next_level()



        else:


            restart = True
            villains.next_level(restart)