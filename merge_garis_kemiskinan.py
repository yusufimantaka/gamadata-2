import pandas as pd

# URL dasar folder data
base_url = 'https://raw.githubusercontent.com/yusufimantaka/gamadata-2/main/data/'
tahun_list = range(2000, 2026) 

dfs = []

for tahun in tahun_list:
    filename = f'Garis Kemiskinan Makanan (Rupiah_Kapita_Bulan) Menurut Provinsi dan Daerah, {tahun}.csv'
    # Encode spasi dan koma untuk URL
    encoded_filename = filename.replace(" ", "%20").replace(",", "%2C")
    file_url = base_url + encoded_filename
    
    try:
        df = pd.read_csv(file_url)
        df['Tahun'] = tahun  # Tambahkan kolom Tahun
        dfs.append(df)
        print(f"✅ {filename} berhasil dimuat")
    except Exception as e:
        print(f"❌ Gagal memuat {filename}: {e}")

if dfs:
    df_all = pd.concat(dfs, ignore_index=True)
    df_all.to_csv('garis_kemiskinan_makanan_mentah.csv', index=False)
    print("🎉 Semua data berhasil digabung ke 'garis_kemiskinan_makanan_mentah.csv'")
else:
    print("Tidak ada data yang berhasil dimuat.")
