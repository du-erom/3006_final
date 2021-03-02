#
# Author: Ben Hersh
# Class: Comp 3006 Winter 2021
#

import unittest
from collections import namedtuple
import processors
from processors import FipsData
import logging

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(funcName)s] %(message)s")
stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)
root_logger.addHandler(stdout_handler)

class TestProcessors(unittest.TestCase):

    def test_census_cbsa_selection(self):
        TestData = namedtuple("TestData", ["cbsa", "central_flag", "expected_results"])
        test_file = "../data/test/census_cbsa.csv"
        test_dataset = [TestData(10100, True, [FipsData(46, 13)]),
                        TestData(10100, False, [FipsData(46, 45)]),
                        TestData(12060, True, [FipsData(13, 57),
                                               FipsData(13, 63),
                                               FipsData(13, 67),
                                               FipsData(13, 77),
                                               FipsData(13, 89),
                                               FipsData(13, 97),
                                               FipsData(13, 113),
                                               FipsData(13, 117),
                                               FipsData(13, 121),
                                               FipsData(13, 135),
                                               FipsData(13, 151),
                                               FipsData(13, 217),
                                               FipsData(13, 223),
                                               FipsData(13, 247),
                                               FipsData(13, 255),
                                               FipsData(13, 297)])
                     ]
        test_df = processors.load_data(test_file)
        for test_data in test_dataset:
            with self.subTest(f"{test_data.cbsa} : {test_data.central_flag}"):
                result = processors.find_fips_for_cbsa(test_data.cbsa, test_data.central_flag, test_df)
                self.assertEqual(len(test_data.expected_results), len(result))
                for expected in test_data.expected_results:
                    self.assertIn(expected, result)

    def test_census_population(self):
        TestData = namedtuple("TestData", ["fips_selectors", "expected_population"])
        test_file = "../data/test/census_population_ala.csv"
        test_dataset = [TestData([FipsData(1, 3)], 223234),
                        TestData([FipsData(1,3),
                                  FipsData(1, 5)], 247920),
                        TestData([FipsData(1, 51),
                                  FipsData(1, 53),
                                  FipsData(1, 55),
                                  FipsData(1, 57),
                                  FipsData(1, 59)], 267774)]
        test_df = processors.load_data(test_file)
        for index, test_data in enumerate(test_dataset):
            with self.subTest(f"test index {index}"):
                result = processors.population_by_fips(test_data.fips_selectors, test_df)
                self.assertEqual(test_data.expected_population, result)

    def test_group_covid_by_fips(self):
        test_file = "../data/test/us-counties-nh.csv"
        TestCovidData = namedtuple("CovidData", ["date", "total_cases"])
        TestData = namedtuple("TestData", ["fips_selector", "expected_series"])
        test_dataset = [TestData([FipsData(33, 1)], [TestCovidData('2020-03-21', 3),
                                                     TestCovidData('2020-03-22', 4),
                                                     TestCovidData('2020-03-23', 7),
                                                     TestCovidData('2020-03-24', 7),
                                                     TestCovidData('2020-03-25', 8)]),
                        TestData([FipsData(33, 1),
                                  FipsData(33, 9)], [TestCovidData('2020-03-21', 17),
                                                     TestCovidData('2020-03-22', 19),
                                                     TestCovidData('2020-03-23', 27),
                                                     TestCovidData('2020-03-24', 28),
                                                     TestCovidData('2020-03-25', 30)
                                                     ]),

                        TestData([FipsData(33, 1),
                                  FipsData(33, 9),
                                  FipsData(33, 15)], [TestCovidData('2020-03-21', 42),
                                                      TestCovidData('2020-03-22', 47),
                                                      TestCovidData('2020-03-23', 65),
                                                      TestCovidData('2020-03-24', 70),
                                                      TestCovidData('2020-03-25', 86)
                                                      ])
                        ]
        test_df = processors.load_data(test_file)
        for index, test_data in enumerate(test_dataset):
            with self.subTest(f"test index {index}"):
                result_df = processors.aggregate_covid_cases_by_group(test_data.fips_selector, ["date"], test_df)
                self.assertEqual(len(test_data.expected_series), len(result_df))
                for expected_records in test_data.expected_series:
                    result = result_df[result_df["date"] == expected_records.date]
                    self.assertEqual(1, len(result))

    def test_covid_fips(self):
        TestData = namedtuple("TestData", ["fips", "expected_value"])
        test_dataset = [TestData(FipsData(33, 15), 33015),
                        TestData(FipsData(8, 31), 8031),
                        TestData(FipsData(6, 59), 6059),
                        TestData(FipsData(53, 67), 53067)]
        for test_data in test_dataset:
            covid_fips_id = processors.covid_fips(test_data.fips)
            self.assertEqual(test_data.expected_value, covid_fips_id)
