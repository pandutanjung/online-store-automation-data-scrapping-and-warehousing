from utils.extract import scrapping_data
from utils.transform import transform_data
from utils.load import load_to_csv, load_to_google_sheets, load_to_postgresql

def jalankan_pipeline():
    LINK_UTAMA = 'https://fashion-studio.dicoding.dev/'
    kumpulan_produk = []

    # Iterasi untuk mengambil data dari 50 halaman
    for halaman in range(1, 51):
        tautan = LINK_UTAMA if halaman == 1 else f"{LINK_UTAMA}page{halaman}"
        print(f"Mengambil data dari halaman {halaman}: {tautan}")
        try:
            hasil_scrape = scrapping_data(tautan)
            kumpulan_produk.extend(hasil_scrape)
        except Exception as kesalahan:
            print(f"Scraping gagal pada halaman {halaman}: {kesalahan}")

    # Transformasi data mentah menjadi data siap olah
    data_bersih = transform_data(kumpulan_produk)

    # Load ke file CSV lokal
    load_to_csv(data_bersih)

    # Load ke database PostgreSQL
    load_to_postgresql(data_bersih)

    # Load ke Google Sheets
    load_to_google_sheets(data_bersih,'1d8mDuUK3d-u-78MeC9knc0sKdkbwb4Z7EgJMbextm3M','Sheet1!A2')

if __name__ == '__main__':
    jalankan_pipeline()