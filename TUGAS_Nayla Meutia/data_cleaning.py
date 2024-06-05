import pandas as pd

# Dataset
data = {
    'ID Penjualan': [1, 2, 3, 4, 5],
    'ID Pelanggan': [1, 2, 3, 4, 1],
    'ID Produk': [101, 102, 103, 101, 104],
    'Jumlah Terjual': [2, 3, 5, 1, 2],
    'Tanggal Pembelian': ['2023-05-01', '2023-05-02', '2023-05-03', '2023-05-04', '2023-05-05'],
    'Harga Satuan': [500000, 250000, 10000, 500000, 700000],
    'Kode Pos Pengiriman': [12345, 23456, 34567, 12345, 12345]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menghapus duplikasi berdasarkan kolom ID Penjualan
df_cleaned = df.drop_duplicates(subset=['ID Penjualan'])

# Menangani missing values, jika ada
df_cleaned.fillna(method='ffill', inplace=True)

print("Data setelah pembersihan:")
print(df_cleaned)
