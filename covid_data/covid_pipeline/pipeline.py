#
# Author: Ben Hersh
# Class : Comp 3006 Winter 2021
import processors as cdp
import pandas as pd
"""
Main data data processing pipeline.
1. Load the data
"""
COUNTIES_SOURCE_DATA = "../data/us-counties.csv"
CENSUS_DATA = "../data/census_cbsa.csv"


def main():
    counties_covid_df = cdp.load_data(COUNTIES_SOURCE_DATA)
    print(counties_covid_df.info(verbose=True))
    census_place_df = cdp.load_data(CENSUS_DATA)
    print(census_place_df.info(verbose=True))
    county_fips, state_fips = cdp.find_fips_for_cbsa("10100", True, census_place_df)
    print(county_fips, state_fips)


if __name__ == "__main__":
    main()
