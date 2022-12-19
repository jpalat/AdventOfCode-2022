import argparse






def score(game):
    # score 0: loss; 3: draw; 6 win
    scoring = {'loss':0, 'draw':3, 'win':6}
    moves_us = ['X', 'Y', 'Z'] # rock, paper, scisors
    moves_them = ['A', 'B', 'C'] # rock, paper, scisors
    victory = {'A X': 'draw', 'A Y': 'win', 'A Z': 'loss',
            'B X': 'loss', 'B Y': 'draw', 'B Z': 'win',
            'C X': 'win', 'C Y': 'loss', 'C Z': 'draw'}

    clean= game.rstrip()
    them, us = clean.split(' ')
    our_move = moves_us.index(us) + 1
    outcome = victory[clean]
    return scoring[outcome] + our_move

def score_new(game):
    result_options = ['X', 'Y', 'Z'] # lose, draw, win
    scoring = {'X':0, 'Y':3, 'Z':6}
    game_moves = ['A', 'B', 'C'] # rock, paper, scisors
    strategy = {'A X': 'C', 'A Y': 'A', 'A Z': 'B',
            'B X': 'A', 'B Y': 'B', 'B Z': 'C',
            'C X': 'B', 'C Y': 'C', 'C Z': 'A'}

    clean= game.rstrip()
    them, result = clean.split(' ')
    
    move = strategy[clean]
    score = scoring[result]  + game_moves.index(move) + 1
    # print('Match', clean, 'result', result, 'score',  score)
    return score
    


def score_total(guide, part=False):
    total = 0
    for i in guide:
        if part:
            total = score_new(i) + total
        else:
            total = score(i) + total
    return total

    
     

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("-p", "--part", action="store_true")


    args = parser.parse_args()
    with open(args.file) as my_file:
        input = my_file.readlines()

    print('Total: ', score_total(input, args.part))
        
    

if __name__ == "__main__":
    main()