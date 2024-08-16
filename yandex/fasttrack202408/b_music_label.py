import sys


class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = []
        self.permissions = {}

    def add_child(self, node: 'Node'):
        self.children.append(node)

    def grant(self, user: str, mode: str):
        if user not in self.permissions:
            self.permissions[user] = {}
        self.permissions[user][mode] = True

    def block(self, user: str, mode: str):
        if user not in self.permissions:
            self.permissions[user] = {}
        self.permissions[user][mode] = False

    def get_permissions(self, user: str, mode: str):
        if user in self.permissions:
            if mode in self.permissions[user]:
                return self.permissions[user][mode]
            else:
                return None
        return None


class PermissionSystem:
    def __init__(self):
        self.root = Node('')

    def grant(self, username: str, mode: str, path: str):
        parts = self._split_path(path)
        nodes = self._build_chain(parts)
        nodes[-1].grant(username, mode)

    def block(self, username: str, mode: str, path: str):
        parts = self._split_path(path)
        nodes = self._build_chain(parts)
        nodes[-1].block(username, mode)

    def check(self, username: str, mode: str, path: str) -> bool:
        parts = self._split_path(path)
        for node in self._build_chain(parts)[::-1]:
            permission = node.get_permissions(username, mode)
            if permission is None:
                continue
            return permission

    @staticmethod
    def _split_path(path: str) -> list[str]:
        [_, *parts] = path.split('/')
        if len(parts) == 1 and parts[0] == '':  # path == '/'
            parts = []
        return parts

    def _build_chain(self, parts: list):
        chain = [self.root]
        current_node = self.root
        for part in parts:
            for node in current_node.children:
                if part == node.name:
                    current_node = node
                    break
            else:
                new_node = Node(part)
                current_node.children.append(new_node)
                current_node = new_node
            chain.append(current_node)
        return chain


def main():
    log = []
    lines = sys.stdin.readlines()
    permission_system = PermissionSystem()
    for line in lines:
        line = line.strip()
        command, username, mode, path = line.split(' ')
        if command == 'grant':
            permission_system.grant(username, mode, path)
            log.append('done')
        elif command == 'block':
            permission_system.block(username, mode, path)
            log.append('done')
        elif command == 'check':
            if permission_system.check(username, mode, path):
                log.append('allowed')
            else:
                log.append('forbidden')
    return log


if __name__ == "__main__":
    log = main()
    print(log)
    expected = ['forbidden', 'forbidden', 'forbidden', 'done', 'done', 'allowed', 'forbidden', 'done', 'allowed', 'forbidden']
    assert log == expected
