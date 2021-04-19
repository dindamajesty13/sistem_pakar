Menggunakan logika fuzzy Tsukamoto untuk melihat berapa jumlah produksi yang harus dilakukan sebuah perusahaan apabila diketahui jumlah permintaan dan persediaan barang perusahaan, hasil dapat dilihat melalui grafik yang ditampilkan dengan menggunakan library matplotlib. Apabila diketahui permintaan yaitu sebanyak 2000 dan persediaan 300, maka berapa barang yang harus diproduksi? menurut metode ini perusahaan harus memproduksi sebanyak 4016 barang.

berikut logika yang digunakan :
1. [R1] IF permintaan TURUN AND Persediaan BANYAK, THEN Produksi Barang dr
2. [R2] IF permintaan TURUN AND Persediaan SEDIKIT, THEN Produksi Barang BERKURANG
3. [R3] IF permintaan NAIK AND Persediaan BANYAK, THEN Produksi Barang BERTAMBAH
4. [R4] IF permintaan NAIK AND Persediaan SEDIKIT, THEN Produksi Barang BERTAMBAH
