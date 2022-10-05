## Untuk melihat tugas 5, pencet [Link ini](#tugas-5-pbp)
# Tugas 4 PBP
Tugas ini diselesaikan oleh Andi Muhamad Dzaky Raihan, NPM 2106631412, kode Asdos FRA.

Berikut link ke aplikasi yang dibuat:
* [Link to-do list][to-do list heroku]

### 1. Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Pada elemen `<form>`, `{% csrf_token %}` digunakan untuk menghindari serangan-serangan jahat khususnya **_Cross-Site Request Forgery (CSRF) attack_**. `{% csrf_token %}` membuat sebuah _token_ di bagian _server_ ketika merender sebuah halaman dan memastikan untuk _cross-check_ token ini untuk _request_ yang datang kembali. Jika _request_ yang datang kembali tidak mengandung token, _request_-nya tidak dieksekusi. Apabila tidak ada elemen `{% csrf_token %}`, akan muncul error `Forbidden (403) CSRF verification failed. Request aborted.` Ketika berusaha submit form tanpa elemen csrf_token ini karena csrf_token yang ada di form pasti berbeda dengan crsf_token yang ada di server.
    

### 2. Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Ya, kita bisa membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`). Alternatifnya adalah menggunakan tag `<form>` di html. Berikut adalah tag `<form>` pada umumnya:
```html
<form action=[URL DESTINATION] method=[METHOD]>
    <input type=[INPUT TYPE] other attributes>
    ....
    ....
    <input type=[INPUT TYPE] other attributes>
</form>
```
* URL DESTINATION : Posting data to URL endpoint
* METHOD : Method on passing variables to URL DESTINATION (GET or POST)
* INPUT & INPUT TYPE: Data attributes from Browser to Server

Pada umumnya, html memiliki setidaknya satu tag input dengan tipe apa saja untuk memasukan data dan satu inpu dengan tipe submit untuk mengirimkan atau submit form dari pengguna. Setelah submit, akan dikirimkan http request dengan method yang sudah dituliskan ke alamat url yang sudah dituliskan berisikan data-data dari input form.


### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Pada umumnya, pertama-tama user akan mengisi field-field yang tertera pada html form dan melakukan submit. Setelah submit, akan dikirimkan HTTP Request dan form ini beserta isi-isi dari fieldnya dari html ke `views.py` (dalam konteks django). Setelah itu, berdasarkan jenis http requestnya, data akan diolah di `views.py` dan kemudian akan disimpan ke _database_ (Jika memang ingin disimpan). Setelah disimpan di _database_, data dari submisi form ini akan dapat dimunculkan kapanpun ketika template html yang ingin dirender &ditampilkan memanggil data yang baru disimpan di _database_ ini.


**Berikut contoh dalam tugas ini:**

Pertama-tama, _user_ input data di _form_ yang tertera di `./todolist/create-task`. Setelah _field title_ dan _description_ sudah diisi di _form_ dan _user_ memencet tombol `tambah`, _request_ berupa **_POST_** akan dikirimkan beserta dengan isi formnya. Jika _form_-nya valid, maka akan diambil isi dari _field title_ dan _description_. Setelah itu, akan dibuat data baru untuk dimasukkan ke database dengan input field usernya adalah user yang membuat, description & title berdasarkan input di form, dan tanggal berupa tanggal ketika dia buat. Berikut potongan kodenya
```py
if request.method == 'POST' and form.is_valid():
    title = form.cleaned_data['title']
    description = form.cleaned_data['description']
    task_baru = ToDoList.objects.create(title=title, description=description,
                                        user=request.user, date=datetime.date.today())
```
Setelah ditambahkan, data akan ditampilkan di `./todolist` dalam bentuk tabel. Task yang ditampilkan hanyalah task yang dimiliki user yang log in. Berikut implementasinya
1. Pada `views.py`
```py
todolist = ToDoList.objects.filter(user=request.user)
context = {
    'list_kerjaan': todolist,
    'user_name': request.user.username,
    'last_login': request.COOKIES.get('last_login', 'not found'),
}
return render(request, 'todolist.html', context)
```
2. Pada `todolist.html`
```html
<table border="1" style="text-align: center; padding: 15px 15px;">
    <tr>
    <th style="padding: 15px;">Tanggal Pembuatan</th>
    <th style="padding: 15px;">Judul Task</th>
    <th style="padding: 15px;">Deskripsi Task</th>
    <th style="padding: 15px;">Penyelesaian Task</th>
    <th style="padding: 15px;">Toggle penyelesaian Task</th>
    <th style="padding: 15px;">Delete Task</th>
    </tr>
{% comment %} Tambahkan data di bawah baris ini {% endcomment %}
{% for task in list_kerjaan %}
    <tr>
        <td style="text-align: center; padding: 15px;">{{task.date}}</td>
        <td style="text-align: center; padding: 15px;">{{task.title}}</td>
        <td style="text-align: center; padding: 15px;">{{task.description}}</td>
        <td style="text-align: center; padding: 15px;">{{task.is_finished}}</td>
        <td style="text-align: center; padding: 15px;"><button><a href="toggle/{{ task.id }}">Toggle</a></button></td>
        <td style="text-align: center; padding: 15px;"><button><a href="delete/{{ task.id }}">Hapus</a></button></td>
    </tr>
{% endfor %}
```
### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. **Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.**
    * Pertama-tama, saya membuat applikasi baru di proyek Django Tugas 3 pekan lalu di terminal dengan menuliskan `py manage.py startapp todolist`.
    * Setelah itu, saya menambahkan **todolist** ke **INSTALLED_APPS** di `settings.py` project_django 

2. **Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.**
    * Pertama-tama, saya routing dari urls yang ada di **project_django** dengan menambahkan `path('todolist/', include('todolist.urls'))`. 
    * Setelah itu, menambahkan `urls.py` di dalam app **todolist** dan melakukan routing lagi di dalamnya. Dalam `urls.py` ini, saya menuliskan 
    ``` py
    from django.urls import path
    from mywatchlist.views import *

    app_name = 'todolist'

    urlpatterns = [
        ...
        path('', show_todolist, name='show_todolist'),
        ...
    ]
    ``` 
    dimana `show_todolist` adalah fungsi di `views.py` yang ingin dipanggil untuk ditampilkan di halaman http://localhost:8000/todolist

3. **Membuat sebuah model Task yang memiliki atribut sebagai berikut:**
    * Pertama-tama, di dalam saya membuat class `ToDoList` yang  merepresentasikan sebuah data model to-do list. Atribut yang ada di dalam class ini adalah sebagai berikut:
        1. `user` untuk menghubungkan _task_ dengan pengguna yang membuat _task_ tersebut. Untuk ini, saya menggunakan tipe model `models.ForeignKey` dengan parameter `User` (`User` diimport dari `django.contrib.auth.models`). Berikut potongan kodenya `user = models.ForeignKey(User, on_delete=models.CASCADE)`
        2. date untuk mendeskripsikan tanggal pembuatan task. Untuk ini, saya menggunakan field date. Berikut kodenya: `date = models.DateField()`
        3. title untuk mendeskripsikan judul task. Untuk ini, saya menggunakan field char yang di-_limit_ sebanyak 255 karakter. Berikut kodenya `title = models.CharField(max_length=255)`
        4. description untuk mendeskripsikan deskripsi task. Untuk ini, saya menggunakan text field (mengingat deskripsi isinya bisa panjang). Berikut kodenya `description = models.TextField()`

4. **Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.**
    * **Registasi:**
    Untuk registrasi, berikut implementasinya:
        * `views.py`
            1. Pertama-tama, saya meng-import forms untuk membuat user, fungsi untuk memberikan message, dan fungsi untuk melakukan redirect sebagai berikut:
            ```py
            from django.shortcuts import redirect
            from django.contrib.auth.forms import UserCreationForm
            from django.contrib import messages
            ```
            2. Kemudian, masukkan potongan kode di bawah ini ke dalam `views.py` yang sudah ada. Potongan kode ini berfungsi untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.

            ```py
            def register(request):
                # Ambil form pembuatan user
                form = UserCreationForm()
                
                # Handle jika request merupakan POST
                if request.method == "POST":
                    
                    # Jika form yang diberikan valid, maka simpan user yang disubmit kemudian
                    # Redirect ke page login
                    form = UserCreationForm(request.POST)
                    if form.is_valid():
                        form.save()
                        messages.success(request, 'Akun telah berhasil dibuat!')
                        return redirect('todolist:login')

                # Kembalikan render halaman register
                context = {'form': form}
                return render(request, 'register.html', context)
            ```
            3. Buatlah berkas HTML baru dengan nama `register.html` pada folder `todolist/templates`. Isi dari register.html adalah sebagai berikut.
    
            ```html
            {% extends 'base.html' %}

            {% block meta %}
            <title>Registrasi Akun</title>
            {% endblock meta %}

            {% block content %}  

            <div class = "login">
                
                <h1>Formulir Registrasi</h1>  

                    <form method="POST" >  
                        {% csrf_token %}  
                        <table>  
                            {{ form.as_table }}  
                            <tr>  
                                <td></td>
                                <td><input type="submit" name="submit" value="Daftar"/></td>  
                            </tr>  
                        </table>  
                    </form>

                {% if messages %}  
                    <ul>   
                        {% for message in messages %}  
                            <li>{{ message }}</li>  
                            {% endfor %}  
                    </ul>   
                {% endif %}

            </div>  

            {% endblock content %}
            ```
            
            4. Routing di `urls.py` sehingga ketika kita memasukkan link `./todolist/register` akan memanggil fungsi registrasi dan menampilkan halaman registrasi. Berikut routing yang dimasukkan di dalam `urls.py`
    
            ```py
            urlpatterns = [
                ...
                path('register/', register, name='register'),
                ...
            ]
            ```
        * **Login:**
        Untuk login, berikut implementasinya:
            1. pertama-tama, import `authenticate` untuk memproses _username_ dan _password_ untuk login serta import `login` untuk melakukan proses _login_ di views.py. Berikut importnya: `from django.contrib.auth import authenticate, login`

            2. Buat fungsi `login_user` Untung meng-handle fitur user login. Kodenya adalah sebagai berikut:

            ```py
            def login_user(request):
                # Handle jika request merupakan POST
                if request.method == 'POST':
                    # Autentikasi user berdasarkan username dan password yang dimasukkan
                    username = request.POST.get('username')
                    password = request.POST.get('password')
                    user = authenticate(request, username=username, password=password)
                    
                    # Handle jika user ditemukan
                    if user is not None:
                        login(request, user)  # melakukan login terlebih dahulu
                        response = HttpResponseRedirect(
                            reverse("todolist:show_todolist"))  # membuat response
                        # membuat cookie last_login dan menambahkannya ke dalam response
                        response.set_cookie('last_login', str(datetime.datetime.now()))
                        return response
                    
                    # Jika tidak ditemukan, berikan info
                    else:
                        messages.info(request, 'Username atau Password salah!')
                
                # Render halaman login.html
                context = {}
                return render(request, 'login.html', context)
            ```

            3. Kemudian, buat berkas HTML baru dengan nama `login.html` pada folder `todolist/templates`. Isi dari `login.html` adalah sebagai berikut:

            ```html
            {% extends 'base.html' %}

            {% block meta %}
            <title>Login</title>
            {% endblock meta %}

            {% block content %}

            <div class = "login">

                <h1>Login</h1>

                <form method="POST" action="">
                    {% csrf_token %}
                    <table>
                        <tr>
                            <td>Username: </td>
                            <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                        </tr>
                                
                        <tr>
                            <td>Password: </td>
                            <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                        </tr>

                        <tr>
                            <td></td>
                            <td><input class="btn login_btn" type="submit" value="Login"></td>
                        </tr>
                    </table>
                </form>

                {% if messages %}
                    <ul>
                        {% for message in messages %}
                            <li>{{ message }}</li>
                        {% endfor %}
                    </ul>
                {% endif %}     
                    
                Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>

            </div>

            {% endblock content %}
            ```
            4. Routing di `urls.py` sehingga ketika kita memasukkan link `./todolist/login` akan memanggil fungsi login dan menampilkan halaman login. Berikut routing yang dimasukkan di dalam `urls.py`

            ```py
            urlpatterns = [
                ...
                path('login/', login_user, name='login'),
                ...
            ]
            ```
        * **Logout:**
        Untuk logout, berikut implementasinya:
            1. Pertama-tama, import fungsi `logout` ke dalam `views.py`. Berikut importnya: `from django.contrib.auth import logout`
            2. Buat fungsi untuk logout di dalam `views.py`. Berikut fungsinya:

            ```py
            def logout_user(request):
                logout(request)
                response = HttpResponseRedirect(reverse('todolist:login'))
                response.delete_cookie('last_login')
                return response
            ```
            3. Tambahkan potongan kode di bawah ini ke dalam `todolist.html` untuk menambahkan tombol logout
    
            ```html
            ...
            <button><a href="{% url 'wishlist:logout' %}">Logout</a></button>
            ...
            ```
             4. Routing di `urls.py` sehingga ketika kita memasukkan link `./todolist/logout` akan memanggil fungsi logout dan user akan di-logout dari akunnya. Berikut routing yang dimasukkan di dalam `urls.py`

            ```py
            urlpatterns = [
                ...
                path('logout/', logout_user, name='login'),
                ...
            ]
            ```

5. **Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.**
    1. Pertama-tama, saya membuat fungsi di dalam `views.py` yang nantinya akan me-render halaman utama ini. Dalam fungsi ini, saya menaruh context yang akan passing data task yang berkaitan dengan user, username dari user, dan data kapan terakhir login. Berikut potongan kode untuk merender-nya

    ```py
    ...
    todolist = ToDoList.objects.filter(user=request.user)
    ...
    context = {
        'list_kerjaan': todolist,
        'user_name': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'not found'),
    }
    return render(request, 'todolist.html', context)
    ...
    ```
    2. Kemudian, saya membuat todolist.html yang dapat menampilkan hal-hal yang diinginkan. Berikut potongan kode untuk setiap elemen yang ingin diperlihatkan:
        * Username Pengguna:

        ```html
        <h4>User Name: {{user_name}}</h4>
        ```
        * tombol Tambah Task Baru:
        
        ```html
        <button><a href="{% url 'todolist:add_todolist' %}">Tambah Task Baru</a></button>
        ```

        * tombol logout:

        ```html
        <button><a href="{% url 'todolist:logout' %}">Logout</a></button>
        ```

        * tabel berisi tanggal pembuatan task, judul task, dan deskripsi task (Kode di bawah termasuk penyelesaian bonus, yakni ditambahkan status, toggle status, dan hapus task):
        ```html
        <table border="1" style="text-align: center; padding: 15px 15px;">
            <tr>
            <th style="padding: 15px;">Tanggal Pembuatan</th>
            <th style="padding: 15px;">Judul Task</th>
            <th style="padding: 15px;">Deskripsi Task</th>
            <th style="padding: 15px;">Penyelesaian Task</th>
            <th style="padding: 15px;">Toggle penyelesaian Task</th>
            <th style="padding: 15px;">Delete Task</th>
            </tr>
        {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
        {% for task in list_kerjaan %}
            <tr>
                <td style="text-align: center; padding: 15px;">{{task.date}}</td>
                <td style="text-align: center; padding: 15px;">{{task.title}}</td>
                <td style="text-align: center; padding: 15px;">{{task.description}}</td>
                <td style="text-align: center; padding: 15px;">
                    {% if task.is_finished %}
                    Selesai
                    {% else %}
                    Belum Selesai
                    {% endif %}
                </td>
                <td style="text-align: center; padding: 15px;"><button><a href="toggle/{{ task.id }}">Toggle</a></button></td>
                <td style="text-align: center; padding: 15px;"><button><a href="delete/{{ task.id }}">Hapus</a></button></td>
            </tr>
        {% endfor %}
        </table>
        ```
6. **Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.**
    1. Pertama-tama, saya membuat `forms.py` yang berisi forms yang nanti akan saya gunakan untuk mengambil data untuk membuat task. Di dalam `forms.py` ini saya mengimport forms dan membuat class yang merepresentasikan sebuah form, dengan field title dan description. Berikut class-nya:

    ```py
    class ToDoListForms(forms.Form):
        title = forms.CharField(max_length=255)
        description = forms.CharField(widget=forms.TextInput)
    ```

    2. Kemudian, saya membuat fungsi di `views.py` untuk handle penambahan task. Pastikan di fungsi ini kita bisa render halaman untuk add task dan passing form tambah task sebagai context. 

    3. Setelah itu, buat sebuah template html yang bisa menampilkan form yang diinginkan. Potongan kode yang saya gunakan untuk menampilkan form adalah sbg berikut:
    ```html
    <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Tambah"/></td>  
                </tr>  
            </table>  
        </form>
    ```

    4. Terakhir, pada fungsi di `views.py` yang digunakan untuk handle penambahan task tadi, tambahkanlah kode untuk mengambil isi dari form lalu buat task baru berdasarkan isi formnya, dan redirect ke halaman utama todolist. Berikut potongan kode yang saya gunakan:
    ```py
    # Ambil form-nya dari http request
    form = ToDoListForms(request.POST)

    # Handle jika form valid dan method request adl. POST
    if request.method == 'POST' and form.is_valid():
        # Ambil title & description dari form, buat task baru, lalu redirect
        # ke halaman utama
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        task_baru = ToDoList.objects.create(title=title, description=description,
                                            user=request.user, date=datetime.date.today())
        return redirect('todolist:show_todolist')
    ```

7. **Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut:**
    
    Pertama-tama, saya mengimpor seluruh fungsi yang ada di `views.py` ke `urls.py`. Setelah itu, saya menambahkan potongan kode berikut ke dalam `urls.py` untuk melakukan routing sehingga beberapa fungsi yang dimaksud bisa diakses melalui url yang diinginkan. Berikut potongannya:
    ```py
    urlpatterns = [
        ...
        # http://localhost:8000/todolist/ berisi halaman utama yang memuat tabel task.
        path('', show_todolist, name='show_todolist'),
        # http://localhost:8000/todolist/register berisi form registrasi akun.
        path('register/', register, name='register'),
        # http://localhost:8000/todolist/login berisi form login.
        path('login/', login_user, name='login'),
        # http://localhost:8000/todolist/logout berisi mekanisme logout.
        path('logout/', logout_user, name='logout'),
        # http://localhost:8000/todolist/create-task berisi form pembuatan task.
        path('create-task/', add_todolist, name='add_todolist'),
        ...
    ]
    ```

8. **Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**

    Karena saya membuat ini ke dalam sebuah repo yang sebelumnya sudah dideploy di heroku, saya hanya tinggal melakukan add, commit, dan push aplikasi yang saya buat ke github (**Pastikan secret key untuk nama app dan api key di github benar**). Dengan demikian, aplikasi yang saya buat ini bisa diakses di `nama-app-heroku-minggu-lalu.herokuapp.com/todolist/`, yakni ada di https://lab-1-pbp-saya.herokuapp.com/todolist/

9. **Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.**

    Manfaatkan fitur registrasi akun di web untuk membuat 2 akun pengguna. Setelah itu, gunakan fitur `create-task` untuk membuat 3 dummy data di masing-masing akun

# Tugas 5 PBP
Tugas ini diselesaikan oleh Andi Muhamad Dzaky Raihan, NPM 2106631412, kode Asdos FRA.

Berikut link ke aplikasi yang dibuat:
* [Link to-do list][to-do list heroku]

### 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing _style_?
* Inline
    
    Inline CSS adalah styling/kode CSS yang digunakan langsung untuk suatu tag html secara spesifik. Atribut `<style>` digunakan untuk memberikan style ke suatu tag html. Berikut contohnya:
    ```html
    <h2 style="text-align: center">To-Do List</h2>
    ```
    * Kelebihan: Untuk perbaikan cepat, pemintaan HTTP yang kecil, dan untuk menguji dan melihat perbuahan
    * Kekurangan: Hanya mengatur 1 tag, jika ingin satu halaman maka perlu diterapkan untuk setiap tag 
* Internal

    Internal CSS adalah kode CSS internal yang ditaruh di dalam bagian `<head>` pada sebuah halaman. Class dan ID dapat digunakan untuk merujuk kode pada CSS, namun hanya akan aktif pada halaman tersebut.

    * Kelebihan: Class & Id bisa digunakan oleh internal stylesheet, Perubahan hanya pada 1 halaman, Tidak perlu menggunakan beberapa file
    * Kekurangan: Meningkatkan waktu akses website, Tidak efisien jika ingin menggunakan style css yang sama pada beberapa halaman
* External CSS

    External CSS adalah kode CSS yang ditulis pada sebuah file .CSS terpisah. File CSS ini akan dilink di dalam file html tepatnya di bagian `<head>`. Berikut contohnya 
    ```html
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    ```
    * Kelebihan: File CSS bisa digunakan di berbagai halaman, Kecepatan load jadi lebih cepat, ukuran file HTML mengecil dan strukturnya rapih
    * Kekurangan: Halaman tidak akan tampil sempurna selama file CSS belum selesai dipanggil

### 2. Jelaskan tag HTML5 yang kamu ketahui.
```html
<a> = Mendefinisikan hyperlink
<b> = Menampilkan text dalam bentuk bold
<body> = Mendefinisikan Body dokumen
<br> = Menghasilkan sebuah line break
<button> = Membuat sebuah tombol yang bisa dipencet
<div> = Menjelaskan sebuah divisi atau bagian di sebuah dokumen
<form> = Mendefinisikan sebuah form HTML untuk input user
<head> = Mendefiniskan bagian head dari sebuah dokumen yang mengandung informasi mengenai dokumennya seperti judul/title
<h1> - <h6> = Mendefinisikan Heading/judul pada HTML
<hr> = Membuat sebuah garis horizontal
<input> = Mendefinisikan input control
<label> = Mendefinisikan label untuk <input> control
<li> = Mendefinisikan list item
<meta> = Menyajikan metadata terstruktur mengenai kontek dokumennya
<ol> = Mendefinisikan ordered list
<p> = Mendefinisikan sebuah paragraf
<span> = Mendefinisikan sebuah inline bagian tanpa style di sebuah dokumen
<style> = Memasukkan informasi style (Biasanya CSS) ke dalam Head sebuah dokumen
<table> = Mendefiniskan sebuah tabel data
<tbody> = Mengelompokan sekumpulan baris mendefinisikan badan utama sebuah tabel data
<td> = Mendefinisikan sebuah cell di dalam tabel
<textarea> = Tempat user dapat memasukkan text (multi line)
<th> = Mendefinisikan header cell dalam sebuah tabel
<thead> = Mengelompokkan sejumlah baris yang mendeskripsikan label kolom sebuah tabel
<title> = Mendefinisikan judul dari sebuah dokumen
<tr> = Mendefinisikan sebuah baris cell di dalam tabel
<ul> = Mendefinisikan list tak berurut
```

### 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
* Element Selector: _Element Selector_ menggunakan tag HTML sebagai _selector_ untuk mengubah properti yang ada di dalam tag tersebut. Berikut contohnya:
    ```cSS
    form {
            margin: 2%;
            width: 40vw;
            padding: 1em;
            border: 2px solid rgb(87, 73, 73);
            border-radius: 1em;
            font-size: 15px;
        }
    ```
* ID Selektor: _ID Selector_ menggunakan ID pada tag HTML sebagai _selector_-nya (ID harus unik). Pada CSS-nya, menggunakan format `#id`. Berikut contohnya

    Untuk Tag-nya:
    ```html
    ...
        <div id="text">
            <p>Ini Text percobaan</p>
        </div>
    ...
    ```
    Selector di CSS
    ```CSS
    #text {
        font-family: arial;
    }
    ```

* Class Selector: _Class Selector_ menggunakan class pada tag HTML sebagai _selector_-nya. Pada CSS-nya, menggunakan format `.class`. Berikut contohnya:

    Untuk Tag-nya
    ```html
    ...
    <div class="card-header card-finished">
        <h4>{{task.title}}</h4>
        <p>(Selesai)</p>
    </div>
    ...
    ```

    Selector di CSS:
    ```CSS
    .card-finished {
        background: green;
        color: white;
    }
    ```
* `*` Selector: Mengatur semua elemen yang ada di dokumen. _Selector_ ini juga bisa seluruh elemen di dalam sebuah elemen lainnya. Berikut contohnya:
    ```CSS
    * {
    background-color: black;
    }
    ```

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. **Kustomisasi templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma)**
    
    Pertama-tama, saya menggunakan CSS framework Bootstrap sehingga saya menambahkan link bootstrap di head yang ada di `base.html` sebagai berikut :
    ```CSS
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    ```
    Selain itu, saya juga menambahkan 2 scripts di bagian body `base.html`:
    ```CSS
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"
    integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3"
    crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.min.js"
    integrity="sha384-7VPbUDkoPSGFnVtYi0QogXtr74QeVeeIs99Qfg5YCF+TidwNdjvaKZX19NZ/e6oz"
    crossorigin="anonymous"></script>
    ```
    Kemudian berikut yang saya lakukan untuk masing-masing halaman:
    * create-task
        * Membuat styling untuk element form, seperti border, padding, margin, dll
        * Membuka penyingkat dari django untuk form yakni dari `{{form.as_table}}` menjadi baris-baris html
        * Semua elemen form tadi ditaruh di dalam sebuah container yang berukuran seluruh halaman dan dibuat center halaman
        * Memanfaatkan class yang ada di bootstrap untuk mengubah penampilan input field, label, dan button submitnya

    * login
        * Membuat styling untuk element form, seperti border, padding, margin, dll. Serta membuat class untuk menambahkan buffer di bagian atas
        * Membuat container seukuran halaman untuk menyimpan seluruh elemen yang nantinya akan digunakan dan bisa di-_center_ di tengah halaman elemennya
        * Memanfaatkan _grid layout_ yang ada di Bootstrap untuk menaruh elemen-elemen input, label, button, dan lainnya di form
        * Memanfaatkan class yang ada di bootstrap untuk mengubah penampilan input field, label, dan button submitnya. 
    
    * Register
        * Membuat styling untuk element form, seperti border, padding, margin, dll. Serta membuat class untuk menambahkan buffer di bagian atas, dan juga mengubah style dari beberapa elemen
        * Membuat container seukuran halaman untuk menyimpan seluruh elemen yang nantinya akan digunakan dan bisa di-_center_ di tengah halaman elemennya
        * Membuka penyingkat dari django untuk form yakni dari `{{form.as_table}}` menjadi baris-baris html
        * Memanfaatkan _grid layout_ yang ada di Bootstrap untuk menaruh elemen-elemen input, label, button, list, dan lainnya di form
        * Memanfaatkan class yang ada di bootstrap untuk mengubah penampilan input field, label, dan button submitnya.

    * _todo list_
        * Untuk looping setiap objek di todolist, bukannya membuat elemen tabel saya membuat sebuah card dan field-field dari objek ini saya masukkan ke _card_.
        * Saya memanfaatkan _grid layout_ di Bootstrap 5.2 sehingga alignment elemen di dalam card dan layout cardnya di halaman itu sendiri bisa diatur sehingga rapih.
        * Dengan dilakukannya kedua langkah di atas, akan terbuat _card_ sebanyak objek _todo list_ yang ada dan layout dari setiap _card_ seragam.
        * Selanjutnya, saya melakukan customasi beberapa elemen dan menambahkan beberapa class baru di style.
        * Terakhir, saya merubah beberapa penampilan elemen html menggunakan class, container, dan grid yang dimiliki bootstrap 

2. **Membuat keempat halaman yang dikustomisasi menjadi responsive.**
    
    Sebelumnya, saya menggunakan _framework_ Bootstrap 5.2 untuk aplikasi ini. Untungnya, Bootstrap ini menyediakan _media query_ berdasarkan _breakpoint-breakpoint_ yang sudah disediakan [See Here](https://getbootstrap.com/docs/5.2/layout/breakpoints/). Ditambah lagi, class grid dan container memanfaatkan _breakpoint-breakpoint_ ini sehingga mereka bisa responsive menyesuaikan dengan _breakpoint_-nya (Misal jika sebuah row telah mencapai batas breakpoint yang dispesifikasinya tampilannya akan berubah).
    
    Dengan demikian, agar halamannya responsive saya membungkus elemen-elemen html di dalam sebuah grid dan/atau sebuah container sehingga elemen-elemennya responsif. Ditambah lagi, saya membuat ukuran beberapa elemen relatif terhadap ukuran halaman sedemikian sehingga elemen tersebut menjadi responsif.
    




[to-do list heroku]: https://lab-1-pbp-saya.herokuapp.com/todolist/
