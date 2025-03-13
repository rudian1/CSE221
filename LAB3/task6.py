import sys

def build_post_order(inorder_seq, pre_order_seq, index_inorder_map, in_bam, in_dan, index):
    if in_bam > in_dan:
        return []

    first = pre_order_seq[index[0]]
    index[0] += 1
    root_idx = index_inorder_map[first]
    bam_post_order = build_post_order(inorder_seq,pre_order_seq,index_inorder_map, in_bam, root_idx - 1, index)
    dan_post_order = build_post_order(inorder_seq,pre_order_seq,index_inorder_map, root_idx + 1, in_dan, index)

    return bam_post_order + dan_post_order + [first]

input_data = sys.stdin.read().splitlines()
n = int(input_data[0])
inorder_str = input_data[1].split()
preorder_str = input_data[2].split()
inorder_seq = []
pre_order_seq = []
for i in range(n):
    inorder_seq.append(int(inorder_str[i]))
for i in range(n):
    pre_order_seq.append(int(preorder_str[i]))
index_inorder_map = {}
for i in range(n):
    index_inorder_map[inorder_seq[i]] = i
index = [0]
post_order = build_post_order(inorder_seq, pre_order_seq, index_inorder_map, 0, n - 1, index)
output_str = ""
for i in range(n):
    output_str += str(post_order[i]) + " "
sys.stdout.write(output_str.strip() + "\n")