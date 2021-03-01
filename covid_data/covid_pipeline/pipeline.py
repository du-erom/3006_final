#
# Author: Ben Hersh
# Class : Comp 3006 Winter 2021
import logging

import processors as cdp
import matplotlib.pyplot as plt
import numpy as np

"""
Main data data processing pipeline.
1. Load the data
"""
COUNTIES_SOURCE_DATA = "../data/us-counties.csv"
CENSUS_REGION_DATA = "../data/census_cbsa.csv"
CENSUS_POPULATION_DATA = "../data/census_population_only_estimates_2019.csv"


def main():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(funcName)s] %(message)s")
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.INFO)
    stdout_handler.setFormatter(formatter)
    root_logger.addHandler(stdout_handler)

    # lets pick Central areas of Georgia
    census_cbsa_df = cdp.load_data(CENSUS_REGION_DATA)
    fips = cdp.find_fips_for_cbsa(12060, True, census_cbsa_df)
    covid_df = cdp.load_data(COUNTIES_SOURCE_DATA)
    covid_data = cdp.group_covid_by_fips(fips, covid_df)
    shape = covid_data.shape
    logging.info("covid_data size %s", covid_data.shape)
    plt.figure(1)
    plt.plot(covid_data["date"], covid_data["cases"])
    plt.xticks(np.arange(0, shape[0]+1, 20.0), rotation=90)
    plt.title("Census Region: Georia, Central")
    plt.xlabel("Date")
    plt.ylabel("Total New Cases/Day")
    plt.tight_layout()
    plt.savefig("sample.png")
    plt.show()




if __name__ == "__main__":
    main()
