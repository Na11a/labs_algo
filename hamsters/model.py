class Hamster:
    def __init__(self, eat_myself, greed):
        self.eat_myself = eat_myself
        self.greed = greed

    def need_food_for_hamster(self, n):
        return self.eat_myself + self.greed * n

    @staticmethod
    def get_hamsters(file):
        with open(file, 'r') as f:
            s = int(f.readline())
            c = int(f.readline())
            hamsters = []
            for _ in range(c):
                hamster = Hamster(*list(map(int, f.readline().split(" "))))
                if hamster.eat_myself <= s:
                    hamsters.append(hamster)
        return hamsters, s

    @staticmethod
    def can_buy(file):
        hamsters, all_food = Hamster.get_hamsters(file)
        result = 0
        avaliable_food = 0
        while avaliable_food <= all_food:
            avaliable_food = sum(hamster.need_food_for_hamster(result) for hamster in hamsters[:result])
            result += 1
            if avaliable_food > all_food: result -= 1
        return result
