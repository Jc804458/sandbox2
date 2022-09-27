# display menu
# get choice
# while choice != <quit option>
#     if choice == <first option>
#         <do first task>
#     else if choice == <second option>
#         <do second task>
#     ...
#     else if choice == <n-th option>
#         <do n-th task>
#     else
#         display invalid input error message
#     display menu
#     get choice
#


def main():
    score = get_score()
    while (score < 0) or (score > 100):
        print("Invalid score")
        score = get_score()
    if score >= 90:
        print("Excellent")
    elif score < 50:
        print("bad")
    else:
        print("passable")


def get_score():
    score = float(input("Enter score: "))
    return score


main()
