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
    cdp.split_covid_fips_into_cbsa_values(covid_df)
    covid_df.info(verbose=True)
    logging.info(covid_df.head(5))
    covid_data = cdp.aggregate_covid_cases_by_group(fips, ["date"], covid_df)
    covid_data.info(verbose=True)
    logging.info(covid_data.head(5))
    covid_data["dCases"] = covid_data["cases", "sum"] - covid_data["cases", "sum"].shift(1)
    shape = covid_data.shape
    covid_data.info(verbose=True)
    logging.info(covid_data.head(5))
    logging.info("covid_data size %s", covid_data.shape)
    plt.figure(1, figsize=(10,10))
    plt.plot(covid_data["date"], covid_data["cases","sum"])
    plt.xticks(np.arange(0, shape[0]+1, 20.0), rotation=90)
    plt.title("Census Region: Georgia, Central")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.tight_layout()
    plt.savefig("sample1.png")
    plt.show()
    plt.figure(2, figsize=(10,10))
    plt.plot(covid_data["date"], covid_data["dCases"])
    plt.xticks(np.arange(0, shape[0]+1, 20.0), rotation=90)
    plt.title("Census Region: Georgia, Central")
    plt.xlabel("Date")
    plt.ylabel("Total New Cases/Day")
    plt.tight_layout()
    plt.savefig("sample2.png")
    plt.show()



if __name__ == "__main__":
    main()
