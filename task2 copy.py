import sys
def merge_sorted_lists():
    # Read the input for Alice's list
    numput1 = int(sys.stdin.readline().strip())
    alc = list(map(int, sys.stdin.readline().strip().split()))

    # Read the input for Bob's list
    numput2 = int(sys.stdin.readline().strip())
    bob = list(map(int, sys.stdin.readline().strip().split()))

    # Initialize two pointers for both lists
    first, snd = 0, 0
    mrg_list = []

    # Merge the two sorted lists
    while first < numput1 and snd < numput2:
        if alc[first] <= bob[snd]:
            mrg_list.append(alc[first])
            first += 1
        else:
            mrg_list.append(bob[snd])
            snd += 1

    # If there are remaining elements in Alice's list
    while first < numput1:
        mrg_list.append(alc[first])
        first += 1

    # If there are remaining elements in Bob's list
    while snd < numput2:
        mrg_list.append(bob[snd])
        snd += 1

    # Output the merged list
    sys.stdout.write(" ".join(map(str, mrg_list)) + "\n")
#call function
merge_sorted_lists()