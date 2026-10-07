import time
import chess
import puzzle #Karışık olmasın diye ayrı yazdım

def move_cleaner(move):
    clear_move = ""
    garbish = []
    wrong_worlds = ["+","#","x"]
    for chracter in move.lower():
        if chracter not in wrong_worlds:
            clear_move += chracter
        else:
            garbish.append(chracter)
    return clear_move.strip()
    
def board_display(board):
    print(board)

def play_puzzle(puzzle_data):
    print(f"\nMarch: {puzzle_data['match']}")
    print(f"Goals: {puzzle_data['desc']}\n")
    
    board = chess.Board(puzzle_data["fen"])
    board_display(board)

    moves = puzzle_data["moves"]
    current_index = 0
    while current_index < len(moves):
        user_move = input("Your move:")
        clean_user_move = move_cleaner(user_move)

        if clean_user_move == moves[current_index]:
            print(" Correct Move!")
            current_index += 1

            # Eğer bulmaca henüz bitmediyse rakibin cevabını oynatıyoruz
            if current_index < len(moves):
                opponent_move = moves[current_index]
                print(f"Oppenent Move: {opponent_move}")
                current_index += 1
        else:
            print(" Wrong Move! Try Again.")

    print("\n Congratulations, you have successfully solved the puzzle!\n")
    return True        

play_puzzle(puzzle.PUZZLES["easy"][0])    


