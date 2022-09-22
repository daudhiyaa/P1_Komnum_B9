# numerical-computing
this lecture is learn the methods to find the (approximation) roots of a polynomial

## 1. Bolzano Method
also called as the `Half Interval method`, the `Divide method`, the `Bisection method`, or the `Binary Cutting method`.

<!-- <blockquote> -->
> Langkah-langkah yang harus dilakukan pada metode Bolzano adalah :

1. Hitung fungsi pada interval yang sama dari x hingga terjadi perubahan tanda dari f(xn) dan f(xn+1). Atau dengan kata lain: f(xn) x f(xn+1) < 0;

2. Estimasi pertama untuk akar persamaan dapat diperoleh melalui :  xt = (xn + xn+1) / 2;

3. Lakukan evaluasi untuk menentukan dalam interval mana akar persamaan berada :

	a.  Jika f(xn) * f(xn+1) < 0
		akar persamaan dalam sub-interval pertama, tetapkan xn+1 = xt, dan 
		lanjutkan ke langkah 4;

	b.  Jika f(xn) * f(xn+1) > 0
		akar persamaan dalam sub-interval kedua, tetapkan xn = xt, dan 
		lanjutkan ke langkah 4;

	c.  Jika f(xn) * f(xn+1) = 0
		akar persamaan adalah xt, dan hitungan selesai;

4. Kembali ke langkah 2 untuk menghitung nilai perkiraan akar yang baru;

5. Jika nilai yang didapat pada no. 4 sudah sesuai denga  batasan yang ditentukan, maka proses selesai, dan xt adalah akar yang dicari.
<!-- </blockquote> -->