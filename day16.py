from time import perf_counter
import numpy as np
def main():
    with open("data/day16_data.txt") as f:
        data = f.readlines()

    h_matrix = np.zeros((len(data),len(data)))

    valves = {}

    for line in data:
        line = line.strip().split(" ")
        valves[line[1]] = {
            "i" : -1,
            "flow_rate" : int(line[4].lstrip("rate=").rstrip(";")),
            "leads" : [valve.rstrip(",") for valve in line[9:]]
        }

    valves_order_letter = sorted(valves.keys())
    for i, valve in enumerate(valves_order_letter):
        valves[valve]["i"] = i

    for valve, info in valves.items():
        for output_valve in info["leads"]:
            out_idx = valves_order_letter.index(output_valve)
            h_matrix[info["i"], out_idx] = 1
            h_matrix[out_idx, info["i"]] = 1

    def recursive(node_list, node_index, depth):
        new_layer = []
        for node in node_list:
            out_idx = valves[node]["i"]

            if h_matrix[node_index, out_idx] == 0 or depth < h_matrix[node_index, out_idx] != -1:
                h_matrix[node_index, out_idx] = depth
                h_matrix[out_idx, node_index] = depth

            new_layer.extend(valves[node]["leads"])

        if h_matrix[node_index].size - np.count_nonzero(h_matrix[node_index]) == 0:
            return True
        elif depth == h_matrix[node_index].size:
            return False
        else:
            return recursive(new_layer, node_index, depth+1)


    for valve, info in valves.items():
        print(valve)
        h_matrix[info["i"], info["i"]] = -1
        check = recursive(info["leads"],info["i"],1)
        assert check, "Ei onnistunt"

    delete_idxs = []
    for valve, info in valves.items():
        if info["flow_rate"] == 0 and valve != "AA":
            delete_idxs.append(info["i"])

    h_matrix = np.delete(h_matrix, delete_idxs, 0)
    h_matrix = np.delete(h_matrix, delete_idxs, 1)
    valves_order_letter = np.delete(valves_order_letter, delete_idxs,0)

    def brute(best_result, current, not_visited, time, node):
        new_current = current
        for next_node in not_visited:
            if time <= h_matrix[node][next_node] + 1:
                continue

            recursive_not_visited = not_visited.copy()
            recursive_not_visited.remove(next_node)
            new_time = time - h_matrix[node][next_node] - 1
            name = valves_order_letter[next_node]
            new_current = current + new_time * valves[name]['flow_rate']
            best_result = brute(best_result, new_current, recursive_not_visited, new_time, next_node)

        return best_result if new_current < best_result else new_current


    best_result = 0
    for i in range(1,h_matrix.shape[0]):
        not_visited = [num for num in range(1,len(valves_order_letter))]
        time = 30 - h_matrix[0][i] - 1
        name = valves_order_letter[i]
        current_result = time * valves[name]['flow_rate']
        not_visited.remove(i)
        s = perf_counter()
        best_result = brute(best_result, current_result, not_visited, time, i)
        e = perf_counter()
        print(f'Kierros {i}: {e-s:.2f}')

    silver = best_result
    print(f'Silver: {silver}')


if __name__ == "__main__":
    main()