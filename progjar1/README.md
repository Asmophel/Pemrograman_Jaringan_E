# Tugas 1 Pemrograman Jaringan

Fandi Wahyu Rusydi

05111840000108

Pemrograman Jaringan E

# Jawaban :

## No 1 Buatlah fork dari https://github.com/rm77/progjar.git ke repo kalian masing-masing (yang sudah disetorkan ke asisten)

Ada pada github ini

## No 2 Jalankan simulator, gunakan 3 buah node alpine , pastikan 3 buah node alpine tersebut tersambung (cek dengan command ping ip address masing-masing)

Berikut adalah gambar topologi yang digunakan. Setelah pengecekan semua ip address telah tersambung.

![](https://github.com/Asmophel/Pemrograman_Jaringan_E/blob/master/progjar1/img1/1.PNG)

alpine-1 ping alpine 2

![](https://github.com/Asmophel/Pemrograman_Jaringan_E/blob/master/progjar1/img1/2.PNG)

alpine-2 ping alpine 3

![](https://github.com/Asmophel/Pemrograman_Jaringan_E/blob/master/progjar1/img1/3.PNG)

alpine-3 ping alpine 1

![](https://github.com/Asmophel/Pemrograman_Jaringan_E/blob/master/progjar1/img1/4.PNG)

## No 3 Clone lah repository hasil fork tersebut di masing-masing node tersebut di direktori /home/work (jika belum ada dapat dibuat dulu dengan mkdir -p /home/work)

Setelah di clone pada tiap node

![](https://github.com/Asmophel/Pemrograman_Jaringan_E/blob/master/progjar1/img1/5.PNG)

## No 4 Dari direktori progjar1 dari repository tersebut:

### Jalankan program server.py di alpine-1 dan alpine-2, jalankan program client.py di alpine 3

Sebelum menjalankan program server.py pada alpine-1 dan alpine-2, ubah ip pada masing program menjadi ip alpine-1 dan alpine-2, untuk lebih lengkap dapat melihat file server.py

alpine-1 menjadi seperti berikut

![](https://github.com/Asmophel/Pemrograman_Jaringan_E/blob/master/progjar1/img1/6.PNG)

alpine-2 menjadi seperti berikut

![](https://github.com/Asmophel/Pemrograman_Jaringan_E/blob/master/progjar1/img1/7.PNG)

lalu, sebelum menjalankan program client.py pada alpine-3, ubah server_address, print, socket, dan response sesuai ip pada alpine-1 dan alpine-2, untuk lebih lengkap dapat melihat file client.py

![](https://github.com/Asmophel/Pemrograman_Jaringan_E/blob/master/progjar1/img1/8.PNG)

setelah itu, jalankan server pada alpine-1 dan 2 terlebih dahulu sebelum menjalankan client

![](https://github.com/Asmophel/Pemrograman_Jaringan_E/blob/master/progjar1/img1/9.PNG)

![](https://github.com/Asmophel/Pemrograman_Jaringan_E/blob/master/progjar1/img1/10.PNG)

Setelah itu jalankan client pada alpine 3

![](https://github.com/Asmophel/Pemrograman_Jaringan_E/blob/master/progjar1/img1/11.PNG)

berikut alpine-1 setelah client dijalankan

![](https://github.com/Asmophel/Pemrograman_Jaringan_E/blob/master/progjar1/img1/12.PNG)

berikut alpine-2 setelah client dijalankan

![](https://github.com/Asmophel/Pemrograman_Jaringan_E/blob/master/progjar1/img1/13.PNG)

### Modifikasilah program client.py tersebut untuk mengirim string sebesar 2 megabytes


### Modifikasilah program client.py tersebut untuk mengirim file gambar, dan menulis respon baliknya ke dalam nama file yang berbeda


