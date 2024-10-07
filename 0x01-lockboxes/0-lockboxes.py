#!/usr/bin/python3

"""
returning True
"""


def canUnlockAll(boxes):
    """
    determining if all boxes can be opened.
    """

    if not boxes:
        return False

    visited = [False] * len(boxes)
    visited[0] = True

    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if 0 <= key < len(boxes) and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
