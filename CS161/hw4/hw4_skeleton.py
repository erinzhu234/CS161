##############
# Homework 4 #
##############

# Exercise: Fill this function.
# Returns the index of the variable that corresponds to the fact that
# "Node n gets Color c" when there are k possible colors
def node2var(n, c, k):
    return (n-1)*k + c

# Exercise: Fill this function
# Returns *a clause* for the constraint:
# "Node n gets at least one color from the set {1, 2, ..., k}"
def at_least_one_color(n, k):
    ret_ls = []
    for i in range(1, k+1):
        ret_ls = ret_ls + [node2var(n, i, k)]
    return ret_ls

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Node n gets at most one color from the set {1, 2, ..., k}"
def at_most_one_color(n, k):
    clause_ls = []
    for i in range(1, k+1):
        for j in range(i+1, k+1):
            clause = []
            clause = clause + [-1*node2var(n, i, k)]
            clause = clause + [-1*node2var(n, j, k)]
            clause_ls = clause_ls + [clause]

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Node n gets exactly one color from the set {1, 2, ..., k}"
def generate_node_clauses(n, k):
    # exactly one color = at least one color and at most one color
    clause_ls = []
    clause_ls = clause_ls + [at_least_one_color(n,k)]
    clause_ls = clause_ls + at_most_one_color(n,k)

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Nodes connected by an edge e (represented by a list)
# cannot have the same color"
def generate_edge_clauses(e, k):
    clause_ls = []
    for edge in e:
        for color in range(1, k+1):
            # nodes at the ends of edges cannot have same color
            clause = []
            clause = clause + [-1*node2var(edge[1], color, k)]
            clause = clause + [-1*node2var(edge[2], color, k)]
            clause_ls = clause_ls + [clause]

# The function below converts a graph coloring problem to SAT
# DO NOT MODIFY
def graph_coloring_to_sat(graph_fl, sat_fl, k):
    clauses = []
    with open(graph_fl) as graph_fp:
        node_count, edge_count = tuple(map(int, graph_fp.readline().split()))
        for n in range(1, node_count + 1):
            clauses += generate_node_clauses(n, k)
        for _ in range(edge_count):
            e = tuple(map(int, graph_fp.readline().split()))
            clauses += generate_edge_clauses(e, k)
    var_count = node_count * k
    clause_count = len(clauses)
    with open(sat_fl, 'w') as sat_fp:
        sat_fp.write("p cnf %d %d\n" % (var_count, clause_count))
        for clause in clauses:
            sat_fp.write(" ".join(map(str, clause)) + " 0\n")


# Example function call
if __name__ == "__main__":
   graph_coloring_to_sat("graph1.txt", "graph1_3colors.txt", 4)
