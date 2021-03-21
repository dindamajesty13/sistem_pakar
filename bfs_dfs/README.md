Pembahasan contoh DFS dan BFS algorithm

DFS algorithm
contohnya, disini kita memiliki lima simpul yaitu (0, 1, 2, 3, 4) lalu kita buat graph seperti pada kode dibawah ini:
```sh
graph = {'0': set(['1', '2', '3']),
         '1': set(['0']),
         '2': set(['0', '1', '4']),
         '3': set(['0']),
         '4': set(['2'])}
```

![graph](https://user-images.githubusercontent.com/44759037/111896318-5e0ca780-8a4b-11eb-86b8-8232a7b4961a.PNG)

kita akan melihat bagaimana algoritma dfs bekerja dan mengetahui urutan node yang dikunjungi/dilalui oleh algoritma dfs. Dengan algoritma dfs kita akan memulai dengan vertex 0 sebagai node list pertama yang akan dikunjungi (expand node), lalu kita akan melihat apakah 0 memiliki anak (turunan) atau tidak, jika ya maka turunannya akan kita masukkan ke node list  yang akan kita expand. Ternyata 0 memiliki expand node yaitu 1, 2, dan 3. Selanjutnya kita akan lakukan expand pada node 1 dan node 1 tidak memiliki turunan. Setelah node 1 kita akan expand node 2, dan kita menemukan node 4 sebagai turunannya (kita tambahkan 4 ke node list paling atas), selanjutnya karena 4 berada di tumpukan paling atas maka kita expand node 4, kita tidak menemukan turunannya. Terakhir kita expand node 3 dan tidak menemukan turunannya.

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
    
sehingga DFS memiliki urutan kunjungan 0, 1, 2, 4, 3 karena node yang didapatkan diletakkan pada tumpukan stack paling atas, dan DFS akan mengunjungi stack paling atas terlebih dahulu (menerapkan sistem tumpukan).

BFS algorithm
kita menggunakan contoh yang sama dengan algoritma dfs diatas. perbedaannya yaitu terdapat pada penempatan stack, jika pada DFS stack ditempatkan paling atas (paling depan) sedangkan pada BFS stack yang baru ditemukan diletakkan paling bawah (paling belakang) seperti sistem antrian. Sehingga urutan kunjungan (visited) BFS dan DFS akan berbeda.
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
    
sehingga BFS memiliki urutan kunjungan 0, 1, 2, 3, 4 karena node yang didapatkan diletakkan pada tumpukan stack paling bawah (paling belakang), sehingga node 4 yang ditemukan paling akhir akan di kunjungi paling akhir (menerapkan sistem antrian).
