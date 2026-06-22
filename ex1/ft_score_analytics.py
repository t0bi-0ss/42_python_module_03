import sys

if __name__ == "__main__":
    print(" === Player Score Analytics ===")
    if len(sys.argv) < 2:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py",
            " <score1> <score2> ...",
        )
    scores = []
    for item in sys.argv[1:]:
        try:
            score = int(item)
            score_l = [score]
            scores += score_l
        except ValueError:
            print(f"Invalid parameter: '{item}'")
    if not len(scores):
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py",
            " <score1> <score2> ...",
        )
    else:
        print(scores)
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores)/len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores)-min(scores)}")
