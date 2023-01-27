import json
import sys


def load() -> list:
    result = []
    count_feeds = int(sys.stdin.readline().strip())
    for _ in range(count_feeds):
        feed = json.loads(sys.stdin.readline().strip())
        result.extend(feed["offers"])
    return result


def main():
    data = load()
    data.sort(key=lambda d: (d["price"], d["offer_id"]))
    print(json.dumps({"offers": data}))


if __name__ == "__main__":
    main()

