#
# Author: Ben Hersh
# Class : Comp 3006 Winter 2021
import logging

import processors as cdp
import matplotlib.pyplot as plt
import numpy as np
import os

"""
Main data data processing pipeline.
1. Load the data
"""
COUNTIES_SOURCE_DATA = "../data/us-counties.csv"
CENSUS_REGION_DATA = "../data/census_cbsa.csv"
CENSUS_POPULATION_DATA = "../data/census_population_only_estimates_2019.csv"


def main():
    if os.path.exists("covid_prepped.csv"):
        covid_df = cdp.load_data("covid_prepped.csv")
    else:
        covid_df = step_1_data_prep()
    if os.path.exists("covid_by_state_year_month.csv"):
        by_state_df = cdp.load_data("covid_by_state_year_month.csv")
    else:
        by_state_df = step2_aggregate_by_state(covid_df)
    quarters = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    for q_number, months in enumerate(quarters):
        logging.info("months : %s", months)
        quarter_selection = by_state_df[(by_state_df["year"] == 2020) & (by_state_df["month"].isin(months))]
        new_cases_agg = cdp.aggregate_covid_cases_by_group(None, ["state_id"], quarter_selection, "new_cases_total")
        logging.info(new_cases_agg.head(100))
        plt.figure(1)
        plt.bar(new_cases_agg["state_id"], new_cases_agg["new_cases_total", "sum"])
        plt.yscale("log")
        plt.title(f"Q{q_number+1} 2020 : New Cases")
        plt.xlabel("state id")
        plt.ylabel("new cases")
        plt.savefig(f"q{q_number+1}_new_cases.png")
        plt.show()






def step2_aggregate_by_state(covid_df):
    states_series = covid_df["state_id"]
    states = states_series.unique()
    by_state_df = None
    for state_id in states:
        logging.info("getting aggregate for state id %d", state_id)
        state_df = covid_df[covid_df["state_id"] == state_id]
        state_df.sort_values(by=["date"])
        agg_result = cdp.aggregate_covid_cases_by_group(None, ["state_id", "year", "month"], state_df)
        agg_result["new_cases_total"] = agg_result["cases", "sum"] - agg_result["cases", "sum"].shift(1)
        if by_state_df is not None:
            by_state_df = by_state_df.append(agg_result)
        else:
            by_state_df = agg_result
    logging.info(by_state_df.info(verbose=True))
    logging.info(by_state_df.head(5))
    logging.info(by_state_df.shape)
    by_state_df.to_csv("covid_by_state_year_month.csv", index=False)
    return by_state_df


def step_1_data_prep():
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
    covid_df.to_csv("covid_prepped.csv", index=False)
    return covid_df


if __name__ == "__main__":
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(funcName)s] %(message)s")
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.INFO)
    stdout_handler.setFormatter(formatter)
    root_logger.addHandler(stdout_handler)
    main()
