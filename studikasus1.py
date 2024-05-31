import pandas as pd

# Membuat dataframe dari data yang diberikan
data = {
    'HARI': ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'],
    'DATANG': [2, 3, 4, 1, 2, 5, 2],
    'BIAYA': [30000*2, 35000*3, 25000*4, 15000*1, 20000*2, 30000*5, 35000*2],
    'MAHASISWA': ['Ani', 'Budi', 'Jono', 'Lono', 'Joni', 'Ani', 'Budi']
}
df = pd.DataFrame(data)

# a) Berapa rata-rata mahasiswa datang pada minggu ini?
average_datang = df['DATANG'].mean()

# b) Kapan biaya tertinggi terjadi?
highest_biaya_day = df[df['BIAYA'] == df['BIAYA'].max()]['HARI'].values[0]

# c) Hari apa biaya lebih dari 110000?
days_biaya_above_110000 = df[df['BIAYA'] > 110000]['HARI'].tolist()

# d) Siapa yang paling banyak datang ke kampus?
most_frequent_mahasiswa = df['MAHASISWA'].mode().values[0]

# e) Siapa yang datang pada hari minggu?
mahasiswa_minggu = df[df['HARI'] == 'Minggu']['MAHASISWA'].values[0]

# f) Berapa biaya tertinggi dan terendah?
highest_biaya = df['BIAYA'].max()
lowest_biaya = df['BIAYA'].min()

# g) Berapa frekuensi datang tertinggi dan terendah?
highest_datang = df['DATANG'].max()
lowest_datang = df['DATANG'].min()

# Menampilkan hasil
print(f"a) Rata-rata mahasiswa datang pada minggu ini: {average_datang}")
print(f"b) Biaya tertinggi terjadi pada hari: {highest_biaya_day}")
print(f"c) Hari dengan biaya lebih dari 110000: {days_biaya_above_110000}")
print(f"d) Mahasiswa yang paling banyak datang ke kampus: {most_frequent_mahasiswa}")
print(f"e) Mahasiswa yang datang pada hari minggu: {mahasiswa_minggu}")
print(f"f) Biaya tertinggi: {highest_biaya}, Biaya terendah: {lowest_biaya}")
print(f"g) Frekuensi datang tertinggi: {highest_datang}, Frekuensi datang terendah: {lowest_datang}")
