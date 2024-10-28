# Remote Access Trojan (RAT) ⚙️


## Deskripsi
Proyek ini adalah implementasi **Remote Access Trojan (RAT)** yang memungkinkan pengguna untuk mengakses dan mengendalikan sistem dari jarak jauh. Dengan menggunakan socket dan JSON, proyek ini menyediakan berbagai perintah seperti meng-upload dan mengunduh file, dan menjalankan perintah shell basic.

## Fitur
- **cd <path>**: Pindah ke direktori yang ditentukan.
- **clear**: Membersihkan layar terminal.
- **ls**: Menampilkan daftar file dan direktori di direktori saat ini.
- **mkdir <folder_name>**: Membuat direktori baru dengan nama yang ditentukan.
- **touch <file_name>**: Membuat file baru dengan nama yang ditentukan.
- **run <file.exe>**: Menjalankan file executable.
- **upload <file>**: Mengupload file dari klien ke server.
- **download <file>**: Mengunduh file dari server ke klien

## Cara Kerja
1. **Client**: Menghubungkan ke server dan mendengarkan perintah dari server.
2. **Server**: Menerima koneksi dari klien dan mengirimkan perintah untuk dieksekusi.

## Persyaratan
- Python 3.x
- Library: `socket`, `json`, `os`, `ctypes`, `subprocess`, `time`
- Harus terhubung dengan network / jaringan yang sama

## Mengatur IP dan PORT 
Jika anda kebingungan untuk mencari ip server anda, anda dapat ketik perintah berikut pada terminal server anda :

**Windows**
```powershell
  ipconfig
```

**Linux**
```bash
  ifconifg
```

Setelah mengetikan command tersebut , akan muncul konfigurasi ip anda dan anda dapat meng-copy ip tersebut dan masukan ke script.

IP yang digunakan disini adalah IPv4 yang memiliki kombinasi seperti : 192.168.0.1 **(angka berbeda beda tergantung perangkat)**


## Instalasi
1. Clone repositori ini:
   ```bash
   git clone https://github.com/LeroCyS/RAT-python.git
   cd RAT-python


## Langkah Penggunaan

Siapkan 2 device desktop untuk menjalankan script ini, lalu Lakukan proses instalasi pada masing masing device.

Jalankan perintah berikut pada terminal di sisi client (device 1) :
```bash
  python client.py
```

Jalankan perintah berikut pada terminal di sisi server (device 2) :
```bash
  python server.py
```

Setelah mengikuti langkah langkah diatas, pada sisi server akan terdapat peringatan bahwa script berhasil dan koneksi (reverse shell) sudah terhubung.

Anda bisa mulai menjalankan command command yang terdapat pada Fitur di terminal server.
