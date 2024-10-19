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
    while len(id_str)<4:
        id_str = '0' + id_str
    return f"MYSPA{id_str}"

#fungsi untuk validasi email
def is_valid_email(email):
    return '@' in email and '.' in email

#fungsi untuk validasi no hp
def is_valid_nohp(no_hp):
    return len(no_hp)<=12 and no_hp.isdigit()

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
        table = [[c['customer_id'], c['nama'], c['usia'], c['no_hp'], c['email'], c['birthday']] for c in customers]
        print(tabulate(table, headers, tablefmt="grid"))

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
    add_dummy_data()
    while True:
        print('MySPA CRM System')
        print('1. Lihat Semua Data Customer')
        print('2. Tambah Customer Baru')
        print('3. Update Data Customer')
        print('4. Hapus Data Customer')
        print('0. Keluar')

        pilih_menu = input('Masukkan nomor menu: ')

        try:
            if pilih_menu == '1':
                read_data_customer()
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
                
                birtday = input('Masukkan TTL (DD-MM-YYYY): ')
                create_data_customer(nama,no_hp,email,birtday)
                print(f'Data pelanggan {nama} berhasil ditambahkan.')
            elif  pilih_menu == '3':
                print('Menu 3')
            elif  pilih_menu == '4':
                print('Menu 4')
            elif  pilih_menu == '0':
                print('Keluar dari sistem.')
                break
            else :
                print('Pilihan tidak ada dalam menu. Coba lagi.')
        except Exception as e:
            print(f"An error occurred: {e}") #ada error dari sistem

main_menu()
