import os
import sys
import csv
import logging
import argparse
import unittest
#import matplotlib as plt
#import numpy as np
from collections import namedtuple, defaultdict

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#create a file handler object
fh = logging.FileHandler('housing.log', 'w')
#set the level to DEBUG
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
#add the file handler to the logger object
logger.addHandler(fh)
#create a stream handler
sh = logging.StreamHandler()
#set level to INFO
sh.setLevel(logging.INFO)
sh.setFormatter(formatter)
#add stream handler to
logger.addHandler(sh)

class Housing:
    '''class that defines a single housing price index record'''
    def __init__(self, hpi_type, hpi_flavor, level, place_name, place_id, year, \
    period, index_nsa, index_sa):
        self.hpi_type = hpi_type
        self.hpi_flavor  = hpi_flavor
        self.level = level
        self.place_name = place_name
        self.place_id = place_id
        self.year = int(year)
        self.period = int(period)
        self.index_nsa = float(index_nsa)
        logger.debug('Housing object created for %s, Q%d %d' %(self.place_name, \
        self.period, self.year))
    def __repr__(self):
        return('Housing (%s, %s, %s, %s, %s, %d, %d, %2f)' \
        %(self.hpi_type, self.hpi_flavor, self.level, self.place_name, self.place_id, \
        self.year, self.period, self.index_nsa))
        logger.debug('repr called for Housing object')
    def __str__(self):
        return(repr(self))
class HousingData:
    '''Class that loads data from a csv to a Housing object, and stores all \
    relevent objects in one of two lists'''
    #method to instantiate HousingData object
    def __init__(self):
        logger.debug('HousingData object instantiated')
        self.state_data, self.metro_data = self._load_data()
        logger.debug('State level housing data loaded into HousingData object')
        logger.debug('Metro level housing data loaded into HousingData object')
    #method to interate through HousingData object
    def __iter__(self):
        iter([list(self.state_data), list(self.metro_data)])
    #method to parse lines from the csv data into Housing objects
    def parse_line(self, line):
        #define the named tuple Record
        Record = namedtuple('Record', 'hpi_type hpi_flavor frequency level place_name place_id year period index_nsa index_sa')
        #instantiate a record object with the data from the csv file
        c = Record(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])
        #records csv data into Housing data object
        h = Housing(c.hpi_type, c.hpi_flavor, c.level, c.place_name, c.place_id, c.year, c.period, c.index_nsa, c.index_sa)
        logger.debug('Housing obeject created for %s' %repr(h))
        return h
    #method that looks at a housing object and decides if it should be included in state data
    def sort_state(self, z):
            #looks for state in level,  traditional in type, for years greater than 2014,
            #and hpi_flavor is all-transactions
            if z.level == 'State' and z.hpi_type == 'traditional' and z.year > 2014 and z.hpi_flavor == 'all-transactions':
                return True
            else:
                return False
    #method that looks at a housing object and decides if it should be included\
    #in the metro data
    def sort_metro(self, z):
        #looks for Metro Statistical Area in level, all-transactions flavor,
        #and years greater than 2018
        if z.level == 'MSA'and z.hpi_flavor == 'all-transactions' and z.year >2014:
            return True
        #looks for non-metro in type, state in level, and year greater than 2014
        if z.hpi_type == 'non-metro' and z.level == 'State' and z.year > 2014:
            return True
        else:
            return False

    #method for writing state data out to a .csv file
    def state_out(self):
        s= self.state_data
        file = 'state_housing_data.csv'
        with open(file, 'w', newline = '') as f:
            writer = csv.writer(f)
            header = ['hpi_type', 'hpi_flavor', 'level', 'placename', 'place_id', 'year', 'quarter', 'index_nsa']
            writer.writerow(header)
            for a in s:
                r = [a.hpi_type, a.hpi_flavor, a.level, a.place_name, a.place_id, a.year, a.period, a.index_nsa]
                writer.writerow(r)
                logger.debug('Record for %s saved to state data file.' %repr(a))
            logger.info('Saved state data to state_housing_data.csv.')
    def metro_out(self):
        h= self.metro_data
        file = 'metro_housing_data.csv'
        with open(file, 'w', newline = '') as f:
            writer = csv.writer(f)
            header = ['hpi_type', 'hpi_flavor', 'level', 'placename', 'place_id', 'year', 'quarter', 'index_nsa']
            writer.writerow(header)
            for a in h:
                r = [a.hpi_type, a.hpi_flavor, a.level, a.place_name, a.place_id, a.year, a.period, a.index_nsa]
                writer.writerow(r)
                logger.debug('Record for %s saved to metro data file.' %repr(a))
            logger.info('Saved metro and non-metro state data to metro_housing_data.csv.')
    #method to load state data from FHFA HSI master csv file
    def _load_data(self):
        #instantiate an empty file for the sate housing data
        state_data= []
        metro_data= []
        #defines the expected file name
        raw_file = 'HPI_master.csv'
        #checks for existance of data file
        if os.path.isfile(raw_file):
            logger.info('Data file found in directory')
        #if the file is absent
        else:
            logger.error('Data file not found in working directory')
        #opens the file
        with open(raw_file) as file:
            logger.debug('Housing data file opened')
            #uses the csv reader to read the data
            reader = csv.reader(file)
            logger.debug('csv reader object instantiated')
            #skip the header line
            next(reader, None)
            #iterates through the lines of the file
            for line in reader:
                #calls the parse line method to parse the line and create a Housing object
                z = self.parse_line(line)
                #checks object level and hpi_type, to select only whole state data
                if self.sort_state(z) == True:
                    state_data.append(z)
                    logger.debug('added record for %s to HousingData state_data' %repr(z))
                if self.sort_metro(z) == True:
                    metro_data.append(z)
                    logger.debug('added record for %s to HousingData metro_data' %repr(z))
            logger.debug('Finished reading data file')
            return (state_data, metro_data)
def yoy_change(list, year):
    year_data=[]
    prev_year_data=[]
    for geo in list:
        l = [geo.place_name, geo.place_id, geo.year, geo.period, geo.index_nsa]
        if geo.year == year:
            year_data.append(l)
        if geo.year == year - 1:
            prev_year_data.append(l)
    yoy_change = []
    for i in year_data:
        for j in prev_year_data:
            if i[0]==j[0] and i[1]==j[1] and i[3]==j[3]:
                d = i[4]-j[4]
                p = d/j[4]*100
                i.append(d)
                i.append(p)
                yoy_change.append(i)
    return yoy_change
def main():
    #instantiate argparse object
    parser = argparse.ArgumentParser(description = \
    'Accept optional argument --plot')
    logger.debug('Parser started')
    #add reload optional argument
    #parser.add_argument('--reload', '-r', action = 'store_true', default = False)
    #logger.debug('Listening for reload options')
    #add optional argurment for plots
    parser.add_argument('--plot', '-p', choices = ['hist', 'trend', 'all'])
    logger.debug('Listening for plot option')
    #save the parsed arguements
    args = parser.parse_args()
    #log that we parsed the arguements
    logger.info('Parsed command line arguments')

    try:
        o = HousingData()
        logger.info('HousingData object successfully created.')
    except Exception as e:
        logger.error('An exception occured while trying to create a HousingData object.')
    state_change = yoy_change(o.state_data, 2020)
    logger.info('State year over year change recorded')
    msa_cange = yoy_change(o.metro_data, 2020)
    logger.info('Metro area year over year change recorded')
    file = 'state_fips_codes.txt'
    dic={}
    with open(file) as f:
        reader = csv.reader(f, delimiter = "|")
        next(reader, None)
        for line in reader:
            key = line[1]
            value = line[0]
            dic[key] = int(value)
        for record in state_change:
            st = record[1]
            a = dic.get(st)
            record[1]=a
    ofile = 'state_year_over_year_change.csv'
    header = ['Place Name', 'Place ID', 'Year', 'Quarter', 'HPI', 'YoY change', '% YoY change']
    with open(ofile, 'w', newline ='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for line in state_change:
            writer.writerow(line)
    logger.debug('End of main function! Your program ran to completion.')
if __name__ == '__main__':
    main()
