#
# Author: Ben Hersh
# Class : Comp 3006 Winter 2021
import county_data_processor as cdp
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


if __name__ == "__main__":
    main()
