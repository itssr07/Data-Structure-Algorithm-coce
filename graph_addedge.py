def add_node(v):
    global node_count
    if v in nodes:
        print(v,"is already present in the graph")
    else:
        node_count=node_count+1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2,cost):
    if v1 not in  nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2,"is not present in the graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost
        graph[index2][index1]=cost

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()

nodes=[]
graph=[]
node_count=0
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",7)
add_edge("A","C",10)
print(graph)
print_graph()