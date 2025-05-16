import random

class Runner:
    def __init__(self, id, start):
        self.id = id
        self.steps = 0
        self.pos = start

    def roll_dice(self):
        self.steps = random.randint(1, 3)

    def move(self, board):
        self.check_before_move(board)
        for _ in range(self.steps):
            i = board[self.pos].index(self)
            for runner in board[self.pos][i:]:
                runner.pos += 1
                board[runner.pos].append(runner)
            board[self.pos-1][i:] = []
            if self.pos == len(board)-1:
                return True
            self.check_stack(board[self.pos])
        return False

    def check_before_turn(self, order):
        pass

    def check_before_move(self, board):
        pass

    def check_stack(self, stack):
        i = stack.index(self)
        self.check_after_step(stack)
        if i > 0:
            stack[i-1].check_after_step(stack)

    def check_after_step(self, stack):
        pass


class Changli(Runner):
    def __init__(self, start = 0):
        super().__init__("Changli", start)
        self.delayed = False

    def check_before_turn(self, order):
        if self.delayed:
            order.remove(self)
            order.append(self)
            self.delayed = False

    def check_after_step(self, stack):
        if stack.index(self) > 0 and random.random() < 0.65:
            self.delayed = True


class Jinhsi(Runner):
    def __init__(self, start = 0):
        super().__init__("Jinhsi", start)

    def check_after_step(self, stack):
        if stack.index(self) != len(stack)-1 and random.random() < 0.4:
            stack.remove(self)
            stack.append(self)


class Shorekeeper(Runner):
    def __init__(self, start = 0):
        super().__init__("Shorekeeper", start)

    def roll_dice(self):
        self.steps = random.randint(2, 3)


class Carlotta(Runner):
    def __init__(self, start = 0):
        super().__init__("Carlotta", start)

    def roll_dice(self):
        self.steps = random.randint(1, 3)
        if random.random() < 0.28:
            self.steps *= 2


class Calcharo(Runner):
    def __init__(self, start = 0):
        super().__init__("Calcharo", start)

    def check_before_move(self, board):
        for stack in board:
            if stack:
                if stack[0] == self:
                    self.steps += 4
                break


class Camellya(Runner):
    def __init__(self, start = 0):
        super().__init__("Camellya", start)

    def move(self, board):
        if random.random() < 0.5:
            self.steps += len(board[self.pos]) - 1
            for _ in range(self.steps):
                board[self.pos].remove(self)
                self.pos += 1
                board[self.pos].append(self)
                if self.pos == len(board)-1:
                    return True
                self.check_stack(board[self.pos])
            return False
        else:
            return super().move(board)


class Roccia(Runner):
    def __init__(self, start = 0):
        super().__init__("Roccia", start)


class Brant(Runner):
    def __init__(self, start = 0):
        super().__init__("Brant", start)


class Cantarella(Runner):
    def __init__(self, start = 0):
        super().__init__("Cantarella", start)


class Zani(Runner):
    def __init__(self, start = 0):
        super().__init__("Zani", start)


class Cartethyia(Runner):
    def __init__(self, start = 0):
        super().__init__("Cartethyia", start)


class Phoebe(Runner):
    def __init__(self, start = 0):
        super().__init__("Phoebe", start)
