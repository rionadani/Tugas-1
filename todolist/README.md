# README Tugas 3

### Link Heroku
https://tugas-1-riona.herokuapp.com/todolist
   
### Apa kegunaan `{% csrf_token %}`  pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
`{% csrf_token %}` berfungsi untuk melindungi dari salah satu serangan keamanan web. `{% csrf_token %}` akan membuat sebuah token yang berfungsi untuk mem-filter request yang masuk. Apabila `{% csrf_token %}` tidak diimplementasikan penyerang dapat mengirim suatu request secara illegal.
 
### Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Kita bisa membuat elemen `<form>` secara manual. Hal ini dapat dilakukan dengan membuat input field dari masing-masing data yang ingin disimpan pada file html. Lalu pada file views.py melakukan get untuk masing-masing data field.

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Pertama, sistem melakukan request ke views.py untuk melakukan penyimpanan data. Lalu, akan dibuat form. Setelah itu, akan dijalankan method is_valid() apabila true maka form tersebut akan disave. Lalu akan melakukan redirect. 

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Menjalankan perintah python manage.py startapp wishlist
2. Menambahkan mywatchlist ke dalam variabel installed_apps dalam file settings.py pada folder project_django dan menambahkan 
3. Membuat class Task yang berisi user, date, title, description di models.py
4. Membuat fungsi register, login_user, logout_user di views.py
5. Membuat file register.html dan login.html
6. Membuat file todolist.html dan menambahkan fungsi show_todolist di views.py
7. Membuat file add-task.html dan menambahkan fungsi add_task di views.py
8. Menambahkan 
    ```shell
    path('', show_todolist, name='show_todolist'),
    path('create-task/', add_task, name='add_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
   ``` 
   ke dalam file urls.py pada folder todolist
9. Menjalakan perintah python manage.py makemigrations dan python manage.py migrate
10. Melakukan push dan commit ke Github dan deploy ke Heroku
11. Membuat akun dummy

