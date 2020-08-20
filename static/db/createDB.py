##########################
## Import Libraries and Dependencies
##########################
import sqlite3
import csv
import pandas as pd
from numpy import genfromtxt
from time import time
from datetime import datetime, timedelta
from sqlalchemy import Column, String, Integer, Float, Date, VARCHAR, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from random import randint
import os
import sys

###################################
## How to use this file
###################################
## Run this file once to create the database from 
## the CSVs in the data file
## Open this file in the terminal and run: python createDB.py

##################################
## SQLAlchemy Declarative base
# ################################
# The declarative base is a function that returns 
# a new base class from which all mapped classes 
# should inherit.
# Refer to these sqlalchemy tutorials:
# https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/basic_use.html
#https://docs.sqlalchemy.org/en/13/core/tutorial.html


#Create the database
engine = create_engine('sqlite:///researchimpactreview.sqlite')

#Map which table in database will be related to each class
Base = declarative_base()

#Create a metadata instance
metadata = MetaData(engine)
#A metadata is an object container that will store attributes and name of table 

Base.metadata.drop_all(engine)  

##################################
## Define Schema (i.e. Create Classes)
##################################
#Create a class that describes each table in the database
#https://images.webofknowledge.com/images/help/WOS/hs_wos_fieldtags.html
# ID column in Wos Documents becomes KP
# extend_existing=True, autoload=True, autoload_with=engine

class WoS_Documents(Base):
    __tablename__ = 'wos_documents'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    PT = Column(VARCHAR(40))
    AU = Column(Text)
    BA = Column(Text)
    BE = Column(Text)
    GP = Column(Text)
    AF = Column(Text)
    BF = Column(Text)
    CA = Column(Text)
    TI = Column(Text)
    SO = Column(Text)
    SE = Column(Text)
    BS = Column(Text)
    LA = Column(Text)
    DT = Column(Text)
    CT = Column(Text)
    CY = Column(Text)
    CL = Column(Text)
    SP = Column(Text)
    HO = Column(Text)
    DE = Column(Text)
    KP = Column(Text)
    AB = Column(Text)
    C1 = Column(Text)
    RP = Column(Text)
    EM = Column(Text)
    RI = Column(Text)
    OI = Column(Text)
    FU = Column(Text)
    FX = Column(Text)
    CR = Column(Text)
    NR = Column(Integer)
    TC = Column(Integer)
    Z9 = Column(Text)
    U1 = Column(Integer)
    U2 = Column(Integer)
    PU = Column(Text)
    PI = Column(Text)
    PA = Column(Text)
    SN = Column(Text)
    EI = Column(Text)
    BN = Column(Text)
    J9 = Column(Text)
    JI = Column(Text)
    PD = Column(Text)
    PY = Column(Text)
    VL = Column(Text)
    IS = Column(Text)
    PN = Column(Text)
    SU = Column(Text)
    SI = Column(Text)
    MA = Column(Text)
    BP = Column(Integer)
    EP = Column(Integer)
    AR = Column(Text)
    DI = Column(Text)
    D2 = Column(Text)
    EA = Column(Text)
    PG = Column(Text)
    WC = Column(Text)
    SC = Column(Text)
    GA = Column(Text)
    UT = Column(Text)
    PM = Column(Text)
    OA = Column(Text)
    HC = Column(Text)
    HP = Column(Text)
    DA = Column(Text)

   
 

class WoS_Documents_Org_Enhanced(Base):
    __tablename__ = 'wos_documents_org_enhanced'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    Organizations_Enhanced = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)
    
    
class WoS_Documents_Funding_Agencies(Base):
    __tablename__ = 'wos_documents_funding_agencies'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    Funding_Agencies = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)

class WoS_Documents_Countries(Base):
    __tablename__ = 'wos_documents_countries'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    Countries_Regions = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)
    
class WoS_Documents_Grant_Numbers(Base):
    __tablename__ = 'wos_documents_grant_numbers'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    Grant_Numbers = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)
    
class WoS_Documents_Citation_Review(Base):
    __tablename__ = 'wos_documents_citation_review'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)  
    Title = Column(Text)
    Authors = Column(Text)
    Corporate_Authors = Column(Text)
    Editors = Column(Text)
    Book_Editors = Column(Text)
    Source_Title = Column(Text)
    Publication_Date = Column(Text)
    Publication_Year = Column(Text)
    Volume = Column(Text)
    Issue = Column(Text)
    Part_Number = Column(Text)
    Supplement = Column(Text)
    Special_Issue = Column(Text)
    Beginning_Page = Column(Integer)
    Ending_page = Column(Integer)
    Article_Number = Column(Text)
    DOI = Column(Text)
    Conference_Title = Column(Text)
    Conference_Date = Column(Text)
    Total_Citations = Column(Integer)
    Average_per_Year = Column(Float)
    y1900 = Column(Integer)
    y1901 = Column(Integer)
    y1902 = Column(Integer)
    y1903 = Column(Integer)
    y1904 = Column(Integer)
    y1905 = Column(Integer)
    y1906 = Column(Integer)
    y1907 = Column(Integer)
    y1908 = Column(Integer)
    y1909 = Column(Integer)
    y1910 = Column(Integer)
    y1911 = Column(Integer)
    y1912 = Column(Integer)
    y1913 = Column(Integer)
    y1914 = Column(Integer)
    y1915 = Column(Integer)
    y1916 = Column(Integer)
    y1917 = Column(Integer)
    y1918 = Column(Integer)
    y1919 = Column(Integer)
    y1920 = Column(Integer)
    y1921 = Column(Integer)
    y1922 = Column(Integer)
    y1923 = Column(Integer)
    y1924 = Column(Integer)
    y1925 = Column(Integer)
    y1926 = Column(Integer)
    y1927 = Column(Integer)
    y1928 = Column(Integer)
    y1929 = Column(Integer)
    y1930 = Column(Integer)
    y1931 = Column(Integer)
    y1932 = Column(Integer)
    y1933 = Column(Integer)
    y1934 = Column(Integer)
    y1935 = Column(Integer)
    y1936 = Column(Integer)
    y1937 = Column(Integer)
    y1938 = Column(Integer)
    y1939 = Column(Integer)
    y1940 = Column(Integer)
    y1941 = Column(Integer)
    y1942 = Column(Integer)
    y1943 = Column(Integer)
    y1944 = Column(Integer)
    y1945 = Column(Integer)
    y1946 = Column(Integer)
    y1947 = Column(Integer)
    y1948 = Column(Integer)
    y1949 = Column(Integer)
    y1950 = Column(Integer)
    y1951 = Column(Integer)
    y1952 = Column(Integer)
    y1953 = Column(Integer)
    y1954 = Column(Integer)
    y1955 = Column(Integer)
    y1956 = Column(Integer)
    y1957 = Column(Integer)
    y1958 = Column(Integer)
    y1959 = Column(Integer)
    y1960 = Column(Integer)
    y1961 = Column(Integer)
    y1962 = Column(Integer)
    y1963 = Column(Integer)
    y1964 = Column(Integer)
    y1965 = Column(Integer)
    y1966 = Column(Integer)
    y1967 = Column(Integer)
    y1968 = Column(Integer)
    y1969 = Column(Integer)
    y1970 = Column(Integer)
    y1971 = Column(Integer)
    y1972 = Column(Integer)
    y1973 = Column(Integer)
    y1974 = Column(Integer)
    y1975 = Column(Integer)
    y1976 = Column(Integer)
    y1977 = Column(Integer)
    y1978 = Column(Integer)
    y1979 = Column(Integer)
    y1980 = Column(Integer)
    y1981 = Column(Integer)
    y1982 = Column(Integer)
    y1983 = Column(Integer)
    y1984 = Column(Integer)
    y1985 = Column(Integer)
    y1986 = Column(Integer)
    y1987 = Column(Integer)
    y1988 = Column(Integer)
    y1989 = Column(Integer)
    y1990 = Column(Integer)
    y1991 = Column(Integer)
    y1992 = Column(Integer)
    y1993 = Column(Integer)
    y1994 = Column(Integer)
    y1995 = Column(Integer)
    y1996 = Column(Integer)
    y1997 = Column(Integer)
    y1998 = Column(Integer)
    y1999 = Column(Integer)
    y2000 = Column(Integer)
    y2001 = Column(Integer)
    y2002 = Column(Integer)
    y2003 = Column(Integer)
    y2004 = Column(Integer)
    y2005 = Column(Integer)
    y2006 = Column(Integer)
    y2007 = Column(Integer)
    y2008 = Column(Integer)
    y2009 = Column(Integer)
    y2010 = Column(Integer)
    y2011 = Column(Integer)
    y2012 = Column(Integer)
    y2013 = Column(Integer)
    y2014 = Column(Integer)
    y2015 = Column(Integer)
    y2016 = Column(Integer)
    y2017 = Column(Integer)
    y2018 = Column(Integer)
    y2019 = Column(Integer)
    y2020 = Column(Integer)
    y2021 = Column(Integer)
    


    
    
class WoS_Citations_WOS_Category (Base):
    __tablename__ = 'wos_citations_WOS_category'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    WOS_Category = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)
    
class WoS_Citations_Years(Base):
    __tablename__ = 'wos_citations_years'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False) 
    Publication_Year = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)
    

class WoS_Citations_Org_Enhanced(Base):
    __tablename__ = 'wos_citations_org_enhanced'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    Organization_Enhanced = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)
    

class WoS_Citations_Funding_Agencies(Base):
    __tablename__ = 'wos_citations_funding_agencies'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    Funding_Agencies = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)
    
class WoS_Citations_Source_Title(Base):
    __tablename__ = 'wos_citations_source_title'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    Source_Title = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)

class WoS_Citations_Book_Series_Title(Base):
    __tablename__ = 'wos_citations_book_series_title'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    Book_Series_Title = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)

class WoS_Citations_Meeting_Title(Base):
    __tablename__ = 'wos_citations_meeting_title'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    Meeting_Title = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)
    
class WoS_Citations_Countries(Base):
    __tablename__ = 'wos_citations_countries'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False) 
    Countries_Regions = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)

class WoS_Citations_Group_Authors(Base):
    __tablename__ = 'wos_citations_group_authors'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False) 
    Group_Authors = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)
    
class WoS_Citations_Language(Base):
    __tablename__ = 'wos_citations_language'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False) 
    Language = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)
    
class WoS_Citations_Research_Area(Base):
    __tablename__ = 'wos_citations_research_area'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False) 
    Research_Area = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)
    
class WoS_Citations_Grant_Numbers(Base):
    __tablename__ = 'wos_citations_grant_numbers'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    Grant_Numbers = Column(Text)
    records = Column(Integer)
    percent = Column(Integer)

class InCites_Documents (Base):
    __tablename__ = 'incites_documents'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    Accession_Number = Column(Text)
    DOI = Column(Text)
    Pubmed_ID = Column(Text)
    Article_Title = Column(Text)
    Link = Column(Text)
    Authors = Column(Text)
    Source = Column(Text)
    Research_Area = Column(Text)
    Document_Type = Column(Text)
    Volume = Column(Text)
    Issue = Column(Text)
    Pages = Column(Text)
    Publication_Date = Column(Text)
    Times_Cited = Column(Integer)
    Journal_Expected_Citations = Column(Float)
    Category_Expected_Citations = Column(Float)
    Journal_Normalized_Citation_Impact = Column(Float)
    Category_Normalized_Citation_Impact = Column(Float)
    Percentile_in_Subject_Area = Column(Float)
    Journal_Impact_Factor = Column(Float)

class InCites_Documents_Journals (Base):
    __tablename__ = 'incites_documents_journals'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    Name = Column(Text)
    Rank = Column(Text)
    Web_of_Science_Documents = Column(Integer)
    Times_Cited = Column(Integer)
    Percent_Docs_Cited = Column(Float)
    Quartile = Column(Text)
    Five_Year_Impact_Factor = Column(Float)
    Article_Influence = Column(Float)
    Category_Normalized_Citation_Impact = Column(Float)
    Cited_Half_Life = Column(Float)
    Eigenfactor = Column(Float)
    Immediacy_Index = Column(Float)
    Impact_Factor_wo_Self_Cites = Column(Float)
    Journal_Impact_Factor = Column(Float)
    Journal_Normalized_Citation_Impact = Column(Float)
    Percent_All_Open_Access_Documents = Column(Float)
    Percent_Bronze_Documents = Column(Float)
    Percent_DOAJ_Gold_Documents = Column(Float)
    Percent_Green_Accepted_Documents = Column(Float)
    Percent_Green_Published_Documents = Column(Float)
    Percent_Other_Gold_Documents = Column(Float)
    All_Open_Access_Documents = Column(Float)
    Bronze_Documents = Column(Integer)
    DOAJ_Gold_Documents = Column(Integer)
    Green_Accepted_Documents = Column(Integer)
    Green_Published_Documents = Column(Integer)
    Other_Gold_Documents = Column(Integer)

class InCites_Citations (Base):
    __tablename__ = 'incites_citations'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    Accession_Number = Column(Text)
    DOI = Column(Text)
    Pubmed_ID = Column(Text)
    Article_Title = Column(Text)
    Link = Column(Text)
    Authors = Column(Text)
    Source = Column(Text)
    Research_Area = Column(Text)
    Document_Type = Column(Text)
    Volume = Column(Text)
    Issue = Column(Text)
    Pages = Column(Text)
    Publication_Date = Column(Text)
    Times_Cited = Column(Integer)
    Journal_Expected_Citations = Column(Float)
    Category_Expected_Citations = Column(Float)
    Journal_Normalized_Citation_Impact = Column(Float)
    Category_Normalized_Citation_Impact = Column(Float)
    Percentile_in_Subject_Area = Column(Float)
    Journal_Impact_Factor = Column(Float)
    

WoS_Documents.__table__.create(bind=engine, checkfirst=True)
WoS_Documents_Org_Enhanced.__table__.create(bind=engine, checkfirst=True)
WoS_Documents_Funding_Agencies.__table__.create(bind=engine, checkfirst=True)
WoS_Documents_Countries.__table__.create(bind=engine, checkfirst=True)
WoS_Documents_Grant_Numbers.__table__.create(bind=engine, checkfirst=True)
WoS_Documents_Citation_Review.__table__.create(bind=engine, checkfirst=True)
WoS_Citations_WOS_Category.__table__.create(bind=engine, checkfirst=True)
WoS_Citations_Years.__table__.create(bind=engine, checkfirst=True)
WoS_Citations_Org_Enhanced.__table__.create(bind=engine, checkfirst=True)
WoS_Citations_Funding_Agencies.__table__.create(bind=engine, checkfirst=True)
WoS_Citations_Source_Title.__table__.create(bind=engine, checkfirst=True)
WoS_Citations_Book_Series_Title.__table__.create(bind=engine, checkfirst=True)
WoS_Citations_Meeting_Title.__table__.create(bind=engine, checkfirst=True)
WoS_Citations_Countries.__table__.create(bind=engine, checkfirst=True)
WoS_Citations_Group_Authors.__table__.create(bind=engine, checkfirst=True)
WoS_Citations_Language.__table__.create(bind=engine, checkfirst=True)
WoS_Citations_Grant_Numbers.__table__.create(bind=engine, checkfirst=True)
InCites_Documents.__table__.create(bind=engine, checkfirst=True)
InCites_Documents_Journals.__table__.create(bind=engine, checkfirst=True)
InCites_Citations.__table__.create(bind=engine, checkfirst=True)

####################################
## Extract: Use SQLAlchemy to Load CSV data into Tables
####################################
#Within the if statement that will create the database using 
# the classes that have already been described (see above)

 
def load_1():
    #energy_consumption_sector_data = genfromtxt("../data/Energy_Consumption_by_Sector_2017.csv", delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    #print(energy_consumption_sector_data)
    #return energy_consumption_sector_data.tolist()
    wos_documents_data = pd.read_csv("../data/wos_documents.csv")
    wos_documents_data_list = wos_documents_data.values.tolist()
    #print(wos_documents_data_list)
    return wos_documents_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_1 = load_1()
    #print(data_1)
    for i in data_1:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Documents(**{
                    'PT' : i[0], 
                    'AU' : i[1], 
                    'BA' : i[2], 
                    'BE' : i[3], 
                    'GP' : i[4], 
                    'AF' : i[5], 
                    'BF' : i[6], 
                    'CA' : i[7], 
                    'TI' : i[8], 
                    'SO' : i[9], 
                    'SE' : i[10], 
                    'BS' : i[11], 
                    'LA' : i[12], 
                    'DT' : i[13], 
                    'CT' : i[14], 
                    'CY' : i[15], 
                    'CL' : i[16], 
                    'SP' : i[17], 
                    'HO' : i[18], 
                    'DE' : i[19], 
                    'KP' : i[20], 
                    'AB' : i[21], 
                    'C1' : i[22], 
                    'RP' : i[23], 
                    'EM' : i[24], 
                    'RI' : i[25], 
                    'OI' : i[26], 
                    'FU' : i[27], 
                    'FX' : i[28], 
                    'CR' : i[29], 
                    'NR' : i[30], 
                    'TC' : i[31], 
                    'Z9' : i[32], 
                    'U1' : i[33], 
                    'U2' : i[34], 
                    'PU' : i[35], 
                    'PI' : i[36], 
                    'PA' : i[37], 
                    'SN' : i[38], 
                    'EI' : i[39], 
                    'BN' : i[40], 
                    'J9' : i[41], 
                    'JI' : i[42], 
                    'PD' : i[43], 
                    'PY' : i[44], 
                    'VL' : i[45], 
                    'IS' : i[46], 
                    'PN' : i[47], 
                    'SU' : i[48], 
                    'SI' : i[49], 
                    'MA' : i[50], 
                    'BP' : i[51], 
                    'EP' : i[52], 
                    'AR' : i[53], 
                    'DI' : i[54], 
                    'D2' : i[55], 
                    'EA' : i[56], 
                    'PG' : i[57], 
                    'WC' : i[58], 
                    'SC' : i[59], 
                    'GA' : i[60], 
                    'UT' : i[61], 
                    'PM' : i[62], 
                    'OA' : i[63], 
                    'HC' : i[64], 
                    'HP' : i[65], 
                    'DA' : i[66] 



                        })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')


def load_2():
    wos_documents_org_enhanced_data = pd.read_csv("../data/wos_documents_org_enhanced.csv")
    wos_documents_org_enhanced_data_list = wos_documents_org_enhanced_data.values.tolist()
    #print(wos_documents_org_enhanced_data_list)
    return wos_documents_org_enhanced_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_2 = load_2()
    #print(data_2)
    for i in data_2:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Documents_Org_Enhanced(**{
                    'Organizations_Enhanced' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')

def load_3():
    wos_documents_funding_agencies_data = pd.read_csv("../data/wos_documents_funding_agencies.csv")
    wos_documents_funding_agencies_data_list = wos_documents_funding_agencies_data.values.tolist()
    #print(wos_documents_funding_agencies_data_list)
    return wos_documents_funding_agencies_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_3 = load_3()
    #print(data_3)
    for i in data_3:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Documents_Funding_Agencies(**{
                    'Funding_Agencies' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')

def load_4():
    wos_documents_countries_data = pd.read_csv("../data/wos_documents_countries.csv")
    wos_documents_countries_data_list = wos_documents_countries_data.values.tolist()
    #print(wos_documents_countries_data_list)
    return wos_documents_countries_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_4 = load_4()
    #print(data_4)
    for i in data_4:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Documents_Countries(**{
                    'Countries_Regions' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')

def load_5():
    wos_documents_grant_numbers_data = pd.read_csv("../data/wos_documents_grant_numbers.csv")
    wos_documents_grant_numbers_data_list = wos_documents_grant_numbers_data.values.tolist()
    #print(wos_documents_grant_numbers_data_list)
    return wos_documents_grant_numbers_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_5 = load_5()
    #print(data_5)
    for i in data_5:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Documents_Grant_Numbers(**{
                    'Grant_Numbers' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')

def load_6():
    wos_documents_citation_review_data = pd.read_csv("../data/wos_documents_citation_review.csv")
    wos_documents_citation_review_data_list = wos_documents_citation_review_data.values.tolist()
    #print(wos_documents_citation_review_data_list)
    return wos_documents_citation_review_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_6 = load_6()
    #print(data_6)
    for i in data_6:
        #print([i[142]])
        #below is the Class name and column names from the database
        record = WoS_Documents_Citation_Review(**{
                        'Title' : i[0],
                        'Authors' : i[1],
                        'Corporate_Authors' : i[2],
                        'Editors' : i[3],
                        'Book_Editors' : i[4],
                        'Source_Title' : i[5],
                        'Publication_Date' : i[6],
                        'Publication_Year' : i[7],
                        'Volume' : i[8],
                        'Issue' : i[9],
                        'Part_Number' : i[10],
                        'Supplement' : i[11],
                        'Special_Issue' : i[12],
                        'Beginning_Page' : i[13],
                        'Ending_page' : i[14],
                        'Article_Number' : i[15],
                        'DOI' : i[16],
                        'Conference_Title' : i[17],
                        'Conference_Date' : i[18],
                        'Total_Citations' : i[19],
                        'Average_per_Year' : i[20],
                        'y1900' : i[21],
                        'y1901' : i[22],
                        'y1902' : i[23],
                        'y1903' : i[24],
                        'y1904' : i[25],
                        'y1905' : i[26],
                        'y1906' : i[27],
                        'y1907' : i[28],
                        'y1908' : i[29],
                        'y1909' : i[30],
                        'y1910' : i[31],
                        'y1911' : i[32],
                        'y1912' : i[33],
                        'y1913' : i[34],
                        'y1914' : i[35],
                        'y1915' : i[36],
                        'y1916' : i[37],
                        'y1917' : i[38],
                        'y1918' : i[39],
                        'y1919' : i[40],
                        'y1920' : i[41],
                        'y1921' : i[42],
                        'y1922' : i[43],
                        'y1923' : i[44],
                        'y1924' : i[45],
                        'y1925' : i[46],
                        'y1926' : i[47],
                        'y1927' : i[48],
                        'y1928' : i[49],
                        'y1929' : i[50],
                        'y1930' : i[51],
                        'y1931' : i[52],
                        'y1932' : i[53],
                        'y1933' : i[54],
                        'y1934' : i[55],
                        'y1935' : i[56],
                        'y1936' : i[57],
                        'y1937' : i[58],
                        'y1938' : i[59],
                        'y1939' : i[60],
                        'y1940' : i[61],
                        'y1941' : i[62],
                        'y1942' : i[63],
                        'y1943' : i[64],
                        'y1944' : i[65],
                        'y1945' : i[66],
                        'y1946' : i[67],
                        'y1947' : i[68],
                        'y1948' : i[69],
                        'y1949' : i[70],
                        'y1950' : i[71],
                        'y1951' : i[72],
                        'y1952' : i[73],
                        'y1953' : i[74],
                        'y1954' : i[75],
                        'y1955' : i[76],
                        'y1956' : i[77],
                        'y1957' : i[78],
                        'y1958' : i[79],
                        'y1959' : i[80],
                        'y1960' : i[81],
                        'y1961' : i[82],
                        'y1962' : i[83],
                        'y1963' : i[84],
                        'y1964' : i[85],
                        'y1965' : i[86],
                        'y1966' : i[87],
                        'y1967' : i[88],
                        'y1968' : i[89],
                        'y1969' : i[90],
                        'y1970' : i[91],
                        'y1971' : i[92],
                        'y1972' : i[93],
                        'y1973' : i[94],
                        'y1974' : i[95],
                        'y1975' : i[96],
                        'y1976' : i[97],
                        'y1977' : i[98],
                        'y1978' : i[99],
                        'y1979' : i[100],
                        'y1980' : i[101],
                        'y1981' : i[102],
                        'y1982' : i[103],
                        'y1983' : i[104],
                        'y1984' : i[105],
                        'y1985' : i[106],
                        'y1986' : i[107],
                        'y1987' : i[108],
                        'y1988' : i[109],
                        'y1989' : i[110],
                        'y1990' : i[111],
                        'y1991' : i[112],
                        'y1992' : i[113],
                        'y1993' : i[114],
                        'y1994' : i[115],
                        'y1995' : i[116],
                        'y1996' : i[117],
                        'y1997' : i[118],
                        'y1998' : i[119],
                        'y1999' : i[120],
                        'y2000' : i[121],
                        'y2001' : i[122],
                        'y2002' : i[123],
                        'y2003' : i[124],
                        'y2004' : i[125],
                        'y2005' : i[126],
                        'y2006' : i[127],
                        'y2007' : i[128],
                        'y2008' : i[129],
                        'y2009' : i[130],
                        'y2010' : i[131],
                        'y2011' : i[132],
                        'y2012' : i[133],
                        'y2013' : i[134],
                        'y2014' : i[135],
                        'y2015' : i[136],
                        'y2016' : i[137],
                        'y2017' : i[138],
                        'y2018' : i[139],
                        'y2019' : i[140],
                        'y2020' : i[141],
                        'y2021' : i[142],

                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed') 


def load_7():
    wos_citations_wos_category_data = pd.read_csv("../data/wos_citations_wos_category.csv")
    wos_citations_wos_category_data_list = wos_citations_wos_category_data.values.tolist()
    #print(wos_citations_wos_category_data_list)
    return wos_citations_wos_category_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_7 = load_7()
    #print(data_7)
    for i in data_7:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Citations_WOS_Category(**{
                    'WOS_Category' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')

def load_8():
    wos_citations_citaton_years_data = pd.read_csv("../data/wos_citations_citation_years.csv")
    wos_citations_citaton_years_data_list = wos_citations_citaton_years_data.values.tolist()
    #print(wos_citations_citaton_years_data_list)
    return wos_citations_citaton_years_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_8 = load_8()
    #print(data_8)
    for i in data_8:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Citations_Years(**{
                    'Publication_Year' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')


def load_9():
    wos_citations_org_enhanced_data = pd.read_csv("../data/wos_citations_org_enhanced.csv")
    wos_citations_org_enhanced_data_list = wos_citations_org_enhanced_data.values.tolist()
    #print(wos_citations_org_enhanced_data_list)
    return wos_citations_org_enhanced_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_9 = load_9()
    #print(data_9)
    for i in data_9:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Citations_Org_Enhanced(**{
                    'Organization_Enhanced' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')

def load_10():
    wos_citations_funding_agencies_data = pd.read_csv("../data/wos_citations_funding_agencies.csv")
    wos_citations_funding_agencies_data_list = wos_citations_funding_agencies_data.values.tolist()
    #print(wos_citations_funding_agencies_data_list)
    return wos_citations_funding_agencies_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_10 = load_10()
    #print(data_10)
    for i in data_10:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Citations_Funding_Agencies(**{
                    'Funding_Agencies' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')

def load_11():
    wos_citations_source_title_data = pd.read_csv("../data/wos_citations_source_title.csv")
    wos_citations_source_title_data_list = wos_citations_source_title_data.values.tolist()
    #print(wos_citations_source_title_data_list)
    return wos_citations_source_title_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_11 = load_11()
    #print(data_11)
    for i in data_11:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Citations_Source_Title(**{
                    'Source_Title' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')


def load_12():
    wos_citations_book_series_title_data = pd.read_csv("../data/wos_citations_book_series_title.csv")
    wos_citations_book_series_title_data_list = wos_citations_book_series_title_data.values.tolist()
    #print(wos_citations_book_series_title_data_list)
    return wos_citations_book_series_title_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_12 = load_12()
    #print(data_12)
    for i in data_12:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Citations_Book_Series_Title(**{
                    'Book_Series_Title' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')


def load_13():
    wos_citations_meeting_title_data = pd.read_csv("../data/wos_citations_meeting_title.csv")
    wos_citations_meeting_title_data_list = wos_citations_meeting_title_data.values.tolist()
    #print(wos_citations_meeting_title_data_list)
    return wos_citations_meeting_title_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_13 = load_13()
    #print(data_13)
    for i in data_13:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Citations_Meeting_Title(**{
                    'Meeting_Title' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')


def load_14():
    wos_citations_countries_data = pd.read_csv("../data/wos_citations_countries.csv")
    wos_citations_countries_data_list = wos_citations_countries_data.values.tolist()
    #print(wos_citations_countries_data_list)
    return wos_citations_countries_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_14 = load_14()
    #print(data_14)
    for i in data_14:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Citations_Countries(**{
                    'Countries_Regions' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')


def load_15():
    wos_citations_group_authors_data = pd.read_csv("../data/wos_citations_group_authors.csv")
    wos_citations_group_authors_data_list = wos_citations_group_authors_data.values.tolist()
    #print(wos_citations_group_authors_data_list)
    return wos_citations_group_authors_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_15 = load_15()
    #print(data_15)
    for i in data_15:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Citations_Group_Authors(**{
                    'Group_Authors' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')

def load_16():
    wos_citations_language_data = pd.read_csv("../data/wos_citations_languages.csv")
    wos_citations_language_data_list = wos_citations_language_data.values.tolist()
    #print(wos_citations_language_data_list)
    return wos_citations_language_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_16 = load_16()
    #print(data_16)
    for i in data_16:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Citations_Language(**{
                    'Language' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')


def load_17():
    wos_citations_grant_numbers_data = pd.read_csv("../data/wos_citations_grant_numbers.csv")
    wos_citations_grant_numbers_data_list = wos_citations_grant_numbers_data.values.tolist()
    #print(wos_citations_grant_numbers_data_list)
    return wos_citations_grant_numbers_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_17 = load_17()
    #print(data_17)
    for i in data_17:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = WoS_Citations_Grant_Numbers(**{
                    'Grant_Numbers' : i[0], 
                    'records' : i[1], 
                    'percent' : i[2] 
                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')

def load_18():
    incites_documents_data = pd.read_csv("../data/incites_documents.csv")
    incites_documents_data_list = incites_documents_data.values.tolist()
    #print(incites_documents_data_list)
    return incites_documents_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_18 = load_18()
    #print(data_18)
    for i in data_18:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = InCites_Documents(**{
                'Accession_Number' : i[0],
                'DOI' : i[1],
                'Pubmed_ID' : i[2],
                'Article_Title' : i[3],
                'Link' : i[4],
                'Authors' : i[5],
                'Source' : i[6],
                'Research_Area' : i[7],
                'Document_Type' : i[8],
                'Volume' : i[9],
                'Issue' : i[10],
                'Pages' : i[11],
                'Publication_Date' : i[12],
                'Times_Cited' : i[13],
                'Journal_Expected_Citations' : i[14],
                'Category_Expected_Citations' : i[15],
                'Journal_Normalized_Citation_Impact' : i[16],
                'Category_Normalized_Citation_Impact' : i[17],
                'Percentile_in_Subject_Area' : i[18],
                'Journal_Impact_Factor' : i[19]


                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')


def load_19():
    incites_documents_journals_data = pd.read_csv("../data/incites_documents_journals.csv")
    incites_documents_journals_data_list = incites_documents_journals_data.values.tolist()
    #print(incites_documents_journals_data_list)
    return incites_documents_journals_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_19 = load_19()
    #print(data_19)
    for i in data_19:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = InCites_Documents_Journals(**{
                    'Name' : i[0],
                    'Rank' : i[1],
                    'Web_of_Science_Documents' : i[2],
                    'Times_Cited' : i[3],
                    'Percent_Docs_Cited' : i[4],
                    'Quartile' : i[5],
                    'Five_Year_Impact_Factor' : i[6],
                    'Article_Influence' : i[7],
                    'Category_Normalized_Citation_Impact' : i[8],
                    'Cited_Half_Life' : i[9],
                    'Eigenfactor' : i[10],
                    'Immediacy_Index' : i[11],
                    'Impact_Factor_wo_Self_Cites' : i[12],
                    'Journal_Impact_Factor' : i[13],
                    'Journal_Normalized_Citation_Impact' : i[14],
                    'Percent_All_Open_Access_Documents' : i[15],
                    'Percent_Bronze_Documents' : i[16],
                    'Percent_DOAJ_Gold_Documents' : i[17],
                    'Percent_Green_Accepted_Documents' : i[18],
                    'Percent_Green_Published_Documents' : i[19],
                    'Percent_Other_Gold_Documents' : i[20],
                    'All_Open_Access_Documents' : i[21],
                    'Bronze_Documents' : i[22],
                    'DOAJ_Gold_Documents' : i[23],
                    'Green_Accepted_Documents' : i[24],
                    'Green_Published_Documents' : i[25],
                    'Other_Gold_Documents' : i[26]


                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')

def load_20():
    incites_citations_data = pd.read_csv("../data/incites_citations.csv")
    incites_citations_data_list = incites_citations_data.values.tolist()
    #print(incites_citations_data_list)
    return incites_citations_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_20 = load_20()
    #print(data_20)
    for i in data_20:
        #print([i[0]])
        #below is the Class name and column names from the database
        record = InCites_Citations(**{
                    'Accession_Number' : i[0],
                    'DOI' : i[1],
                    'Pubmed_ID' : i[2],
                    'Article_Title' : i[3],
                    'Link' : i[4],
                    'Authors' : i[5],
                    'Source' : i[6],
                    'Research_Area' : i[7],
                    'Document_Type' : i[8],
                    'Volume' : i[9],
                    'Issue' : i[10],
                    'Pages' : i[11],
                    'Publication_Date' : i[12],
                    'Times_Cited' : i[13],
                    'Journal_Expected_Citations' : i[14],
                    'Category_Expected_Citations' : i[15],
                    'Journal_Normalized_Citation_Impact' : i[16],
                    'Category_Normalized_Citation_Impact' : i[17],
                    'Percentile_in_Subject_Area' : i[18],
                    'Journal_Impact_Factor' : i[19]


                 })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   

#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
    #print('session closed')