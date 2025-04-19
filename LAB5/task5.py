num_nodes, num_edges = map(int, input().split())
adj_list = [[] for _ in range(num_nodes + 1)]
for _ in range(num_edges):
    src, dest = map(int, input().split())
    adj_list[src].append(dest)


visit_status = [0] * (num_nodes + 1)


def detect_cycle(current_node):
    traversal_stack = [(current_node, 0)]
    current_path = []

    while traversal_stack:
        node, neighbor_index = traversal_stack[-1]
        if visit_status[node] == 0:
            visit_status[node] = 1
            current_path.append(node)
        neighbors = adj_list[node]

        if neighbor_index < len(neighbors):
            next_node = neighbors[neighbor_index]
            traversal_stack[-1] = (node, neighbor_index + 1)
            if visit_status[next_node] == 0:
                traversal_stack.append((next_node, 0))
            elif visit_status[next_node] == 1:
                return True
        else:
            visit_status[node] = 2
            traversal_stack.pop()
            current_path.pop()
    return False


for node_id in range(1, num_nodes + 1):
    if visit_status[node_id] == 0:
        if detect_cycle(node_id):
            print("YES")
            break
else:
    print("NO")


# Grid and diamond collection
num_rows, num_cols = map(int, input().split())
maze_grid = [list(input().strip()) for _ in range(num_rows)]


def collect_diamonds(x_pos, y_pos):
    if x_pos < 0 or x_pos >= num_rows or y_pos < 0 or y_pos >= num_cols or maze_grid[x_pos][y_pos] == '#' or maze_grid[x_pos][y_pos] == 'V':
        return 0
    total_diamonds = 1 if maze_grid[x_pos][y_pos] == 'D' else 0
    maze_grid[x_pos][y_pos] = 'V'
    for delta_x, delta_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        total_diamonds += collect_diamonds(x_pos + delta_x, y_pos + delta_y)
    return total_diamonds


max_diamonds_collected = 0
for row in range(num_rows):
    for col in range(num_cols):
        if maze_grid[row][col] != '#' and maze_grid[row][col] != 'V':
            max_diamonds_collected = max(max_diamonds_collected, collect_diamonds(row, col))


print(max_diamonds_collected)