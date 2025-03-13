import sys

def construct_post_order(in_order, pre_order):
    ind_map = {val: idx for idx, val in enumerate(in_order)}
    stack, post_order = [], []
    pre_order_ind = 0
    in_order_ind = 0

    for value in pre_order:
        stack.append(value)
        while stack and stack[-1] == in_order[in_order_ind]:
            post_order.append(stack.pop())
            in_order_ind += 1

    return post_order

data = sys.stdin.read().splitlines()
n = int(data[0])
in_order = list(map(int, data[1].split()))
pre_order = list(map(int, data[2].split()))

post_order = construct_post_order(in_order, pre_order)
print(" ".join(map(str, post_order)))