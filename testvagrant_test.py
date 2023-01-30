class Newspaper:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices

def get_combinations(newspapers, budget, index, combination, combinations):
    if budget < 0:
        return
    if budget == 0:
        combinations.append(list(combination))
        print(combinations)
        return
    for i in range(index, len(newspapers)):
        n = newspapers[i]
        for j in range(7):
            combination.append(n.name)
            get_combinations(newspapers, budget - n.prices[j], i + 1, combination, combinations)
            combination.pop()

def main(budget):
    newspapers = [
        Newspaper("TOI", [3, 3, 3, 3, 3, 5, 6]),
        Newspaper("Hindu", [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4]),
        Newspaper("ET", [4, 4, 4, 4, 4, 4, 10]),
        Newspaper("BM", [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]),
        Newspaper("HT", [2, 2, 2, 2, 2, 4, 4])
    ]

    combinations = []
    get_combinations(newspapers, budget, 0, [], combinations)

    for combination in combinations:
        print(combination)

if __name__ == "__main__":
    main(35)
