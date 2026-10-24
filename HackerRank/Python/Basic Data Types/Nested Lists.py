if __name__ == "__main__":
    scores_dict = {}

    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores_dict.setdefault(score, []).append(name)

    second_lowest_score = sorted(set(scores_dict.keys()))[1]

    for name in sorted(scores_dict[second_lowest_score]):
        print(name)
