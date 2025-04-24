"""
Помимо того чтобы логи писать, нужно их ещё и уметь читать,
иначе мы будем как в известном анекдоте, писателями, а не читателями.

Для вас мы написали простую функцию обхода binary tree по уровням.
Также в репозитории есть файл с логами, написанными этой программой.

Напишите функцию restore_tree, которая принимает на вход путь до файла с логами
    и восстанавливать исходное BinaryTree.

Функция должна возвращать корень восстановленного дерева

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass

Примечание: гарантируется, что все значения, хранящиеся в бинарном дереве уникальны
"""
import itertools
import logging
import random
from collections import deque, defaultdict
from dataclasses import dataclass
from typing import Optional, Dict
import re

logger = logging.getLogger("tree_walk")


@dataclass
class BinaryTreeNode:
    val: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def walk(root: BinaryTreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


counter = itertools.count(random.randint(1, 10 ** 6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)
    node_right = get_tree(max_depth - 1, level=level + 1)
    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node


def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    node_dict: Dict[int, BinaryTreeNode] = {}
    children_map = defaultdict(dict)  # val: {"left": left_val, "right": right_val}
    root_val = None

    with open(path_to_log_file, "r") as f:
        for line in f:
            # Visiting <BinaryTreeNode[123]>
            visit_match = re.search(r"Visiting <BinaryTreeNode\[(\d+)\]>", line)
            if visit_match:
                val = int(visit_match.group(1))
                if root_val is None:
                    root_val = val
                if val not in node_dict:
                    node_dict[val] = BinaryTreeNode(val)
                continue

            # <BinaryTreeNode[123]> left is not empty. Adding <BinaryTreeNode[456]> to the queue
            left_match = re.search(
                r"<BinaryTreeNode\[(\d+)\]> left is not empty\. Adding <BinaryTreeNode\[(\d+)\]>", line)
            if left_match:
                parent, child = map(int, left_match.groups())
                children_map[parent]["left"] = child
                continue

            # <BinaryTreeNode[123]> right is not empty. Adding <BinaryTreeNode[456]> to the queue
            right_match = re.search(
                r"<BinaryTreeNode\[(\d+)\]> right is not empty\. Adding <BinaryTreeNode\[(\d+)\]>", line)
            if right_match:
                parent, child = map(int, right_match.groups())
                children_map[parent]["right"] = child
                continue

    # Создаем все узлы
    for val in children_map:
        if val not in node_dict:
            node_dict[val] = BinaryTreeNode(val)
        for child_side in ["left", "right"]:
            child_val = children_map[val].get(child_side)
            if child_val is not None and child_val not in node_dict:
                node_dict[child_val] = BinaryTreeNode(child_val)

    # Устанавливаем связи
    for parent_val, links in children_map.items():
        parent_node = node_dict[parent_val]
        if "left" in links:
            parent_node.left = node_dict[links["left"]]
        if "right" in links:
            parent_node.right = node_dict[links["right"]]

    return node_dict[root_val]


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        filename="walk_log_4.txt",
    )

    root = get_tree(7)
    walk(root)
