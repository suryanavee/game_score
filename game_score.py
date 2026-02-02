player_name = input("Enter Player Name: ")
games_played = int(input("Enter Number Of Games Played: "))
total_score = int(input("Enter Total Score: "))

if games_played > 0:
    average_score = total_score / games_played
else:
    average_score = 0

print(f"Player : {player_name}")
print()
print(f"Games Played : {games_played}")
print()
print(f"Total Score : {total_score}")
print()
print(f"Average Score : {average_score}")

