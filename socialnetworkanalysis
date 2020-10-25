import networkx as nx
print(nx.__version__) # built for 2.2

# Create a graph
G=nx.Graph()

# Add nodes and attributes
G.add_nodes_from(["Pear","CenterforSecurityPolicy","GoodCorp","Wallmort","WahTimes"], type='company')
G.add_nodes_from(["IslamicReliefCanada","HannahCorp","PennyInc","Watch"], type='org')

# Add edges
G.add_edges_from([("Pear","CenterforSecurityPolicy"),("Pear","Wallmort"), \
                  ("Pear","IslamicReliefCanada"),("Pear","WahTimes"), \
                  ("CenterforSecurityPolicy","GoodCorp"),("CenterforSecurityPolicy","WahTimes"), \
                  ("CenterforSecurityPolicy","Wallmort"),("WahTimes","Wallmort"), \
                  ("Wallmort","IslamicReliefCanada"),("IslamicReliefCanada","HannahCorp"), \
                  ("HannahCorp","Watch"),("HannahCorp","PennyInc"), \
                  ("Watch","PennyInc")])

# Access node attribute
G.nodes['Pear']['type']

# View edges structure
G.edges()

%matplotlib inline
import matplotlib.pyplot as plt

# Define node colors based on attribute
color_map = []
for node in G:
    if G.nodes[node]['type'] == 'company':
        color_map.append('green')
    else: 
        color_map.append('red') 

#Visualize Network
#nx.draw(G) # Default visualization
#nx.draw(G, pos=nx.circular_layout(G)) # Demonstrates layout options
nx.draw(G, node_size = 1500, node_color = color_map, with_labels = True, pos=nx.spring_layout(G)) # Recreation of slide
