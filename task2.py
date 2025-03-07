import sys
import heapq
def mrg_sort_list():
    numput1 = int(sys.stdin.readline().strip())
    alc = list(map(int, sys.stdin.readline().strip().split()))
    numput2 = int(sys.stdin.readline().strip())
    bob = list(map(int, sys.stdin.readline().strip().split()) )
    mrg = heapq.merge(alc, bob)
    sys.stdout.write(" ".join(map(str, mrg)) + "\n")
mrg_sort_list()