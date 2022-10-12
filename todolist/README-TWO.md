# Tugas 4 PBP
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


[to-do list heroku]: https://lab-1-pbp-saya.herokuapp.com/todolist/