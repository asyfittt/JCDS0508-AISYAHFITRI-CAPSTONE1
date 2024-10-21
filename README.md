# Aplikasi MySPA CRM - Aplikasi Customer Relationship Management untuk SPA 🌸

## 📝 Deskripsi
Aplikasi MySPA CRM adalah sistem manajemen hubungan pelanggan (CRM) yang dirancang untuk membantu SPA dalam mengelola data customer secara efektif. Dengan aplikasi ini, Anda dapat menambah, memperbarui, menghapus, dan melihat informasi customer dengan mudah.

## 🖥️ Teknologi yang Digunakan
Aplikasi ini dibangun dengan teknologi berikut:
- **🐍 Python**: Bahasa pemrograman utama yang digunakan untuk mengembangkan aplikasi ini.
- **📊 Tabulate**: Package yang digunakan untuk menampilkan data dalam bentuk tabel yang terformat.
- **📅 Datetime**: Package yang digunakan untuk manipulasi dan validasi tanggal.

## 🤖 Fitur
Aplikasi MySPA CRM menyediakan fitur-fitur berikut:
- Menampilkan semua data customer.
- Menambahkan customer baru dengan validasi.
- Memperbarui data customer yang sudah ada.
- Menghapus data customer berdasarkan ID.
- Melihat detail customer berdasarkan ID atau nomor HP.

## 🔧 Fungsi Utama
Berikut adalah beberapa fungsi penting dalam aplikasi:
- `make_cutomer_id()`: Membuat ID customer yang unik.
- `is_valid_email(email)`: Memvalidasi format email.
- `is_valid_nohp(no_hp)`: Memvalidasi format nomor HP.
- `is_valid_date(birthday)`: Memvalidasi format tanggal lahir.
- `hitung_usia(birthday)`: Menghitung usia berdasarkan tanggal lahir.
- `create_data_customer(...)`: Menambahkan data customer baru ke database.
- `read_data_customer()`: Menampilkan semua data customer.
- `delete_customer(customer_id)`: Menghapus customer berdasarkan ID.
- `update_customer(...)`: Memperbarui informasi customer yang ada.
- `lihat_data_id(customer_id)`: Menampilkan detail customer berdasarkan ID.
- `lihat_data_no_hp(no_hp)`: Menampilkan detail customer berdasarkan nomor HP.
- `add_dummy_data()`: Menambahkan data dummy untuk pengujian.
- `main_menu()`: Menampilkan menu utama untuk interaksi pengguna.

## 🚀 Cara Penggunaan
1. **Instal dependencies**:
   ```bash
   pip install tabulate
2. **Jalankan aplikasi:**:
   ```bash
   python myspa_app.py
3. Ikuti petunjuk yang muncul di menu untuk menambah, memperbarui, atau menghapus data customer.
