# Tabel Pelanggan
pelanggan_data = {
    'ID Pelanggan': [1, 2, 3],
    'Nama': ['Alice', 'Bob', 'Charlie'],
    'Usia': [35, 28, 40],
    'Kota': ['Jakarta', 'Bandung', 'Surabaya']
}

# Tabel Produk
produk_data = {
    'ID Produk': [101, 102, 103],
    'Nama Produk': ['Laptop', 'T-shirt', 'Snack'],
    'Kategori': ['Elektronik', 'Fashion', 'Makanan']
}

# Tabel Penjualan
penjualan_data = {
    'ID Penjualan': [1, 2, 3],
    'ID Pelanggan': [1, 2, 3],
    'ID Produk': [101, 102, 103],
    'Jumlah Terjual': [2, 3, 5]
}

import pandas as pd

# Membuat DataFrame dari data
df_pelanggan = pd.DataFrame(pelanggan_data)
df_produk = pd.DataFrame(produk_data)
df_penjualan = pd.DataFrame(penjualan_data)

# 1. Pelanggan tertua yang melakukan pembelian
pelanggan_tertua = df_pelanggan.loc[df_pelanggan['Usia'].idxmax(), 'Nama']
print("Pelanggan tertua yang melakukan pembelian:", pelanggan_tertua)

# 2. Total penjualan produk dalam kategori Elektronik
total_penjualan_elektronik = df_penjualan.merge(df_produk[df_produk['Kategori'] == 'Elektronik'], on='ID Produk')['Jumlah Terjual'].sum()
print("Total penjualan produk dalam kategori Elektronik:", total_penjualan_elektronik)

# 3. Nama produk yang paling banyak terjual
produk_terlaris_id = df_penjualan.groupby('ID Produk')['Jumlah Terjual'].sum().idxmax()
nama_produk_terlaris = df_produk.loc[df_produk['ID Produk'] == produk_terlaris_id, 'Nama Produk'].values[0]
print("Nama produk yang paling banyak terjual:", nama_produk_terlaris)
