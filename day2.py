def main():

    def rps(p1, p2):
        if p1 == "A": #Rock
            if p2 == "X": return 0
            elif p2 == "Y": return 1
            else: return -1
        elif p1 == "B": #Paper
            if p2 == "X": return -1
            elif p2 == "Y": return 0
            else: return 1
        else: #Scissors
            if p2 == "X": return 1
            elif p2 == "Y": return -1
            else: return 0
    
    # Made a second solution
    def rps2(p1, p2, outcomes=[[0, 1, -1], [-1, 0, 1], [1, -1, 0]]):
        # We use the ascii to determine the correct result from decision matrix 
        # (A = 65) and (X = 88)
        return outcomes[ord(p1) - 65][ord(p2) - 88]


    def score_fun(p1,p2):
        if p1 == "A": #Rock
            if p2 == "X": return 3
            elif p2 == "Y": return 4
            else: return 8
        elif p1 == "B": #Paper
            if p2 == "X": return 1
            elif p2 == "Y": return 5
            else: return 9
        else: #Scissors
            if p2 == "X": return 2
            elif p2 == "Y": return 6
            else: return 7
    
    with open("Advent_of_code22/day2_data.txt", "r") as f:
        data = f.readlines()

    ascii_X = ord('X')
    player2_score_counter = 0
    ultra_top_secret_score = 0
    ultra_top_secret_score2 = 0
    second_part_outcomes = [[3,1,2],[1,2,3],[2,3,1]]

    for game in data:
        player1_input = game[0]
        player2_input = game[2]

        # First part of the puzzle
        game_result = rps2(player1_input, player2_input)
        player2_score_counter += (game_result + 1) * 3 + ord(player2_input) - ascii_X + 1

        # Second part of the puzzle
        # Kinda cheating: Just calculate all the different outcomes
        ultra_top_secret_score += score_fun(player1_input, player2_input)

        # We can reuse the other the function in the second part by inserting new outcomes
        choice_score = rps2(player1_input,player2_input, second_part_outcomes)
        ultra_top_secret_score2 += (ord(player2_input)-ascii_X) * 3 + choice_score

    print(player2_score_counter, f"time: {t:.2f} ms")
    print(ultra_top_secret_score, f"time: {t:.2f} ms")

    
    
if __name__ == "__main__":
    main()