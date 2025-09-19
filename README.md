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

### **Pengguna Aplikasi**

Aplikasi ini membagi pengguna menjadi dua peran utama dengan hak akses yang berbeda, sehingga menjamin keamanan dan kerahasiaan data:

  * **Admin:** Memiliki hak akses penuh untuk melakukan operasi **CRUD** (Create, Read, Update, Delete) pada data karyawan.
  * **Staf:** Memiliki akses terbatas, hanya dapat **melihat** dan **mencari** data karyawan.

-----

## **Fitur & Alur Program**

### **Alur Utama**

1.  Aplikasi dijalankan dan menampilkan menu utama dengan pilihan mode **Admin** atau **Staf**.
2.  Pengguna **Admin** harus memasukkan *password* "admin" untuk otentikasi.
3.  Menu akan disesuaikan dengan peran pengguna, menyediakan opsi yang relevan.
4.  Pengguna dapat memilih opsi untuk keluar dari menu atau mengakhiri program.

### **Fungsionalitas**

  * **Mode Admin:** Menyediakan opsi lengkap untuk **menambah** (Create), **mengubah** (Update), **menghapus** (Delete), **melihat**, dan **mencari** data karyawan.
  * **Mode Staf:** Menyediakan opsi terbatas hanya untuk **melihat** dan **mencari** data karyawan.
    
-----

## **Panduan Penggunaan**

### **Teknologi yang Digunakan**

Program ini dibuat menggunakan bahasa pemrograman **Python** dan memanfaatkan **modul eksternal** `tabulate` untuk menampilkan data dalam format tabel yang rapi.


