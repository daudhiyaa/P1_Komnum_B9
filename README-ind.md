# Komputasi Numerik

## Metode untuk menemukan (perkiraan) akar persamaan polinomial
### Metode Bolzano
Disebut pula sebagai: 
- metode `Setengah Interval` (Interval Halving)
- metode `Bagi Dua`
- metode `Biseksi`
- atau metode `Pemotongan Biner`.

> Langkah-langkah yang harus dilakukan pada metode Bolzano adalah :

1. Hitung fungsi pada interval yang sama dari x hingga terjadi perubahan tanda dari `f(x1)` dan `f(x2)`. Atau dengan kata lain: `f(x1) * f(x2) < 0`
2. Estimasi pertama untuk akar persamaan dapat diperoleh melalui :  `x3 = (x1 + x2) / 2`

3. Lakukan evaluasi untuk menentukan dalam interval mana akar persamaan berada :

	*  Jika `f(x1) * f(x3) < 0`

	    maka akar persamaan berada dalam sub-interval pertama, tetapkan x1 = x3, dan lanjutkan ke langkah 4

	*  Jika `f(x2) * f(x3) < 0`

        maka akar persamaan berada dalam sub-interval kedua, tetapkan x2 = x3, dan lanjutkan ke langkah 4

	*  Jika `f(xn) = 0`

		maka akar persamaan adalah `xn`, dan perhitungan selesai

4. Kembali ke langkah 2 untuk menghitung nilai perkiraan akar yang baru

5. Jika tidak ada batasan yang ditentukan, dan nilai yang diperoleh pada langkah 4 mendekati 0, maka cari `min(abs(f(xn)))` dan proses selesai, dan `xn` adalah akar yang akan dicari.

6. Jika nilai yang didapat pada no. 4 sudah sesuai denga  batasan yang ditentukan, maka proses selesai, dan `x3` adalah akar yang dicari.