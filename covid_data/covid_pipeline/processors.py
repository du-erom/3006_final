#
# Author : Benjamin Hersh
# Class: Comp 3006 Winter 2021
#
import pandas as pd
from collections import namedtuple
import logging

"""
This class defines functions for processing the us-counties data.
"""


class FipsData:
    """
    Encapsulates a census data query result for FIPS ids
    """
    def __init__(self, state_id, county_id):
        """
        Create an new instance
        :param state_id: the FIPS state id (int)
        :param county_id: the FIPS count id (int)
        """
        self.state_id = state_id
        self.county_id = county_id

    def __eq__(self, other):
        """
        Equal if both state id and county id match
        :param other:
        :return:
        True if both fields match
        """
        return self.state_id == other.state_id and self.county_id == other.county_id

    def __str__(self):
        print(f"Fips: state id : {self.state_id}, county id : {self.county_id}")

    def __repr__(self):
        return self.__str__()

def load_data(data_file):
    """
    Load us-counties.csv data into a pandas data frame
    :return:
    Pandas dataframe
    """
    with open(data_file, "r") as counties_data:
        df = pd.read_csv(counties_data)
    logging.debug("loaded %s", data_file)
    return df


def find_fips_for_cbsa(cbsa_code, is_central, df):
    """
    Filter the census delination data for a specific CBSA code and Central/Outlying keyword.
    Census data may have multiple for the query.
    :param cbsa_code: the cbsa code value
    :param is_central: boolean, True if the 'central' Central/Outlying County value is desired
    :param df: the census data frame
    :return:
    list of FipsData namedtuple for matching rows
    """
    if "CBSA Code" in df:
        logging.debug("finding fips code for cbsa code %s, central flag %s", cbsa_code, is_central)
        central_keyword = "Central" if is_central else "Outlying"
        fips_df = df[(df["CBSA Code"] == cbsa_code) & (df["Central/Outlying County"] == central_keyword)]
        result = []
        for row in fips_df.iterrows():
            # row is s tuple, 0 position is an index, 1 position is series with named columns
            result.append(FipsData(row[1][9], row[1][10]))
        logging.debug("returning %d items", len(result))
        return result
    else:
        logging.error("dataframe not supported for this query")
        raise ValueError("'CBSA Code' not in the supplied dataframe")


def population_by_fips(fips_list, df):
    """
    Calculate total population over the selected FIPS identifiers
    :param fips_list: the FipsData list to filter on
    :param df: the census_population df
    :return:
    Total Population summed across the FIPS selectors
    """
    if "SUMLEV" in df:
        logging.debug("summing population across %d areas", len(fips_list))
        state_ids = set([f.state_id for f in fips_list])
        county_ids = set([f.county_id for f in fips_list])
        result = df[(df["STATE"].isin(state_ids)) & (df["COUNTY"].isin(county_ids))]
        logging.debug("found %d matches", len(result))
        population = result["POPESTIMATE2019"].sum()
        logging.debug("population = %d", population)
        return population
    else:
        logging.error("dataframe not supported for this query")
        raise ValueError("SUMLEV not in the dataframe")


def group_covid_by_fips(fips_list, df):
    """
    Group the covid data by the specified FIPS identifiers per day.
    :param fips_list: FipsData list
    :param df: the census dataframe
    :return:
    DataFrame with source df schema
    """
    if "cases" in df:
        query_fips = list(map(covid_fips, fips_list))
        logging.debug("querying over covid_ips ids: %s", query_fips)
        query_result = df[df["fips"].isin(query_fips)]
        return query_result.groupby(["date"], as_index=False).sum()
    else:
        logging.error("dataframe not supported for this query")
        raise ValueError("cases not in the dataframe")


def append_difference(diff_field_name, source_field, sort_fields, df):
    """
    Append a difference field to the dataframe.
    Question how to only apply difference to rows with the same fips values and not on the boundary between
    fips fields.
    N/A set for difference when row is the first row for the sort fields.
    """
    return df

def covid_fips(fips_data):
    """
    Construct the covid data fips id which is state_id*1000 + county_id
    :param fips_data: a FipsData instance
    :return:
    synthetic covid data fips id
    """
    return fips_data.state_id * 1000 + fips_data.county_id