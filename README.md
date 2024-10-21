# Aplikasi MySPA CRM - Aplikasi Customer Relationship Management untuk SPA

## 📝 Deskripsi
<p>Aplikasi MySPA CRM adalah aplikasi yang digunakan untuk manajemen data customer di SPA ABC.</p>

## 👤 Target Pengguna
<p>Pengguna aplikasi MySPA CRM meliputi bagian administrasi dan pemilik bisnis spa.</p>

## 🖥️ Teknologi yang Digunakan
<p>Teknologi yang digunakan dalam pembuatan aplikasi ini sebagai berikut:</p>
<ul>
  <li>🐍 Python</li>
  <p>Python sebagai bahasa pemrograman utama.</p>
  <li>📊 Package Tabulate</li>
  <p>Package yang digunakan untuk membuat tabel.</p>
  <li>📅 Package Datetime</li>
  <p>Package yang digunakan untuk memanipulasi dan memformat tanggal.</p>
</ul>

## 🤖 Fitur
<p>Aplikasi MySPA CRM memiliki beberapa fitur yang memudahkan kegiatan administrasi di SPA terkait dengan manajemen hubungan pelanggan, yaitu:</p>
<ul>
  <li>Menampilkan semua data customer.</li>
  <li>Menampilkan data berdasarkan ID.</li>
  <li>Menampilkan data berdasarkan Nomor HP.</li>
  <li>Menambahkan data customer baru.</li>
  <li>Memperbarui data customer berdasarkan ID.</li>
  <li>Menghapus data customer berdasarkan ID.</li>
</ul>

## 🪛 Fungsi di dalam Aplikasi
<ul>
  <li><strong>make_customer_id()</strong>: Menghasilkan ID customer yang unik.</li>
  <li><strong>is_valid_email(email)</strong>: Memvalidasi format email.</li>
  <li><strong>is_valid_nohp(no_hp)</strong>: Memvalidasi format nomor HP.</li>
  <li><strong>is_valid_date(birthday)</strong>: Memvalidasi format tanggal lahir.</li>
  <li><strong>hitung_usia(birthday)</strong>: Menghitung usia berdasarkan tanggal lahir.</li>
  <li><strong>create_data_customer(customer_id, nama, no_hp, email, birthday)</strong>: Menambahkan customer baru ke database.</li>
  <li><strong>read_data_customer()</strong>: Menampilkan semua data customer.</li>
  <li><strong>delete_customer(customer_id)</strong>: Menghapus customer berdasarkan ID.</li>
  <li><strong>update_customer(customer_id, nama, no_hp, email, birthday)</strong>: Memperbarui informasi customer.</li>
  <li><strong>lihat_data_id(customer_id)</strong>: Menampilkan detail customer berdasarkan ID.</li>
  <li><strong>lihat_data_no_hp(no_hp)</strong>: Menampilkan detail customer berdasarkan nomor HP.</li>
  <li><strong>add_dummy_data()</strong>: Menambahkan data dummy untuk pengujian.</li>
  <li><strong>main_menu()</strong>: Menampilkan menu utama untuk interaksi pengguna.</li>
</ul>






