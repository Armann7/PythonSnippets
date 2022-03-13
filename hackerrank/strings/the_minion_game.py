import sys


def load_from_stdin() -> str:
    return sys.stdin.readline().strip()


def is_vowel(char: str) -> bool:
    return char in 'AEIOU'


def minion_game(string: str) -> None:
    stuart_score = kevin_score = 0
    score = len(string)
    # Look at string char by char
    for pos in range(len(string)):
        if is_vowel(string[pos]):
            kevin_score += score
        else:
            stuart_score += score
        score -= 1
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = load_from_stdin()
    minion_game(s)
