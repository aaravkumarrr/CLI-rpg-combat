import character
import enemy
import questionary

def run_combat(player, enemy):
    round = 1
    while player.is_alive() and enemy.is_alive():
        print(f"round {round}")
        round += 1
        print(f"{player} vs {enemy}")
        player_decision = questionary.select("What will you do?", choices = ["1. Attack", "2. Special Ability"]).ask()
        if player_decision == "1. Attack":
            player.attack(enemy)
        elif player_decision == "2. Special Ability":
            player.special_ability(enemy)
        
        if enemy.is_alive():
            enemy.take_turn(player)
        
    if player.is_alive():
        print(f"{player.name} Wins!")
    else:
        print(f"{enemy.name} Wins!")
