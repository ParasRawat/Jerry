from DepthFirstSearch.Node import node
import DFS
node1=node("a")
node2=node("b")
node3=node("c")
node4=node("d")
node5=node("e")
node6=node("f")
node7=node("g")
node1.adjancey.append(node2)
node1.adjancey.append(node3)
node2.adjancey.append(node4)
node4.adjancey.append(node5)

DFS.dfs(node1)
