# Tugas 3 PBP
Tugas ini diselesaikan oleh Andi Muhamad Dzaky Raihan, NPM 2106631412, kode Asdos FRA.

Berikut link ke aplikasi yang dibuat:
* [Versi HTML][mywatchlist html]
* [Versi JSON][mywatchlist JSON]
* [Versi XML][mywatchlist XML]

### 1. Jelaskan perbedaan antara JSON, XML, dan HTML!
    
*  **JSON**: JSON (JavaScript Object Notation) adalah format _data-interchange_ ringan untuk menyimpan dan memindahkan data. JSON berbasis bahasa pemrograman JavaScript dan mudah untuk dimengerti. JSON sering digunakan ketika data dikirimkan dari server menuju _web page_. Selain itu, data dari JSON mudah untuk diakses, JSON bisa digunakan di berbagai _browser_, lebih mudah dibaca dibandingkan XML, lebih kurang aman dibandingkan XML, dan hanya bisa menggunakan _encoding_ UTF-8

* **XML**: XML (Extensible Markup Language) didesain untuk membawa data dan bukan untuk menampilkannya. XML adalah _markup language_ yang mendefinisikan sejumlah aturan untuk _encoding_ sebuah dokumen dalam format yang bisa dibaca manusia dan mesin. Selain itu, data dari XML perlu di-_parse_ terlebih dahulu, _Parsing_ XML lintas _browser_ cukup sulit, lebih sulit dibaca dibandingkan JSON, lebih aman dibandingkan JSON, dan bisa menggunakan berbagai jenis _encoding_

* **HTML**: HTML (Hyper Text Markup Language) adalah _markup language_ yang digunakan untuk membuat _web page_ dan _web app_. HTML menggunakan struktur kode _tag_ dan atribut untuk membuat sebuah elemen yang nantinya akan mendeskripsikan struktur sebuah halaman web. Pada dasarnya, HTML digunakan untuk menampilkan halaman web, bukan untuk membawa data.

### 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery penting dalam pengimplementasian sebuah platform karena pada dasarnya _user/client_ akan terus menerus bertukaran data dalam penggunaan sebuah _platform_. Salah satu proses yang wajib ada jika berhubungan dengan data adalah CRUD (Create, Read, Update, Delete) Process. Berikut adalah beberapa contoh interaksi HTTPS:

1. Browser meminta HTML page. Server mengembalikan HTML file.
2. Browser meminta style sheet. Server mengembalikan CSS file.
3. Browser meminta JPG image. Server mengembalikan JPG file.
4. Browser meminta JavaScript code. Server mengembalikan JS file.
5. Browser meminta data. Server mengembalikan data (dalam XML atau JSON).

Untuk melakukan ini, diperlukan format penyampaian data seperti XML, JSON, dan HTML. 

### 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 3 di atas.
1. **Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu**
    * Pertama-tama, saya membuat applikasi baru di proyek Django Tugas 2 pekan lalu di terminal dengan menuliskan `py manage.py startapp mywatchlist`.
    * Setelah itu, saya menambahkan **_mywatchlist_** ke **INSTALLED_APPS** di `settings.py` project_django 

2. **Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist**
    * Pertama-tama, saya routing dari urls yang ada di **project_django** dengan menambahkan `path('mywatchlist/', include('mywatchlist.urls'))`. 
    * Setelah itu, menambahkan `urls.py` di dalam app **mywatchlist** dan melakukan routing lagi di dalamnya. Dalam `urls.py` ini, saya menuliskan 
    ``` 
    from django.urls import path
    from mywatchlist.views import *

    app_name = 'wishlist'

    urlpatterns = [
        ...
        path('', show_html, name='show_html'),
        ...
    ]
    ``` 
    dimana `show_html` adalah fungsi di `views.py` yang ingin dipanggil untuk ditampilkan di halaman http://localhost:8000/mywatchlist

2. **Membuat sebuah model MyWatchList yang memiliki atribut yang dideskripsikan**
    * Pertama-tama, di dalam saya membuat class `WatchListMovies` yang  merepresentasikan sebuah data model watchlist model. Atribut yang ada di dalam class ini adalah sebagai berikut:
        1. watched untuk mendeskripsikan film tersebut sudah ditonton atau belum. Untuk ini. Untuk ini, saya menggunakan field boolean karena di sini hanya bisa 2 pilihan, yakni sudah (true) atau belum (false) menonton. Berikut kodenya `watched = models.BooleanField()`
        2. title untuk mendeskripsikan judul film. Untuk ini, saya menggunakan field char yang di-_limit_ sebanyak 255 karakter. Berikut kodenya `title = models.CharField(max_length=255)` 
        3. rating untuk mendeskripsikan rating film dalam rentang 1 sampai dengan 5. Untuk ini, saya menggunakan field integer yang dilimit nilainya 1-5 menggunakan validator. Berikut kodenya
        ```
        rating_validator = [MaxValueValidator(5), MinValueValidator(1)]
        rating = models.IntegerField(rating_validator)
        ```
        4. release_date untuk mendeskripsikan kapan film dirilis. Untuk ini, saya menggunakan field Date (di json formatnya yyyy-mm-dd). Berikut kodenya `release_date = models.DateField()`
        5. review untuk mendeskripsikan review untuk film tersebut. Untuk ini, saya menggunakan text field (mengingat review isinya bisa panjang). Berikut kodenya `review = models.TextField(default='-')`

### Berikut _screenshot_ pengaksesan 3 url di poin 6
![Foto JSON](https://user-images.githubusercontent.com/101728915/191546189-72f26e0d-6010-4239-8351-b1d1c1aa2c87.jpg)
![Foto XML](https://user-images.githubusercontent.com/101728915/191546201-8396e850-f286-4e8e-9860-75c43360570e.jpg)
![Foto HTML](https://user-images.githubusercontent.com/101728915/191546210-088a3187-99cc-42bc-a831-b8becc02611b.jpg)

[mywatchlist html]: https://lab-1-pbp-saya.herokuapp.com/mywatchlist/html
[mywatchlist JSON]: https://lab-1-pbp-saya.herokuapp.com/mywatchlist/json
[mywatchlist XML]: https://lab-1-pbp-saya.herokuapp.com/mywatchlist/xml