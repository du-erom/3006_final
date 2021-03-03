import unittest
import housing

class TestHousing(unittest.TestCase):
    '''Test housing Housing class methods'''
    def test_Housing_init(self):
        a = housing.Housing('traditional', 'all-transactions','State', 'Delaware', 'DE', 2020, 2, 491.63, 0)
        self.assertEqual(a.hpi_type, 'traditional')
        self.assertEqual(a.hpi_flavor, 'all-transactions')
        self.assertEqual(a.level, 'State')
        self.assertEqual(a.place_name, 'Delaware')
        self.assertEqual(a.place_id, 'DE')
        self.assertEqual(a.year, 2020)
        self.assertEqual(a.period, 2)
        self.assertEqual(a.index_nsa, 491.63)
    def test_Housing_repr(self):
        a = housing.Housing('traditional', 'all-transactions','State', 'Delaware', 'DE', 2020, 2, 491.63, 0)
        self.assertEqual(repr(a), \
        'Housing (traditional, all-transactions, State, Delaware, DE, 2020, 2, 491.630000)')
class TestHousingData(unittest.TestCase):
    '''Test housing HousingData class methods'''
    def test_parse_line(self):
        l = ['traditional', 'all-transactions','Quarterly','State', 'Delaware', 'DE', 2020, 2, 491.63, 0]
        h = housing.HousingData
        a = h.parse_line(h, l)
        self.assertEqual(a.hpi_type, 'traditional')
        self.assertEqual(a.hpi_flavor, 'all-transactions')
        self.assertEqual(a.level, 'State')
        self.assertEqual(a.place_name, 'Delaware')
        self.assertEqual(a.place_id, 'DE')
        self.assertEqual(a.year, 2020)
        self.assertEqual(a.period, 2)
        self.assertEqual(a.index_nsa, 491.63)
    def test_sort_state_true(self):
        c = housing.Housing('traditional', 'all-transactions','State', 'Delaware', 'DE', 2020, 2, 491.63, 0)
        h = housing.HousingData
        a = h.sort_state(h, c)
        self.assertTrue(a)
    def test_sort_state_metro(self):
        c = housing.Housing('traditional', 'all-transactions','MSA', 'Delaware', 'DE', 2020, 2, 491.63, 0)
        h = housing.HousingData
        a = h.sort_state(h, c)
        self.assertFalse(a)
    def test_sort_state_type(self):
        c = housing.Housing('non-metro', 'all-transactions','State', 'Delaware', 'DE', 2020, 2, 491.63, 0)
        h = housing.HousingData
        a = h.sort_state(h, c)
        self.assertFalse(a)
    def test_sort_state_year(self):
        c = housing.Housing('traditional', 'all-transactions','State', 'Delaware', 'DE', 2012, 2, 491.63, 0)
        h = housing.HousingData
        a = h.sort_state(h, c)
        self.assertFalse(a)
    def test_sort_state_flavor(self):
        c = housing.Housing('traditional', 'purchase-only','State', 'Delaware', 'DE', 2012, 2, 491.63, 0)
        h = housing.HousingData
        a = h.sort_state(h, c)
        self.assertFalse(a)
    def test_sort_metro_true(self):
        c = housing.Housing('traditional', 'all-transactions', 'MSA','Chico, CA', '17020', 2018,2, 243.26,0)
        h=housing.HousingData
        a = h.sort_metro(h, c)
        self.assertTrue(a)
    def test_sort_metro_flavor(self):
        c = housing.Housing('traditional', 'purchase-only', 'MSA','Chico, CA', '17020', 2018,2, 243.26,0)
        h=housing.HousingData
        a = h.sort_metro(h, c)
        self.assertFalse(a)
    def test_sort_metro_year(self):
        c = housing.Housing('traditional', 'all-transactions', 'MSA','Chico, CA', '17020', 2014,2, 243.26,0)
        h=housing.HousingData
        a = h.sort_metro(h, c)
        self.assertFalse(a)
    def test_sort_non_metro_true(self):
        c = housing.Housing('non-metro', 'all-transactions', 'State','Alaska', 'AK', 2019, 4, 224.85,0)
        h=housing.HousingData
        a = h.sort_metro(h, c)
        self.assertTrue(a)
    def test_sort_non_metro_year(self):
        c = housing.Housing('non-metro', 'all-transactions', 'State','Alaska', 'AK', 2010, 4, 224.85,0)
        h=housing.HousingData
        a = h.sort_metro(h, c)
        self.assertFalse(a)
class TestFunctions(unittest.TestCase):
    def test_yoy_change(self):
        a = housing.Housing('non-metro', 'all-transactions', 'State','New Hampshire', 'NH', 2019, 4, 100,0)
        b =  housing.Housing('non-metro', 'all-transactions', 'State','New Hampshire', 'NH', 2020, 4, 105,0)
        l = [a, b]
        r = housing.yoy_change(l, 2020)
        self.assertEqual(r, [['New Hampshire', 'NH', 2020, 4, 105.0, 5.0, 5.0]])
if __name__ == '__main__':
    unittest.main()
