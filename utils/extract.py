import requests
from bs4 import BeautifulSoup

def scrapping_data(url):
    try:
        halaman = requests.get(url, timeout=5)
        halaman.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Gagal mengakses {url}: {err}")
        return []

    try:
        konten = BeautifulSoup(halaman.text, 'html.parser')
        daftar_produk = []

        for item in konten.find_all('div', class_='collection-card'):
            ambil_teks = lambda elemen: elemen.text.strip() if elemen else 'Tidak Tersedia'

            nama = ambil_teks(item.find('h3', class_='product-title')) or 'Tanpa Nama'
            harga = ambil_teks(item.find('div', class_='price-container')) or 'Harga Tidak Diketahui'
            rating = ambil_teks(item.find('p', string=lambda x: x and 'Rating' in x)) or 'Tanpa Rating'
            warna = ambil_teks(item.find('p', string=lambda x: x and 'Colors' in x)) or 'Tanpa Info Warna'
            ukuran = ambil_teks(item.find('p', string=lambda x: x and 'Size' in x)) or 'Tanpa Info Ukuran'
            gender = ambil_teks(item.find('p', string=lambda x: x and 'Gender' in x)) or 'Tanpa Info Gender'

            info_produk = ({
                'title': nama,
                'price': harga,
                'rating': rating,
                'colors': warna,
                'size': ukuran,
                'gender': gender
            })

            daftar_produk.append(info_produk)

        return daftar_produk

    except Exception as err:
        raise Exception(f"Kesalahan saat memproses HTML: {err}")