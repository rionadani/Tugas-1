# README Tugas 6

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
- Asynchronous programming: Proses running program dapat dilakukan secara bersamaan tanpa harus menunggu antrian. Selain itu, asynchronous programming menggunakan metode full page refresh.
- Synchronous programming: Proses running program secara sequential, artinya diproses berdasarkan antrian eksekusi program. Selain itu, user tidak perlu melakukan refresh lagi karena halaman website akan diupdate secara langsung.

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven adalah suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event yang merupakan keluaran atau tindakan pengguna, atau bisa berupa pesan dari program lainnya. Contohnya adalah pada saat menekan tombol Tambah Task akan muncul sebuah modal.

### Jelaskan penerapan asynchronous programming pada AJAX.
Script akan mengirimkan request ke server dan akan melanjutkan eksekusi tanpa menunggu responds. Apabila responds telah diterima, scrip akan mengeksekusi action yang berkaitan tanpa diperlukan refresh oleh user.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat fungsi show_json, show_todolist_ajax, dan add_task_ajax pada views.py 
2. Menambahkan path `json/, ajax/, add/` pada urls.py
3. Membuat file todolist-ajax.html
4. Membuat script pada todolist-ajax.html
5. Membuat modal pada todolist-ajax.html