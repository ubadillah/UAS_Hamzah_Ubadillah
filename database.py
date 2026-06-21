import csv
import os

FILE_NAME = "penerbangan.csv"

def muat_data():
    """Memuat data dari CSV ke Hash Map (Dictionary)"""
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return {row['kode']: {'maskapai': row['maskapai'], 'rute': row['rute'], 'harga': int(row['harga'])} for row in reader}

def simpan_data(data_perjalanan):
    """Menyimpan kembali Hash Map ke file CSV"""
    with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["kode", "maskapai", "rute", "harga"])
        writer.writeheader()
        for kode, info in data_perjalanan.items():
            writer.writerow({'kode': kode, **info})