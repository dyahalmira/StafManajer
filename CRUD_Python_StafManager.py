from tabulate import tabulate

# Password admin
password_admin = "admin"

# list-dict karyawan 
employees = [
    {
        'id': 1,
        'nama': 'Ria Lestari',
        'posisi': 'Manajer Operasional',
        'gender': 'Wanita',
        'tanggal_bergabung': '2020-01-20',
        'tanggal_lahir': '1990-08-01',
        'nomor_telepon': '081345678901',
        'email': 'ria.l@mail.com',
        'alamat': 'Jl. Merpati Indah No. 12',
        'status': 'Aktif'
    },
    {
        'id': 2,
        'nama': 'Bambang Sudarmo',
        'posisi': 'Spesialis Pemasaran',
        'gender': 'Pria',
        'tanggal_bergabung': '2021-06-15',
        'tanggal_lahir': '1992-11-23',
        'nomor_telepon': '081456789012',
        'email': 'bambang.s@mail.com',
        'alamat': 'Perumahan Sejahtera Blok B',
        'status': 'Aktif'
    },
    {
        'id': 3,
        'nama': 'Sinta Dewi',
        'posisi': 'Akuntan',
        'gender': 'Wanita',
        'tanggal_bergabung': '2022-02-28',
        'tanggal_lahir': '1995-04-05',
        'nomor_telepon': '081567890123',
        'email': 'sinta.d@mail.com',
        'alamat': 'Jl. Bunga Melati No. 7',
        'status': 'Aktif'
    },
    {
        'id': 4,
        'nama': 'Fajar Ramadhan',
        'posisi': 'Desainer Grafis',
        'gender': 'Pria',
        'tanggal_bergabung': '2022-09-01',
        'tanggal_lahir': '1997-09-30',
        'nomor_telepon': '081678901234',
        'email': 'fajar.r@mail.com',
        'alamat': 'Jl. Cempaka Raya No. 10',
        'status': 'Aktif'
    },
    {
        'id': 5,
        'nama': 'Maudy Ayunda',
        'posisi': 'Pengembang Web',
        'gender': 'Wanita',
        'tanggal_bergabung': '2023-01-18',
        'tanggal_lahir': '1998-07-22',
        'nomor_telepon': '081789012345',
        'email': 'maudy.a@mail.com',
        'alamat': 'Perumahan Asri No. 15',
        'status': 'Aktif'
    },
    {
        'id': 6,
        'nama': 'Gilang Nugraha',
        'posisi': 'Staf Layanan Pelanggan',
        'gender': 'Pria',
        'tanggal_bergabung': '2023-04-05',
        'tanggal_lahir': '1996-03-22',
        'nomor_telepon': '081890123456',
        'email': 'gilang.n@mail.com',
        'alamat': 'Jl. Bintang Timur No. 3',
        'status': 'Aktif'
    },
    {
        'id': 7,
        'nama': 'Putri Cahaya',
        'posisi': 'Staf Gudang',
        'gender': 'Wanita',
        'tanggal_bergabung': '2023-08-10',
        'tanggal_lahir': '1990-12-01',
        'nomor_telepon': '081901234567',
        'email': 'putri.c@mail.com',
        'alamat': 'Gg. Kemerdekaan No. 8',
        'status': 'Cuti'
    },
    {
        'id': 8,
        'nama': 'Joko Susilo',
        'posisi': 'Asisten Admin',
        'gender': 'Pria',
        'tanggal_bergabung': '2024-01-30',
        'tanggal_lahir': '1999-04-14',
        'nomor_telepon': '082123456789',
        'email': 'joko.s@mail.com',
        'alamat': 'Jl. Pahlawan No. 20',
        'status': 'Aktif'
    },
    {
        'id': 9,
        'nama': 'Intan Iriana',
        'posisi': 'Spesialis Konten',
        'gender': 'Wanita',
        'tanggal_bergabung': '2024-03-11',
        'tanggal_lahir': '1994-05-28',
        'nomor_telepon': '082234567890',
        'email': 'intan.p@mail.com',
        'alamat': 'Perumahan Harmoni Blok B',
        'status': 'Aktif'
    },
    {
        'id': 10,
        'nama': 'Bayu Seto',
        'posisi': 'Spesialis SEO',
        'gender': 'Pria',
        'tanggal_bergabung': '2024-05-02',
        'tanggal_lahir': '1993-01-25',
        'nomor_telepon': '082345678901',
        'email': 'bayu.a@mail.com',
        'alamat': 'Jl. Cendrawasih No. 5',
        'status': 'Aktif'
    }
]

# fungsi validasi perintah
def validation_confirm(prompt):
    while True:
        choice = input(f"{prompt} (y/n): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")

# fungsi untuk menampilkan data berdasarkan ID
def find_employee_by_id():
    while True:
        try:
            employee_id = int(input("Pilih ID karyawan (ketik 0 untuk batal): "))
            if employee_id == 0:
                print("Perintah dibatakan.")
                return None

            for emp in employees:
                if emp['id'] == employee_id:
                    return emp
            
            print("ID tidak ditemukan. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan ID dalam bentuk angka.")

# fungsi untuk menampilkan tabel list karyawan(employee)
def display_employees():
    while True:
        print(""""\n=== Tampilkan Data Karyawan ===
1. Tampilkan Semua Data
2. Tampilkan Berdasarkan ID
3. Kembali ke Menu Admin""")
        
        choice = input("Pilih menu (1-3): ")
        
        if choice == '1':
            _display_table(employees)
        elif choice == '2':
            emp = find_employee_by_id()
            if emp:
                _display_table([emp])
        elif choice == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

#fungsi table untuk menampilkan list karyawan
def _display_table(employee_list):
      
    headers = [
        'ID',
        'Nama',
        'Posisi',
        'Jenis Kelamin',
        'Tgl. Bergabung',
        'Tgl. Lahir',
        'Nomor Telepon',
        'Email',
        'Alamat',
        'Status'
    ]
    table_data = []
    for emp in employee_list:
        table_data.append([
            emp['id'],
            emp['nama'],
            emp['posisi'],
            emp['gender'],
            emp['tanggal_bergabung'],
            emp['tanggal_lahir'],
            emp['nomor_telepon'],
            emp['email'],
            emp['alamat'],
            emp['status']
        ])
    print("\n=== Data Karyawan ===")
    print(tabulate(table_data, headers=headers, tablefmt='fancy_grid'))

#fungsi untuk menambahkan karyawan baru
def create_employee():
    while True:
        print("\n=== Tambah Data Karyawan ===")
        nama = input("Nama Karyawan: ").title()
        posisi = input("Posisi: ").title()
        
        while True:
            gender = input("Jenis Kelamin (Pria/Wanita): ").capitalize()
            if gender in ["Pria", "Wanita"]:
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan 'Pria' atau 'Wanita'.")
        
        tanggal_bergabung = input("Tanggal Bergabung (YYYY-MM-DD): ")
        tanggal_lahir = input("Tanggal Lahir (YYYY-MM-DD): ")
        
        while True:
            nomor_telepon = input("Nomor Telepon: ")
            if nomor_telepon.isdigit() and len(nomor_telepon) >= 10:
                break
            else:
                print("Nomor telepon tidak valid. Masukkan minimal 10 digit angka dan hanya angka.")
        
        email = input("Email: ")
        alamat = input("Alamat: ").title()
        status = input("Status (Aktif/Cuti): ").capitalize()

        # Menentukan ID untuk employee baru 
        last_id = employees[-1]['id'] if employees else 0
        new_id = last_id + 1

        new_employee = {
            'id' : new_id,
            'nama' : nama,
            'posisi' : posisi,
            'gender': gender,
            'tanggal_bergabung' : tanggal_bergabung,
            'tanggal_lahir' : tanggal_lahir,
            'nomor_telepon' : nomor_telepon,
            'email' : email,
            'alamat' : alamat,
            'status' : status
        }
        
        # Tampilkan data yang baru diinput untuk konfirmasi
        _display_table([new_employee])
        
        if validation_confirm("Yakin ingin menyimpan data ini?"):
            employees.append(new_employee)
            print("Data karyawan berhasil ditambahkan.")
        else:
            print("Penambahan data dibatalkan.")
        
        if not validation_confirm("Apa ada yang mau ditambahkan lagi?"):
            break

#fungsi untuk mengubah data karyawan yang sudah ada. 
def update_employee():
    while True:
        print("\n=== Ubah Data Karyawan ===")
        _display_table(employees)
        
        emp = find_employee_by_id()
        if emp:
            print(f"Mengubah data untuk: {emp['nama']}")
            emp['nama'] = input(f"Nama Karyawan ({emp['nama']}): ").title() or emp['nama']
            emp['posisi'] = input(f"Posisi ({emp['posisi']}): ").title() or emp['posisi']
            
            while True:
                gender_baru = input(f"Jenis Kelamin ({emp['gender']}): ").capitalize() or emp['gender']
                if gender_baru in ["Pria", "Wanita"]:
                    emp['gender'] = gender_baru
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan 'Pria' atau 'Wanita'.")
            
            emp['tanggal_bergabung'] = input(f"Tanggal Bergabung (YYYY-MM-DD)({emp['tanggal_bergabung']}): ") or emp['tanggal_bergabung']
            emp['tanggal_lahir'] = input(f"Tanggal Lahir (YYYY-MM-DD)({emp['tanggal_lahir']}): ") or emp['tanggal_lahir']

            while True:
                nomor_telepon_baru = input(f"Nomor Telepon ({emp['nomor_telepon']}): ")
                if not nomor_telepon_baru:
                    break
                if nomor_telepon_baru.isdigit() and len(nomor_telepon_baru) >= 10:
                    emp['nomor_telepon'] = nomor_telepon_baru
                    break
                print("Nomor telepon tidak valid. Masukkan minimal 10 digit angka.")
            
            emp['email'] = input(f"Email ({emp['email']}): ") or emp['email']
            emp['alamat'] = input(f"Alamat ({emp['alamat']}): ").title() or emp['alamat']
            emp['status'] = input(f"Status ({emp['status']}): ").capitalize() or emp['status']
            
            _display_table([emp])
            
            if validation_confirm("Yakin ingin mengubah data ini?"):
                print("Data karyawan berhasil diubah!")
            else:
                print("Perubahan data dibatalkan.")
            
            if not validation_confirm("Ada yang mau diubah lagi?"):
                break
        
        else:
            break


#fungsi untuk menghapus data
def delete_employee():
    print("\n=== Hapus Data Karyawan ===")
    _display_table(employees)
    
    emp_to_delete = find_employee_by_id()
    if emp_to_delete:
        if validation_confirm(f"Apakah Anda yakin ingin menghapus data karyawan '{emp_to_delete['nama']}'?"):
            employees.remove(emp_to_delete)
            print(f"Data karyawan '{emp_to_delete['nama']}' berhasil dihapus.")
    else:
        print("Penghapusan data dibatalkan.")

# fungsi mencari data karyawan berdasarkan nama atau posisi
def search_employee():
    """Mencari karyawan berdasarkan nama atau posisi."""
    while True:
        print("\n=== Pencarian Karyawan ===")
        keyword = input("Masukkan nama atau posisi yang ingin dicari (ketik 0 untuk kembali): ")
        
        if keyword == '0':
            print("Kembali ke menu sebelumnya.")
            return

        search_results = [
            emp for emp in employees 
            if keyword.lower() in emp['nama'].lower() or keyword.lower() in emp['posisi'].lower()
        ]
        
        if search_results:
            _display_table(search_results)
            if not validation_confirm("Ada yang mau dicari lagi?"):
                break
        else:
            print(f"Hasil tidak ditemukan untuk '{keyword}'. Silakan coba lagi atau ketik 0 untuk kembali.")

#fungsi menu utama dalam admin
def admin_menu():
    while True:
        print("""\n=== Menu Admin ===
1. Tampilkan Data Karyawan
2. Tambahkan Data Karyawan
3. Ubah Data Karyawan
4. Hapus Data Karyawan
5. Cari Karyawan
6. Kembali ke Menu Utama
7. Keluar""")
        choice = input("Pilih menu (1-7): ")
        if choice == '1':
            display_employees()
        elif choice == '2':
            create_employee()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            search_employee()
        elif choice == '6':
            if validation_confirm("Anda yakin ingin kembali ke Menu Utama?"):
                break
        elif choice == '7':
            if validation_confirm("Anda yakin ingin keluar dari program?"):
                return True
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")
    return False

#fungsi login untuk masuk ke menu admin
def login_admin():
    max_attempts = 3
    for attempt in range(max_attempts):
        print(f"\n=== Login Admin (Percobaan ke-{attempt + 1}/{max_attempts}) ===")
        password = input("Masukkan password admin: ")

        if password == password_admin:
            print("Login berhasil.")
            return admin_menu()
        else:
            print("Password salah.")
    print("Anda telah 3x salah memasukkan password. Kembali ke menu utama.")
    return

#fungsi untuk menu staff
def staff_menu():

    while True:
        print("""\n=== Menu Staff ===
1. Tampilkan Data Karyawan
2. Cari Data Karyawan
3. Kembali ke menu utama
4. Keluar """)
        choice = input("Pilih menu (1-4): ")
        if choice =='1':
            _display_table(employees)
        elif choice == '2':
            search_employee()
        elif choice == '3':
            if validation_confirm("Anda yakin ingin kembali ke Menu Utama?"):
                break
        elif choice == '4':
            if validation_confirm("Anda yakin ingin keluar dari program?"):
                return True
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    return False

def main_menu():
    while True:
        print("""\n=== Selamat Datang Di Aplikasi Management Karyawan ===
Silahkan pilih mode masuk:
1. Admin
2. Staff
3. Keluar""")
        choice = input("Pilih mode(1-3): ")
        if choice =='1':
            if login_admin():
                break
        elif choice == '2':
            if staff_menu():
                break
        elif choice == '3':
            if validation_confirm("Anda yakin ingin keluar dari program?"):
                break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main_menu()