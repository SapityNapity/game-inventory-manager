import os
players = {
    "Hunain": {
        "inventory": ["AKM", "Kar98k", "Bandage", "Desert Eagle"]
    },
    "Sam": {
        "inventory": ["M416", "UMP45", "Vest", "UMP45", "Bandage"]
    },
    "Jack": {
        "inventory": ["Groza", "Desert Eagle", "Helmet", "Groza", "AKM"]
    }
}
def clear_screen():
    os.system('cls')

def show_inventory(player_name):
    if player_name in players:
        inv = players[player_name]["inventory"]
        print(f"Player: {player_name} || Inventory: {inv}")
    else:
        print("Player not found.")

def count_unique_items(player_name):
    if player_name in players:
        inv = players[player_name]["inventory"]
        unique = set(inv)
        return len(unique)
    else:
        print("Player not found.")
        return None

def has_item(player_name, item):
    if player_name in players:
        inv = players[player_name]["inventory"]
        return item in inv
    else:
        return "Player not found.\n"

def compare_inventories(player1, player2):
    if player1 in players and player2 in players:
        inv1 = set(players[player1]["inventory"])
        inv2 = set(players[player2]["inventory"])

        both_own = inv1 & inv2
        inv1_excl = inv1 - inv2
        inv2_excl = inv2 - inv1

        print(f"\nItems both players own: {both_own}")
        print(f"Items only Player 1({player1}) owns: {inv1_excl}")
        print(f"Items only Player 2({player2}) owns: {inv2_excl}\n")
    else:
        print("Player(s) not found.")

def show_all_players():
    for key in players:
        print(f"{key}\n")

def all_items():
    for items in players.values():
        everything = items["inventory"]
        everything_set = set(everything)
        print(everything_set)


while True:
    clear_screen()

    print("===== GAME INVENTORY MANAGER =====")
    print("1. Show all players\n2. Count unique items\n3. Check for an item\n4. Compare inventories\n5. Show inventory\n6. Exit\n")
    num = int(input("Choose an option 1-6: "))

    if num == 1:
        print("\n--All Players--\n")
        show_all_players()


    elif num == 2:
        show_all_players()
        choice = int(input("Choose a Player (top to bottom, 1-3 respectively): "))
        if choice == 1:
            choice = "Hunain"
            print(f"The player {choice} has {count_unique_items(choice)} items.")
        elif choice == 2:
            choice = "Sam"
            print(f"The player {choice} has {count_unique_items(choice)} items.")
        elif choice == 3:
            choice = "Jack"
            print(f"The player {choice} has {count_unique_items(choice)} items.")
        else:
            print("Please provide the correct input.")



    elif num == 3:
        show_all_players()
        print("\n-All items-\n")
        all_items()
        player_name = input("\nEnter Player Name: ").capitalize()
        item = input("\nChoose an Item: ").capitalize()
        print(f"\n{has_item(player_name, item)}")


    elif num == 4:
        print()
        show_all_players()
        print()
        plyr1 = input("Choose Player 1: ").capitalize()
        plyr2 = input("Choose Player 2: ").capitalize()
        if plyr1 in players and plyr2 in players:
            compare_inventories(plyr1, plyr2)
        else:
            print("\nInvalid Player ID, Choose from the list.")

    elif num == 5:
        show_all_players()
        choice_user = input("Enter Player name: ").capitalize()
        show_inventory(choice_user)


    elif num == 6:
        break

    else:
        print("Please enter the correct number.")


    input("\nPress Enter to continue...")
