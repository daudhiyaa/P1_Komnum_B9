# Kelompok 9 Komputasi Numerik B

## Anggota

|     | Nama                              | NRP        |
| --- | --------------------------------- | ---------- |
| 1   | Daud Dhiya' Rozaan                | 5025211021 |
| 2   | Gracetriana Survinta Septinaputri | 5025211199 |
| 3   | Nadira Milha Nailul Fath          | 5025211253 |

## **Result's Preview**

![1](https://user-images.githubusercontent.com/90663569/197921542-dc4943e9-a103-4317-8146-f26d7bffba60.png)
![2](https://user-images.githubusercontent.com/90663569/197921547-3d0f75f0-2dc2-458a-8702-5b271b89cef3.png)

## Penjelasan

- ### Fungsi-fungsi

| Nama Fungsi      | Penjelasan                                                                                                                                                                                                                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| def f(x)         | berfungsi untuk mengembalikan nilai persamaan dari variabel yang dipassing                                                                                                                                                                                                                              |
| def cek()        | berfungsi untuk mengecek nilai minimum antara `f(x1), f(x2), & f(x3)`. Lalu mengembalikan `x(n)` sesuai `f(x(n))` yang terkecil                                                                                                                                                                         |
| def grafik()     | berfungsi untuk menampilkan grafik dari persamaan yang dimiliki, dan menampilkan urutan keberadaan `x3` dengan menggambar garis vertikal dengan urutan warna seperti pelangi yang disimpan pada list bernama `lst_clr`                                                                                  |
| def show_table() | berfungsi untuk menampilkan tabel data yang berisikan `x1, f(x1), x2, f(x2), x3, dan f(x3)`                                                                                                                                                                                                             |
| def show_root()  | berfungsi untuk menampilkan akar yang didapat (dengan jumlah angka dibelakang koma sesuai ketelitian yang diinputkan user) beserta `f(akar)` nya                                                                                                                                                        |
| def bolza()      | berfungsi untuk melakukan pencarian akar menggunakan metode bolzano. Fungsi ini akan terus melakukan rekursi selama `abs(f(x3))` lebih besar dari 10^(-ketelitian). Jika ketelitian yang diminta hingga 7, maka fungsi bolzano akan terus melakukan rekursi selama `abs(f(x))` lebih besar dari 10^(-7) |

- ### Alur Program

1. Pada fungsi main(), user akan diminta untuk melakukan inputan untuk batas bawah (baca: x1), batas atas (baca: x2), dan tingkat ketelitian yang diinginkan.
2. Lalu pada fungsi main(), akan melakukan `try-except` untuk fungsi bolzano yang kita miliki. Akan tetapi, jika rekursi berjalan terus menerus hingga mencapai `max depth recursion` atau mengalami `RecursionError`, maka program akan menampilkan pesan bahwa akar tidak ditemukan, dan langsung menampilkan tabel data beserta grafiknya.
3. Jika tidak mendapatkan `RecursionError`, maka program akan terus melakukan pencarian akar pada fungsi `bolza()`, selama `abs(f(x3))` lebih besar dari 10^(-ketelitian).
4. Jika rekursi telah berhenti, maka program akan menampilkan akar yang didapat lalu menampilkan tabel data dan terkahir akan menampilkan grafik yang dibuat.

- ### def bolza()

> Penjelasan tentang alur pencarian akar menggunakan algoritma dari metode bolzano

```py
! NOTE: fungsi bolza() akan terus melakukan rekursi selama abs(f(x3)) lebih besar dari 10^(-ketelitian).
```

Jika kondisi tersebut tepenuhi, maka program akan berlanjut sesuai beberapa kondisi dibawah ini :

1. Jika `fA * fX > 0` (baca: f(x1) \* f(x3) lebih besar dari 0), maka :

   - set nilai `x1` menjadi `x3`
   - set nilai `f(x1)` menjadi `f(x3)`
   - dan nilai `f(x2)` tetap menjadi `f(x2)`

2. Selain kondisi diatas, maka :

   - set nilai `x2` menjadi `x3`
   - set nilai `f(x2)` menjadi `f(x3)`
   - dan nilai `f(x1)` tetap menjadi `f(x1)`

Lalu set nilai `x3` menjadi (x1 + x2) / 2 dan set juga nilai `f(x3)`

Sekian, terimakasih!
