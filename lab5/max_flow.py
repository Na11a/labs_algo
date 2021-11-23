import math


def get_max_vertex(current_vertex, graph, vertex_viewed):
    min_flow = 0
    vertex = -1
    for i, w in enumerate(graph[current_vertex]):
        if i in vertex_viewed:
            continue

        if w[2] == 1:
            if min_flow < w[0]:
                min_flow = w[0]
                vertex = i
        else:
            if min_flow < w[1]:
                min_flow = w[1]
                vertex = i
    return vertex


def get_max_flow(mark):
    w = [x[0] for x in mark]
    return min(*w)


def update_graph(graph, mark, flows):
    for vertex in mark:
        if vertex[1] == -1:
            continue

        sgn = graph[vertex[2]][vertex[1]][2]

        graph[vertex[1]][vertex[2]][0] -= flows * sgn
        graph[vertex[1]][vertex[2]][1] += flows * sgn

        graph[vertex[2]][vertex[1]][0] -= flows * sgn
        graph[vertex[2]][vertex[1]][1] += flows * sgn


def max_flow(graph, init, end):
    first_vertex = (math.inf, -1, init)
    max_flow_vertex = init
    flows = []
    while max_flow_vertex != -1:
        current_vertex = init
        mark = [first_vertex]
        vertex_viewed = {init}

        while current_vertex != end:
            max_flow_vertex = get_max_vertex(current_vertex, graph,
                                             vertex_viewed)
            if max_flow_vertex == -1:
                if current_vertex == init:
                    break
                else:
                    current_vertex = mark.pop()[2]
                    continue

            current_flow = graph[current_vertex][max_flow_vertex][1] if graph[current_vertex][max_flow_vertex][
                                                                            2] != 1 else \
                graph[current_vertex][max_flow_vertex][0]
            mark.append((current_flow, max_flow_vertex, current_vertex))
            vertex_viewed.add(max_flow_vertex)

            if max_flow_vertex == end:
                flows.append(get_max_flow(mark))
                update_graph(graph, mark, flows[-1])
                break

            current_vertex = max_flow_vertex
    return sum(flows)



