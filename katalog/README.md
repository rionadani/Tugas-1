# README Tugas 2

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
<img width="621" alt="Bagan Tugas 1" src="https://user-images.githubusercontent.com/95161209/190307694-9914444b-eb53-480a-94f8-4921f25e93c6.png">


### Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment membantu setiap proyek untuk  memisahkan pengaturan dan package yang diinstal. Oleh karena itu, apabila terdapat perubahan pada satu proyek, proyek lainnya tidak akan terpengaruh oleh perubahan tersebut. Kita tetap dapat bisa membuat aplikasi berbasis Django tanpa menggunakan virtual environment, akan tetapi lebih baik setiap proyek memiliki virtual enviromentnya masing-masing.


### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Poin 1:
    Membuat fungsi dengan parameter request dengan return render(request, "katalog.html", context). Isi fungsinya adalah variabel data_barang_katalog yang berfungsi untuk menyimpan hasil query yang didapatkan dari pemanggilan fungsi query ke model database
<p>Poin 2:
    Menggunakan files urls.py yang berada di folder katalog lalu membuat variabel app_name dan menambahkan path url ke urlpatterns
<p>Poin 3:
   Membuka file HTML pada folder templates yang ada di dalam direktori katalog. Mengubah Fill me! yang ada di dalam HTML menjadi {{nama}} dan {{npm}} serta melakukan iterasi terhadap variabel list_barang
<p>Poin 4:
    Membuat aplikasi pada heroku, lalu meng-copy API key dari akun. Menambahkan repository secret untuk API key dan Nama aplikasi pada heroku, dan melakukan re-run.

### Link Heroku
https://tugas-1-riona.herokuapp.com/katalog/
