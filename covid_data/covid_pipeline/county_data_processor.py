#
# Author : Benjamin Hersh
# Class: Comp 3006 Winter 2021
#
import pandas as pd

"""
This class defines functions for processing the us-counties data.
"""


def load_data(data_file):
    """
    Load us-counties.csv data into a pandas data frame
    :return:
    Pandas dataframe
    """
    with open(data_file, "r") as counties_data:
        df = pd.read_csv(counties_data)
    return df

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
