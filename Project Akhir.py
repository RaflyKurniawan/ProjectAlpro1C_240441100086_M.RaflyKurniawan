destinasi = {
    "Jakarta - Bali": {
        "ekonomi": 1000000,
        "bisnis": 2000000,
        "first_class": 5000000
    },
    "Jakarta - Surabaya": {
        "ekonomi": 500000,
        "bisnis": 1000000,
        "first_class": 2500000
    },
    "Jakarta - Medan": {
        "ekonomi": 750000,
        "bisnis": 1500000,
        "first_class": 3500000
    },
    "Jakarta - Yogyakarta": {
        "ekonomi": 600000,
        "bisnis": 1200000,
        "first_class": 3000000
    },
    "Jakarta - Makassar": {
        "ekonomi": 850000,
        "bisnis": 1700000,
        "first_class": 4000000
    }
}

waktu_penerbangan = {
    "Jakarta - Bali": ["Pagi (07:00)", "Siang (12:00)", "Malam (18:00)"],
    "Jakarta - Surabaya": ["Pagi (06:00)", "Siang (13:00)", "Malam (19:00)"],
    "Jakarta - Medan": ["Pagi (08:00)", "Siang (14:00)", "Malam (20:00)"],
    "Jakarta - Yogyakarta": ["Pagi (07:30)", "Siang (13:30)", "Malam (18:30)"],
    "Jakarta - Makassar": ["Pagi (06:30)", "Siang (14:30)", "Malam (21:00)"]
}

riwayat_pembelian = []

def tampilkan_destinasi():
    print("\nDaftar Tujuan Penerbangan:")
    for no, rute in enumerate(destinasi.keys(), 1):
        print(f"{no}. {rute}")

def tampilkan_waktu_penerbangan(rute_terpilih):
    print(f"\nPilih waktu penerbangan untuk {rute_terpilih}:")
    for no, waktu in enumerate(waktu_penerbangan[rute_terpilih], 1):
        print(f"{no}. {waktu}")

def tampilkan_kelas():
    print("\nPilih kelas penerbangan:")
    print("1. Ekonomi")
    print("2. Bisnis")
    print("3. First Class")

def hitung_total(harga_per_orang, jumlah_tiket, diskon_tambahan=0):
    total = harga_per_orang * jumlah_tiket
    if jumlah_tiket > 5:
        diskon = 0.1 * total
        total -= diskon
        print(f"Diskon 10% untuk pembelian lebih dari 5 tiket! Anda menghemat Rp {diskon:,.0f}")
    
    if diskon_tambahan > 0:
        total -= diskon_tambahan
        print(f"Diskon usia diterapkan! Anda menghemat Rp {diskon_tambahan:,.0f}")
    
    pajak = total * 0.05
    total += pajak
    print(f"Pajak 5% diterapkan: Rp {pajak:,.0f}")
    
    biaya_admin = 50000
    total += biaya_admin
    print(f"Biaya administrasi: Rp {biaya_admin:,.0f}")

    return total

def tampilkan_riwayat():
    if not riwayat_pembelian:
        print("\nBelum ada riwayat pembelian.")
    else:
        print("\nRiwayat Pembelian:")
        for no, pembelian in enumerate(riwayat_pembelian, 1):
            print(f"{no}. {pembelian}")

def batalkan_tiket():
    if not riwayat_pembelian:
        print("\nTidak ada tiket yang dapat dibatalkan.")
        return
    
    tampilkan_riwayat()
    
    pilihan_batal = input("\nPilih nomor pembelian yang ingin dibatalkan (0 untuk kembali): ")
    
    if pilihan_batal.isdigit():
        pilihan_batal = int(pilihan_batal)
        if pilihan_batal == 0:
            return
        elif 1 <= pilihan_batal <= len(riwayat_pembelian):
            tiket_batal = riwayat_pembelian.pop(pilihan_batal - 1)
            print(f"\nTiket berikut telah dibatalkan:\n{tiket_batal}")
        else:
            print("Nomor pilihan tidak valid. Harap pilih nomor yang ada.")
    else:
        print("Input tidak valid. Harap masukkan angka yang benar.")

def update_tiket():
    if not riwayat_pembelian:
        print("\nTidak ada tiket yang dapat diperbarui.")
        return
    
    tampilkan_riwayat()
    pilihan_update = input("\nPilih nomor pembelian yang ingin diperbarui (0 untuk kembali): ")

    if pilihan_update.isdigit():
        pilihan_update = int(pilihan_update)
        if pilihan_update == 0:
            return
        elif 1 <= pilihan_update <= len(riwayat_pembelian):
            tiket_update = riwayat_pembelian[pilihan_update - 1]
            print(f"\nTiket yang dipilih untuk diperbarui:\n{tiket_update}")
            
            print("\nApa yang ingin diubah?")
            print("1. Tujuan")
            print("2. Waktu Penerbangan")
            print("3. Kelas Penerbangan")
            print("4. Jumlah Tiket")
            print("5. Kembali")
            
            pilihan_perubahan = input("Pilih perubahan (1-5): ")

            if pilihan_perubahan == "1":
                tampilkan_destinasi()
                destinasi_baru = input("Pilih tujuan baru (1-5): ")
                if destinasi_baru.isdigit() and 1 <= int(destinasi_baru) <= 5:
                    tiket_update["tujuan"] = list(destinasi.keys())[int(destinasi_baru) - 1]
                else:
                    print("Pilihan tujuan tidak valid.")
            
            elif pilihan_perubahan == "2":
                tampilkan_waktu_penerbangan(tiket_update["tujuan"])
                waktu_pilih = input("Pilih waktu baru (1-3): ")
                if waktu_pilih.isdigit() and 1 <= int(waktu_pilih) <= 3:
                    tiket_update["waktu"] = waktu_penerbangan[tiket_update["tujuan"]][int(waktu_pilih) - 1]
                else:
                    print("Pilihan waktu tidak valid.")
            
            elif pilihan_perubahan == "3":
                print("\nPilih kelas penerbangan baru:")
                print("1. Ekonomi")
                print("2. Bisnis")
                print("3. First Class")
                kelas_penerbangan = input("Pilih kelas penerbangan baru (1-3): ")
                if kelas_penerbangan == "1":
                    tiket_update["kelas"] = "ekonomi"
                elif kelas_penerbangan == "2":
                    tiket_update["kelas"] = "bisnis"
                    
                elif kelas_penerbangan == "3":
                    tiket_update["kelas"] = "first_class"
                else:
                    print("Pilihan kelas tidak valid.")
            
            elif pilihan_perubahan == "4":
                jumlah_tiket = input("Masukkan jumlah tiket baru: ")
                if jumlah_tiket.isdigit() and int(jumlah_tiket) > 0:
                    tiket_update["jumlah_tiket"] = int(jumlah_tiket)
                else:
                    print("Jumlah tiket tidak valid.")
            
            elif pilihan_perubahan == "5":
                return
            else:
                print("Pilihan tidak valid.")
            
            # Perhitungan ulang total biaya
            harga_per_tiket = destinasi[tiket_update["tujuan"]][tiket_update["kelas"]]
            diskon_usia = 0  # Diskon usia hanya diterapkan saat pembelian awal
            tiket_update["total"] = hitung_total(harga_per_tiket, tiket_update["jumlah_tiket"], diskon_usia)

            riwayat_pembelian[pilihan_update - 1] = tiket_update
            print(f"\nTiket yang telah diperbarui:\n{tiket_update}")
        else:
            print("Nomor pilihan tidak valid.")
    else:
        print("Input tidak valid.")

def menu_utama():
    while True:
        print("\n===== Menu Utama =====")
        print("1. Beli Tiket Pesawat")
        print("2. Lihat Daftar Tujuan")
        print("3. Lihat Waktu Penerbangan")
        print("4. Lihat Kelas Penerbangan")
        print("5. Lihat Riwayat Pembelian")
        print("6. Batalkan Tiket")
        print("7. Update Tiket")
        print("8. Keluar")
        
        pilihan = input("Pilih menu (1-8): ")
        
        if pilihan == "1":
            beli_tiket()
        elif pilihan == "2":
            tampilkan_destinasi()
        elif pilihan == "3":
            rute = input("\nMasukkan nomor tujuan untuk melihat waktu penerbangan: ")
            if rute.isdigit() and 1 <= int(rute) <= 5:
                rute_terpilih = list(destinasi.keys())[int(rute) - 1]
                tampilkan_waktu_penerbangan(rute_terpilih)
            else:
                print("Pilihan tidak valid.")
        elif pilihan == "4":
            tampilkan_kelas()
        elif pilihan == "5":
            tampilkan_riwayat()
        elif pilihan == "6":
            batalkan_tiket()
        elif pilihan == "7":
            update_tiket()
        elif pilihan == "8":
            print("Terima kasih telah menggunakan sistem kami. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Harap masukkan angka antara 1 hingga 8.")

def beli_tiket():
    print("\nSelamat datang di Sistem Penjualan Tiket Pesawat!")
    
    while True:
        tampilkan_destinasi()

        pilihan = input("\nPilih tujuan penerbangan (1-5): ")
        if pilihan not in ["1", "2", "3", "4", "5"]:
            print("Pilihan tidak valid. Harap masukkan angka antara 1 hingga 5.")
            continue
        rute_terpilih = list(destinasi.keys())[int(pilihan) - 1]
        tampilkan_waktu_penerbangan(rute_terpilih)

        waktu_pilih = input("\nPilih waktu penerbangan (1-3): ")
        if waktu_pilih not in ["1", "2", "3"]:
            print("Pilihan waktu tidak valid. Harap masukkan angka antara 1 hingga 3.")
            continue

        waktu_terpilih = waktu_penerbangan[rute_terpilih][int(waktu_pilih) - 1]

        tampilkan_kelas()
        kelas_penerbangan = input("\nPilih kelas penerbangan (1-3): ")
        if kelas_penerbangan == "1":
            kelas = "ekonomi"
        elif kelas_penerbangan == "2":
            kelas = "bisnis"
        elif kelas_penerbangan == "3":
            kelas = "first_class"
        else:
            print("Pilihan kelas tidak valid. Harap masukkan angka antara 1 hingga 3.")
            continue

        harga = destinasi[rute_terpilih][kelas]
        jumlah_tiket = input(f"Berapa tiket yang ingin dibeli untuk {rute_terpilih} ({waktu_terpilih}) dengan kelas {kelas.capitalize()}? ")
        if not jumlah_tiket.isdigit() or int(jumlah_tiket) <= 0:
            print("Jumlah tiket tidak valid. Harap masukkan angka yang lebih besar dari 0.")
            continue
        jumlah_tiket = int(jumlah_tiket)
        
        usia = input("Masukkan usia pembeli: ")
        if not usia.isdigit() or int(usia) <= 0:
            print("Usia tidak valid. Harap masukkan angka yang valid.")
            continue
        usia = int(usia)
        diskon_usia = 0
        if usia < 12:
            diskon_usia = 0.2 * harga * jumlah_tiket
            print(f"Diskon anak-anak 20% diterapkan! Anda menghemat Rp {diskon_usia:,.0f}")
        elif usia > 60:
            diskon_usia = 0.2 * harga * jumlah_tiket
            print(f"Diskon lansia 20% diterapkan! Anda menghemat Rp {diskon_usia:,.0f}")
        
        total_biaya = hitung_total(harga, jumlah_tiket, diskon_usia)
        print(f"\nRincian Pembelian:") 
        print(f"Tujuan: {rute_terpilih}")
        print(f"Waktu Penerbangan: {waktu_terpilih}")
        print(f"Kelas: {kelas.capitalize()}")
        print(f"Jumlah Tiket: {jumlah_tiket}")
        print(f"Total Biaya: Rp {total_biaya:,.0f}")
        
        riwayat_pembelian.append({
            "tujuan": rute_terpilih,
            "waktu": waktu_terpilih,
            "kelas": kelas,
            "jumlah_tiket": jumlah_tiket,
            "total": total_biaya
        })
        
        lagi = input("\nApakah Anda ingin membeli tiket lagi? (iya/tidak): ").lower()
        if lagi != 'iya':
            break
menu_utama()