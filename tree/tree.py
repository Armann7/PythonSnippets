from collections import defaultdict
from typing import List, Dict, Any


def build_tree(source: List[tuple]) -> Dict[Any, dict]:
    """
    Строим дерево.
    :param source: список кортежей (родитель, потомок)
    :return: корневой узел
    """
    nodes = defaultdict(dict)
    # Формируем список узлов
    for parent, child in source:
        nodes[parent][child] = None
        if parent:
            nodes[child] = dict()
    # Связываем узлы
    for node in nodes.values():
        for child in node.keys():
            node[child] = nodes[child]
    # Вернем корень
    return nodes[None]
