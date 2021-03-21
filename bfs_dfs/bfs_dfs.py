# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 10:39:54 2021

@author: MAJESTY
"""

"""
DFS algorithm
contohnya, disini kita memiliki lima simpul yaitu (0, 1, 2, 3, 4) lalu kita buat graph
seperti pada kode dibawah ini, dan kita akan melihat bagaimana algoritma dfs bekerja
dan mengetahui urutan node yang dikunjungi/dilalui oleh algoritma dfs.
dengan algoritma dfs kita akan memulai dengan vertex 0 sebagai node list 
pertama yang akan dikunjungi (expand node), lalu kita akan melihat apakah 0 memiliki
anak (turunan) atau tidak, jika ya maka turunannya akan kita masukkan ke node list 
yang akan kita expand. Ternyata 0 memiliki expand node yaitu 1, 2, dan 3.
selanjutnya kita akan lakukan expand pada node 1 dan node 1 tidak memiliki turunan.
setelah node 1 kita akan expand node 2, dan kita menemukan node 4 sebagai turunannya 
(kita tambahkan 4 ke node list paling atas), selanjutnya karena 4 berada di tumpukan 
paling atas maka kita expand node 4, kita tidak menemukan turunannya. terakhir kita expand
node 3 dan tidak menemukan turunannya.

berikut simulasi:
    langkah 1
    visited = 0
    stack = 1, 2, 3
    
    langkah 2
    visited = 0, 1
    stack = 2, 3
    
    langkah 3
    visited = 0, 1, 2
    stack = 4, 3
    
    langkah 4
    visited = 0, 1, 2, 4
    stack = 3
    
    langkah 5
    visited = 0, 1, 2, 4, 3
    stack = null
    
sehingga DFS memiliki urutan kunjungan 0, 1, 2, 4, 3 karena node yang didapatkan diletakkan
pada tumpukan stack paling atas, dan DFS akan mengunjungi stack paling atas terlebih dahulu.
"""

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2', '3']),
         '1': set(['0']),
         '2': set(['0', '1', '4']),
         '3': set(['0']),
         '4': set(['2'])}

print("Following is Depth First Traversal: ")
dfs(graph, '0')

"""
BFS algorithm
kita menggunakan contoh yang sama dengan algoritma dfs diatas.
perbedaannya yaitu terdapat pada penempatan stack, jika pada DFS stack ditempatkan paling atas (paling depan) 
sedangkan pada BFS stack yang baru ditemukan diletakkan paling bawah (paling belakang). Sehingga urutan kunjungan (visited)
akan berbeda.
berikut simulasi:
    langkah 1
    visited = 0
    stack = 1, 2, 3
    
    langkah 2
    visited = 0, 1
    stack = 2, 3
    
    langkah 3
    visited = 0, 1, 2
    stack = 3, 4
    
    langkah 4
    visited = 0, 1, 2, 3
    stack = 4
    
    langkah 5
    visited = 0, 1, 2, 3, 4
    stack = null
    
sehingga BFS memiliki urutan kunjungan 0, 1, 2, 3, 4 karena node yang didapatkan diletakkan
pada tumpukan stack paling bawah (paling belakang), sehingga node 4 yang ditemukan paling akhir 
akan di kunjungi paling akhir.
"""

import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {'0': set(['1', '2', '3']),
         '1': set(['0']),
         '2': set(['0', '1', '4']),
         '3': set(['0']),
         '4': set(['2'])}
    print("Following is Breadth First Traversal: ")
    bfs(graph, '0')