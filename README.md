-----

# **StafManajer: Sistem Manajemen Data Karyawan**

**StafManajer** adalah sebuah aplikasi sederhana yang dirancang untuk membantu **Usaha Kecil Menengah (UKM)** mengelola informasi staf secara digital dan terpusat. Aplikasi ini menyediakan cara yang efisien untuk mencatat, menyimpan, dan mengakses data karyawan, menjadikannya solusi ideal untuk beralih dari metode manual ke sistem yang lebih terstruktur.

-----
## **Pemangku Kepentingan & Pengguna**

### **Pemangku Kepentingan (Stakeholders)**

Proyek ini relevan bagi beberapa pihak di dalam perusahaan:

  * **Pemilik/Manajer Perusahaan:** Pihak yang membutuhkan akses penuh untuk memantau dan mengelola data karyawan sebagai dasar pengambilan keputusan strategis.
  * **Staf HR/Admin:** Pihak yang bertanggung jawab langsung atas input, pembaruan, dan pemeliharaan data harian.
  * **Karyawan:** Pengguna akhir yang datanya dikelola oleh sistem ini dan dapat melihat informasi dasar untuk keperluan internal.

### **Pengguna**

  * **Admin:** Menyediakan opsi lengkap untuk **menambah** (Create), **mengubah** (Update), **menghapus** (Delete), **melihat**, dan **mencari** data karyawan.
  * **Staf:** Menyediakan opsi terbatas hanya untuk **melihat** dan **mencari** data karyawan.

-----

## **Fitur & Alur Program**

### **Alur Utama**

Program **StafManajer** didesain agar mudah dioperasikan. Cukup ikuti alur di bawah ini:

1.  **Mulai Program:** Jalankan skrip Python dari terminal.
2.  **Pilih Mode Akses:** Saat program pertama kali berjalan, anda akan disajikan menu utama untuk memilih mode **Admin** atau **Staf**.
3.  **Masuk ke Sistem:**
    * Jika memilih **Admin**, anda akan diminta memasukkan *password* "admin" untuk otentikasi.
    * Jika memilih **Staf**, anda akan langsung masuk ke menu tanpa *password*.
4.  **Operasi Data:**
    * **Admin:** Di menu Admin, anda bisa **menambah, melihat, mengubah, mencari dan menghapus** data karyawan. Cukup pilih angka yang sesuai dengan operasi yang anda inginkan.
    * **Staf:** Di menu Staf, anda hanya bisa **melihat** atau **mencari** data karyawan.
5.  **Keluar:** Pilih opsi `Keluar` di menu mana pun untuk mengakhiri program.

----

### **Teknologi dan Modul yang Digunakan**

Program ini dibangun menggunakan dua jenis modul:

* **Modul Eksternal:**
    * **`tabulate`**: Modul ini berfungsi untuk mengubah data dari format *list of dictionaries* menjadi tabel yang rapi dan mudah dibaca langsung di terminal. Ini sangat membantu untuk menyajikan data karyawan secara profesional.
* **Modul Bawaan Python:**
    * Program ini menggunakan struktur data dasar Python seperti **List**, **Dictionary**, dan **Function** (fungsi).
    * Fungsi-fungsi seperti `input()` untuk menerima masukan dan `print()` untuk menampilkan informasi adalah bagian integral dari program ini.
    
-----

## **Panduan Penggunaan**

### **Teknologi yang Digunakan**

Program ini dibuat menggunakan bahasa pemrograman **Python** dan memanfaatkan **modul eksternal** `tabulate` untuk menampilkan data dalam format tabel yang rapi.


