import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import seaborn as sns

# Data
pelanggan_data = {
    'ID Pelanggan': [1, 2, 3],
    'Nama': ['Alice', 'Bob', 'Charlie'],
    'Usia': [35, 28, 40],
    'Kota': ['Jakarta', 'Bandung', 'Surabaya']
}

produk_data = {
    'ID Produk': [101, 102, 103],
    'Nama Produk': ['Laptop', 'T-shirt', 'Snack'],
    'Kategori': ['Elektronik', 'Fashion', 'Makanan']
}

penjualan_data = {
    'ID Penjualan': [1, 2, 3],
    'ID Pelanggan': [1, 2, 3],
    'ID Produk': [101, 102, 103],
    'Jumlah Terjual': [2, 3, 5]
}

# Create DataFrames
df_pelanggan = pd.DataFrame(pelanggan_data)
df_produk = pd.DataFrame(produk_data)
df_penjualan = pd.DataFrame(penjualan_data)

# Histogram Usia Pelanggan
plt.figure(figsize=(8, 6))
sns.histplot(df_pelanggan['Usia'], bins=10, kde=True, color='skyblue')
plt.title('Histogram Usia Pelanggan')
plt.xlabel('Usia')
plt.ylabel('Frekuensi')
plt.show()

# Scatterplot Penjualan vs Usia Pelanggan
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_pelanggan['Usia'], y=df_penjualan['Jumlah Terjual'], color='orange')
plt.title('Scatterplot Penjualan vs Usia Pelanggan')
plt.xlabel('Usia Pelanggan')
plt.ylabel('Jumlah Terjual')
plt.show()

# Venn Diagram Kategori Produk
elektronik_set = set(df_produk[df_produk['Kategori'] == 'Elektronik']['ID Produk'])
fashion_set = set(df_produk[df_produk['Kategori'] == 'Fashion']['ID Produk'])
venn2([elektronik_set, fashion_set], ('Elektronik', 'Fashion'))
plt.title('Venn Diagram Kategori Produk')
plt.show()

# Pie Chart Penjualan Berdasarkan Kategori Produk
total_penjualan_per_kategori = df_penjualan.merge(df_produk, on='ID Produk').groupby('Kategori')['Jumlah Terjual'].sum()
plt.figure(figsize=(8, 6))
plt.pie(total_penjualan_per_kategori, labels=total_penjualan_per_kategori.index, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart Penjualan Berdasarkan Kategori Produk')
plt.axis('equal')
plt.show()

# Bar Chart Total Penjualan Berdasarkan Kota
penjualan_per_kota = df_penjualan.merge(df_pelanggan, on='ID Pelanggan').groupby('Kota')['Jumlah Terjual'].sum()
plt.figure(figsize=(10, 6))
penjualan_per_kota.plot(kind='bar', color='green')
plt.title('Bar Chart Total Penjualan Berdasarkan Kota')
plt.xlabel('Kota')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=45)
plt.show()
