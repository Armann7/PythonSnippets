import sys
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data: str):
        if data.find("\n") >= 0:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(f"{data}")

    def handle_data(self, data):
        if data.strip() != "":
            print(">>> Data")
            print(f"{data}")


def load_from_stdin() -> str:
    data = ""
    lines = int(sys.stdin.readline().strip())
    for line in range(lines):
        data = data + sys.stdin.readline().strip() + "\n"
    return data


def main():
    data = load_from_stdin()
    parser = MyHTMLParser()
    parser.feed(data)
    parser.close()


if __name__ == "__main__":
    main()
