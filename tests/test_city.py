# -*- coding: utf-8 -*-
import codecs
import unittest

import pygeoip
from tests.config import CITY_DB_PATH

def set_default_values(self):
    self.us_hostname = 'google.com'
    self.us_ip = '64.233.161.99'

    self.gb_hostname = 'bbc.com'
    self.gb_ip = '212.58.253.68'

    self.us_code = 'US'
    self.gb_code = 'GB'

    self.us_name = 'United States'
    self.gb_name = 'United Kingdom'

    self.us_record_data = {
        'city': 'Mountain View',
        'region_name': 'CA',
        'area_code': 650,
        'longitude': -122.05740356445312,
        'country_code3': 'USA',
        'latitude': 37.419200897216797,
        'postal_code': '94043',
        'dma_code': 807,
        'country_code': 'US',
        'country_name': 'United States',
        'time_zone': 'America/Los_Angeles'
    }

    self.gb_record_data = {
        'city': 'Tadworth',
        'region_name': 'N7',
        'area_code': 0,
        'longitude': -0.23339999999998895,
        'country_code3': 'GBR',
        'latitude': 51.283299999999997,
        'postal_code': '',
        'dma_code': 0,
        'country_code': 'GB',
        'country_name': 'United Kingdom',
        'time_zone': 'Europe/London'
    }

    self.us_region_data = {'region_name': 'CA', 'country_code': 'US'}
    self.gb_region_data = {'region_name': 'N7', 'country_code': 'GB'}

class TestGeoIPCityFunctions(unittest.TestCase):
    def setUp(self):
        set_default_values(self)
        self.gic = pygeoip.GeoIP(CITY_DB_PATH)

    def testCountryCodeByName(self):
        us_code = self.gic.country_code_by_name(self.us_hostname)
        gb_code = self.gic.country_code_by_name(self.gb_hostname)

        self.assertEqual(us_code, self.us_code)
        self.assertEqual(gb_code, self.gb_code)

    def testCountryCodeByAddr(self):
        us_code = self.gic.country_code_by_addr(self.us_ip)
        gb_code = self.gic.country_code_by_addr(self.gb_ip)

        self.assertEqual(us_code, self.us_code)
        self.assertEqual(gb_code, self.gb_code)

    def testCountryNameByName(self):
        us_name = self.gic.country_name_by_name(self.us_hostname)
        gb_name = self.gic.country_name_by_name(self.gb_hostname)

        self.assertEqual(us_name, self.us_name)
        self.assertEqual(gb_name, self.gb_name)

    def testCountryNameByAddr(self):
        us_name = self.gic.country_name_by_addr(self.us_ip)
        gb_name = self.gic.country_name_by_addr(self.gb_ip)

        self.assertEqual(us_name, self.us_name)
        self.assertEqual(gb_name, self.gb_name)

    def testRegionByName(self):
        us_region_data = self.gic.region_by_name(self.us_hostname)
        gb_region_data = self.gic.region_by_name(self.gb_hostname)

        self.assertEqual(us_region_data, self.us_region_data)
        self.assertEqual(gb_region_data, self.gb_region_data)

    def testRegionByAddr(self):
        us_region = self.gic.region_by_addr(self.us_ip)
        gb_region = self.gic.region_by_addr(self.gb_ip)

        self.assertEqual(us_region, self.us_region_data)
        self.assertEqual(gb_region, self.gb_region_data)

    def testTimeZoneByAddr(self):
        us_time_zone = self.gic.time_zone_by_addr(self.us_ip)
        gb_time_zone = self.gic.time_zone_by_addr(self.gb_ip)

        self.assertEquals(us_time_zone, 'America/Los_Angeles')
        self.assertEquals(gb_time_zone, 'Europe/London')

    def testTimeZoneByName(self):
        us_time_zone = self.gic.time_zone_by_name(self.us_hostname)
        gb_time_zone = self.gic.time_zone_by_name(self.gb_hostname)

        self.assertEquals(us_time_zone, 'America/Los_Angeles')
        self.assertEquals(gb_time_zone, 'Europe/London')

    def testRecordByAddr(self):
        equal_keys = ('city', 'region_name', 'area_code', 'country_code3',
                      'postal_code', 'dma_code', 'country_code',
                      'country_name', 'time_zone')
        almost_equal_keys = ('longitude', 'latitude')

        us_record = self.gic.record_by_addr(self.us_ip)
        for key, value in us_record.items():
            if key in equal_keys:
                test_value = self.us_record_data[key]
                self.assertEqual(value, test_value, 'Key: %s' % key)
            elif key in almost_equal_keys:
                test_value = self.us_record_data[key]
                self.assertAlmostEqual(value, test_value, 3, 'Key: %s' % key)

        gb_record = self.gic.record_by_addr(self.gb_ip)
        for key, value in gb_record.items():
            if key in equal_keys:
                test_value = self.gb_record_data[key]
                self.assertEqual(value, test_value, 'Key: %s' % key)
            elif key in almost_equal_keys:
                test_value = self.gb_record_data[key]
                self.assertAlmostEqual(value, test_value, 3, 'Key: %s' % key)

    def testRecordByName(self):
        equal_keys = ('city', 'region_name', 'area_code', 'country_code3',
                      'postal_code', 'dma_code', 'country_code',
                      'country_name', 'time_zone')
        almost_equal_keys = ('longitude', 'latitude')

        us_record = self.gic.record_by_name(self.us_hostname)
        for key, value in us_record.items():
            if key in equal_keys:
                test_value = self.us_record_data[key]
                self.assertEqual(value, test_value, 'Key: %s' % key)
            elif key in almost_equal_keys:
                test_value = self.us_record_data[key]
                self.assertAlmostEqual(value, test_value, 3, 'Key: %s' % key)

        gb_record = self.gic.record_by_name(self.gb_hostname)
        for key, value in gb_record.items():
            if key in equal_keys:
                test_value = self.gb_record_data[key]
                self.assertEqual(value, test_value, 'Key: %s' % key)
            elif key in almost_equal_keys:
                test_value = self.gb_record_data[key]
                self.assertAlmostEqual(value, test_value, 3, 'Key: %s' % key)


class TestGeoIPCityFunctionsWithPreloadedContent(TestGeoIPCityFunctions):
    def setUp(self):
        set_default_values(self)
        with codecs.open(CITY_DB_PATH, 'rb', 'latin_1') as db_file:
            contents = db_file.read()

        self.gic = pygeoip.GeoIP(db_contents=contents)

    def test_filename_or_db_contents_must_be_specified(self):
        try:
            pygeoip.GeoIP()
        except ValueError, err:
            assert str(err) == 'Either filename or db_contents must be specified'
            return
        assert False, "Should not have gotten this far"
