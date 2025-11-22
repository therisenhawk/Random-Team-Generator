import random

def get_players():

    players_names = [] # This is where you save the names of players

    print("Make sure to enter player's names one by one.")
    print("If you wish to finish, press Enter.\n")

    # Loop for adding the players to the list. If it's empty it breaks the loop.
    while True:
        give_players_names = input("Enter the player's name: ").strip() # strip removes blank spaces
        if give_players_names == "":
            break
        players_names.append(give_players_names) 
        
    return players_names                    

def get_number_of_teams(max_teams):

    while True:         #creates an infinite loop

        #catching errors here with try and ex if user's input is not an integer it will loop until user gives a number

        try:        
            user_input = int(input("How many teams do you want? "))
        except ValueError:
            print("That's not a valid integer. It must be a number. Please try again.")  
            continue
        if 2 <= user_input <= max_teams:
            return user_input
        else:
            print(f"Each team needs to have at least 2 members. Please enter a number between 2 and {max_teams}.")

def create_teams(players, no_of_teams):
   players_copy = players[:] # making a copy of the list so it can be shuffled
   random.shuffle(players_copy)

   # creates list of N empty lists. N is going to be the size of no_of_teams
   # modulo (%) gives remainder after division. If I keep dividing into groups of size X, what is left over?
   # (e.g. no_of_teams = 3) 0 % 3, remainder is 0; 1 % 3  remainder is 1; 2 % 3 remainder is 2; 3 % 3 remainder is 0
   # modulo cycles; for 3 it's 0,1,2,0,1,2,0.....

   teams =[[] for _ in range(no_of_teams)]
   for index, player in enumerate(players_copy): #index gives index and player gives the item from players_copy list
       team_index = index % no_of_teams
       teams[team_index].append(player)
   return teams

def print_teams(teams):
    print("\n----Teams----")
    for i, team in enumerate(teams, start=1): #starts counting from 1 cuz start=1. team is a list from teams list
        print(f"\nTeam {i}:")
        for member in team:     #extracts the actual name from the team list
            print(f" - {member}")

def main():

   players = get_players()   
   print("\nThe Players Are: \n")   
   print(players)     
   if len(players) < 4:
     print("You need at least 2 players to form a team!")
     return
   max_teams = len(players) // 2
   no_of_teams = get_number_of_teams(max_teams)
   print(f"\nYou have chosen {no_of_teams} teams.")
   teams = create_teams(players, no_of_teams) 

   print_teams(teams) 

if __name__ == "__main__":
    main()