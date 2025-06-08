# breadth first search
# def bfs(data, start, visited=set()):
#
#     queue = [start]
#
#     while queue:
#         current_node = queue.pop(0)
#         if current_node not in visited:
#             print(current_node, end=" ")
#         visited.add(current_node)
#
#         for i in data[current_node] - visited:
#             queue.append(i)
#     return
#
#
# if __name__ == '__main__':
#
#     data = {
#         'A': {'B'}, 'B': {'A', 'C', 'D'}, 'C': {'B', 'E'}, 'D': {'B', 'E'},
#         'E': {'C', 'D', 'F'}, 'F': {'E'}
#     }
#
#     bfs(data, 'A')

# BFS Traversal of a graph in python using graph given in dictionary
#
# Implement a function to find whether a path exists for a given set of airline routes. The routes are depicted using graphs as a dictionary of sets, where keys represent as source and elements of sets represent destinations. Print the path if it exists.
#
# Example: A, B, C, D, E, F are the nodes of the graph.
#
# For example, if you are given following data:
#
# data = {
#         'A': {'B'},
#         'B': {'A', 'C', 'D'},
#         'C': {'B', 'E'},
#         'D': {'B', 'E'},
#         'E': {'C', 'D', 'F'},
#         'F': {'E'}
# }
# The resultant graph will be:
# Example: Source is A, Destination is D.
# Expected Output:
# Path : A->B->D


def bfs(data, start, end, visited=[]):
    queue = [start]

    while queue:
        current_node = queue.pop(0)
        if current_node == end:
            print("Path: " + "->".join(visited) + "->" + end)
            return
        visited.append(current_node)

        for i in data[current_node] - set(visited):
            queue.append(i)
    print("Path does not exist!")
    return


if __name__ == '__main__':
    data = {
        'A': {'B'},
        'B': {'C', 'D'},
        'C': {'E'},
        'D': {'E'},
        'E': {'F'},
        'F': set()
    }
    bfs(data, 'A', 'D')
