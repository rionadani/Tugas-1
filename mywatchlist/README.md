# README Tugas 3

### Link Heroku
https://tugas-1-riona.herokuapp.com/mywatchlist/html
<p>https://tugas-1-riona.herokuapp.com/mywatchlist/xml
<p>https://tugas-1-riona.herokuapp.com/mywatchlist/json

### Screenshot postman
![mywatchlist:html](https://user-images.githubusercontent.com/95161209/191501702-139646d5-d134-4f60-bb1d-4d9ffaab93cf.png)
![mywatchlist:json](https://user-images.githubusercontent.com/95161209/191501718-f3606d3f-395a-499b-b3de-507e99e97058.png)
![mywatchlist:xml](https://user-images.githubusercontent.com/95161209/191501732-73ef5d8b-590f-4d75-9e6a-9d0cdd8ec8d8.png)

### Jelaskan perbedaan antara JSON, XML, dan HTML!
XML: self-descriptive, digunakan menyimpan dan mengirimkan data. Untuk mengirim, menerima, menyimpan, atau menampilkan informasi tersebut, diperlkukan sebuah program.
JSON: self-describing, digunakan untuk menyimpan dan mengirimkan data. Memiliki format text sehingga untuk membaca dan membuat JSON banyak terdapat dibanyak bahasa pemrograman.
HTML: bahasa standar pemrograman yang digunakan untuk membuat halaman website, yang diakses melalui internet. 

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena dalam mengimplementasikan sebuah platform kita membutuhkan untuk melakukan pengiriman data dari satu stack ke stack lainnya.

###  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Membuat suatu aplikasi baru bernama mywatchlist:
1) Menjalankan perintah python manage.py startapp wishlist 
2) Menambahkan mywatchlist ke dalam variabel installed_apps dalam file settings.py pada folder project_django 
3) Membuat kelas MyWatchList dengan parameter models.Model dan menambahkan variabel watched, title, rating, release_date, dan review
4) Membuat file initial_mywatchlist_data.json dalam folder fixtures pada folder mywatchlist dan menambahkan data-data seperti watched, 
5) Membuat file mywatchlist.html dalam folder templates pada folder mywatchlist
6) Membuat fungsi show_wishlist, show_xml, dan show_json dalam file views.py pada folder mywatchlisst
7) Menambahkan path('html/', show_watchlist, name='show_watchlist'), path('xml/', show_xml, name='show_xml'), path('json/', show_json, name='show_json') ke variabel urlpatterns dalam file urls.py pada folder mywatchlist
8) Menambahkan path('mywatchlist/', include('mywatchlist.urls')) ke dalam variabel urlpatterns dalam file urls.py pada folder project_django
9) Menambahkan sh -c 'python manage.py migrate && python manage.py loaddata initial_mywatchlist_data.json dalam file procfile