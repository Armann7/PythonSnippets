import sys
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            val = attr[1] if attr[1] != "" else "None"
            print(f"-> {attr[0]} > {val}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            val = attr[1] if attr[1] != "" else "None"
            print(f"-> {attr[0]} > {val}")
            

def load_from_stdin() -> str:
    data = ""
    lines = int(sys.stdin.readline().strip())
    for line in range(lines):
        data = data + sys.stdin.readline().strip()
    return data


def main():
    data = load_from_stdin()
    parser = MyHTMLParser()
    parser.feed(data)


if __name__ == "__main__":
    main()
