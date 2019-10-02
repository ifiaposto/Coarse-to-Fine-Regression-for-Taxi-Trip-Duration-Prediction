import networkx as nx
import numpy as np
import pandas as pd
import metis
import csv


def graph_tree_clustering(G, h, root_name, hk, clusters):

    if hk==0: #at the root of the tree, all of the nodes belong to the root
        clusters = [[root_name] for i in range(G.number_of_nodes())]
    if hk==h: #end of recursion maximum depth of cluster tree has been reached
        return clusters
    if G.number_of_nodes()==1: #there is one node in the graph and it cannot be bisected further
        for l in  [clusters[i] for i in G.nodes()]:
            l.append(root_name)
        return graph_tree_clustering(G, h, root_name, hk+1, clusters)

    #bisect the graph
    [cost, parts] = metis.part_graph(G, nparts=2, recursive=True)

    #get the nodes in the first cluster
    nodes_0 = [list(G.nodes)[x] for x in [i for i, x in enumerate(parts) if x == 0]]
    cluster_id_0=root_name+1

    #update the subcluster at depth hk for each node in the cluster at depth hk
    for l in  [clusters[i] for i in nodes_0]:
        l.append(cluster_id_0)

    if nodes_0:
        G_0=G.subgraph(nodes_0)
        clusters=graph_tree_clustering(G_0, h, cluster_id_0, hk+1, clusters)

    nodes_1 = [list(G.nodes)[x] for x in [i for i, x in enumerate(parts) if x == 1]]
    if nodes_0:
        m=max([max(l) for l in  [clusters[i] for i in nodes_0]])
        cluster_id_1=m+1
    else:
        cluster_id_1=root_name+1

    for l in  [clusters[i] for i in nodes_1]:
        l.append(cluster_id_1)
    if nodes_1:
        G_1=G.subgraph(nodes_1)
        clusters=graph_tree_clustering(G_1, h, cluster_id_1, hk+1, clusters)

    return(clusters)
    


# staten island graph
G_staten_island = nx.Graph()
x44=0
G_staten_island.add_node(x44, weight=1)
x204=1
G_staten_island.add_node(x204, weight=1)
x84=2
G_staten_island.add_node(x84, weight=1)
x5=3
G_staten_island.add_node(x5, weight=1)
x99=4
G_staten_island.add_node(x99, weight=1)
x109=5
G_staten_island.add_node(x109, weight=1)
x118=6
G_staten_island.add_node(x118, weight=1)
x110=7
G_staten_island.add_node(x110, weight=1)
x176=8
G_staten_island.add_node(x176, weight=1)
x172=9
G_staten_island.add_node(x172, weight=1)
x214=10
G_staten_island.add_node(x214, weight=1)
x6=11
G_staten_island.add_node(x6, weight=1)
x221=12
G_staten_island.add_node(x221, weight=1)
x115=13
G_staten_island.add_node(x115, weight=1)
x245=14
G_staten_island.add_node(x245, weight=1)
x206=15
G_staten_island.add_node(x206, weight=1)
x251=16
G_staten_island.add_node(x251, weight=1)
x187=17
G_staten_island.add_node(x187, weight=1)
x156=18
G_staten_island.add_node(x156, weight=1)
x23=19
G_staten_island.add_node(x156, weight=1)

D_staten_island =	{
    0: 44,
    1: 204,
    2: 84,
    3: 5,
    4: 99,
    5:109,
    6:118,
    7:110,
    8:176,
    9:172,
    10:214,
    11:6,
    12:221,
    13:115,
    14:245,
    15:206,
    16:251,
    17:187,
    18:156,
    19:23
}

G_staten_island.add_edge(x44,x204)
G_staten_island.add_edge(x44,x84)

G_staten_island.add_edge(x204, x44)
G_staten_island.add_edge(x204, x84)
G_staten_island.add_edge(x204, x5)
G_staten_island.add_edge(x204, x99)

G_staten_island.add_edge(x84, x204)
G_staten_island.add_edge(x84, x44)
G_staten_island.add_edge(x84, x5)
G_staten_island.add_edge(x84, x109)

G_staten_island.add_edge(x5, x204)
G_staten_island.add_edge(x5, x84)
G_staten_island.add_edge(x5, x109)
G_staten_island.add_edge(x5, x99)

G_staten_island.add_edge(x99, x5)
G_staten_island.add_edge(x99, x109)
G_staten_island.add_edge(x99, x118)
G_staten_island.add_edge(x99, x23)
G_staten_island.add_edge(x99, x204)

G_staten_island.add_edge(x109, x84)
G_staten_island.add_edge(x109, x110)
G_staten_island.add_edge(x109, x176)
G_staten_island.add_edge(x109, x118)
G_staten_island.add_edge(x109, x99)
G_staten_island.add_edge(x109, x5)

G_staten_island.add_edge(x110, x109)
G_staten_island.add_edge(x110, x176)

G_staten_island.add_edge(x176, x110)
G_staten_island.add_edge(x176, x172)
G_staten_island.add_edge(x176, x109)
G_staten_island.add_edge(x176, x118)

G_staten_island.add_edge(x172, x176)
G_staten_island.add_edge(x172, x118)
G_staten_island.add_edge(x172, x214)

G_staten_island.add_edge(x214, x172)
G_staten_island.add_edge(x214, x118)
G_staten_island.add_edge(x214, x6)

G_staten_island.add_edge(x6, x214)
G_staten_island.add_edge(x6, x118)
G_staten_island.add_edge(x6, x115)
G_staten_island.add_edge(x6, x221)

G_staten_island.add_edge(x23, x99)
G_staten_island.add_edge(x23, x118)
G_staten_island.add_edge(x23, x156)
G_staten_island.add_edge(x23, x187)
G_staten_island.add_edge(x23, x251)


G_staten_island.add_edge(x156, x23)
G_staten_island.add_edge(x156, x187)

G_staten_island.add_edge(x187, x156)
G_staten_island.add_edge(x187, x251)
G_staten_island.add_edge(x187, x206)

G_staten_island.add_edge(x221, x6)
G_staten_island.add_edge(x221, x115)
G_staten_island.add_edge(x221, x206)

G_staten_island.add_edge(x115, x221)
G_staten_island.add_edge(x115, x6)
G_staten_island.add_edge(x115, x118)
G_staten_island.add_edge(x115, x251)
G_staten_island.add_edge(x115, x245)


G_staten_island.add_edge(x118, x99)
G_staten_island.add_edge(x118, x109)
G_staten_island.add_edge(x118, x176)
G_staten_island.add_edge(x118, x172)
G_staten_island.add_edge(x118, x214)
G_staten_island.add_edge(x118, x6)
G_staten_island.add_edge(x118, x115)
G_staten_island.add_edge(x118, x251)
G_staten_island.add_edge(x118, x23)

G_staten_island.add_edge(x251, x187)
G_staten_island.add_edge(x251, x23)
G_staten_island.add_edge(x251, x206)
G_staten_island.add_edge(x251, x245)
G_staten_island.add_edge(x251, x115)
G_staten_island.add_edge(x251, x118)

G_staten_island.add_edge(x245, x251)
G_staten_island.add_edge(x245, x206)
G_staten_island.add_edge(x245, x115)
G_staten_island.add_edge(x245, x221)

G_staten_island.add_edge(x206, x187)
G_staten_island.add_edge(x206, x251)
G_staten_island.add_edge(x206, x245)
G_staten_island.add_edge(x206, x221)


#G_staten_island.graph['edge_weight_attr']='weight'
G_staten_island.graph['node_weight_attr']='weight'
##[cost, parts] = metis.part_graph(G, nparts=2, recursive=True)
#
#clusters=graph_tree_clustering(G_staten_island,3,1, 0, [])
#print(clusters)

#bronx graph
#TODO: get the root name for the next graph given the ids of the clusters from the previous one

G_bronx = nx.Graph()

x168=0
G_bronx.add_node(x168, weight=1)
x126=1
G_bronx.add_node(x126, weight=1)
x147=2
G_bronx.add_node(x147, weight=1)
x159=3
G_bronx.add_node(x159, weight=1)
x69=4
G_bronx.add_node(x69, weight=1)
x247=5
G_bronx.add_node(x247, weight=1)
x199=6
G_bronx.add_node(x199, weight=1)
x167=7 ###
G_bronx.add_node(x167, weight=1)
x60=8
G_bronx.add_node(x60, weight=1)
x213=9
G_bronx.add_node(x213, weight=1)
x212=10
G_bronx.add_node(x212, weight=1)
x250=11
G_bronx.add_node(x250, weight=1)
x208=12
G_bronx.add_node(x208, weight=1)
x242=13
G_bronx.add_node(x242, weight=1)
x183=14
G_bronx.add_node(x183, weight=1)
x58=15
G_bronx.add_node(x58, weight=1)
x184=16
G_bronx.add_node(x184, weight=1)
x182=17
G_bronx.add_node(x182, weight=1)
x119=18
G_bronx.add_node(x119, weight=1)
x169=19
G_bronx.add_node(x169, weight=1)
x235=20
G_bronx.add_node(x235, weight=1)
x94=21
G_bronx.add_node(x94, weight=1)
x136=22
G_bronx.add_node(x136, weight=1)
x47=23
G_bronx.add_node(x47, weight=1)
x59=24
G_bronx.add_node(x59, weight=1)
x78=25
G_bronx.add_node(x78, weight=1)
x20=26
G_bronx.add_node(x20, weight=1)
x248=27
G_bronx.add_node(x248, weight=1)
x51=28
G_bronx.add_node(x51, weight=1)
x46=29
G_bronx.add_node(x46, weight=1)
x81=30
G_bronx.add_node(x81, weight=1)
x31=31
G_bronx.add_node(x31, weight=1)
x185=32
G_bronx.add_node(x185, weight=1)
x18=33
G_bronx.add_node(x18, weight=1)
x241=34
G_bronx.add_node(x241, weight=1)
x174=35
G_bronx.add_node(x174, weight=1)
x240=36
G_bronx.add_node(x240, weight=1)
x220=37
G_bronx.add_node(x220, weight=1)
x9=38
G_bronx.add_node(x9, weight=1)
x200=39
G_bronx.add_node(x200, weight=1)
#x185=40
#G_bronx.add_node(x185, weight=1)
x32=40
G_bronx.add_node(x32, weight=1)
x254=41
G_bronx.add_node(x254, weight=1)
x3=42
G_bronx.add_node(x3, weight=1)
x259=43
G_bronx.add_node(x259, weight=1)


D_bronx=	{
    0: 168,
    1: 126,
    2: 147,
    3: 159,
    4: 69,
    5: 247,
    6: 199,
    7:167,
    8:60,
    9:213,
    10:212,
    11:250,
    12:208,
    13:242,
    14:183,
    15:58,
    16:184,
    17:182,
    18:119,
    19:169,
    20:235,
    21:94,
    22:136,
    23:47,
    24:59,
    25:78,
    26:20,
    27:248,
    28:51,
    29:46,
    30:81,
    31:31,
    32:185,
    33:18,
    34:241,
    35:174,
    36:240,
    37:220,
    38:9,
    39:200,
    #40:185,
    40:32,
    41:254,
    42:3,
    43:259
    }


G_bronx.add_edge(x168,x126)
G_bronx.add_edge(x168,x147)
G_bronx.add_edge(x168,x159)
G_bronx.add_edge(x168,x69)
G_bronx.add_edge(x168,x247)
G_bronx.add_edge(x168,x199)

G_bronx.add_edge(x126,x168)
G_bronx.add_edge(x126,x147)
G_bronx.add_edge(x126,x167)
G_bronx.add_edge(x126,x60)
G_bronx.add_edge(x126,x213)
G_bronx.add_edge(x126,x199)

G_bronx.add_edge(x199, x126)
G_bronx.add_edge(x199, x168)

G_bronx.add_edge(x213, x126)
G_bronx.add_edge(x213, x212)
G_bronx.add_edge(x213, x250)
G_bronx.add_edge(x213, x208)

G_bronx.add_edge(x208, x250)
G_bronx.add_edge(x208, x213)
G_bronx.add_edge(x208, x242)
G_bronx.add_edge(x208, x183)
G_bronx.add_edge(x208, x58)

G_bronx.add_edge(x58, x208)
G_bronx.add_edge(x58, x183)
G_bronx.add_edge(x58, x184)


G_bronx.add_edge(x250, x213)
G_bronx.add_edge(x250, x212)
G_bronx.add_edge(x250, x182)
G_bronx.add_edge(x250, x242)
G_bronx.add_edge(x250, x208)

G_bronx.add_edge(x147, x168)
G_bronx.add_edge(x147, x167)
G_bronx.add_edge(x147, x126)
G_bronx.add_edge(x147, x159)

G_bronx.add_edge(x159, x168)
G_bronx.add_edge(x159, x69)
G_bronx.add_edge(x159, x167)
G_bronx.add_edge(x159, x147)

G_bronx.add_edge(x247, x119)
G_bronx.add_edge(x247, x69)
G_bronx.add_edge(x247, x169)
G_bronx.add_edge(x247, x168)

G_bronx.add_edge(x119, x247)
G_bronx.add_edge(x119, x235)

G_bronx.add_edge(x235, x119)
G_bronx.add_edge(x235, x169)
G_bronx.add_edge(x235, x94)
G_bronx.add_edge(x235, x136)


G_bronx.add_edge(x169, x247)
G_bronx.add_edge(x169, x69)
G_bronx.add_edge(x169, x47)
G_bronx.add_edge(x169, x94)
G_bronx.add_edge(x169, x235)

G_bronx.add_edge(x69, x247)
G_bronx.add_edge(x69, x159)
G_bronx.add_edge(x69, x167)
G_bronx.add_edge(x69, x47)
G_bronx.add_edge(x69, x169)

G_bronx.add_edge(x167, x69)
G_bronx.add_edge(x167, x159)
G_bronx.add_edge(x167, x147)
G_bronx.add_edge(x167, x60)
G_bronx.add_edge(x167, x59)
G_bronx.add_edge(x167, x47)
G_bronx.add_edge(x167, x126)

G_bronx.add_edge(x47, x69)
G_bronx.add_edge(x47, x169)
G_bronx.add_edge(x47, x167)
G_bronx.add_edge(x47, x59)
G_bronx.add_edge(x47, x78)
G_bronx.add_edge(x47, x20)

G_bronx.add_edge(x59, x167)
G_bronx.add_edge(x59, x47)
G_bronx.add_edge(x59, x78)
G_bronx.add_edge(x59, x60)

G_bronx.add_edge(x60, x126)
G_bronx.add_edge(x60, x167)
G_bronx.add_edge(x60, x59)
G_bronx.add_edge(x60, x78)
G_bronx.add_edge(x60, x248)
G_bronx.add_edge(x60, x212)

G_bronx.add_edge(x212, x213)
G_bronx.add_edge(x212, x250)
G_bronx.add_edge(x212, x182)
G_bronx.add_edge(x212, x248)
G_bronx.add_edge(x212, x60)

G_bronx.add_edge(x248, x212)
G_bronx.add_edge(x248, x60)
G_bronx.add_edge(x248, x182)
G_bronx.add_edge(x248, x242)

G_bronx.add_edge(x182, x248)
G_bronx.add_edge(x182, x212)
G_bronx.add_edge(x182, x250)
G_bronx.add_edge(x182, x242)

G_bronx.add_edge(x183, x242)
G_bronx.add_edge(x183, x184)
G_bronx.add_edge(x183, x208)

G_bronx.add_edge(x184, x51)
G_bronx.add_edge(x184, x183)
G_bronx.add_edge(x184, x46)

G_bronx.add_edge(x46, x184)

G_bronx.add_edge(x51, x81)
G_bronx.add_edge(x51, x184)

G_bronx.add_edge(x78, x47)
G_bronx.add_edge(x78, x59)
G_bronx.add_edge(x78, x60)
G_bronx.add_edge(x78, x242)
G_bronx.add_edge(x78, x20)
G_bronx.add_edge(x78, x31)

G_bronx.add_edge(x136, x185)
G_bronx.add_edge(x136, x94)
G_bronx.add_edge(x136, x18)
G_bronx.add_edge(x136, x241)

G_bronx.add_edge(x241, x136)
G_bronx.add_edge(x241, x18)
G_bronx.add_edge(x241, x174)
G_bronx.add_edge(x241, x240)
G_bronx.add_edge(x241, x220)

G_bronx.add_edge(x18, x94)
G_bronx.add_edge(x18, x136)
G_bronx.add_edge(x18, x241)
G_bronx.add_edge(x18, x174)
G_bronx.add_edge(x18, x20)

G_bronx.add_edge(x94, x169)
G_bronx.add_edge(x94, x185)
G_bronx.add_edge(x94, x136)
G_bronx.add_edge(x94, x18)
G_bronx.add_edge(x94, x47)

G_bronx.add_edge(x20, x47)
G_bronx.add_edge(x20, x78)
G_bronx.add_edge(x20, x31)
G_bronx.add_edge(x20, x174)
G_bronx.add_edge(x20, x18)
G_bronx.add_edge(x20, x9)

G_bronx.add_edge(x200, x220)
G_bronx.add_edge(x200, x240)

G_bronx.add_edge(x220,x241)
G_bronx.add_edge(x220,x240)
G_bronx.add_edge(x220,x200)

G_bronx.add_edge(x31,x20)
G_bronx.add_edge(x31,x78)
G_bronx.add_edge(x31,x242)
G_bronx.add_edge(x31,x185)
G_bronx.add_edge(x31,x32)
G_bronx.add_edge(x31,x254)
G_bronx.add_edge(x31,x174)

G_bronx.add_edge(x32, x31)
G_bronx.add_edge(x32, x254)
G_bronx.add_edge(x32, x3)
G_bronx.add_edge(x32, x185)

G_bronx.add_edge(x240, x220)
G_bronx.add_edge(x240, x200)
G_bronx.add_edge(x240, x241)
G_bronx.add_edge(x240, x174)
G_bronx.add_edge(x240, x254)

G_bronx.add_edge(x242, x78)
G_bronx.add_edge(x242, x248)
G_bronx.add_edge(x242, x182)
G_bronx.add_edge(x242, x250)
G_bronx.add_edge(x242, x183)
G_bronx.add_edge(x242, x185)
G_bronx.add_edge(x242, x31)

G_bronx.add_edge(x185, x242)
G_bronx.add_edge(x185, x31)
G_bronx.add_edge(x185, x32)
G_bronx.add_edge(x185, x3)

G_bronx.add_edge(x3, x185)
G_bronx.add_edge(x3, x32)
G_bronx.add_edge(x3, x254)
G_bronx.add_edge(x3, x81)
G_bronx.add_edge(x3, x242)

G_bronx.add_edge(x81, x3)
G_bronx.add_edge(x81, x254)
G_bronx.add_edge(x81, x259)
G_bronx.add_edge(x81, x51)

G_bronx.add_edge(x259, x240)
G_bronx.add_edge(x259, x254)
G_bronx.add_edge(x259, x81)

G_bronx.add_edge(x254, x240)
G_bronx.add_edge(x254, x259)
G_bronx.add_edge(x254, x81)
G_bronx.add_edge(x254, x3)
G_bronx.add_edge(x254, x32)

G_bronx.add_edge(x174, x18)
G_bronx.add_edge(x174, x31)
G_bronx.add_edge(x174, x240)
G_bronx.add_edge(x174, x241)

G_bronx.graph['node_weight_attr']='weight'

#manhattan graph

G_manhattan = nx.Graph()

x153=0
G_manhattan.add_node(x153, weight=1)
x128=1
G_manhattan.add_node(x128, weight=1)
x127=2
G_manhattan.add_node(x127, weight=1)
x243=3
G_manhattan.add_node(x243, weight=1)
x120=4
G_manhattan.add_node(x120, weight=1)
x244=5
G_manhattan.add_node(x244, weight=1)
x116=6
G_manhattan.add_node(x116, weight=1)
x42=7
G_manhattan.add_node(x42, weight=1)
x152=8
G_manhattan.add_node(x152, weight=1)
x41=9
G_manhattan.add_node(x41, weight=2)
x74=10
G_manhattan.add_node(x74, weight=2)
x166=11
G_manhattan.add_node(x166, weight=2)
x24=12
G_manhattan.add_node(x24, weight=1)
x75=13
G_manhattan.add_node(x75, weight=3)
x194=14
G_manhattan.add_node(x194, weight=1)
x43=15
G_manhattan.add_node(x43, weight=4)
x236=16
G_manhattan.add_node(x236, weight=10)
x263=17
G_manhattan.add_node(x263, weight=5)
x262=18
G_manhattan.add_node(x262, weight=4)
x151=19
G_manhattan.add_node(x151, weight=3)
x238=20
G_manhattan.add_node(x238, weight=6)
x239=21
G_manhattan.add_node(x239, weight=7)
x143=22
G_manhattan.add_node(x143, weight=4)
x142=23
G_manhattan.add_node(x142, weight=8)
x50=24
G_manhattan.add_node(x50, weight=3)
x246=25
G_manhattan.add_node(x246, weight=5)
x48=26
G_manhattan.add_node(x48, weight=8)
x237=27
G_manhattan.add_node(x237, weight=10)
x163=28
G_manhattan.add_node(x163, weight=7)
x141=29
G_manhattan.add_node(x141, weight=7)
x140=30
G_manhattan.add_node(x140, weight=5)
x229=31
G_manhattan.add_node(x229, weight=5)
x202=32
G_manhattan.add_node(x202, weight=1)
x162=33
G_manhattan.add_node(x162, weight=9)
x230=34
G_manhattan.add_node(x230, weight=9)
x161=35
G_manhattan.add_node(x161, weight=10)
x100=36
G_manhattan.add_node(x100, weight=5)
x68=37
G_manhattan.add_node(x68, weight=7)
x158=38
G_manhattan.add_node(x158, weight=4)
x186=39
G_manhattan.add_node(x186, weight=9)
x90=40
G_manhattan.add_node(x90, weight=5)
x249=41
G_manhattan.add_node(x249, weight=6)
x164=42
G_manhattan.add_node(x164, weight=7)
x170=43
G_manhattan.add_node(x170, weight=9)
x233=44
G_manhattan.add_node(x233, weight=4)
x137=45
G_manhattan.add_node(x137, weight=4)
x107=46
G_manhattan.add_node(x107, weight=7)
x224=47
G_manhattan.add_node(x224, weight=1)
x79=48
G_manhattan.add_node(x79, weight=8)
x4=49
G_manhattan.add_node(x4, weight=2)
x234=50
G_manhattan.add_node(x234, weight=9)
x113=51
G_manhattan.add_node(x113, weight=5)
x114=52
G_manhattan.add_node(x114, weight=4)
x125=53
G_manhattan.add_node(x125, weight=2)
x148=54
G_manhattan.add_node(x148, weight=4)
x232=55
G_manhattan.add_node(x232, weight=1)
x45=56
G_manhattan.add_node(x45, weight=1)
x144=57
G_manhattan.add_node(x144, weight=3)
x231=58
G_manhattan.add_node(x231, weight=5)
x211=59
G_manhattan.add_node(x211, weight=3)
x209=60
G_manhattan.add_node(x209, weight=1)
x261=61
G_manhattan.add_node(x261, weight=2)
x13=62
G_manhattan.add_node(x13, weight=3)
x87=63
G_manhattan.add_node(x87, weight=3)
x88=64
G_manhattan.add_node(x88, weight=2)
x12=65
G_manhattan.add_node(x12, weight=1)
x105=66
G_manhattan.add_node(x105, weight=1)
x103=67
G_manhattan.add_node(x103, weight=1)
x104=68
G_manhattan.add_node(x104, weight=1)

D_manhattan=	{
    0:153,
    1:128,
    2:127,
    3:243,
    4:120,
    5:244,
    6:116,
    7:42,
    8:152,
    9:41,
    10:74,
    11:166,
    12:24,
    13:75,
    14:194,
    15:43,
    16:236,
    17:263,
    18:262,
    19:151,
    20:238,
    21:239,
    22:143,
    23:142,
    24:50,
    25:246,
    26:48,
    27:237,
    28:163,
    29:141,
    30:140,
    31:229,
    32:202,
    33:162,
    34:230,
    35:161,
    36:100,
    37:68,
    38:158,
    39:186,
    40:90,
    41:249,
    42:164,
    43:170,
    44:233,
    45:137,
    46:107,
    47:224,
    48:79,
    49:4,
    50:234,
    51:113,
    52:114,
    53:125,
    54:148,
    55:232,
    56:45,
    57:144,
    58:231,
    59:211,
    60:209,
    61:261,
    62:13,
    63:87,
    64:88,
    65:12,
    66:105,
    67:103,
    68:104
}


G_manhattan.add_edge(x153, x128)
G_manhattan.add_edge(x153, x127)

G_manhattan.add_edge(x128, x153)
G_manhattan.add_edge(x128, x127)
G_manhattan.add_edge(x128, x243)

G_manhattan.add_edge(x127, x128)
G_manhattan.add_edge(x127, x153)
G_manhattan.add_edge(x127, x243)
G_manhattan.add_edge(x127, x120)

G_manhattan.add_edge(x243, x128)
G_manhattan.add_edge(x243, x127)
G_manhattan.add_edge(x243, x120)
G_manhattan.add_edge(x243, x244)

G_manhattan.add_edge(x244, x243)
G_manhattan.add_edge(x244, x120)
G_manhattan.add_edge(x244, x116)

G_manhattan.add_edge(x120, x243)
G_manhattan.add_edge(x120, x244)
G_manhattan.add_edge(x120, x127)
G_manhattan.add_edge(x120, x42)

G_manhattan.add_edge(x42, x120)
G_manhattan.add_edge(x42, x116)
G_manhattan.add_edge(x42, x152)
G_manhattan.add_edge(x42, x41)
G_manhattan.add_edge(x42, x74)

G_manhattan.add_edge(x116, x152)
G_manhattan.add_edge(x116, x42)
G_manhattan.add_edge(x116, x244)

G_manhattan.add_edge(x152, x116)
G_manhattan.add_edge(x152, x166)
G_manhattan.add_edge(x152, x41)
G_manhattan.add_edge(x152, x42)

G_manhattan.add_edge(x166, x24)
G_manhattan.add_edge(x166, x41)
G_manhattan.add_edge(x166, x152)

G_manhattan.add_edge(x41, x42)
G_manhattan.add_edge(x41, x166)
G_manhattan.add_edge(x41, x74)
G_manhattan.add_edge(x41, x24)

G_manhattan.add_edge(x74, x41)
G_manhattan.add_edge(x74, x75)
G_manhattan.add_edge(x74, x42)
G_manhattan.add_edge(x74, x194)

G_manhattan.add_edge(x194, x74)

G_manhattan.add_edge(x75, x74)
G_manhattan.add_edge(x75, x43)
G_manhattan.add_edge(x75, x41)
G_manhattan.add_edge(x75, x236)
G_manhattan.add_edge(x75, x263)
G_manhattan.add_edge(x75, x262)

G_manhattan.add_edge(x24, x166)
G_manhattan.add_edge(x24, x41)
G_manhattan.add_edge(x24, x43)
G_manhattan.add_edge(x24, x151)

G_manhattan.add_edge(x151, x24)
G_manhattan.add_edge(x151, x238)
G_manhattan.add_edge(x151, x43)

G_manhattan.add_edge(x238, x239)
G_manhattan.add_edge(x238, x151)
G_manhattan.add_edge(x238, x43)

G_manhattan.add_edge(x239, x238)
G_manhattan.add_edge(x239, x143)
G_manhattan.add_edge(x239, x142)

G_manhattan.add_edge(x143, x50)
G_manhattan.add_edge(x143, x239)
G_manhattan.add_edge(x143, x142)

G_manhattan.add_edge(x50, x246)
G_manhattan.add_edge(x50, x48)
G_manhattan.add_edge(x50, x143)

G_manhattan.add_edge(x142, x143)
G_manhattan.add_edge(x142, x239)
G_manhattan.add_edge(x142, x43)
G_manhattan.add_edge(x142, x48)

G_manhattan.add_edge(x43, x142)
G_manhattan.add_edge(x43, x239)
G_manhattan.add_edge(x43, x238)
G_manhattan.add_edge(x43, x151)
G_manhattan.add_edge(x43, x24)
G_manhattan.add_edge(x43, x41)
G_manhattan.add_edge(x43, x75)
G_manhattan.add_edge(x43, x236)
G_manhattan.add_edge(x43, x237)
G_manhattan.add_edge(x43, x163)

G_manhattan.add_edge(x236, x43)
G_manhattan.add_edge(x236, x237)
G_manhattan.add_edge(x236, x263)
G_manhattan.add_edge(x236, x75)
G_manhattan.add_edge(x236, x141)

G_manhattan.add_edge(x263, x236)
G_manhattan.add_edge(x263, x75)
G_manhattan.add_edge(x263, x262)
G_manhattan.add_edge(x263, x141)

G_manhattan.add_edge(x262, x263)
G_manhattan.add_edge(x262, x140)

G_manhattan.add_edge(x140, x141)
G_manhattan.add_edge(x140, x229)
G_manhattan.add_edge(x140, x263)
G_manhattan.add_edge(x140, x262)
G_manhattan.add_edge(x140, x202)

G_manhattan.add_edge(x202, x140)

G_manhattan.add_edge(x237, x43)
G_manhattan.add_edge(x237, x163)
G_manhattan.add_edge(x237, x162)
G_manhattan.add_edge(x237, x141)
G_manhattan.add_edge(x237, x236)

G_manhattan.add_edge(x141, x140)
G_manhattan.add_edge(x141, x263)
G_manhattan.add_edge(x141, x236)
G_manhattan.add_edge(x141, x237)
G_manhattan.add_edge(x141, x229)

G_manhattan.add_edge(x163, x43)
G_manhattan.add_edge(x163, x142)
G_manhattan.add_edge(x163, x48)
G_manhattan.add_edge(x163, x230)
G_manhattan.add_edge(x163, x161)
G_manhattan.add_edge(x163, x162)

G_manhattan.add_edge(x48, x50)
G_manhattan.add_edge(x48, x100)
G_manhattan.add_edge(x48, x143)
G_manhattan.add_edge(x48, x142)
G_manhattan.add_edge(x48, x163)
G_manhattan.add_edge(x48, x230)
G_manhattan.add_edge(x48, x68)

G_manhattan.add_edge(x246, x50)
G_manhattan.add_edge(x246, x48)
G_manhattan.add_edge(x246, x68)
G_manhattan.add_edge(x246, x158)

G_manhattan.add_edge(x68, x246)
G_manhattan.add_edge(x68, x48)
G_manhattan.add_edge(x68, x100)
G_manhattan.add_edge(x68, x186)
G_manhattan.add_edge(x68, x90)
G_manhattan.add_edge(x68, x158)
G_manhattan.add_edge(x68, x249)

G_manhattan.add_edge(x230, x48)
G_manhattan.add_edge(x230, x163)
G_manhattan.add_edge(x230, x161)
G_manhattan.add_edge(x230, x100)

G_manhattan.add_edge(x100, x230)
G_manhattan.add_edge(x100, x48)
G_manhattan.add_edge(x100, x68)
G_manhattan.add_edge(x100, x186)
G_manhattan.add_edge(x100, x164)

G_manhattan.add_edge(x161, x163)
G_manhattan.add_edge(x161, x230)
G_manhattan.add_edge(x161, x164)
G_manhattan.add_edge(x161, x170)
G_manhattan.add_edge(x161, x162)

G_manhattan.add_edge(x162, x161)
G_manhattan.add_edge(x162, x163)
G_manhattan.add_edge(x162, x229)
G_manhattan.add_edge(x162, x233)
G_manhattan.add_edge(x162, x237)
G_manhattan.add_edge(x162, x170)

G_manhattan.add_edge(x229, x162)
G_manhattan.add_edge(x229, x233)
G_manhattan.add_edge(x229, x141)
G_manhattan.add_edge(x229, x140)

G_manhattan.add_edge(x233, x229)
G_manhattan.add_edge(x233, x162)
G_manhattan.add_edge(x233, x170)
G_manhattan.add_edge(x233, x137)

G_manhattan.add_edge(x170, x233)
G_manhattan.add_edge(x170, x162)
G_manhattan.add_edge(x170, x161)
G_manhattan.add_edge(x170, x164)
G_manhattan.add_edge(x170, x107)
G_manhattan.add_edge(x170, x137)

G_manhattan.add_edge(x137, x170)
G_manhattan.add_edge(x137, x233)
G_manhattan.add_edge(x137, x107)
G_manhattan.add_edge(x137, x224)

G_manhattan.add_edge(x224, x137)
G_manhattan.add_edge(x224, x107)
G_manhattan.add_edge(x224, x79)
G_manhattan.add_edge(x224, x4)

G_manhattan.add_edge(x107, x224)
G_manhattan.add_edge(x107, x137)
G_manhattan.add_edge(x107, x170)
G_manhattan.add_edge(x107, x234)
G_manhattan.add_edge(x107, x79)

G_manhattan.add_edge(x164, x161)
G_manhattan.add_edge(x164, x170)
G_manhattan.add_edge(x164, x100)
G_manhattan.add_edge(x164, x186)
G_manhattan.add_edge(x164, x234)

G_manhattan.add_edge(x186, x100)
G_manhattan.add_edge(x186, x68)
G_manhattan.add_edge(x186, x164)
G_manhattan.add_edge(x186, x234)
G_manhattan.add_edge(x186, x90)

G_manhattan.add_edge(x234, x164)
G_manhattan.add_edge(x234, x186)
G_manhattan.add_edge(x234, x90)
G_manhattan.add_edge(x234, x107)
G_manhattan.add_edge(x234, x113)

G_manhattan.add_edge(x90, x68)
G_manhattan.add_edge(x90, x186)
G_manhattan.add_edge(x90, x234)
G_manhattan.add_edge(x90, x249)

G_manhattan.add_edge(x249, x158)
G_manhattan.add_edge(x249, x68)
G_manhattan.add_edge(x249, x90)
G_manhattan.add_edge(x249, x113)
G_manhattan.add_edge(x249, x114)
G_manhattan.add_edge(x249, x125)

G_manhattan.add_edge(x158, x246)
G_manhattan.add_edge(x158, x68)
G_manhattan.add_edge(x158, x249)
G_manhattan.add_edge(x158, x125)

G_manhattan.add_edge(x113, x249)
G_manhattan.add_edge(x113, x234)
G_manhattan.add_edge(x113, x79)
G_manhattan.add_edge(x113, x114)

G_manhattan.add_edge(x79, x4)
G_manhattan.add_edge(x79, x148)
G_manhattan.add_edge(x79, x114)
G_manhattan.add_edge(x79, x113)
G_manhattan.add_edge(x79, x107)
G_manhattan.add_edge(x79, x224)

G_manhattan.add_edge(x4, x79)
G_manhattan.add_edge(x4, x224)
G_manhattan.add_edge(x4, x232)

G_manhattan.add_edge(x232, x4)
G_manhattan.add_edge(x232, x148)
G_manhattan.add_edge(x232, x45)

G_manhattan.add_edge(x148, x232)
G_manhattan.add_edge(x148, x79)
G_manhattan.add_edge(x148, x144)
G_manhattan.add_edge(x148, x45)

G_manhattan.add_edge(x144, x148)
G_manhattan.add_edge(x144, x45)
G_manhattan.add_edge(x144, x231)
G_manhattan.add_edge(x144, x211)
G_manhattan.add_edge(x144, x114)

G_manhattan.add_edge(x114,x144)
G_manhattan.add_edge(x114,x79)
G_manhattan.add_edge(x114,x113)
G_manhattan.add_edge(x114,x249)
G_manhattan.add_edge(x114,x211)
G_manhattan.add_edge(x114,x125)

G_manhattan.add_edge(x125, x114)
G_manhattan.add_edge(x125, x211)
G_manhattan.add_edge(x125, x158)
G_manhattan.add_edge(x125, x249)
G_manhattan.add_edge(x125, x231)

G_manhattan.add_edge(x211,x125)
G_manhattan.add_edge(x211,x114)
G_manhattan.add_edge(x211,x144)
G_manhattan.add_edge(x211,x231)

G_manhattan.add_edge(x231, x211)
G_manhattan.add_edge(x231, x125)
G_manhattan.add_edge(x231, x144)
G_manhattan.add_edge(x231, x45)
G_manhattan.add_edge(x231, x209)
G_manhattan.add_edge(x231, x261)
G_manhattan.add_edge(x231, x13)

G_manhattan.add_edge(x45, x231)
G_manhattan.add_edge(x45, x144)
G_manhattan.add_edge(x45, x148)
G_manhattan.add_edge(x45, x232)
G_manhattan.add_edge(x45, x209)

G_manhattan.add_edge(x209, x45)
G_manhattan.add_edge(x209, x231)
G_manhattan.add_edge(x209, x261)
G_manhattan.add_edge(x209, x87)

G_manhattan.add_edge(x87, x209)
G_manhattan.add_edge(x87, x261)
G_manhattan.add_edge(x87, x88)

G_manhattan.add_edge(x261, x87)
G_manhattan.add_edge(x261, x209)
G_manhattan.add_edge(x261, x231)
G_manhattan.add_edge(x261, x13)
G_manhattan.add_edge(x261, x12)
G_manhattan.add_edge(x261, x88)

G_manhattan.add_edge(x13, x261)
G_manhattan.add_edge(x13, x231)
G_manhattan.add_edge(x13, x12)

G_manhattan.add_edge(x261, x13)
G_manhattan.add_edge(x261, x231)
G_manhattan.add_edge(x261, x209)
G_manhattan.add_edge(x261, x87)
G_manhattan.add_edge(x261, x88)
G_manhattan.add_edge(x261, x12)

G_manhattan.add_edge(x12, x261)
G_manhattan.add_edge(x12, x13)
G_manhattan.add_edge(x12, x88)
G_manhattan.add_edge(x12, x105)
G_manhattan.add_edge(x12, x103)
G_manhattan.add_edge(x12, x104)

G_manhattan.add_edge(x104, x12)
G_manhattan.add_edge(x104, x103)

G_manhattan.add_edge(x103, x104)
G_manhattan.add_edge(x103, x12)

G_manhattan.add_edge(x88,x12)
G_manhattan.add_edge(x88,x261)
G_manhattan.add_edge(x88,x105)
G_manhattan.add_edge(x88,x87)

G_manhattan.add_edge(x105, x12)
G_manhattan.add_edge(x105,x88)

G_manhattan.graph['node_weight_attr']='weight'

#brooklyn graph

G_brooklyn = nx.Graph()
x55=0
G_brooklyn.add_node(x55, weight=1)
x108=1
G_brooklyn.add_node(x108, weight=1)
x29=2
G_brooklyn.add_node(x29, weight=1)
x21=3
G_brooklyn.add_node(x21, weight=1)
x123=4
G_brooklyn.add_node(x123, weight=1)
x210=5
G_brooklyn.add_node(x210, weight=1)
x150=6
G_brooklyn.add_node(x150, weight=1)
x154=7
G_brooklyn.add_node(x154, weight=1)
x155=8
G_brooklyn.add_node(x155, weight=1)
x149=9
G_brooklyn.add_node(x149, weight=1)
x178=10
G_brooklyn.add_node(x178, weight=1)
x165=11
G_brooklyn.add_node(x165, weight=1)
x39=12
G_brooklyn.add_node(x39, weight=1)
x91=13
G_brooklyn.add_node(x91, weight=1)
x26=14
G_brooklyn.add_node(x26, weight=1)
x22=15
G_brooklyn.add_node(x22, weight=1)
x11=16
G_brooklyn.add_node(x11, weight=1)
x67=17
G_brooklyn.add_node(x67, weight=1)
x14=18
G_brooklyn.add_node(x14, weight=1)
x228=19
G_brooklyn.add_node(x228, weight=1)
x227=20
G_brooklyn.add_node(x227, weight=1)
x111=21
G_brooklyn.add_node(x111, weight=1)
x181=22
G_brooklyn.add_node(x181, weight=1)
x106=23
G_brooklyn.add_node(x106, weight=1)
x89=24
G_brooklyn.add_node(x89, weight=1)
x133=25
G_brooklyn.add_node(x133, weight=1)
x257=26
G_brooklyn.add_node(x257, weight=1)
x71=27
G_brooklyn.add_node(x71, weight=1)
x85=28
G_brooklyn.add_node(x85, weight=1)
x188=29
G_brooklyn.add_node(x188, weight=1)
x190=30
G_brooklyn.add_node(x190, weight=1)
x62=31
G_brooklyn.add_node(x62, weight=1)
x189=32
G_brooklyn.add_node(x189, weight=1)
x72=33
G_brooklyn.add_node(x72, weight=1)
x61=34
G_brooklyn.add_node(x61, weight=1)
x35=35
G_brooklyn.add_node(x35, weight=1)
x76=36
G_brooklyn.add_node(x76, weight=1)
x97=37
G_brooklyn.add_node(x97, weight=1)
x25=38
G_brooklyn.add_node(x25, weight=1)
x40=39
G_brooklyn.add_node(x40, weight=1)
x195=40
G_brooklyn.add_node(x195, weight=1)
x54=41
G_brooklyn.add_node(x54, weight=1)
x52=42
G_brooklyn.add_node(x52, weight=1)
x33=43
G_brooklyn.add_node(x33, weight=1)
x65=44
G_brooklyn.add_node(x65, weight=1)
x66=45
G_brooklyn.add_node(x66, weight=1)
x34=46
G_brooklyn.add_node(x34, weight=1)
x49=47
G_brooklyn.add_node(x49, weight=1)
x217=48
G_brooklyn.add_node(x217, weight=1)
x17=49
G_brooklyn.add_node(x17, weight=1)
x225=50
G_brooklyn.add_node(x225, weight=1)
x37=51
G_brooklyn.add_node(x37, weight=1)
x80=52
G_brooklyn.add_node(x80, weight=1)
x177=53
G_brooklyn.add_node(x177, weight=1)
x222=54
G_brooklyn.add_node(x222, weight=1)
x77=55
G_brooklyn.add_node(x77, weight=1)
x63=56
G_brooklyn.add_node(x63, weight=1)
x36=57
G_brooklyn.add_node(x36, weight=1)
x112=58
G_brooklyn.add_node(x112, weight=1)
x255=59
G_brooklyn.add_node(x255, weight=1)
x256=60
G_brooklyn.add_node(x256, weight=1)



D_brooklyn=	{
    0:55,
    1:108,
    2:29,
    3:21,
    4:123,
    5:210,
    6:150,
    7:154,
    8:155,
    9:149,
    10:178,
    11:165,
    12:39,
    13:91,
    14:26,
    15:22,
    16:11,
    17:67,
    18:14,
    19:228,
    20:227,
    21:111,
    22:181,
    23:106,
    24:89,
    25:133,
    26:257,
    27:71,
    28:85,
    29:188,
    30:190,
    31:62,
    32:189,
    33:72,
    34:61,
    35:35,
    36:76,
    37:97,
    38:25,
    39:40,
    40:195,
    41:54,
    42:52,
    43:33,
    44:65,
    45:66,
    46:34,
    47:49,
    48:217,
    49:17,
    50:225,
    51:37,
    52:80,
    53:177,
    54:222,
    55:77,
    56:63,
    57:36,
    58:112,
    59:255,
    60:256
}


G_brooklyn.add_edge(x55,x108)
G_brooklyn.add_edge(x55,x29)

G_brooklyn.add_edge(x108, x55)
G_brooklyn.add_edge(x108, x21)
G_brooklyn.add_edge(x108, x123)
G_brooklyn.add_edge(x108, x29)

G_brooklyn.add_edge(x29, x55)
G_brooklyn.add_edge(x29, x108)
G_brooklyn.add_edge(x29, x123)
G_brooklyn.add_edge(x29, x210)
G_brooklyn.add_edge(x29, x150)
G_brooklyn.add_edge(x29, x154)

G_brooklyn.add_edge(x150, x29)
G_brooklyn.add_edge(x150, x154)

G_brooklyn.add_edge(x154, x150)
G_brooklyn.add_edge(x154, x29)
G_brooklyn.add_edge(x154, x210)
G_brooklyn.add_edge(x154, x155)

G_brooklyn.add_edge(x210, x154)
G_brooklyn.add_edge(x210, x149)
G_brooklyn.add_edge(x210, x29)
G_brooklyn.add_edge(x210, x123)

G_brooklyn.add_edge(x123, x210)
G_brooklyn.add_edge(x123, x29)
G_brooklyn.add_edge(x123, x108)
G_brooklyn.add_edge(x123, x21)
G_brooklyn.add_edge(x123, x178)
G_brooklyn.add_edge(x123, x165)
G_brooklyn.add_edge(x123, x149)

G_brooklyn.add_edge(x149,  x210)
G_brooklyn.add_edge(x149,  x123)
G_brooklyn.add_edge(x149,  x154)
G_brooklyn.add_edge(x149,  x155)
G_brooklyn.add_edge(x149,  x165)
G_brooklyn.add_edge(x149,  x178)

G_brooklyn.add_edge(x154, x150)
G_brooklyn.add_edge(x154, x210)
G_brooklyn.add_edge(x154, x155)
G_brooklyn.add_edge(x154, x149)
G_brooklyn.add_edge(x154, x39)

G_brooklyn.add_edge(x155, x149)
G_brooklyn.add_edge(x155, x154)
G_brooklyn.add_edge(x155, x39)
G_brooklyn.add_edge(x155, x91)

G_brooklyn.add_edge(x21, x108)
G_brooklyn.add_edge(x21, x123)
G_brooklyn.add_edge(x21, x178)
G_brooklyn.add_edge(x21, x26)
G_brooklyn.add_edge(x21, x22)

G_brooklyn.add_edge(x22, x11)
G_brooklyn.add_edge(x22, x21)
G_brooklyn.add_edge(x22, x67)
G_brooklyn.add_edge(x22, x26)

G_brooklyn.add_edge(x11, x22)
G_brooklyn.add_edge(x11, x67)

G_brooklyn.add_edge(x14, x228)
G_brooklyn.add_edge(x14, x227)
G_brooklyn.add_edge(x14, x67)

G_brooklyn.add_edge(x67, x11)
G_brooklyn.add_edge(x67, x22)
G_brooklyn.add_edge(x67, x14)
G_brooklyn.add_edge(x67, x227)
G_brooklyn.add_edge(x67, x26)

G_brooklyn.add_edge(x228, x14)
G_brooklyn.add_edge(x228, x227)
G_brooklyn.add_edge(x228, x111)
G_brooklyn.add_edge(x228, x181)
G_brooklyn.add_edge(x228, x106)

G_brooklyn.add_edge(x227, x228)
G_brooklyn.add_edge(x227, x14)
G_brooklyn.add_edge(x227, x67)
G_brooklyn.add_edge(x227, x26)
G_brooklyn.add_edge(x227, x111)

G_brooklyn.add_edge(x26,x227)
G_brooklyn.add_edge(x26,x67)
G_brooklyn.add_edge(x26,x22)
G_brooklyn.add_edge(x26,x89)
G_brooklyn.add_edge(x26,x178)
G_brooklyn.add_edge(x26,x133)
G_brooklyn.add_edge(x26,x111)

G_brooklyn.add_edge(x111,x228)
G_brooklyn.add_edge(x111,x227)
G_brooklyn.add_edge(x111,x26)
G_brooklyn.add_edge(x111,x257)
G_brooklyn.add_edge(x111,x133)

G_brooklyn.add_edge(x178, x21)
G_brooklyn.add_edge(x178, x26)
G_brooklyn.add_edge(x178, x123)
G_brooklyn.add_edge(x178, x165)
G_brooklyn.add_edge(x178, x89)

G_brooklyn.add_edge(x165, x178)
G_brooklyn.add_edge(x165, x123)
G_brooklyn.add_edge(x165, x149)
G_brooklyn.add_edge(x165, x91)
G_brooklyn.add_edge(x165, x89)

G_brooklyn.add_edge(x133, x89)
G_brooklyn.add_edge(x133, x26)
G_brooklyn.add_edge(x133, x111)
G_brooklyn.add_edge(x133, x257)

G_brooklyn.add_edge(x89, x133)
G_brooklyn.add_edge(x89, x178)
G_brooklyn.add_edge(x89, x26)
G_brooklyn.add_edge(x89, x165)
G_brooklyn.add_edge(x89, x91)
G_brooklyn.add_edge(x89, x71)
G_brooklyn.add_edge(x89, x85)
G_brooklyn.add_edge(x89, x188)
G_brooklyn.add_edge(x89, x190)
G_brooklyn.add_edge(x89, x257)

G_brooklyn.add_edge(x257, x133)
G_brooklyn.add_edge(x257, x111)
G_brooklyn.add_edge(x257, x89)
G_brooklyn.add_edge(x257, x190)
G_brooklyn.add_edge(x257, x181)

G_brooklyn.add_edge(x190, x257)
G_brooklyn.add_edge(x190, x181)
G_brooklyn.add_edge(x190, x89)
G_brooklyn.add_edge(x190, x188)
G_brooklyn.add_edge(x190, x62)
G_brooklyn.add_edge(x190, x189)

G_brooklyn.add_edge(x91, x155)
G_brooklyn.add_edge(x91, x165)
G_brooklyn.add_edge(x91, x89)
G_brooklyn.add_edge(x91, x71)
G_brooklyn.add_edge(x91, x72)
G_brooklyn.add_edge(x91, x39)

G_brooklyn.add_edge(x85,x89)
G_brooklyn.add_edge(x85,x71)
G_brooklyn.add_edge(x85,x188)

G_brooklyn.add_edge(x71, x85)
G_brooklyn.add_edge(x71, x89)
G_brooklyn.add_edge(x71, x188)
G_brooklyn.add_edge(x71, x72)
G_brooklyn.add_edge(x71, x91)

G_brooklyn.add_edge(x72, x71)
G_brooklyn.add_edge(x72, x39)
G_brooklyn.add_edge(x72, x91)
G_brooklyn.add_edge(x72, x188)
G_brooklyn.add_edge(x72, x62)
G_brooklyn.add_edge(x72, x61)
G_brooklyn.add_edge(x72, x35)
G_brooklyn.add_edge(x72, x76)
G_brooklyn.add_edge(x72, x39)

G_brooklyn.add_edge(x188,x72)
G_brooklyn.add_edge(x188,x71)
G_brooklyn.add_edge(x188,x85)
G_brooklyn.add_edge(x188,x89)
G_brooklyn.add_edge(x188,x190)
G_brooklyn.add_edge(x188,x62)

G_brooklyn.add_edge(x62, x188)
G_brooklyn.add_edge(x62, x190)
G_brooklyn.add_edge(x62, x61)
G_brooklyn.add_edge(x62, x72)
G_brooklyn.add_edge(x62, x189)

G_brooklyn.add_edge(x181, x257)
G_brooklyn.add_edge(x181, x228)
G_brooklyn.add_edge(x181, x106)
G_brooklyn.add_edge(x181, x190)
G_brooklyn.add_edge(x181, x189)
G_brooklyn.add_edge(x181, x97)
G_brooklyn.add_edge(x181, x25)

G_brooklyn.add_edge(x106, x181)
G_brooklyn.add_edge(x106, x228)
G_brooklyn.add_edge(x106, x40)
G_brooklyn.add_edge(x106, x25)

G_brooklyn.add_edge(x40,x106)
G_brooklyn.add_edge(x40,x195)
G_brooklyn.add_edge(x40,x54)
G_brooklyn.add_edge(x40,x52)
G_brooklyn.add_edge(x40,x25)

G_brooklyn.add_edge(x195,x40)
G_brooklyn.add_edge(x195,x54)

G_brooklyn.add_edge(x54,x195)
G_brooklyn.add_edge(x54,x52)
G_brooklyn.add_edge(x54,x33)

G_brooklyn.add_edge(x52,x54)
G_brooklyn.add_edge(x52,x40)
G_brooklyn.add_edge(x52,x25)
G_brooklyn.add_edge(x52,x33)

G_brooklyn.add_edge(x33,x54)
G_brooklyn.add_edge(x33,x52)
G_brooklyn.add_edge(x33,x25)
G_brooklyn.add_edge(x33,x65)
G_brooklyn.add_edge(x33,x66)

G_brooklyn.add_edge(x25,x33)
G_brooklyn.add_edge(x25,x52)
G_brooklyn.add_edge(x25,x40)
G_brooklyn.add_edge(x25,x106)
G_brooklyn.add_edge(x25,x65)
G_brooklyn.add_edge(x25,x97)

G_brooklyn.add_edge(x65,x25)
G_brooklyn.add_edge(x65,x33)
G_brooklyn.add_edge(x65,x66)
G_brooklyn.add_edge(x65,x97)

G_brooklyn.add_edge(x66,x65)
G_brooklyn.add_edge(x66,x33)
G_brooklyn.add_edge(x66,x34)
G_brooklyn.add_edge(x66,x97)

G_brooklyn.add_edge(x97, x65)
G_brooklyn.add_edge(x97, x66)
G_brooklyn.add_edge(x97, x25)
G_brooklyn.add_edge(x97, x181)
G_brooklyn.add_edge(x97, x189)
G_brooklyn.add_edge(x97, x49)
G_brooklyn.add_edge(x97, x34)

G_brooklyn.add_edge(x34, x97)
G_brooklyn.add_edge(x34, x65)
G_brooklyn.add_edge(x34, x66)
G_brooklyn.add_edge(x34, x49)
G_brooklyn.add_edge(x34, x217)

G_brooklyn.add_edge(x189, x97)
G_brooklyn.add_edge(x189, x181)
G_brooklyn.add_edge(x189, x190)
G_brooklyn.add_edge(x189, x62)
G_brooklyn.add_edge(x189, x61)
G_brooklyn.add_edge(x189, x49)

G_brooklyn.add_edge(x49, x189)
G_brooklyn.add_edge(x49, x97)
G_brooklyn.add_edge(x49, x34)
G_brooklyn.add_edge(x49, x217)
G_brooklyn.add_edge(x49, x17)
G_brooklyn.add_edge(x49, x61)

G_brooklyn.add_edge(x17, x49)
G_brooklyn.add_edge(x17, x61)
G_brooklyn.add_edge(x17, x225)
G_brooklyn.add_edge(x17, x37)
G_brooklyn.add_edge(x17, x80)
G_brooklyn.add_edge(x17, x217)

G_brooklyn.add_edge(x61, x17)
G_brooklyn.add_edge(x61, x49)
G_brooklyn.add_edge(x61, x189)
G_brooklyn.add_edge(x61, x62)
G_brooklyn.add_edge(x61, x72)
G_brooklyn.add_edge(x61, x177)
G_brooklyn.add_edge(x61, x225)
G_brooklyn.add_edge(x61, x35)

G_brooklyn.add_edge(x39, x155)
G_brooklyn.add_edge(x39, x91)
G_brooklyn.add_edge(x39, x72)
G_brooklyn.add_edge(x39, x76)
G_brooklyn.add_edge(x39, x155)
G_brooklyn.add_edge(x39, x222)

G_brooklyn.add_edge(x222, x39)
G_brooklyn.add_edge(x222, x76)

G_brooklyn.add_edge(x76, x222)
G_brooklyn.add_edge(x76, x77)
G_brooklyn.add_edge(x76, x35)
G_brooklyn.add_edge(x76, x63)
G_brooklyn.add_edge(x76, x39)

G_brooklyn.add_edge(x63, x76)
G_brooklyn.add_edge(x63, x177)
G_brooklyn.add_edge(x63, x37)

G_brooklyn.add_edge(x77, x76)
G_brooklyn.add_edge(x77, x63)
G_brooklyn.add_edge(x77, x177)
G_brooklyn.add_edge(x77, x35)

G_brooklyn.add_edge(x35, x76)
G_brooklyn.add_edge(x35, x72)
G_brooklyn.add_edge(x35, x61)
G_brooklyn.add_edge(x35, x177)
G_brooklyn.add_edge(x35, x77)

G_brooklyn.add_edge(x177, x35)
G_brooklyn.add_edge(x177, x61)
G_brooklyn.add_edge(x177, x225)
G_brooklyn.add_edge(x177, x77)
G_brooklyn.add_edge(x177, x37)
G_brooklyn.add_edge(x177, x63)

G_brooklyn.add_edge(x225, x177)
G_brooklyn.add_edge(x225, x61)
G_brooklyn.add_edge(x225, x17)
G_brooklyn.add_edge(x225, x37)


G_brooklyn.add_edge(x37, x225)
G_brooklyn.add_edge(x37, x177)
G_brooklyn.add_edge(x37, x63)
G_brooklyn.add_edge(x37, x17)
G_brooklyn.add_edge(x37, x36)
G_brooklyn.add_edge(x37, x80)

G_brooklyn.add_edge(x36, x37)
G_brooklyn.add_edge(x36, x80)

G_brooklyn.add_edge(x80, x36)
G_brooklyn.add_edge(x80, x112)
G_brooklyn.add_edge(x80, x255)
G_brooklyn.add_edge(x80, x37)
G_brooklyn.add_edge(x80, x256)
G_brooklyn.add_edge(x80, x17)
G_brooklyn.add_edge(x80, x217)

G_brooklyn.add_edge(x217, x80)
G_brooklyn.add_edge(x217, x256)
G_brooklyn.add_edge(x217, x34)
G_brooklyn.add_edge(x217, x49)
G_brooklyn.add_edge(x217, x17)

G_brooklyn.add_edge(x256, x217)
G_brooklyn.add_edge(x256, x80)
G_brooklyn.add_edge(x256, x255)
G_brooklyn.add_edge(x256, x34)

G_brooklyn.add_edge(x255, x256)
G_brooklyn.add_edge(x255, x80)
G_brooklyn.add_edge(x255, x112)

G_brooklyn.add_edge(x112, x255)
G_brooklyn.add_edge(x112, x80)

G_brooklyn.graph['node_weight_attr']='weight'
#queens graph

G_queens = nx.Graph()


D_queens=	{
    0:64,
    1:101,
    2:19,
    3:175,
    4:16,
    5:191,
    6:131,
    7:122,
    8:205,
    9:38,
    10:98,
    11:15,
    12:121,
    13:92,
    14:73,
    15:171,
    16:252,
    17:139,
    18:218,
    19:219,
    20:203,
    21:132,
    22:216,
    23:124,
    24:2,
    25:201,
    26:117,
    27:180,
    28:197,
    29:258,
    30:10,
    31:215,
    32:130,
    33:28,
    34:96,
    35:134,
    36:102,
    37:95,
    38:196,
    39:160,
    40:198,
    41:157,
    42:93,
    43:135,
    44:192,
    45:53,
    46:253,
    47:56,
    48:173,
    49:57,
    50:70,
    51:138,
    52:82,
    53:129,
    54:223,
    55:83,
    56:260,
    57:207,
    58:226,
    59:7,
    60:146,
    61:145,
    62:193,
    63:179,
    64:8,
    65:27,
    66:86,
    67:30
}

x64=0
G_queens.add_node(x64, weight=1)
x101=1
G_queens.add_node(x101, weight=1)
x19=2
G_queens.add_node(x19, weight=1)
x175=3
G_queens.add_node(x175, weight=1)
x16=4
G_queens.add_node(x16, weight=1)
x191=5
G_queens.add_node(x191, weight=1)
x131=6
G_queens.add_node(x131, weight=1)
x122=7
G_queens.add_node(x122, weight=1)
x205=8
G_queens.add_node(x205, weight=1)
x38=9
G_queens.add_node(x38, weight=1)
x98=10
G_queens.add_node(x98, weight=1)
x15=11
G_queens.add_node(x15, weight=1)
x121=12
G_queens.add_node(x121, weight=1)
x92=13
G_queens.add_node(x92, weight=1)
x73=14
G_queens.add_node(x73, weight=1)
x171=15
G_queens.add_node(x171, weight=1)
x252=16
G_queens.add_node(x252, weight=1)
x139=17
G_queens.add_node(x139, weight=1)
x218=18
G_queens.add_node(x218, weight=1)
x219=19
G_queens.add_node(x219, weight=1)
x203=20
G_queens.add_node(x203, weight=1)
x132=21
G_queens.add_node(x132, weight=4)
x216=22
G_queens.add_node(x216, weight=1)
x124=23
G_queens.add_node(x124, weight=1)
x2=24
G_queens.add_node(x2, weight=1)
x201=25
G_queens.add_node(x201, weight=1)
x117=26
G_queens.add_node(x117, weight=1)
x180=27
G_queens.add_node(x180, weight=1)
x197=28
G_queens.add_node(x197, weight=1)
x258=29
G_queens.add_node(x258, weight=1)
x10=30
G_queens.add_node(x10, weight=1)
x215=31
G_queens.add_node(x215, weight=1)
x130=32
G_queens.add_node(x130, weight=1)
x28=33
G_queens.add_node(x28, weight=1)
x96=34
G_queens.add_node(x96, weight=1)
x134=35
G_queens.add_node(x134, weight=1)
x102=36
G_queens.add_node(x102, weight=1)
x95=37
G_queens.add_node(x95, weight=1)
x196=38
G_queens.add_node(x196, weight=1)
x160=39
G_queens.add_node(x160, weight=1)
x198=40
G_queens.add_node(x198, weight=1)
x157=41
G_queens.add_node(x157, weight=1)
x93=42
G_queens.add_node(x93, weight=1)
x135=43
G_queens.add_node(x135, weight=1)
x192=44
G_queens.add_node(x192, weight=1)
x53=45
G_queens.add_node(x53, weight=1)
x253=46
G_queens.add_node(x253, weight=1)
x56=47
G_queens.add_node(x56, weight=1)
x173=48
G_queens.add_node(x173, weight=1)
x57=49
G_queens.add_node(x57, weight=1)
x70=50
G_queens.add_node(x70, weight=1)
x138=51
G_queens.add_node(x138, weight=5)
x82=52
G_queens.add_node(x82, weight=1)
x129=53
G_queens.add_node(x129, weight=1)
x223=54
G_queens.add_node(x223, weight=1)
x83=55
G_queens.add_node(x83, weight=1)
x260=56
G_queens.add_node(x260, weight=1)
x207=57
G_queens.add_node(x207, weight=1)
x226=58
G_queens.add_node(x226, weight=1)
x7=59
G_queens.add_node(x7, weight=1)
x146=60
G_queens.add_node(x146, weight=1)
x145=61
G_queens.add_node(x145, weight=1)
x193=62
G_queens.add_node(x193, weight=1)
x179=63
G_queens.add_node(x179, weight=1)
x8=64
G_queens.add_node(x8, weight=1)
x27=65
G_queens.add_node(x27, weight=1)
x86=66
G_queens.add_node(x86, weight=1)
x30=67
G_queens.add_node(x86, weight=1)

G_queens.add_edge(x64,x101)
G_queens.add_edge(x64,x19)
G_queens.add_edge(x64,x175)
G_queens.add_edge(x64,x16)

G_queens.add_edge(x101,x64)
G_queens.add_edge(x101,x19)

G_queens.add_edge(x19,x101)
G_queens.add_edge(x19,x64)
G_queens.add_edge(x19,x175)
G_queens.add_edge(x19,x191)

G_queens.add_edge(x191,x19)
G_queens.add_edge(x191,x175)
G_queens.add_edge(x191,x131)
G_queens.add_edge(x191,x122)
G_queens.add_edge(x191,x205)
G_queens.add_edge(x191,x38)

G_queens.add_edge(x175,x191)
G_queens.add_edge(x175,x19)
G_queens.add_edge(x175,x64)
G_queens.add_edge(x175,x16)
G_queens.add_edge(x175,x98)

G_queens.add_edge(x16,x175)
G_queens.add_edge(x16,x15)
G_queens.add_edge(x16,x9)
G_queens.add_edge(x16,x98)

G_queens.add_edge(x98,x16)
G_queens.add_edge(x98,x9)
G_queens.add_edge(x98,x121)
G_queens.add_edge(x98,x131)
G_queens.add_edge(x98,x175)

G_queens.add_edge(x9,x98)
G_queens.add_edge(x9,x92)
G_queens.add_edge(x9,x73)
G_queens.add_edge(x9,x171)
G_queens.add_edge(x9,x16)

G_queens.add_edge(x15,x252)
G_queens.add_edge(x15,x171)
G_queens.add_edge(x15,x16)

G_queens.add_edge(x38, x191)
G_queens.add_edge(x38, x205)
G_queens.add_edge(x38, x139)

G_queens.add_edge(x139, x38)
G_queens.add_edge(x139, x205)
G_queens.add_edge(x139, x218)
G_queens.add_edge(x139, x219)
G_queens.add_edge(x139, x203)

G_queens.add_edge(x203, x139)
G_queens.add_edge(x203, x219)
G_queens.add_edge(x203, x132)

G_queens.add_edge(x132, x203)
G_queens.add_edge(x132, x219)
G_queens.add_edge(x132, x216)
G_queens.add_edge(x132, x124)
G_queens.add_edge(x132, x2)

G_queens.add_edge(x2, x132)
G_queens.add_edge(x2, x201)
G_queens.add_edge(x2, x117)
G_queens.add_edge(x2, x30)

G_queens.add_edge(x30, x20)

G_queens.add_edge(x124, x132)
G_queens.add_edge(x124, x216)
G_queens.add_edge(x124, x180)

G_queens.add_edge(x180, x124)
G_queens.add_edge(x180, x216)
G_queens.add_edge(x180, x197)
G_queens.add_edge(x180, x258)

G_queens.add_edge(x216, x180)
G_queens.add_edge(x216, x124)
G_queens.add_edge(x216, x132)
G_queens.add_edge(x216, x10)
G_queens.add_edge(x216, x215)
G_queens.add_edge(x216, x130)
G_queens.add_edge(x216, x197)
G_queens.add_edge(x216, x219)

G_queens.add_edge(x219, x216)
G_queens.add_edge(x219, x132)
G_queens.add_edge(x219, x203)
G_queens.add_edge(x219, x139)
G_queens.add_edge(x219, x218)
G_queens.add_edge(x219, x10)

G_queens.add_edge(x218, x219)
G_queens.add_edge(x218, x10)
G_queens.add_edge(x218, x205)
G_queens.add_edge(x218, x139)

G_queens.add_edge(x10, x218)
G_queens.add_edge(x10, x216)
G_queens.add_edge(x10, x219)
G_queens.add_edge(x10, x205)
G_queens.add_edge(x10, x215)

G_queens.add_edge(x205, x10)
G_queens.add_edge(x205, x218)
G_queens.add_edge(x205, x139)
G_queens.add_edge(x205, x38)
G_queens.add_edge(x205, x191)
G_queens.add_edge(x205, x122)
G_queens.add_edge(x205, x130)
G_queens.add_edge(x205, x215)

G_queens.add_edge(x122, x205)
G_queens.add_edge(x122, x130)
G_queens.add_edge(x122, x131)
G_queens.add_edge(x122, x191)
G_queens.add_edge(x122, x38)
G_queens.add_edge(x122, x139)

G_queens.add_edge(x131, x122)
G_queens.add_edge(x131, x191)
G_queens.add_edge(x131, x98)
G_queens.add_edge(x131, x121)
G_queens.add_edge(x131, x28)
G_queens.add_edge(x131, x130)

G_queens.add_edge(x215, x216)
G_queens.add_edge(x215, x10)
G_queens.add_edge(x215, x205)
G_queens.add_edge(x215, x130)

G_queens.add_edge(x130, x215)
G_queens.add_edge(x130, x122)
G_queens.add_edge(x130, x131)
G_queens.add_edge(x130, x28)
G_queens.add_edge(x130, x197)

G_queens.add_edge(x258, x197)
G_queens.add_edge(x258, x96)

G_queens.add_edge(x197, x258)
G_queens.add_edge(x197, x216)
G_queens.add_edge(x197, x130)
G_queens.add_edge(x197, x134)
G_queens.add_edge(x197, x96)

G_queens.add_edge(x96, x197)
G_queens.add_edge(x96, x134)
G_queens.add_edge(x96, x102)
G_queens.add_edge(x96, x258)
G_queens.add_edge(x96, x95)

G_queens.add_edge(x102, x96)
G_queens.add_edge(x102, x95)
G_queens.add_edge(x102, x196)
G_queens.add_edge(x102, x160)
G_queens.add_edge(x102, x198)

G_queens.add_edge(x198, x102)
G_queens.add_edge(x198, x160)
G_queens.add_edge(x198, x157)

G_queens.add_edge(x134, x96)
G_queens.add_edge(x134, x95)
G_queens.add_edge(x134, x197)
G_queens.add_edge(x134, x28)
G_queens.add_edge(x134, x93)

G_queens.add_edge(x28, x134)
G_queens.add_edge(x28, x93)
G_queens.add_edge(x28, x135)
G_queens.add_edge(x28, x121)
G_queens.add_edge(x28, x131)
G_queens.add_edge(x28, x130)

G_queens.add_edge(x121, x28)
G_queens.add_edge(x121, x131)
G_queens.add_edge(x121, x98)
G_queens.add_edge(x121, x9)
G_queens.add_edge(x121, x192)
G_queens.add_edge(x121, x135)

G_queens.add_edge(x135, x121)
G_queens.add_edge(x135, x28)
G_queens.add_edge(x135, x192)
G_queens.add_edge(x135, x93)

G_queens.add_edge(x192, x135)
G_queens.add_edge(x192, x121)
G_queens.add_edge(x192, x9)
G_queens.add_edge(x192, x73)
G_queens.add_edge(x192, x92)
G_queens.add_edge(x192, x93)

G_queens.add_edge(x73, x192)
G_queens.add_edge(x73, x92)
G_queens.add_edge(x73, x9)
G_queens.add_edge(x73, x171)

G_queens.add_edge(x171, x73)
G_queens.add_edge(x171, x16)
G_queens.add_edge(x171, x9)
G_queens.add_edge(x171, x15)
G_queens.add_edge(x171, x252)
G_queens.add_edge(x171, x92)

G_queens.add_edge(x252, x171)
G_queens.add_edge(x252, x15)
G_queens.add_edge(x252, x92)
G_queens.add_edge(x252, x53)

G_queens.add_edge(x53,x252)
G_queens.add_edge(x53,x92)

G_queens.add_edge(x92,x53)
G_queens.add_edge(x92,x252)
G_queens.add_edge(x92,x171)
G_queens.add_edge(x92,x73)
G_queens.add_edge(x92,x192)
G_queens.add_edge(x92,x93)
G_queens.add_edge(x92,x253)

G_queens.add_edge(x253, x92)
G_queens.add_edge(x253, x93)

G_queens.add_edge(x93,x253)
G_queens.add_edge(x93,x92)
G_queens.add_edge(x93,x192)
G_queens.add_edge(x93,x135)
G_queens.add_edge(x93,x28)
G_queens.add_edge(x93,x134)
G_queens.add_edge(x93,x95)
G_queens.add_edge(x93,x56)
G_queens.add_edge(x93,x173)
G_queens.add_edge(x93,x57)
G_queens.add_edge(x93,x70)
G_queens.add_edge(x93,x138)

G_queens.add_edge(x95,x93)
G_queens.add_edge(x95,x134)
G_queens.add_edge(x95,x96)
G_queens.add_edge(x95,x102)
G_queens.add_edge(x95,x196)
G_queens.add_edge(x95,x56)

G_queens.add_edge(x196,x95)
G_queens.add_edge(x196,x56)
G_queens.add_edge(x196,x82)
G_queens.add_edge(x196,x160)
G_queens.add_edge(x196,x102)

G_queens.add_edge(x56, x196)
G_queens.add_edge(x56, x95)
G_queens.add_edge(x56, x93)
G_queens.add_edge(x56, x173)
G_queens.add_edge(x56, x82)

G_queens.add_edge(x57, x93)
G_queens.add_edge(x57, x173)

G_queens.add_edge(x173, x57)
G_queens.add_edge(x173, x56)
G_queens.add_edge(x173, x82)
G_queens.add_edge(x173, x129)
G_queens.add_edge(x173, x70)

G_queens.add_edge(x70, x173)
G_queens.add_edge(x70, x138)
G_queens.add_edge(x70, x129)

G_queens.add_edge(x138,x70)
G_queens.add_edge(x138,x129)
G_queens.add_edge(x138,x223)

G_queens.add_edge(x129, x138)
G_queens.add_edge(x129, x223)
G_queens.add_edge(x129, x70)
G_queens.add_edge(x129, x173)
G_queens.add_edge(x129, x83)
G_queens.add_edge(x129, x260)
G_queens.add_edge(x129, x207)
G_queens.add_edge(x129, x82)

G_queens.add_edge(x160, x196)
G_queens.add_edge(x160, x102)
G_queens.add_edge(x160, x198)
G_queens.add_edge(x160, x157)
G_queens.add_edge(x160, x82)

G_queens.add_edge(x82, x160)
G_queens.add_edge(x82, x196)
G_queens.add_edge(x82, x56)
G_queens.add_edge(x82, x173)
G_queens.add_edge(x82, x129)
G_queens.add_edge(x82, x83)
G_queens.add_edge(x82, x157)

G_queens.add_edge(x83, x82)
G_queens.add_edge(x83, x157)
G_queens.add_edge(x83, x260)
G_queens.add_edge(x83, x129)


G_queens.add_edge(x260, x83)
G_queens.add_edge(x260, x129)
G_queens.add_edge(x260, x207)
G_queens.add_edge(x260, x157)
G_queens.add_edge(x260, x226)
G_queens.add_edge(x260, x7)

G_queens.add_edge(x157,x260)
G_queens.add_edge(x157,x226)
G_queens.add_edge(x157,x198)
G_queens.add_edge(x157,x160)
G_queens.add_edge(x157,x83)
G_queens.add_edge(x157,x82)

G_queens.add_edge(x226,x157)
G_queens.add_edge(x226,x260)
G_queens.add_edge(x226,x7)
G_queens.add_edge(x226,x146)
G_queens.add_edge(x226,x145)

G_queens.add_edge(x145, x226)
G_queens.add_edge(x145, x146)
G_queens.add_edge(x145, x193)

G_queens.add_edge(x193, x145)
G_queens.add_edge(x193, x146)
G_queens.add_edge(x193, x179)
G_queens.add_edge(x193, x7)

G_queens.add_edge(x7,x193)
G_queens.add_edge(x7,x146)
G_queens.add_edge(x7,x226)
G_queens.add_edge(x7,x260)
G_queens.add_edge(x7,x207)
G_queens.add_edge(x7,x179)
G_queens.add_edge(x7,x223)

G_queens.add_edge(x179, x7)
G_queens.add_edge(x179, x193)
G_queens.add_edge(x179, x8)
G_queens.add_edge(x179, x223)

G_queens.add_edge(x207, x7)
G_queens.add_edge(x207, x223)
G_queens.add_edge(x207, x260)
G_queens.add_edge(x207, x129)

G_queens.add_edge(x8, x179)
G_queens.add_edge(x8, x223)

G_queens.add_edge(x223, x7)
G_queens.add_edge(x223, x8)
G_queens.add_edge(x223, x179)
G_queens.add_edge(x223, x207)
G_queens.add_edge(x223, x138)

G_queens.add_edge(x27, x201)

G_queens.add_edge(x201, x117)
G_queens.add_edge(x201, x2)

G_queens.add_edge(x117, x201)
G_queens.add_edge(x117, x86)
G_queens.add_edge(x117, x2)

G_queens.add_edge(x86, x117)

G_queens.graph['node_weight_attr']='weight'

tree_depth=6
#cluster the taxi zones in staten island
staten_island_root_name=1
#clusters_staten_island=graph_tree_clustering(G_staten_island,tree_depth,staten_island_root_name, 0, [])
clusters_staten_island=[[staten_island_root_name] * (tree_depth+1)]*len(D_staten_island)
#compute distances between zones in staten island
staten_island_distance = []
for i in range(len(D_staten_island)):
     staten_island_distance.append([0] * len(D_staten_island))

for i in range(len(D_staten_island)):
    for j in range(i,len(D_staten_island)):
        c=nx.shortest_path_length(G_staten_island,source=i,target=j)
        staten_island_distance[i][j]=c
        staten_island_distance[j][i]=c

#cluster the taxi zones in bronx
bronx_root_name= max([max(l) for l in  [clusters_staten_island[i] for i in range(len(D_staten_island))]])+1
#clusters_bronx=graph_tree_clustering(G_bronx,tree_depth,bronx_root_name, 0, [])
clusters_bronx=[[bronx_root_name] * (tree_depth+1)]*len(D_bronx)

bronx_distance = []
for i in range(len(D_bronx)):
    bronx_distance.append([0] * len(D_bronx))

for i in range(len(D_bronx)):
    for j in range(i,len(D_bronx)):
        c=nx.shortest_path_length(G_bronx,source=i,target=j)
        bronx_distance[i][j]=c
        bronx_distance[j][i]=c

#cluster the taxi zones in manhattan
manhattan_root_name= max([max(l) for l in  [clusters_bronx[i] for i in range(len(D_bronx))]])+1
clusters_manhattan=graph_tree_clustering(G_manhattan,tree_depth,manhattan_root_name, 0, [])

manhattan_distance = []
for i in range(len(D_manhattan)):
    manhattan_distance.append([0] * len(D_manhattan))

for i in range(len(D_manhattan)):
    for j in range(i,len(D_manhattan)):
        c=nx.shortest_path_length(G_manhattan,source=i,target=j)
        manhattan_distance[i][j]=c
        manhattan_distance[j][i]=c

#cluster the taxi zones in brooklyn
brooklyn_root_name= max([max(l) for l in  [clusters_manhattan[i] for i in range(len(D_manhattan))]])+1
clusters_brooklyn=graph_tree_clustering(G_brooklyn,tree_depth,brooklyn_root_name, 0, [])

brooklyn_distance = []
for i in range(len(D_brooklyn)):
    brooklyn_distance.append([0] * len(D_brooklyn))

for i in range(len(D_brooklyn)):
    for j in range(i,len(D_brooklyn)):
        c=nx.shortest_path_length(G_brooklyn,source=i,target=j)
        brooklyn_distance[i][j]=c
        brooklyn_distance[j][i]=c


#cluster the taxi zones in queens
queens_root_name= max([max(l) for l in  [clusters_brooklyn[i] for i in range(len(D_brooklyn))]])+1
clusters_queens=graph_tree_clustering(G_queens,tree_depth,queens_root_name, 0, [])
    #for i in range(len(D_queens)):
#clusters_queens[i].append([clusters_queens[i][-1]]*(tree_depth))

#cluster airport
airport_root_name= max([max(l) for l in  [clusters_queens[i] for i in range(len(D_queens))]])+1
clusters_airport=[airport_root_name] * (tree_depth+1)

unknown1_root_name = airport_root_name+1
clusters_unknown1=[unknown1_root_name] * (tree_depth+1)

unknown2_root_name = unknown1_root_name+1
clusters_unknown2=[unknown2_root_name] * (tree_depth+1)

queens_distance = []
for i in range(len(D_queens)):
    queens_distance.append([0] * len(D_queens))

for i in range(len(D_queens)):
    for j in range(i,len(D_queens)):
        c=nx.shortest_path_length(G_queens,source=i,target=j)
        queens_distance[i][j]=c
        queens_distance[j][i]=c

#open the file with the tree cluster of the taxi zones
#with open(path+'taxi_zones_clusters.csv', mode='w') as taxi_zones_cluster_file:
with open('taxi_zones_clusters.csv', mode='w') as taxi_zones_cluster_file:
    taxi_zones_cluster_writer = csv.writer(taxi_zones_cluster_file, delimiter=',')
    cols=['LocationID']
    for i in range(tree_depth+1):
        cols.append("level_"+str(i+1))
    taxi_zones_cluster_writer.writerow(cols)

    #write the taxi zones in staten island
    for i in range(len(D_staten_island)):
        taxi_zones_cluster_writer.writerow([D_staten_island[i]]+clusters_staten_island[i])

    #write the taxi zones in bronx
    for i in range(len(D_bronx)):
        taxi_zones_cluster_writer.writerow([D_bronx[i]]+clusters_bronx[i])

    #write the taxi zones in manhattan
    for i in range(len(D_manhattan)):
        taxi_zones_cluster_writer.writerow([D_manhattan[i]]+clusters_manhattan[i])

    #write the taxi zones in brooklyn:
    for i in range(len(D_brooklyn)):
        taxi_zones_cluster_writer.writerow([D_brooklyn[i]]+clusters_brooklyn[i])

    #write the taxi zones in queens:
    for i in range(len(D_queens)):
        taxi_zones_cluster_writer.writerow([D_queens[i]]+clusters_queens[i])

    taxi_zones_cluster_writer.writerow([1]+clusters_airport)
    taxi_zones_cluster_writer.writerow([264]+clusters_unknown1)
    taxi_zones_cluster_writer.writerow([265]+clusters_unknown2)




#write the distances between taxi-zones in the same area
#with open(path+'distances.csv', mode='w') as distances_file:
with open('distances.csv', mode='w') as distances_file:
    distances_writer = csv.writer(distances_file, delimiter=',')
    cols=['PULocationID', 'DOLocationID', 'distance']
    distances_writer.writerow(cols)
    
    #pickup location in bronx
    for i in range(len(D_bronx)):
        distances_writer.writerow([D_bronx[i], 1, 50])
        distances_writer.writerow([D_bronx[i], 264, 50])
        distances_writer.writerow([D_bronx[i], 265, 50])
        
        for j in range(len(D_bronx)):
            distances_writer.writerow([D_bronx[i], D_bronx[j], bronx_distance[i][j]])

        for j in range(len(D_manhattan)):
            distances_writer.writerow([D_bronx[i], D_manhattan[j], manhattan_distance[j][x168]+bronx_distance[x134][i]])

        for j in range(len(D_queens)):
            distances_writer.writerow([D_bronx[i], D_queens[j], bronx_distance[i][x213]+queens_distance[x53][j]])

        for j in range(len(D_brooklyn)):
            distances_writer.writerow([D_bronx[i], D_brooklyn[j], brooklyn_distance[x63][j]+queens_distance[x53][x258]+bronx_distance[i][x213]])

        for j in range(len(D_staten_island)):
            distances_writer.writerow([D_bronx[i], D_staten_island[j], staten_island_distance[j][x221]+brooklyn_distance[x11][x28]+queens_distance[x258][x53]+bronx_distance[x213][i]])

    #pickup location in manhattan
    for i in range(len(D_manhattan)):
        distances_writer.writerow([D_manhattan[i], 1, 50])
        distances_writer.writerow([D_manhattan[i], 264, 50])
        distances_writer.writerow([D_manhattan[i], 265, 50])
        for j in range(len(D_manhattan)):
            distances_writer.writerow([D_manhattan[i], D_manhattan[j], manhattan_distance[i][j]])
        
        for j in range(len(D_bronx)):
            distances_writer.writerow([D_manhattan[i], D_bronx[j], manhattan_distance[i][x168]+bronx_distance[x134][j]])
        
        for j in range(len(D_queens)):
            distances_writer.writerow([D_manhattan[i], D_queens[j], manhattan_distance[i][x142]+queens_distance[x193][j]])
        
        for j in range(len(D_brooklyn)):
            distances_writer.writerow([D_manhattan[i], D_brooklyn[j], manhattan_distance[i][x232]+brooklyn_distance[x34][j]])
        
        for j in range(len(D_staten_island)):
            distances_writer.writerow([D_manhattan[i], D_staten_island[j], manhattan_distance[i][x105]+staten_island_distance[x206][j]])

    #pickup location in brooklyn
    for i in range(len(D_brooklyn)):
        distances_writer.writerow([D_brooklyn[i], 1, 50])
        distances_writer.writerow([D_brooklyn[i], 264, 50])
        distances_writer.writerow([D_brooklyn[i], 265, 50])
        for j in range(len(D_brooklyn)):
            distances_writer.writerow([D_brooklyn[i], D_brooklyn[j], brooklyn_distance[i][j]])
        
        for j in range(len(D_bronx)):
            distances_writer.writerow([D_brooklyn[i], D_bronx[j], brooklyn_distance[x63][i]+queens_distance[x53][x258]+bronx_distance[j][x213]])

        for j in range(len(D_queens)):
            distances_writer.writerow([D_brooklyn[i], D_queens[j], queens_distance[j][x258]+brooklyn_distance[x63][i]])
        
        for j in range(len(D_manhattan)):
            distances_writer.writerow([D_brooklyn[i], D_manhattan[j], manhattan_distance[j][x232]+brooklyn_distance[x34][i]])

        for j in range(len(D_staten_island)):
            distances_writer.writerow([D_brooklyn[i], D_staten_island[j], staten_island_distance[j][x221]+brooklyn_distance[x11][i]])


    #pickup location in queens
    for i in range(len(D_queens)):
        distances_writer.writerow([D_queens[i], 1, 50])
        distances_writer.writerow([D_queens[i], 264, 50])
        distances_writer.writerow([D_queens[i], 265, 50])
        for j in range(len(D_queens)):
            distances_writer.writerow([D_queens[i], D_queens[j], queens_distance[i][j]])
        
        for j in range(len(D_bronx)):
            distances_writer.writerow([D_queens[i], D_bronx[j], bronx_distance[j][x213]+queens_distance[x53][i]])

        for j in range(len(D_manhattan)):
            distances_writer.writerow([D_queens[i], D_manhattan[j], manhattan_distance[j][x142]+queens_distance[x193][i]])
        
        for j in range(len(D_brooklyn)):
            distances_writer.writerow([D_queens[i], D_brooklyn[j], queens_distance[i][x258]+brooklyn_distance[x63][j]])

        for j in range(len(D_staten_island)):
            distances_writer.writerow([D_queens[i], D_staten_island[j], staten_island_distance[j][x221]+brooklyn_distance[x11][x28]+queens_distance[x258][i]])


    #pickup location in staten island
    for i in range(len(D_staten_island)):
        distances_writer.writerow([D_staten_island[i], 1, 50])
        distances_writer.writerow([D_staten_island[i], 264, 50])
        distances_writer.writerow([D_staten_island[i], 265, 50])
        for j in range(len(D_staten_island)):
            distances_writer.writerow([D_staten_island[i], D_staten_island[j], staten_island_distance[i][j]])
        
        for j in range(len(D_bronx)):
            distances_writer.writerow([D_staten_island[i], D_bronx[j], staten_island_distance[i][x221]+brooklyn_distance[x11][x28]+queens_distance[x258][x53]+bronx_distance[x213][j]])

        for j in range(len(D_manhattan)):
            distances_writer.writerow([D_staten_island[i], D_manhattan[j], manhattan_distance[j][x105]+staten_island_distance[x206][i]])
        
        for j in range(len(D_brooklyn)):
            distances_writer.writerow([D_staten_island[i], D_brooklyn[j], staten_island_distance[i][x221]+brooklyn_distance[x11][j]])

        for j in range(len(D_queens)):
            distances_writer.writerow([D_staten_island[i], D_queens[j], staten_island_distance[i][x221]+brooklyn_distance[x11][x28]+queens_distance[x258][j]])

    #from the airport and unknown areas
    for j in range(len(D_staten_island)):
        distances_writer.writerow([1, D_staten_island[j], 50])
        distances_writer.writerow([264, D_staten_island[j], 50])
        distances_writer.writerow([265, D_staten_island[j], 50])
        
    for j in range(len(D_bronx)):
        distances_writer.writerow([1, D_bronx[j], 50])
        distances_writer.writerow([264, D_bronx[j], 50])
        distances_writer.writerow([265, D_bronx[j], 50])
        
    for j in range(len(D_manhattan)):
        distances_writer.writerow([1, D_manhattan[j], 50])
        distances_writer.writerow([264, D_manhattan[j], 50])
        distances_writer.writerow([265, D_manhattan[j], 50])
        
    for j in range(len(D_brooklyn)):
        distances_writer.writerow([1, D_brooklyn[j], 50])
        distances_writer.writerow([264, D_brooklyn[j], 50])
        distances_writer.writerow([265, D_brooklyn[j], 50])
        
    for j in range(len(D_queens)):
        distances_writer.writerow([1, D_queens[j], 50])
        distances_writer.writerow([264, D_queens[j], 50])
        distances_writer.writerow([265, D_queens[j], 50])

    distances_writer.writerow([1, 1, 0])
    distances_writer.writerow([265, 265, 50])
    distances_writer.writerow([265, 264, 50])
    distances_writer.writerow([264, 264, 50])
    distances_writer.writerow([264, 265, 50])

