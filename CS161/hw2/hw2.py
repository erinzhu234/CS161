##############
# Homework 2 #
##############

##############
# Question 1 #
##############

# TODO: comment code
def BFS(FRINGE):
    # list to store the result
    bfs_list = ()

    # make a list for the remaining nodes in the tree
    # initially equal to the whole tree
    rem = FRINGE

    # while there is still nodes in the remaining list: 
    while rem != ():
    
        # make a list for the new remaining lists after search of the first layer
        new_rem = ()

        for i in rem:
            # if not a leaf node: 
            if type(i) is tuple:
                for j in i:
                    # add the child nodes of this node into the remaining list
                    new_rem = new_rem + (j,)
            # if it is a leaf node: 
            # which means it should be searched in this layer
            else:
                # add this node to the result list
                bfs_list = bfs_list + (i,)
        
        # update the remaining list
        rem = new_rem

    return bfs_list


##############
# Question 2 #
##############


# These functions implement a depth-first solver for the homer-baby-dog-poison
# problem. In this implementation, a state is represented by a single tuple
# (homer, baby, dog, poison), where each variable is True if the respective entity is
# on the west side of the river, and False if it is on the east side.
# Thus, the initial state for this problem is (False False False False) (everybody
# is on the east side) and the goal state is (True True True True).

# The main entry point for this solver is the function DFS, which is called
# with (a) the state to search from and (b) the path to this state. It returns
# the complete path from the initial state to the goal state: this path is a
# list of intermediate problem states. The first element of the path is the
# initial state and the last element is the goal state. Each intermediate state
# is the state that results from applying the appropriate operator to the
# preceding state. If there is no solution, DFS returns [].
# To call DFS to solve the original problem, one would call
# DFS((False, False, False, False), [])
# However, it should be possible to call DFS with a different initial
# state or with an initial path.

# First, we define the helper functions of DFS.

# FINAL-STATE takes a single argument S, the current state, and returns True if it
# is the goal state (True, True, True, True) and False otherwise.
def FINAL_STATE(S):
    if S == (True, True, True, True):
        return True
    else:
        return False


# NEXT-STATE returns the state that results from applying an operator to the
# current state. It takes three arguments: the current state (S), and which entity
# to move (A, equal to "h" for homer only, "b" for homer with baby, "d" for homer
# with dog, and "p" for homer with poison).
# It returns a list containing the state that results from that move.
# If applying this operator results in an invalid state (because the dog and baby,
# or poisoin and baby are left unsupervised on one side of the river), or when the
# action is impossible (homer is not on the same side as the entity) it returns [].
# NOTE that next-state returns a list containing the successor state (which is
# itself a tuple)# the return should look something like [(False, False, True, True)].
def NEXT_STATE(S, A):
    new_state = ()

    # homer only
    if A == "h":
        new_state = new_state + (not(S[0]),)
        new_state = new_state + (S[1],)
        new_state = new_state + (S[2],)
        new_state = new_state + (S[3],)

    # homer with baby
    elif A == "b":
        # if on the same side
        if S[0] == S[1]:
            new_state = new_state + (not(S[0]),)
            new_state = new_state + (not(S[1]),)
            new_state = new_state + (S[2],)
            new_state = new_state + (S[3],)
        # if not on the same side
        else:
            return []
    
    # homer with dog
    elif A == "d":
        # if on the same side
        if S[0] == S[2]:
            new_state = new_state + (not(S[0]),)
            new_state = new_state + (S[1],)
            new_state = new_state + (not(S[2]),)
            new_state = new_state + (S[3],)
        # if not on the same side
        else:
            return []

    # homer with poison
    elif A == "p":
        # if on the same side
        if S[0] == S[3]:
            new_state = new_state + (not(S[0]),)
            new_state = new_state + (S[1],)
            new_state = new_state + (S[2],)
            new_state = new_state + (not(S[3]),)
        # if not on the same side
        else:
            return []

    # if baby and poison or dog and baby are left alone on one side
    if (new_state[1] == new_state[2] and new_state[1] != new_state[0]) or (new_state[1] == S[3] and new_state[1] != new_state[0]):
        return []
    else:
        return [new_state]

# SUCC-FN returns all of the possible legal successor states to the current
# state. It takes a single argument (s), which encodes the current state, and
# returns a list of each state that can be reached by applying legal operators
# to the current state.
def SUCC_FN(S):
    suc_states = []

    # try all 4 possible moves
    for i in ["h", "b", "d", "p"]:
        # add valid states after move to the list
        if NEXT_STATE(S, i) != []:
            suc_states = suc_states + NEXT_STATE(S, i)
    return suc_states


# ON-PATH checks whether the current state is on the stack of states visited by
# this depth-first search. It takes two arguments: the current state (S) and the
# stack of states visited by DFS (STATES). It returns True if s is a member of
# states and False otherwise.
def ON_PATH(S, STATES):
    if S in STATES:
        return True
    else:
        return False


# MULT-DFS is a helper function for DFS. It takes two arguments: a list of
# states from the initial state to the current state (PATH), and the legal
# successor states to the last, current state in the PATH (STATES). PATH is a
# first-in first-out list of states# that is, the first element is the initial
# state for the current search and the last element is the most recent state
# explored. MULT-DFS does a depth-first search on each element of STATES in
# turn. If any of those searches reaches the final state, MULT-DFS returns the
# complete path from the initial state to the goal state. Otherwise, it returns
# [].
    
def MULT_DFS(STATES, PATH):

    # if there is only one successor state
    if len(STATES) == 1:
        
        # if the successor state is the final state
        if FINAL_STATE(STATES[0]):
            # add the successor state to the path and return path
            PATH.append(STATES[0])
            return PATH

        # if the successor state is contained in the path (i.e. there is a loop)
        # drop this successor path
        elif ON_PATH(STATES[0], PATH):
            return []
        
        # if it is a valid successor state
        else:
            # append the state to a new copy of PATH variable
            new_path = PATH
            new_path.append(STATES[0])
            
            # recursive call on the possible successor states and the new path
            return MULT_DFS(SUCC_FN(STATES[0]), new_path)
    
    # if there is no possible successor states: 
    elif len(STATES) == 0:
        return []
    
    # if there is more than 1 successor states
    else:
        # recursively call on each single successor state in STATES
        for i in STATES:
            pos_res = MULT_DFS([i], PATH)
            # if there is a valid path
            if pos_res != []:
                return pos_res
        # if all state in STATES does not have a valid path
        return []
        


# DFS does a depth first search from a given state to the goal state. It
# takes two arguments: a state (S) and the path from the initial state to S
# (PATH). If S is the initial state in our search, PATH is set to [] (empty list). DFS
# performs a depth-first search starting at the given state. It returns the path
# from the initial state to the goal state, if any, or empty list [] otherwise. DFS is
# responsible for checking if S is already the goal state, as well as for
# ensuring that the depth-first search does not revisit a node already on the
# search path.
def DFS(S, PATH):
    # convert MULT_DFS([S], PATH) into DFS(S, PATH), 
    # since MULF_DFS only accepts a list as STATES while S is a single state. 
    return MULT_DFS([S], PATH)
