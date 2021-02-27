#
# Author : Benjamin Hersh
# Class: Comp 3006 Winter 2021
#
import pandas as pd
from collections import namedtuple

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

    def __repr__(self):
        print(f"Fips: state id : {self.state_id}, county id : {self.county_id}")


def load_data(data_file):
    """
    Load us-counties.csv data into a pandas data frame
    :return:
    Pandas dataframe
    """
    with open(data_file, "r") as counties_data:
        df = pd.read_csv(counties_data)
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
        central_keyword = "Central" if is_central else "Outlying"
        fips_df = df[(df["CBSA Code"] == cbsa_code) & (df["Central/Outlying County"] == central_keyword)]
        result = []
        for row in fips_df.iterrows():
            # row is s tuple, 0 position is an index, 1 position is series with named columns
            result.append(FipsData(row[1][9], row[1][10]))
        return result
    else:
        raise ValueError("'CBSA Code' not in the supplied dataframe")


def group_by_state(df):
    """
    Group the us-counties data by state for each day
    :param df: the us-counties data frame
    :return:
    Dataframe of date,  num_records, state, min, max, mean, sum, num_records
    """
def group_counties(county_ids, df):
    """
    Calculates min, max, mean, sum, num_records for data grouping by the list of fips id for each day in the dataset
    :param county_names: array of fips ids
    :param df: the us-counties data frame
    :return:
    pandas data frame of date,num_records,min,max,mean,sum
    """
