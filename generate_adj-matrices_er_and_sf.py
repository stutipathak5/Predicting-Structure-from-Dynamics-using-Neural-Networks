import networkx as nx
import numpy as np

for i in range(0,250):
  seed=i
  G=nx.erdos_renyi_graph(100, 0.185, seed=seed, directed=False)
  F=nx.to_numpy_matrix(G)
  with open("/content/drive/My Drive/ER+SF_New/er"+str(i+1)+".txt",'wb') as f:
    for line in F:
      np.savetxt(f, line, fmt='%.2f')
  C=nx.barabasi_albert_graph(100,10,seed=seed)
  H=nx.to_numpy_matrix(C)
  with open("/content/drive/My Drive/ER+SF_New/sf"+str(i+1)+".txt",'wb') as f:
    for line in H:
      np.savetxt(f, line, fmt='%.2f')
