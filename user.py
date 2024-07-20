import csv
import sqlite3
import os
import re

def create_or_connect_db():
    conn = sqlite3.connect('vouchers.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS vouchers
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT,
                 password TEXT,
                 profile TEXT,
                 used INTEGER DEFAULT 0)''')
    conn.commit()
    return conn

def insert_initial_data(conn, filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
        conn.execute("DELETE FROM vouchers")
        
        for row in reader:
            if row['Profile'] not in ['3-jam', 'Harian', 'Mingguan', 'Bulanan']:
                print(f"Data untuk username {row['Username']} tidak valid (profile tidak sesuai), dilewati.")
                continue
            
            if re.search(r'\w{3}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}', row['Comment']):
                print(f"Data untuk username {row['Username']} sudah digunakan (comment menunjukkan penggunaan), dilewati.")
                continue
            
            conn.execute("INSERT INTO vouchers (username, password, profile, used) VALUES (?, ?, ?, ?)",
                         (row['Username'], row['Password'], row['Profile'], 0))
                
    conn.commit()

def delete_invalid_data(conn):
    invalid_profiles = ['3-jam', 'Harian', 'Mingguan', 'Bulanan']
    conn.execute("DELETE FROM vouchers WHERE profile NOT IN (?, ?, ?, ?)", invalid_profiles)
    
    conn.execute("DELETE FROM vouchers WHERE used = 1")
    
    conn.commit()

def show_menu():
    print("Daftar voucher WiFi:")
    print("1. 3-jam")
    print("2. Harian")
    print("3. Mingguan")
    print("4. Bulanan")
    print("5. Keluar")

    while True:
        choice = input("Pilih salah satu profile (1-5): ")
        if choice in ['1', '2', '3', '4', '5']:
            return int(choice)
        else:
            print("Pilihan tidak tersedia. Silakan pilih 1 sampai 5.")

def show_option_menu():
    while True:
        option = input("1. Gunakan\n2. Kembali\nPilih salah satu (1-2): ")
        if option in ['1', '2']:
            return int(option)
        else:
            print("Pilihan tidak tersedia. Silakan pilih 1 atau 2.")

def get_voucher(conn, profile):
    c = conn.cursor()
    c.execute("SELECT * FROM vouchers WHERE profile = ? AND used = 0 LIMIT 1", (profile,))
    return c.fetchone()

def mark_voucher_used(conn, username):
    c = conn.cursor()
    c.execute("UPDATE vouchers SET used = 1 WHERE username = ?", (username,))
    conn.commit()

def show_continue_menu():
    while True:
        option = input("1. Kembali ke menu utama\n2. Keluar dari program\nPilih salah satu (1-2): ")
        if option in ['1', '2']:
            return int(option)
        else:
            print("Pilihan tidak tersedia. Silakan pilih 1 atau 2.")

if __name__ == "__main__":
    conn = create_or_connect_db()

    if os.path.exists('data.csv'):
        insert_initial_data(conn, 'data.csv')
        delete_invalid_data(conn)

    while True:
        choice = show_menu()

        if choice == 5:
            print("Keluar dari program.")
            break
        
        profiles = ['3-jam', 'Harian', 'Mingguan', 'Bulanan']
        selected_profile = profiles[choice - 1]

        print(f"\nAnda memilih profile: {selected_profile}")

        voucher = get_voucher(conn, selected_profile)

        if voucher:
            print(f"Username: {voucher[1]}, Password: {voucher[2]}")

            option_choice = show_option_menu()

            if option_choice == 1:
                mark_voucher_used(conn, voucher[1])
                print("Voucher berhasil digunakan.\n")
            elif option_choice == 2:
                print("Kembali ke menu utama.\n")
                continue_menu_choice = show_continue_menu()
                if continue_menu_choice == 1:
                    continue
                elif continue_menu_choice == 2:
                    break
        else:
            print("Tidak ada voucher yang tersedia untuk profile ini.\n")

        continue_menu_choice = show_continue_menu()
        if continue_menu_choice == 1:
            continue
        elif continue_menu_choice == 2:
            break

    conn.close()