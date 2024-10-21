from tabulate import tabulate
from datetime import datetime

#inisialisasi list untuk tampung data customer
customers = []

#fungsi untuk membuat ID customer
def make_cutomer_id():
    if customers:
        id = len(customers) + 1
    else:
        id = 1

    #untuk fromat customer_id
    id_str = str(id)
    while len(id_str)<5:
        id_str = '0' + id_str
    return f"MYSPA{id_str}"

#fungsi untuk validasi email
def is_valid_email(email):
    return '@' in email and '.' in email

#fungsi untuk validasi no hp
def is_valid_nohp(no_hp):
    return len(no_hp)<=12 and no_hp.isdigit()

def is_valid_date(birthday):
    try:
        datetime.strptime(birthday, '%d-%m-%Y')
        return True
    except ValueError:
        return False

#fungsi kalkulasi umur dari birthday
def hitung_usia(birthday):
    birthday_date = datetime.strptime(birthday,'%d-%m-%Y')
    today = datetime.now()

    # menghitung usia awal berdasarkan perbedaan tahun
    temp_usia = today.year-birthday_date.year

    # untuk periksa apakah ulang tahun terjadi tahun ini
    birthday_tahun_ini = datetime(today.year, birthday_date.month, birthday_date.day)

    # Jika hari ini sebelum ulang tahun di tahun ini, kurangi satu dari usianya
    if today < birthday_tahun_ini:
        temp_usia -= 1

    return temp_usia


#fungsi untuk menambahkan data customer
def create_data_customer(nama,no_hp,email,birthday):
    #menyimpan umur
    usia = hitung_usia(birthday)

    #menyimpan id customer
    customer_id = make_cutomer_id()

    #dictionary customer untuk menyimpan data customer
    customer = {
        'customer_id': customer_id,
        'nama': nama,
        'usia': usia,
        'no_hp': no_hp,
        'email': email,
        'birthday' : birthday
    }
    customers.append(customer)

#fungsi untuk melihat semua data customer
def read_data_customer():
    if not customers:
        print('Tidak ada data customer di database. Silahkan masukkan data terlebih dahulu.')
    else:
        headers = ["Customer ID", "Nama","Usia", "Nomor HP", "Email", "Birthday"]
        table = [[c['customer_id'], c['nama'].upper(), c['usia'], c['no_hp'], c['email'].lower(), c['birthday']] for c in customers]
        print(tabulate(table, headers, tablefmt="grid"))

#fungsi hapus data customer berdasrkan ID
def delete_customer(customer_id):
    global customers
    for customer in customers:
        if customer['customer_id'] == customer_id:
            customer_name = customer['nama']
            while True:
                konfirmasi = input(f"Apa kamu yakin akan menghapus data customer {customer_name}, ID: {customer_id.upper()}? (y/n):")
                if konfirmasi.lower() == 'y':
                    customers.remove(customer)
                    print(f"Customer {customer_name.upper()}, ID: {customer_id.upper()} berhasil dihapus!")
                    break
                elif konfirmasi.lower() == 'n' :
                    print("proses hapus data dibatalkan")
                    break
                else:
                    print("Input salah. Tolong masukkan 'y' untuk yes  atau 'n' untuk no.")
            return
    print(f"Customer dengan ID {customer_id.upper()} tidak ditemukan.")

#fungsi update data customer
def update_customer(customer_id, nama=None, no_hp=None, email=None, birthday=None):
    for customer in customers:
        if customer['customer_id'] == customer_id:
            original_data = customer.copy()

            if nama: 
                customer['nama'] = nama
            if no_hp: 
                if is_valid_nohp(no_hp):
                    customer['no_hp'] = no_hp
                else:
                    print("Nomor HP tidak valid. Perubahan untuk nomor HP dibatalkan.")
            if email:
                if is_valid_email(email):
                    customer['email'] = email
                else:
                    print("Format email tidak valid. Perubahan untuk email dibatalkan.")
            if birthday:  
                if is_valid_date(birthday):
                    customer['birthday'] = birthday
                    customer['usia'] = hitung_usia(birthday)
                else:
                    print("Format tanggal lahir tidak valid. Perubahan untuk tanggal lahir dibatalkan.")

            print("Data yang akan diperbarui:")
            print("========================================")
            print(f"Nama: {customer['nama'].upper()}")
            print(f"Nomor HP: {customer['no_hp']}")
            print(f"Email: {customer['email'].lower()}")
            print(f"Birthday: {customer['birthday']}")
            
            while True:
                konfirmasi = input("Apakah Anda yakin ingin menyimpan perubahan ini? (y/n): ")
                if konfirmasi.lower() == 'y':
                    print(f"Customer {customer['nama'].upper()}, ID: {customer_id.upper()} berhasil diperbarui!")
                    break
                elif konfirmasi.lower() == 'n':
                    customer.update(original_data)
                    print("Perubahan dibatalkan. Data tidak diperbarui.")
                    break
                else:
                    print("Input salah. Tolong masukkan 'y' untuk yes  atau 'n' untuk no.")



#fungsi data dummy
def add_dummy_data():
    create_data_customer("Andi Saputra", "08123456789", "andi.saputra@example.com", "15-10-1990")
    create_data_customer("Siti Aisyah", "08198765432", "siti.aisyah@example.com", "22-05-1995")
    create_data_customer("Budi Hartono", "08212345678", "budi.hartono@example.com", "01-01-1985")
    create_data_customer("Dewi Lestari", "08567891234", "dewi.lestari@example.com", "30-07-1992")
    create_data_customer("Joko Susanto", "08765432109", "joko.susanto@example.com", "20-03-1988")
    create_data_customer("Rina Maulani", "08123456780", "rina.maulani@example.com", "12-12-1993")
    create_data_customer("Fajar Rahman", "08561234567", "fajar.rahman@example.com", "10-04-1980")
    create_data_customer("Nina Sari", "08234567890", "nina.sari@example.com", "14-09-1991")
    create_data_customer("Agus Prasetyo", "08987654321", "agus.prasetyo@example.com", "05-06-1987")
    create_data_customer("Tina Wulandari", "08123456789", "tina.wulandari@example.com", "25-11-1996")


#fungsi main menu
def main_menu():
    #disini untuk isi data dummy
    # add_dummy_data()
    while True:
        print('\nMySPA CRM System')
        print('1. Lihat Data Customer')
        print('2. Tambah Customer Baru')
        print('3. Update Data Customer')
        print('4. Hapus Data Customer')
        print('0. Keluar')

        pilih_menu = input('Masukkan nomor menu: ')

        try:
            if pilih_menu == '1':
                print("Lihat Data Customer")

                while True:
                    print("======================================================")
                    print("1. Lihat Semua Data")
                    print("2. Lihat data berdasarkan ID")
                    print("0. Kembali ke main menu")
                    pilih_submenu = input("Pilih sub menu: ")
                    if pilih_submenu == '1':
                        print(f"\n Semua data customer ({len(customers)} data): ") #melihat jumlah data customer
                        read_data_customer()
                        break
                    elif pilih_submenu == '2':
                        customer_id = input("Masukkan ID customer untuk update: ").upper()

                        for customer in customers:
                            if customer['customer_id'] == customer_id:
                                print(f"\nDetail Customer dengan ID:{customer_id.upper()}")
                                headers = ["Customer ID", "Nama","Usia", "Email", "Nomor HP", "Birthday"]
                                current_details = [
                                    customer['customer_id'],
                                    customer['nama'].upper(),
                                    hitung_usia(customer['birthday']),
                                    customer['email'].lower(),
                                    customer['no_hp'],
                                    customer['birthday']
                                ]
                                print(tabulate([current_details], headers=headers, tablefmt="grid"))
                                break
                        else:
                            print(f"Customer dengan ID {customer_id.upper()} tidak ditemukan.")
                            continue
                    elif pilih_submenu == '0':
                        print("Kembali ke main menu")
                        break
                    else: 
                        print("Invalid input")

            elif  pilih_menu == '2':
                print('Silahkan masukkan data customer')
                nama = input('Nama: ')

                while True:
                    no_hp = input('Nomor Hp (max 12 digits, only numbers): ')
                    if is_valid_nohp(no_hp):
                        break
                    else:
                        print("Nomor Hp tidak valid. Pastikan hanya mengandung angka dan tidak lebih dari 12 digit.")

                while True:
                    email = input('Email: ')
                    if is_valid_email(email):
                        break
                    else:
                        print("Format email tidak valid. Silakan masukkan email yang benar.")

                while True:
                    birthday = input('Masukkan TTL (DD-MM-YYYY): ')
                    if is_valid_date(birthday):
                        break
                    else:
                        print("Format tanggal lahir tidak valid. Format Tgl-Bln-Thn.")

                print("======================================================")
                while True:
                    konfirmasi = input("Apakah Anda yakin ingin menyimpan data ini? (y/n): ")
                    if konfirmasi.lower() == 'y':
                        create_data_customer(nama,no_hp,email,birthday)

                        last_customer = customers[-1]

                        headers = ["Customer ID", "Nama", "Usia", "Nomor HP", "Email", "Birthday"]
                        table = [[
                            last_customer['customer_id'],
                            last_customer['nama'].upper(),
                            last_customer['usia'],
                            last_customer['no_hp'],
                            last_customer['email'].lower(),
                            last_customer['birthday']
                        ]]

                        print("======================================================")
                        print(f'Data pelanggan {nama.upper()} berhasil ditambahkan.')
                        print(tabulate(table, headers, tablefmt="grid"))
                        break
                    elif konfirmasi.lower() == 'n':
                        print("\nData tidak disimpan. Proses dibatalkan.")
                        break
                    else:
                        print("Input salah. Tolong masukkan 'y' untuk yes  atau 'n' untuk no.")


            elif  pilih_menu == '3':
                customer_id = input("Masukkan ID customer untuk update: ").upper()

                for customer in customers:
                    if customer['customer_id'] == customer_id:
                        print("\nDetail Customer Sebelum Diperbarui:")
                        headers = ["Customer ID", "Nama","Usia", "Email", "Nomor HP", "Birthday"]
                        current_details = [
                            customer['customer_id'],
                            customer['nama'].upper(),
                            hitung_usia(customer['birthday']),
                            customer['email'].lower(),
                            customer['no_hp'],
                            customer['birthday']
                        ]
                        print(tabulate([current_details], headers=headers, tablefmt="grid"))
                        break
                else:
                    print(f"Customer dengan ID {customer_id.upper()} tidak ditemukan.")
                    continue

                print("Kosongkan field jika kamu tidak ingin memperbarui informasi")
                nama = input("Masukkan nama baru (atau kosongkan): ")
                no_hp = input('Masukkan no hp baru (atau kosongkan): ')
                email = input('Masukkan email baru (atau kosongkan): ')
                birthday = input("Masukkan tanggal lahir (DD-MM-YYYY atau kosongkan): ")
                update_customer(customer_id, nama if nama else None, no_hp if no_hp else None, email if email else None, birthday if birthday else None)
            elif  pilih_menu == '4':
                customer_id = input("Masukkan ID Customer (hapus berdasarkan ID): ").upper()

                for customer in customers:
                    if customer['customer_id'] == customer_id:
                        print("\nData yang akan dihapus")
                        headers = ["Customer ID", "Nama","Usia", "Email", "Nomor HP", "Birthday"]
                        current_details = [
                            customer['customer_id'],
                            customer['nama'].upper(),
                            hitung_usia(customer['birthday']),
                            customer['email'].lower(),
                            customer['no_hp'],
                            customer['birthday']
                        ]
                        print(tabulate([current_details], headers=headers, tablefmt="grid"))
                        break
                else:
                    print(f"Customer dengan ID {customer_id.upper()} tidak ditemukan.")
                    continue
                delete_customer(customer_id)
            elif  pilih_menu == '0':
                print('Keluar dari sistem.')
                break
            else :
                print('Pilihan tidak ada dalam menu. Coba lagi.')
        except Exception as e:
            print(f"An error occurred: {e}") #ada pemebritahuan error dari sistem

main_menu()
