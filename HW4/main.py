def is_active_path(from_vertex, mid_vertex, to_vertex):
    if (mid_vertex in adjacency[from_vertex] and to_vertex in adjacency[mid_vertex]) or \
            (from_vertex in adjacency[mid_vertex] and (to_vertex in adjacency[mid_vertex] or mid_vertex in adjacency[to_vertex])):
        return mid_vertex not in active_edges
    elif mid_vertex in adjacency[from_vertex] and mid_vertex in adjacency[to_vertex]:
        return depth_first_search(mid_vertex, set())

def depth_first_search(current_vertex, marked_vertices):
    marked_vertices.add(current_vertex)
    if current_vertex in active_edges:
        return True
    for adjacent_vertex in adjacency[current_vertex]:
        if adjacent_vertex not in marked_vertices:
            if depth_first_search(adjacent_vertex, marked_vertices):
                return True
    return False

def has_active_path(start_vertex, mid_vertex, previous_vertex, target_vertex):
    if is_active_path(previous_vertex, mid_vertex, start_vertex):
        assign[start_vertex] = 1
        for adjacent_vertex in back_and_forth_adjacency[start_vertex]:
            if assign[adjacent_vertex] == 0 and has_active_path(adjacent_vertex, start_vertex, mid_vertex, target_vertex):
                return True
        assign[start_vertex] = 0
        if target_vertex == start_vertex:
            return True
    return False

def has_connection(vertex_a, vertex_b):

    if vertex_b not in back_and_forth_adjacency[vertex_a]:
        assign[vertex_a] = 1
        for adjacent_vertex in back_and_forth_adjacency[vertex_a]:
            if assign[adjacent_vertex] == 0:
                assign[adjacent_vertex] = 1
                for next_vertex in back_and_forth_adjacency[adjacent_vertex]:
                    if assign[next_vertex] == 0 and has_active_path(next_vertex, adjacent_vertex, vertex_a, vertex_b):
                            return True
                assign[adjacent_vertex] = 0
        return False
    else:
        return True

num_vertices = int(input())
num_edges = int(input())
adjacency = [[] for _ in range(num_vertices)]
back_and_forth_adjacency = [[] for _ in range(num_vertices)]
assign = [0] * num_vertices

for _ in range(num_edges):
    from_vertex, to_vertex = map(int, input().split("->"))
    from_vertex -= 1
    to_vertex -= 1
    adjacency[from_vertex].append(to_vertex)
    back_and_forth_adjacency[from_vertex].append(to_vertex)
    back_and_forth_adjacency[to_vertex].append(from_vertex)

num_tests = int(input())

for _ in range(num_tests):
    vertex_a = int(input())
    vertex_a -= 1
    vertex_b = int(input())
    vertex_b -= 1
    active_edges = list(map(int, input().split(" ")))

    for i in range(len(active_edges)):
        active_edges[i] -= 1

    assign = [0] * num_vertices
    print(not has_connection(vertex_a, vertex_b))
