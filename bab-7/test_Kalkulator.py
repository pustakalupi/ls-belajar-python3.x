'''
done
'''
import unittest
import Kalkulator

class TestKalkulator(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("setUpClass - test dimulai")
    
    @classmethod
    def tearDownClass(self):
        print("tearDownClass - test diakhiri")
    

    def setUp(self):
        print("setUp - test dimulai")
    
    def tearDown(self):
        print("tearDown - test diakhiri")

    def test_tambah(self):
        self.assertEqual(Kalkulator.tambah(10, 6), 16)
        self.assertEqual(Kalkulator.tambah(5, -3), 2)
        self.assertEqual(Kalkulator.tambah(-3, -3), -6)
    
    def test_kurang(self):
        self.assertEqual(Kalkulator.kurang(10, 6), 4)
        self.assertEqual(Kalkulator.kurang(5, -3), 8)
        self.assertEqual(Kalkulator.kurang(-3, -3), 0)
    
    def test_kali(self):
        self.assertEqual(Kalkulator.kali(10, 6), 60)
        self.assertEqual(Kalkulator.kali(5, -3), -15)
        self.assertEqual(Kalkulator.kali(-3, -3), 9)
    
    def test_bagi(self):
        self.assertEqual(Kalkulator.bagi(5, 2), 2.5)
        self.assertEqual(Kalkulator.bagi(-8, 2), -4)
        self.assertEqual(Kalkulator.bagi(-8, -2), 4)

        self.assertRaises(ValueError, Kalkulator.bagi, 10, 0)

if __name__ == '__main__':
    unittest.main()