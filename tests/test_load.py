import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from utils.load import load_to_csv, load_to_google_sheets, load_to_postgresql

class UjiPenyimpananData(unittest.TestCase):

    @patch('utils.load.pd.DataFrame.to_csv')
    def test_csv_load(self, mock_csv):
        """Verifikasi bahwa fungsi penyimpanan ke CSV memanggil metode to_csv dengan argumen tepat."""
        data = pd.DataFrame({
            'title': ['Produk 1', 'Produk 2'],
            'price': [10000, 20000],
            'rating': [4.5, 5.0]
        })

        load_to_csv(data, 'uji.csv')
        mock_csv.assert_called_once_with('uji.csv', index=False)

    @patch('utils.load.build')
    @patch('utils.load.Credentials.from_service_account_file')
    def test_google_sheets_load(self, mock_kredensial, mock_build_service):
        """Pastikan fungsi simpan ke Google Sheets memanggil metode update dari API dengan benar."""
        data = pd.DataFrame({
            'title': ['Produk 1', 'Produk 2'],
            'price': [10000, 20000],
            'rating': [4.5, 5.0]
        })

        mock_kredensial.return_value = MagicMock()
        test_service = MagicMock()
        mock_build_service.return_value = test_service

        load_to_google_sheets(data, 'spreadsheet_id', 'Sheet1!A2')
        test_service.spreadsheets.return_value.values.return_value.update.assert_called_once()

    @patch('utils.load.create_engine')
    @patch('utils.load.pd.DataFrame.to_sql')
    def test_postgresql_load_sukses(self, mock_to_sql, mock_create_engine):
        """Pastikan fungsi PostgreSQL memanggil to_sql dengan benar pada skenario sukses."""
        data = pd.DataFrame({
            'title': ['Produk A', 'Produk B'],
            'price': [10000, 20000],
            'rating': [4.0, 5.0]
        })

        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        load_to_postgresql(data, nama_tabel="produk_uji")

        mock_create_engine.assert_called_once()
        mock_to_sql.assert_called_once_with(
            "produk_uji", mock_engine, if_exists="replace", index=False
        )

if __name__ == '__main__':
    unittest.main()