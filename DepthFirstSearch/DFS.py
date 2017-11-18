from  DepthFirstSearch.Node import node
def dfs(node):

    node.visited=True
    print(node.name)
#recursion
    for n in node.adjancey:
        if not n.visited:
            dfs(n)
