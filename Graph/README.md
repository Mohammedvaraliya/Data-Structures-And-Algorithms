# Data-Structures And Algorithms


### 01. Graph Data Structure

    Graph Data Structure
    Graphs in data structures are non-linear data structures made up of a finite number of nodes or vertices and the 
    edges that connect them.
    

    Example Graph:

                  />  Paris
                 /     |     \  
                /      |      \
               /       |       \
              /        |        \> New York       
        Mumbai         |         />         \ 
              \        |        /            \
               \       |       /              \
                \      |      /                \
                 \     |>    /                  \> Toronto
                  \>  Dubai   


    The Routes:

        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    
    There is edges and the nodes in the graph data structure.
    Mumbai, Dubai, Paris, New York and Toronto is the Nodes. 
    and edges are the lines which are pointing from one Node to the other.

    Suppose i want to Know the path from "Mumbai" to "New York"

    There is 3 possible paths available : 

    [['Mumbai', 'Paris', 'Dubai', 'New York'], ['Mumbai', 'Paris', 'New York'], ['Mumbai', 'Dubai', 'New York']]

    And the shortest path is :

    ['Mumbai', 'Paris', 'New York']

