import unittest
from unittest.mock import patch, MagicMock
from utils.extract import scrapping_data

class UjiEkstraksi(unittest.TestCase):

    @patch('utils.extract.requests.get')
    def test_berhasil_scrape_data(self, mock_get):
        """Memastikan data berhasil di-scrape dari halaman valid."""
        url = "https://fashion-studio.dicoding.dev/"

        test_response = MagicMock()
        test_response.status_code = 200
        test_response.text = """
        <html>
            <body>
                <div class="collection-card">
                    <h3 class="product-title">Tes Produk</h3>
                    <div class="price-container">$10</div>
                    <p>Rating: 5 stars</p>
                    <p>Colors: Red, Blue</p>
                    <p>Size: M, L</p>
                    <p>Gender: Unisex</p>
                </div>
            </body>
        </html>
        """
        mock_get.return_value = test_response

        hasil = scrapping_data(url)

        self.assertIsInstance(hasil, list)
        self.assertGreater(len(hasil), 0)
        self.assertIn('title', hasil[0])
        self.assertEqual(hasil[0]['title'], 'Tes Produk')

    @patch('utils.extract.requests.get')
    def test_gagal_scrape_karena_error(self, mock_get):
        """Menguji kondisi saat permintaan HTTP gagal (contoh: 404)."""
        url = "https://fashion-studio.dicoding.dev/"

        error_response = MagicMock()
        error_response.status_code = 404
        error_response.raise_for_status.side_effect = Exception("404 Client Error")
        mock_get.return_value = error_response

        with self.assertRaises(Exception) as context:
            scrapping_data(url)

        self.assertIn("404 Client Error", str(context.exception))

if __name__ == '__main__':
    unittest.main()
