import re

input_file = open("day04_input.txt", 'r');

game_count = 0
total_score = 0

for input_line in input_file:
    scratchie_game = re.split(r': |\|', input_line.strip())
    for winning_number in scratchie_game[1].split():
        if winning_number in scratchie_game[2].split():
            game_count = 1 if game_count == 0 else game_count * 2
    total_score += game_count
    #reset counter
    game_count = 0

print(total_score)