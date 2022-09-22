# Komputasi Numerik
Kuliah ini bertujuan untuk mempelajari metode untuk menemukan (perkiraan) akar polinomial

## 1. Metode Bolzano
Disebut pula sebagai metode `Setengah Interval` (Interval Halving), metode `Bagi Dua`, metode `Biseksi`, atau metode `Pemotongan Biner`.

> Langkah-langkah yang harus dilakukan pada metode Bolzano adalah :

1. Hitung fungsi pada interval yang sama dari x hingga terjadi perubahan tanda dari f(xn) dan f(x(n+1)). Atau dengan kata lain: `f(xn) x f(x(n+1)) < 0`

2. Estimasi pertama untuk akar persamaan dapat diperoleh melalui :  `xt = (xn + x(n+1)) / 2`

3. Lakukan evaluasi untuk menentukan dalam interval mana akar persamaan berada :

	a.  Jika `f(xn) * f(x(n+1)) < 0`

	    maka akar persamaan berada dalam sub-interval pertama, tetapkan x(n+1) = xt, dan lanjutkan ke langkah 4

	b.  Jika `f(xn) * f(x(n+1)) > 0`

        maka akar persamaan berada dalam sub-interval kedua, tetapkan xn = xt, dan lanjutkan ke langkah 4

	c.  Jika `f(xn) * f(x(n+1)) = 0`

		maka akar persamaan adalah xt, dan perhitungan selesai

4. Kembali ke langkah 2 untuk menghitung nilai perkiraan akar yang baru

5. Jika nilai yang didapat pada no. 4 sudah sesuai denga  batasan yang ditentukan, maka proses selesai, dan `xt` adalah akar yang dicari.