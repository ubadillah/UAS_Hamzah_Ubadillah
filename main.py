from database import muat_data, simpan_data

# Queue Sederhana untuk Antrean Tiket
antrean_pembayaran = []

def tampilkan_dan_sort(data):
    """Menampilkan data yang diurutkan berdasar harga termurah (Sorting)"""
    if not data:
        return print("\n[!] Data kosong.")
    
    # Sorting menggunakan fungsi bawaan sorted (Tersirat menggunakan Timsort)
    data_urut = sorted(data.items(), key=lambda x: x[1]['harga'])
    
    print(f"\n{'Kode':<6} | {'Maskapai':<12} | {'Rute':<20} | {'Harga'}")
    print("-" * 55)
    for kode, info in data_urut:
        print(f"{kode:<6} | {info['maskapai']:<12} | {info['rute']:<20} | Rp {info['harga']}")

def main():
    while True:
        data = muat_data()
        print("\n=== TIKET PESAWAT ===")
        print("1. Tambah Rute (Create)     5. Hapus Rute (Delete)")
        print("2. Lihat & Sort (Read)      6. Pesan Tiket (Queue Enqueue)")
        print("3. Cari Rute (Searching)    7. Bayar Tiket (Queue Dequeue)")
        print("4. Edit Rute (Update)       8. Keluar")
        
        pilih = input("Pilih menu: ").strip()
        
        if pilih == '1':
            kode = input("Kode Baru: ").upper()
            if kode in data: print("[!] Kode sudah ada."); continue
            data[kode] = {
                'maskapai': input("Maskapai: "),
                'rute': input("Rute (Asal-Tujuan): "),
                'harga': int(input("Harga: "))
            }
            simpan_data(data)
            print("[+] Berhasil ditambahkan.")
            
        elif pilih == '2':
            tampilkan_dan_sort(data)
            
        elif pilih == '3':
            kode = input("Masukkan Kode yang dicari: ").upper()
            if kode in data:
                print(f"[+] Ditemukan! Maskapai: {data[kode]['maskapai']}, Rute: {data[kode]['rute']}, Harga: Rp {data[kode]['harga']}")
            else:
                print("[-] Kode tidak ditemukan.")
                
        elif pilih == '4':
            kode = input("Masukkan Kode yang diubah: ").upper()
            if kode in data:
                data[kode]['maskapai'] = input("Maskapai Baru: ")
                data[kode]['rute'] = input("Rute Baru: ")
                data[kode]['harga'] = int(input("Harga Baru: "))
                simpan_data(data)
                print("[+] Berhasil diperbarui.")
            else:
                print("[-] Kode tidak ditemukan.")
                
        elif pilih == '5':
            kode = input("Masukkan Kode yang dihapus: ").upper()
            if kode in data:
                del data[kode]
                simpan_data(data)
                print("[+] Berhasil dihapus.")
            else:
                print("[-] Kode tidak ditemukan.")
                
        elif pilih == '6':
            kode = input("Kode Penerbangan yang dipesan: ").upper()
            if kode in data:
                nama = input("Nama Penumpang: ")
                antrean_pembayaran.append({'nama': nama, 'kode': kode})
                print(f"[+] {nama} masuk ke antrean.")
            else:
                print("[-] Rute tidak tersedia.")
                
        elif pilih == '7':
            if antrean_pembayaran:
                proses = antrean_pembayaran.pop(0) # FIFO Queue: mengambil index pertama
                print(f"[+] Tiket berhasil diterbitkan untuk {proses['nama']} (Penerbangan {proses['kode']})!")
            else:
                print("[!] Tidak ada antrean pembayaran.")
                
        elif pilih == '8':
            print("Program selesai.")
            break

if __name__ == "__main__":
    main()