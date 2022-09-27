def main():
    score = get_score()
    while (score < 0) or (score > 100):
        print("Invalid score")
        score = get_score()
    if score >= 90:
        print()
    elif score < 50:
        print()
    else:
        print()


def get_score():
    score = float(input("Enter score: "))
    return score


main()
