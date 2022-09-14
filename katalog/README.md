# Tugas 2 PBP
Tugas ini diselesaikan oleh Andi Muhamad Dzaky Raihan, NPM 2106631412, kode Asdos FRA.

Berikut link ke aplikasi [**katalog**][Link Katalog] yang dibuat

### 1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`;

Berikut bagan yang saya buat
![Bagan Tugas 2 PBP][Gambar Bagan]
Pertama-tama, _user_ mengirimkan permintaan `url` untuk _resource_ ke Django. Kemudian, _Framework_ Django mencari `url` yang sesuai dengan permintaannya. Jika `url` berhasil bersambung dengan `views`, maka `views` yang bersangkutan itu akan dipanggil dan memproses permintaan yang bersangkutan. Jika proses ini membutuhkan keterlibatan _database_, maka `views` akan memanggilakan _query_ ke `models` dan _database_ akan mengembalikan hasil dari _query_ tersebut ke `views`. Setelah itu, `views` akan me-_render_ berkas `html` yang sebelumnya sudah didefinisikan sesuai dengan data yang didapat pada proses sebelumnya. Akhirnya, berkas `html` ini akan dikembalikan ke _user_ sebagai sebuah repons.

### 2. Jelaskan kenapa menggunakan _virtual environment_? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_?
Kita menggunakan _virtual environment_ untuk memisahkan pengaturan dan _package_ yang diinstal pada setiap proyek Django sehingga perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Dengan menggunakan _virtual environment_ ini, kita dapat memiliki berbagai _project_ dengan berbagai pengaturan dan _package_. Berikut contohnya:

1. Project A menggunakan Django 1.7
2. Project B menggunakan Django 3.2
3. Project C menggunakan Django 4.1.1
4. Project D menggunakan Django 3.2

Walaupun _best practice_-nya adalah menggunakan _virtual environment_ untuk setiap aplikasi web berbasis Django, kita **tetap bisa** membuatnya walau tanpa menggunakan _virtual environment_

### 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

1. **Membuat sebuah fungsi pada `views.py` yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.**

    Untuk yang pertama ini, saya meng-_import_ class CatalogItem dari berkas `models.py` yang ada di _folder_ aplikasi katalog. Berikut importnya
    ```
    from katalog.models import CatalogItem
    ```

    Kemudian dalam berkas `views.py` ini saya membuat fungsi yang menerima parameter _request_ dan di dalamnya mengambil seluruh _instance_ dari _class_ CatalogItem ini (dengan kata lain memanggil fungsi _query_ ke model _database_) dan dimasukkan ke dalam sebuah variabel context. Berikut potongan kodenya 
    ```    
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'nama': 'Andi Muhamad Dzaky Raihan',
        'npm' : '2106631412',
    } 
    ```
    Terakhir, fungsi yang ada di dalam `views.py` ini akan mengembalikan fungsi `render(request, "katalog.html", context)`. Dengan demikian akan dikembalikan halaman html sesuai dengan apa yang ada di dalam `katalog.html` dan datanya dari variable **context**

2. **Membuat sebuah _routing_ untuk memetakan fungsi yang telah kamu buat pada `views.py`.**

    Pertama-tama, saya memastikan ada path url yang bisa mengakses aplikasi katalog ini, untuk melakukan itu saya menambahkan
    ```
    ...
    path('katalog/', include('katalog.urls')),
    ...
    ```
    di `urls.py` milik **project_django**. Dengan demikian, jika kita memasukkan `alamat-aplikasi.sesuatu/katalog/` maka akan melihat file `urls.py` yang ada di aplikasi **katalog**. Setelah itu, di dalam `urls.py` yang ada di folder **katalog**, saya men-_import_ fungsi yang sudah dibuat di views sebelumnya sehingga akan dipanggil ketika url ini diakses. Berikut potongan kodenya
    ```
    from django.urls import path
    from katalog.views import show_katalog
    app_name = "katalog"

    urlpatterns = [
        path('', show_katalog, name='show_katalog'),
    ]
    ```
    Dengan demikian, fungsi **show_katalog** dari `views.py` akan mengembalikan respons yang diharapkan.

3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.

    Pertama-tama, saya mengubah **_fill me_** yang ada di dalam berkas `katalog.html` menjadi berikut 
    ```
    <h5>Name: </h5>
    <p>{{nama}}</p>

    <h5>Student ID: </h5>
    <p>{{npm}}</p>
    ```
    dengan demikian nama dan npm saya ditampilkan (menggunakan syntax django yakni {{data}}, variabel nama dan npm sudah dideklarasikan di context yang ada di `views.py`).

    Setelah itu, saya memasukkan data-data dari tabel yang ada di models dengan memanfaatkan syntax for loop, berikut kodenya untuk menuliskan _field_ setiap _instance_ dari data yang didapat
    ```
        {% for barang in list_barang %}
        <tr>
            <td>{{barang.item_name}}</td>
            <td>{{barang.item_price}}</td>
            <td>{{barang.item_stock}}</td>
            <td>{{barang.rating}}</td>
            <td>{{barang.description}}</td>
            <td>{{barang.item_url}}</td>
        </tr>
    {% endfor %}
    ```
    Dengan demikian, setiap _field_ yang diinginkan ditulis dari objek-objek yang ada di **list_barang** atau hasil dari _query_ bisa dituliskan (**list_barang** berisi query yang didapat dari `models.py` dan sudah disimpan di dalam context saat di `views.py`).

    Setelah melakukan semua itu, seharusnya data yang didapatkan berhasil dipetakan ke berkas `html`

4. **Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**

    1. Pertama-tama, meng-_upload_ berkas-berkas proyek django saya ke repo di github dengan melakukan add, commit, dan push.
    2. Kemudian, saya membuat aplikasi baru di herokuapp bernama **lab-1-pbp-saya**
    3. Setelah itu, saya menambahkan 2 buah variabel **_Repository Secret_** yakni:

        * HEROKU_API_KEY yang memiliki _value api key_ akun heroku saya
        * HEROKU_APP_NAME yang memiliki _value_ nama aplikasi yang baru saja saya buat tadi
    4. Terakhir, saya men-_deploy_ ulang repo saya yang ada di github

Setelah deploy berhasil, teman-teman saya bisa melihat aplikasi yang saya buat di `https://<nama-aplikasi-heroku>.herokuapp.com`. Untuk tugas ini, aplikasi saya dapat dilihat di [sini][Link Katalog].


[Gambar Bagan]: https://user-images.githubusercontent.com/101728915/190099725-a3d620a5-c7dc-4d98-887a-38e7f7c026ff.png
[Link Katalog]: https://lab-1-pbp-saya.herokuapp.com/katalog