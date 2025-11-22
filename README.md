This is a simple Python program I built to practice functions, loops, input validation, and working with lists.
The idea is pretty straightforward: you enter a bunch of player names, choose how many teams you want, and the program randomly splits everyone into teams.

It helped me get a better understanding of how to structure a program using multiple functions and how to handle user input safely.

🎯 What the Program Does

Lets you enter player names one at a time.

You press Enter on an empty line when you’re done.

It makes sure you enter a valid number of teams.

Every team must have at least two players.

Randomly shuffles the players.

Distributes them evenly into teams.

Then prints out each team nicely.

It’s all done using basic Python — no external libraries except the built-in random module.

🧠 How Everything Works

The program is split into a few small functions, which makes it much easier to understand and manage:

get_players()

Asks the user to enter player names one by one and returns a list of all names.

get_number_of_teams(max_teams)

Makes sure the user enters a valid number of teams.
It uses a loop and try/except to keep asking until the input is:

an integer

at least 2

and not more than max_teams (which is calculated based on how many players there are)

create_teams(players, no_of_teams)

Makes a copy of the players list

Shuffles it

Creates empty team lists

Uses modulo (%) to distribute players evenly across teams

Returns the final list of teams

print_teams(teams)

Prints each team in a clean, readable format.

main()

💡 What I Learned

How to break a project into smaller functions

How try/except works for input validation

Using list slicing to copy lists (players[:])

How enumerate() and % can be used together for balanced distribution

Why separating logic into functions makes code much cleaner

This was a great beginner project, and I’m planning to keep improving it over time (like maybe adding the option to rerun the generator without restarting the whole program).

Connects all the pieces together.
