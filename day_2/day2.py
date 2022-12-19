import argparse

moves_us = ['X', 'Y', 'Z'] # rock, paper, scisors
moves_them = ['A', 'B', 'C'] # rock, paper, scisors

# score 0: loss; 3: draw; 6 win
scoring = {'loss':0, 'draw':3, 'win':6}
victory = {'A X': 'draw', 'A Y': 'win', 'A Z': 'loss',
            'B X': 'loss', 'B Y': 'draw', 'B Z': 'win',
            'C X': 'win', 'C Y': 'loss', 'C Z': 'draw'}

def score(game):
    clean= game.rstrip()
    them, us = clean.split(' ')
    our_move = moves_us.index(us) + 1
    outcome = victory[clean]
    return scoring[outcome] + our_move

def score_total(guide):
    total = 0
    for i in guide:
        total = score(i) + total
    return total

    
     

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")

    args = parser.parse_args()
    with open(args.file) as my_file:
        input = my_file.readlines()

    print('Total: ', score_total(input))
        
    

if __name__ == "__main__":
    main()