import sys

def final_score(red, blue):
    score = 2 * red + 3 * blue
    return score

def red_blue_nim(red_marbles, blue_marbles, version, start_player, depth):
    print("*******************Welcome to Red Blue Nim Game***************************")
    while red_marbles > 0 and blue_marbles > 0:
        print(f"Red: {red_marbles}, Blue: {blue_marbles}")
        if start_player.lower() == 'computer':
            # Determine which color to pick based on the previous move
            if version == 'standard':
                previous_pile = "blue" if red_marbles % 2 == 0 else "red"
            else:
                previous_pile = "red" if red_marbles % 2 == 0 else "blue"

            if previous_pile == "red":
                color_to_pick = "blue"
            else:
                color_to_pick = "red"

            print(f"Computer moved {color_to_pick}")
            if color_to_pick == "red":
                red_marbles -= 1
            else:
                blue_marbles -= 1
            start_player = "human"
        else:
            print(f"Enter red to remove a red block or blue to remove a blue block: ")
            human_input = input()
            if human_input.lower() == "red":
                red_marbles -= 1
            elif human_input.lower() == "blue":
                blue_marbles -= 1
            else:
                print("Invalid choice. Please select a color between blue and red")
            start_player = "computer"
    
    while red_marbles == 0 or blue_marbles == 0:
        print(f"Red: {red_marbles}, Blue: {blue_marbles}")
        #print(start_player)
        if version == 'standard' or len(sys.argv) <= 3:
            # Determine which color to pick based on the previous move
            if start_player.lower() == 'computer':
              winner = "Computer"
              score = final_score(red_marbles, blue_marbles)
              print(f"{winner} loses {abs(score)} points in {version} version")
              print("Thanks for Playing the Game. Hope you enjoyed!")
              break
            else:
                winner = "Human"
                score = final_score(red_marbles, blue_marbles)
                print(f"{winner} loses {abs(score)} points in {version} version")
                print("Thanks for Playing the Game. Hope you enjoyed!")
                break
            
        elif version == 'misere':
            if start_player.lower() == 'computer':
                  winner = "Computer"
                  score = final_score(red_marbles, blue_marbles)
                  print(f"{winner} loses {abs(score)} points in {version} version")
                  print("Thanks for Playing the Game. Hope you enjoyed!")
                  break
            else:
                winner = "Human"
                score = final_score(red_marbles, blue_marbles)
                print(f"{winner} Wins {abs(score)} points in {version} version")
                print("Thanks for Playing the Game. Hope you enjoyed!")
                break
if len(sys.argv) >= 4:
    red_marbles = int(sys.argv[1])
    blue_marbles = int(sys.argv[2])
    version = sys.argv[3].lower()
    if version not in ['standard', 'misere']:
        version = 'standard'  # Default to standard if version is invalid
    start_player = "computer" if len(sys.argv) <= 5 else sys.argv[4].lower()
else:
    print("Invalid input format. Please use the following format:")
    print("red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>")
    sys.exit(1)

depth_limit = None
if len(sys.argv) >= 6:
    depth_limit = int(sys.argv[5])

red_blue_nim(red_marbles, blue_marbles, version, start_player, depth_limit)
