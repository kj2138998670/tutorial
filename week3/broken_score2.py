def main():
    score = get_score()
    final = gudge_result(score)
    print(final)


def gudge_result(score):
    if score < 0 or score > 100:
        final = ("Invalid score")
    elif score < 50:
        final = ("fail")
    elif score < 90:
        final = ("pass")
    else:
        final = ("excellent")
    return final


def get_score():
    score = float(input("Enter score: "))
    return score


main()
