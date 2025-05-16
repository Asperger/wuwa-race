import random
from collections import Counter
from runner import *

class Game:
    def __init__(self):
        self.board = [list() for _ in range(24)]
        self.board[0] = [Roccia(0), Brant(0), Cantarella(0), Zani(0), Cartethyia(0), Phoebe(0)]

        self.runners = self.ranking()
        random.shuffle(self.runners)

    def ranking(self):
        ranking = []
        for stack in self.board:
            ranking.extend(stack)
        return ranking

    def play(self, verbose=False):
        i = 0
        while True:
            if verbose:
                i+=1
                print(f"Round {i} Current Board:")
                for i, stack in enumerate(self.board):
                    print(f"Stack {i}: {[runner.id for runner in stack]}")
                print("Current Runners:", [runner.id for runner in self.runners])
            for runner in self.runners[:]:
                runner.check_before_turn(self.runners)
            for runner in self.runners:
                runner.roll_dice()
                if runner.move(self.board):
                    return self.ranking()
            random.shuffle(self.runners)

def simulate_games(num_games):
    winners = Counter()
    ranking = Counter()
    skill = Counter()

    for i in range(num_games):
        game = Game()
        result = game.play()
        winners[result[-1].id] += 1
        for i, runner in enumerate(result):
            skill[runner.id] += runner.skill_count
            ranking[runner.id] += len(result)-i

    print("Simulation Results:")
    for runner, wins in sorted(winners.items(), key=lambda x: x[1], reverse=True):
        print(f"{runner}: win rate = {format(wins/num_games, '.1%')}; ideal odd = {0.2*num_games/wins+0.8:.2f}; average rank = {ranking[runner]/num_games:.2f}; average skill count = {skill[runner]/num_games:.2f}")

if __name__ == "__main__":
    simulate_games(10000)
