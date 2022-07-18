from yandiyacbm.py4dbp import Bin

class Pallets:
    standard_quarter = Bin("standard-quarter", 1200, 1200, 800, 300)
    standard_half = Bin("standard-half", 1200, 1200, 1200, 600)
    standard = Bin("standard", 1200, 1200, 2200, 1200)
    euro_quarter = Bin("euro-quarter", 800, 1200, 800, 300)
    euro_half = Bin("euro-half", 800, 1200, 1200, 600)
    euro = Bin("euro", 800, 1200, 2200, 1200)