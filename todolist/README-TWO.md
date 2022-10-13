# Tugas 6 PBP
Tugas ini diselesaikan oleh Andi Muhamad Dzaky Raihan, NPM 2106631412, kode Asdos FRA.

Berikut link ke aplikasi yang dibuat:
* [Link to-do list][to-do list heroku]

### Jelaskan perbedaan antara _asynchronous programming_ dengan _synchronous programming_.
[Source](https://www.mendix.com/blog/asynchronous-vs-synchronous-programming/)
* _Asynchronous Programming_
    
    _Asynchronous programming_ adalah model dengan _multithread_ yang paling cocok digunakan untuk _networking_ dan komunikasi. _Asynchronous_ adalah arsitektur _non-blocking_ yang artinya tidak akan memblokir eksekusi lebih lanjut apabila satu atau lebih operasi sedang berjalan.

    Dengan _asynchronous programming_, beberapa operasi yang saling bersangkutan dapat berjalan di saat yang bersamaan tanpa perlu menunggu satu sama lain selesai. Dalam komunikasi _asynchronous_, pihak-pihak menerima dan memroses pesan ketika itu memungkinkan, bukannya langsung direspon ketika diterima.

    Salah satu contoh yang dapat mudah dicerna adalah sms. Sseseorang dapat memberikan sebuah pesan dan penerima bisa menjawabnya kapanpun dia mau. Selagi menunggu, pengirim boleh melakukan hal lain selagi menunggu respon.

* _Synchronous Programming_

    _Synchronous_ dikenal juga sebagai arsitektur _blocking_ dan ideal untuk sistem programming _reactive_. Sebagai model _single-thread_, model ini mengukuti suatu urutan secara runtut yang artinya operasi dilakukan satu per satu, dalam urutan yang sempurna. Ketika sebuah operasi sedang dijalankan, instruksi operasi lainnya ditahan. Penyelesaian tugas pertama akan menjalankan tugas berikutnya dan seterusnya.

* Berikut perbedaan asyinchronous dan synchronous dalam tabel

| Asynchronous | Asynchronous |
| ----------- | ----------- |
| multi-thread (bisa paralel)      | single-thread (satu persatu)       |
| non-blocking (beberapa request ke server)   | blocking (request satu per satu)        |
| Meningkatkan throughput (bisa beberapa operasi di saat yang sama)   | Lebih lambat dan metodis        |
| Digunakan untuk task yang bersifat independen | Digunakan untuk task yang bersifat dependen|

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
[Source](https://isaaccomputerscience.org/topics/event_driven_programming?examBoard=all&stage=all)

**_Event-driven programgging_** adalah pendekatan dimana kode ditulis untuk merespon terhadap semua _events_. _Events_ bisa dipicu oleh pengguna, seperti dengan memencet icon atau memasukkan sebuah text. Dalam sistem yang otomatis, sensor bisa digunakan untuk mendeteksi sebuah _events_ seperti ketika suatu suhu dicapai di dalam rumah kaca atau ketika suatu ketinggian air terdeteksi pada sistem pencegah bancir.

_Subroutines_ yang menanggapi _events_ ini adalah _event handlers_. Sang _event handler_ akan memastikan _event_ yang memicunya akan diproses dengan baik sedemikian sehingga respon yang tepat akan dikembalikan.

Contohnya pada penerapan tugas ini adalah dalam tombol close modal add-task
    
Kode untuk menampilkan tombolnya adalah sebagai berikut:
```html
<button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                    onclick="resetForm();">Close</button>
```
Dapat kita lihat, pada button ini ada atribut `onclick="resetForm();"` yang artinya fungsi `resetForm` akan dipanggil ketika tombol ini dipencet. Fungsi `resetForm` adalah sebagai berikut:
```js
function resetForm() {
    document.getElementById("formAddTask").reset();
}
```
Yang artinya fungsi ini akan mereset element dengan id `formAddTask`

### Jelaskan penerapan asynchronous programming pada AJAX.
[Source](https://www.theserverside.com/definition/Ajax-Asynchronous-JavaScript-and-XML)

Berikut bagaimana berbagai proses AJAX bekerja secara asynchronous:
* Ketika halaman HTML berhasil dimuat, data dibaca dari server web
* Tanpa perlu untuk memuat ulang halaman web, data bisa diperbaharui
* Pemindahan data menuju _web server_ terjadi di _background_

Semua langkah _asynchronous_ di atas membantu kita untuk membuat konten web HTML yang responsif dan juga memiliki performa yang lebih cepat. Dalam mencapai tujuan ini, mereka membantu mempertahankan interaksi antara pengguna dan halaman web yang natural. Ditambah lagi, karena AJAX tidak bergantung pada web server, hal ini membuat sebuah _data-driven environment_ dibandingkan sebuah _page-driven environment_. Maka dari itu AJAX bisa mengeksekusi tugas secara asynchronous dan pada saat apapun.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

* AJAX GET
    * Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.
    
        Pertama-tama, saya membuat sebuah function yang bisa mengembalikan data dalam bentuk JSON (ke dalam web page) seperti berikut (Data dari task user yang log in):
    
        ```py
        @login_required(login_url='/todolist/login/')
        def get_json(request):
            todolist = ToDoList.objects.filter(user=request.user)
            return HttpResponse(serializers.serialize("json", todolist), content_type="application/json")
        ```

    * Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.

        Setelah itu, link fungsi di atas ke sebuah url `./todolist/json` di `urls.py` yang berada di folder todolist seperti berikut:
    
        ```py
        urlpatterns = [
            ...
            path('json/', get_json, name="get_json"),
            ...
        ]
        ```
    * Lakukan pengambilan task menggunakan AJAX GET.
    
        Pertama-tama, saya membuat sebuah fungsi di dalam javascript untuk mereset/membuat ulang semua card. Berikut fungsinya
    
        ```js
        function resetCard() {
            $("#myCard").empty();
            ...
        }
        ```
        Setelah itu, di fungsi yang sama saya menaruh kode untuk mengambil ajax dari page JSON yang tadi dibuat. Setelah itu, ambil setiap tasknya dan masing-masing task dijadikan sebuah card. Kemudian, card itu dimasukkan ke dalam container yang menyimpan semua card. Berikut kodenya:

        ```js
        $.ajax({
            url: './json/',
            dataType: 'json',
            success: function (data) {
                for (var i = 0; i < data.length; i++) {
                    ...
                    var card = `
                    ...
                    `;
                    $('#myCard').append(card);
        ```
* AJAX POST
    * Buatlah sebuah tombol `Add Task` yang membuka sebuah modal dengan form untuk menambahkan task.
    
        Pertama-tama, saya membuat sebuah modal yang berisikan form untuk menambahkan task. Berikut potongan kode singkatnya:

        ```html
        <div class="modal fade" id="modalTambahTask" tabindex="-1" aria-labelledby="modalTambahTaskLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                <div class="modal-content">
                    ...
                </div>
            </div>
        </div>
        ```
        Setelah memiliki sebuah modal yang menampilkan form, kita tinggal membuat sebuah tombol yang dapat memunculkan modal tsb. Berikut kode untuk tombolnya (kita hanya perlu menambahkan atribut `data-bs-target="#id"`):
    
        ```html
        <button class="btn btn-primary" style="text-align: center;" data-bs-toggle="modal"
                data-bs-target="#modalTambahTask">Tambah Task</button>
        ```
    * Buatlah view baru untuk menambahkan task baru ke dalam database.
        
        Untuk ini, saya hanya menyalin fungsi untuk menambahkan task baru yang saya buat di tugas 4. Bedanya, kali ini ketika berhasil menambahkan saya tidak redirect, melainkan mengembalikan data JSON. Berikut perubahannya

        ```py
        # Jika input valid
        response_data['title'] = title
        response_data['description'] = description
        response_data['date'] = datetime.date.today()
        response_data['msg'] = "success"
        return JsonResponse(response_data)

        # Jika input tidak valid
        response_data['msg'] = "failed"
        return JsonResponse(response_data)
        ```
    
    *  Buatlah path `/todolist/add` yang mengarah ke view yang baru kamu buat.

        Bagian ini sangat simple, saya hanya menaruh satu baris ini di urls.py todolist (Fungsi baru yang tadi dibuat bernama add_todolist_ajax):
        ```py
        urlpatterns = [
            ...
            path('add/', add_todolist_ajax, name="add_todolist_ajax" ),
            ...
        ]
        ```
    
    * Hubungkan form yang telah kamu buat di dalam modal kamu ke path `/todolist/add`

        Pertama-tama, saya membuat sebuah fungsi di js yang dapat mengambil data dari field form dan dimasukkan ke path `/todolist/add` menggunakan AJAX. Berikut potongannya:
        ```js
        function addTask() {
        $.ajax({
            type: 'POST',
            url: './add/',
            data: {
                title: $("#id_title").val(),
                description: $("#id_description").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            ...
        }
        ```

        Setelah itu, saya membuat button yang akan memanggil fungsi ini ketika dipencet (Buttonnya ada di bawah form yang dibuat). Berikut kodenya:
        ```html
        <input type="submit" name="submit" id="addButton" value="Tambah" class="btn btn-primary"
                    onclick="addTask();">
        ```
        Jadi, jika button di atas dipencet, maka data-data dari field form akan di-post ke path `/todolist/add`
    
    * Tutup modal setelah penambahan task telah berhasil dilakukan **dan** Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.

        Masih di dalam pemanggilan AJAX di fungsi `addtask()` di atas, kita tambahkan parameter success yang akan memanggil fungsi dengan parameter data dari JSONResponse milik fungsi `add_todolist_ajax`.
        ```js
        ...
        success: function(data) {
                if (data.msg == "success"){
                    resetCard();
                    resetForm();
                    $('#modalTambahTask').modal('hide');
                } else {
                    alert("Input task tidak valid");
                }
            },
        ...
        ```
        Fungsi di atas hanya dilaksanakan jika pemanggilan AJAX di fungsi `addTask()` berhasil. Dapat dilihat, jika `data.msg` atau pesan status dari fungsi di views.py merupakan sukses, maka list-list card akan diupdate menggunakan fungsi `resetCard()` (Perlu diingat resetCard() mereset hanya semua card yang ada menggunakan AJAX sehingga asynchronous). Setelah itu, isi dari form akan dikosongkan dan terakhir modal akan ditutup menggunakan command `$('#modalTambahTask').modal('hide');`.

    


[to-do list heroku]: https://lab-1-pbp-saya.herokuapp.com/todolist/