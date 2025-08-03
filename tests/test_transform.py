import unittest
import pandas as pd
from utils.transform import transform_data

class UjiTransformasi(unittest.TestCase):

    def test_transformasi_data(self):
        """Mengonfirmasi bahwa data produk yang benar diubah menjadi DataFrame bersih."""
        data_produk = [
            {
                'title': 'Product A', 'price': '10000', 'rating': '4.5', 'colors': '3', 'size': 'M','gender': 'Men'
            },
            {
                'title': 'Product B','price': '20000','rating': '5.0','colors': '3','size': 'L','gender': 'Women'
            }
        ]

        hasil_df = transform_data(data_produk)

        self.assertEqual(len(hasil_df), 2)
        self.assertIn('price', hasil_df.columns)
        self.assertIn('rating', hasil_df.columns)
        self.assertIn('timestamp', hasil_df.columns)
        self.assertGreater(hasil_df['price'].iloc[0], 0)
        self.assertGreater(hasil_df['rating'].iloc[0], 0)

    def test_data_dengan_harga_tidak_valid(self):
        """Pastikan data dengan format harga salah tidak lolos dalam hasil akhir."""
        data_produk = [
            {
                'title': 'Product Error','price': 'harga_tidak_valid','rating': '4.5','colors': '5','size': 'M','gender': 'Men'
            }
        ]

        hasil_df = transform_data(data_produk)

        self.assertEqual(len(hasil_df), 0)

if __name__ == '__main__':
    unittest.main()
