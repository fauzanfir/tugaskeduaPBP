link aplikasi: https://tontonankuu.herokuapp.com/todolist/ajax/

# **Cara mengimplementasikan checklist di atas**
  1. Pertama saya membuat method pada views.py untuk mengembalikan format json.
  2. Lalu, saya membuat method yang akan menerima method POST dari form yang akan kita buat dan me return json response
  3. Lalu, saya buat file baru bernama todolist_ajax.html yang berfungsi memunculkan tabel. Syntax yang digunakan sama seperti tabel pada biasanya
namun untuk mengimplementasi json, kita perlu untuk menambahkan script dari ajax.
  4. Lalu, kita menambahkan url path dari tabel ajax tersebut.
  5. Setelah itu, kita membuat form yang berdasarkan script dari ajax yang akan mengirim method POST.
  6. Data-data pada form tersebut akan diterima oleh method pada views.py lalu di render secara asinkronus pada halaman utama.
