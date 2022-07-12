import unittest
from main import rename_draw_num

class TestRename(unittest.TestCase):

    def setUp(self):
        self.draw_num = ['A354343/3',
                        '8.121.423.53',
                        '465564',
                        'B78437',
                        'C40018/123',
                        '8.10.123.54.3']
        self.re_draw_num = ['A354343[\\s_.]*3',
                            '8[\\s_.]*121[\\s_.]*423[\\s_.]*53',
                            '465564',
                            'B78437',
                            'C40018[\\s_.]*123',
                            '8[\\s_.]*10[\\s_.]*123[\\s_.]*54[\\s_.]*3']

    def test_renaming_draw_numbers(self):
        self.assertEqual(rename_draw_num(self.draw_num), self.re_draw_num)

if __name__ == '__main__':
    unittest.main()
