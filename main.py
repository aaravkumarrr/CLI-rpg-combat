import questionary
import character
from combat import run_combat
import enemy
import player

def main():
    exit = False

    name = input("Welcome! What is your name?\n")
    player_class = questionary.select("What class would you like to play?", choices=["Warrior", "Mage", "Rogue"]).ask()
    if player_class == "Warrior":
        player_char = player.Warrior(name)
    elif player_class == "Mage":
        player_char = player.Mage(name)
    else:
        player_char = player.Rogue(name)

    while not exit:
        player_char.health = player_char.max_health
        enemy_to_fight = questionary.select("Which enemy would you like to battle?", choices=["Goblin", "Dragon"]).ask()

        if enemy_to_fight == "Goblin":
            goblin = enemy.Goblin()
            run_combat(player_char, goblin)
        elif enemy_to_fight == "Dragon":
            dragon = enemy.Dragon()
            run_combat(player_char, dragon)
        
        play_again = questionary.select("Would you like to play again?", choices = ["Yes","No"]).ask()
        if play_again == "No":
            exit = True
        
        if (isinstance(player, player.Mage)):
            player.fireball_used = False
        


if __name__ == "__main__":
    main()
