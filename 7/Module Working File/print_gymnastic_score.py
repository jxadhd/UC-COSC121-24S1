def print_gymnastic_score(mark_gained, maximum=30):
    """
    Presents average score awarded by judges out of max achievable,
    where no max is given use value of 30
    """
    percent = float(round(mark_gained / maximum * 100, 1))
    ratio = f"{float(round(mark_gained, 1))}/{float(round(maximum, 1))}"
    print(f"Your score: {ratio} ({percent}%)")

print_gymnastic_score(20, 40)