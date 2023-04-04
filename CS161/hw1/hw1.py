def PAD(N):
    if N <= 2:
        # the first three entries of the sequence
        return 1
    else:
        # according to the definition, PAD(N) = PAD(N-2) + PAD(N-3)
        return PAD(N-2) + PAD(N-3)

def SUMS(N):
    if N <= 2:
        # no addition required by the first three entries
        return 0
    else: 
        # addition required by PAD(N-2) and PAD(N-3) and one addition required to add PAD(N-2) and PAD(N-3)
        return SUMS(N-2) + SUMS(N-3) + 1


def ANON(TREE):
    if type(TREE) is tuple:
        # if there is more than one node: 
        anon_tree = ()
        for i in TREE:
            # append the anonymized versions of each entry of the tuple into the anonymized tuple
            anon_tree = anon_tree + (ANON(i),)
        return anon_tree
    else:
        # if TREE only contains a single leaf node: 
        return '?'
