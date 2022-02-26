import re
import sys


def load_from_stdin() -> str:
    data = ""
    lines = int(sys.stdin.readline().strip())
    for line in range(lines):
        data = data + sys.stdin.readline().strip()
    return data


def main():
    data = load_from_stdin()
    colors: list[str] = []
    # Выкусываем блоки в скобках
    for block in re.findall(r"{.*?}", data):
        block = block.replace(" ", "").replace("{", "").replace("}", "")
        # Бьем на токены вида свойство: значение
        for token in re.findall(r".*?:.*?;", block):
            # В токенах выискиваем коды цветов
            for color in re.findall(r"#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3}", token):
                colors.append(color)

    for color in colors:
        print(color)


if __name__ == "__main__":
    main()
