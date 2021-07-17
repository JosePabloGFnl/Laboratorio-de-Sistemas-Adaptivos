#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
import networkx as nx


DG = nx.DiGraph()

DG.add_edge('Diego', 'Christopher Nolan', weight=1) 
DG.add_edge('Mario', 'Christopher Nolan', weight=1) 
DG.add_edge('Pablo', 'Christopher Nolan', weight=1) 
DG.add_edge('Christo', 'Christopher Nolan', weight=1) 
DG.add_edge('Alejandro', 'Christopher Nolan', weight=1) 
DG.add_edge('Gabriel', 'Christopher Nolan', weight=1) 
DG.add_edge('Diego', 'Mario', weight=1) 
DG.add_edge('Diego', 'Pablo', weight=1) 
DG.add_edge('Mario', 'Alejandro', weight=1) 
DG.add_edge('Mario', 'Pablo', weight=1) 
DG.add_edge('Pablo', 'Christo', weight=1) 
DG.add_edge('Pablo', 'Alejandro', weight=1) 
DG.add_edge('Gabriel', 'Christo', weight=1) 


DG.has_node('Christopher Nolan')
True
DG.has_edge('Diego', 'Christopher Nolan')
False
list(DG.nodes())
['Christopher Nolan', 'Diego', 'Mario', 'Pablo','Christo', 'Alejandro', 'Gabriel']
list(DG.edges())
[('Christopher Nolan', 'Diego'), ('Christopher Nolan', 'Mario'), ('Christopher Nolan', 'Pablo'),
 ('Christopher Nolan', 'Christo'),
 ('Christopher Nolan', 'Alejandro'), ('Christopher Nolan', 'Gabriel'),
('Diego', 'Mario'), ('Diego', 'Pablo'), ('Mario', 'Alejandro'), ('Mario', 'Pablo'),
 ('Pablo', 'Christo'), ('Pablo', 'Alejandro'), ('Christo', 'Gabriel')]
DG['Diego']['Christopher Nolan']["weight"] += 1
DG['Diego']['Christopher Nolan']["weight"]
3
nx.pagerank(DG, alpha=0.85)


# In[ ]:




