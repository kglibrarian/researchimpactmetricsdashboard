# import necessary libraries
import sqlite3
import json
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import (
    Flask,
    render_template,
    url_for,
    jsonify,
    request,
    redirect)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

#################################################
## Database Connection using SQLAlchemy
#################################################
##http://flask.pocoo.org/docs/1.0/tutorial/database/

## create a connection with the database
engine = create_engine("sqlite:///static/db/researchimpactreview.sqlite", connect_args={'check_same_thread': False})
## reflect an existing database into a new model
Base = automap_base()
## reflect the tables
Base.prepare(engine, reflect=True)
# reflect all of the classes mapped to the Base
Base.classes.keys()
# create a "Metadata" Layer That Abstracts our SQL Database
Base.metadata.create_all(engine)
# Save a reference to the table names in the database 
WoSDocuments = Base.classes.wos_documents
WoSDocumentsOrgEnhanced = Base.classes.wos_documents_org_enhanced
WoSDocumentsFundingAgencies = Base.classes.wos_documents_funding_agencies
WoSDocumentsCountries = Base.classes.wos_documents_countries
WoSDocumentsGrantNumbers = Base.classes.wos_documents_grant_numbers
WoSDocumentsCitationReview = Base.classes.wos_documents_citation_review
WoSCitationsWoSCategory = Base.classes.wos_citations_WOS_category
WoSCitationsYears = Base.classes.wos_citations_years
WoSCitationsOrgEnhanced = Base.classes.wos_citations_org_enhanced
WoSCitationsFundingAgencies = Base.classes.wos_citations_funding_agencies
WoSCitationsBookSeriesTitle = Base.classes.wos_citations_book_series_title
WoSCitationsMeetingTitle = Base.classes.wos_citations_meeting_title
WoSCitationsCountries = Base.classes.wos_citations_countries
WoSCitationsGroupAuthors = Base.classes.wos_citations_group_authors
WoSCitationsLanguage = Base.classes.wos_citations_language
# WoSCitationsResearchArea = Base.classes.wos_citations_research_areas
WoSCitationsGrantNumbers = Base.classes.wos_citations_grant_numbers
InCitesDocuments = Base.classes.incites_documents
InCitesDocumentsJournals = Base.classes.incites_documents_journals
InCitesCitations = Base.classes.incites_citations

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)


#################################################
# Flask Routes
#################################################

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/advancementofknowledge")
def AdvancementofKnowledge():
    return render_template("AdvancementofKnowledge.html")

@app.route("/approximatetranslate")
def ApproximateTranslate():
    return render_template("ApproximateTranslate.html")

@app.route("/attentiononline")
def AttentionOnline():
    return render_template("AttentionOnline.html")

@app.route("/careerdevelopment")
def CareerDevelopment():
    return render_template("CareerDevelopment.html")

@app.route("/citationoverview")
def CitationOverview():
    return render_template("CitationOverview.html")

@app.route("/clinicalimplementation")
def ClinicalImplementation():
    return render_template("ClinicalImplementation.html")

@app.route("/communitybenefit")
def CommunityBenefit():
    return render_template("CommunityBenefit.html")

@app.route("/datacitations")
def DataCitations():
    return render_template("DataCitations.html")

@app.route("/datasets")
def Datasets():
    return render_template("Datasets.html")

@app.route("/legislationpolicy")
def LegislationPolicy():
    return render_template("LegislationPolicy.html")

@app.route("/openaccess")
def OpenAccess():
    return render_template("OpenAccess.html")

@app.route("/outputsyear")
def OutputsYear():
    return render_template("OutputsYear.html")

@app.route("/productivity")
def Productivity():
    return render_template("Productivity.html")

@app.route("/ResearchOutputs")
def ResearchOutputs():
    return render_template("ResearchOutputs.html")

@app.route("/TopAuthors")
def TopAuthors():
    return render_template("TopAuthors.html")

@app.route("/api/v1.0/wosdocuments")
def wosDocuments():
    # Query all data from the table
    results = session.query(
        WoSDocuments.PT, 
        WoSDocuments.AU, 
        WoSDocuments.BA, 
        WoSDocuments.BE, 
        WoSDocuments.GP, 
        WoSDocuments.AF, 
        WoSDocuments.BF, 
        WoSDocuments.CA, 
        WoSDocuments.TI, 
        WoSDocuments.SO, 
        WoSDocuments.SE, 
        WoSDocuments.BS, 
        WoSDocuments.LA, 
        WoSDocuments.DT, 
        WoSDocuments.CT, 
        WoSDocuments.CY, 
        WoSDocuments.CL, 
        WoSDocuments.SP, 
        WoSDocuments.HO, 
        WoSDocuments.DE, 
        WoSDocuments.KP, 
        WoSDocuments.AB, 
        WoSDocuments.C1, 
        WoSDocuments.RP, 
        WoSDocuments.EM, 
        WoSDocuments.RI, 
        WoSDocuments.OI, 
        WoSDocuments.FU, 
        WoSDocuments.FX, 
        WoSDocuments.CR, 
        WoSDocuments.NR, 
        WoSDocuments.TC, 
        WoSDocuments.Z9, 
        WoSDocuments.U1, 
        WoSDocuments.U2, 
        WoSDocuments.PU, 
        WoSDocuments.PI, 
        WoSDocuments.PA, 
        WoSDocuments.SN, 
        WoSDocuments.EI, 
        WoSDocuments.BN, 
        WoSDocuments.J9, 
        WoSDocuments.JI, 
        WoSDocuments.PD, 
        WoSDocuments.PY, 
        WoSDocuments.VL, 
        WoSDocuments.IS, 
        WoSDocuments.PN, 
        WoSDocuments.SU, 
        WoSDocuments.SI, 
        WoSDocuments.MA, 
        WoSDocuments.BP, 
        WoSDocuments.EP, 
        WoSDocuments.AR, 
        WoSDocuments.DI, 
        WoSDocuments.D2, 
        WoSDocuments.EA, 
        WoSDocuments.PG, 
        WoSDocuments.WC, 
        WoSDocuments.SC, 
        WoSDocuments.GA, 
        WoSDocuments.UT, 
        WoSDocuments.PM, 
        WoSDocuments.OA, 
        WoSDocuments.HC, 
        WoSDocuments.HP, 
        WoSDocuments.DA).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_documents = []
    for PT,AU,BA,BE,GP,AF,BF,CA,TI,SO,SE,BS,LA,DT,CT,CY,CL,SP,HO,DE,KP,AB,C1,RP,EM,RI,OI,FU,FX,CR,NR,TC,Z9,U1,U2,PU,PI,PA,SN,EI,BN,J9,JI,PD,PY,VL,IS,PN,SU,SI,MA,BP,EP,AR,DI,D2,EA,PG,WC,SC,GA,UT,PM,OA,HC,HP,DA in results:
        wos_documents_dict = {}
        wos_documents_dict["PT"] = PT
        wos_documents_dict["AU"] = AU
        wos_documents_dict["BA"] = BA
        wos_documents_dict["BE"] = BE
        wos_documents_dict["GP"] = GP
        wos_documents_dict["AF"] = AF
        wos_documents_dict["BF"] = BF
        wos_documents_dict["CA"] = CA
        wos_documents_dict["TI"] = TI
        wos_documents_dict["SO"] = SO
        wos_documents_dict["SE"] = SE
        wos_documents_dict["BS"] = BS
        wos_documents_dict["LA"] = LA
        wos_documents_dict["DT"] = DT
        wos_documents_dict["CT"] = CT
        wos_documents_dict["CY"] = CY
        wos_documents_dict["CL"] = CL
        wos_documents_dict["SP"] = SP
        wos_documents_dict["HO"] = HO
        wos_documents_dict["DE"] = DE
        wos_documents_dict["KP"] = KP
        wos_documents_dict["AB"] = AB
        wos_documents_dict["C1"] = C1
        wos_documents_dict["RP"] = RP
        wos_documents_dict["EM"] = EM
        wos_documents_dict["RI"] = RI
        wos_documents_dict["OI"] = OI
        wos_documents_dict["FU"] = FU
        wos_documents_dict["FX"] = FX
        wos_documents_dict["CR"] = CR
        wos_documents_dict["NR"] = NR
        wos_documents_dict["TC"] = TC
        wos_documents_dict["Z9"] = Z9
        wos_documents_dict["U1"] = U1
        wos_documents_dict["U2"] = U2
        wos_documents_dict["PU"] = PU
        wos_documents_dict["PI"] = PI
        wos_documents_dict["PA"] = PA
        wos_documents_dict["SN"] = SN
        wos_documents_dict["EI"] = EI
        wos_documents_dict["BN"] = BN
        wos_documents_dict["J9"] = J9
        wos_documents_dict["JI"] = JI
        wos_documents_dict["PD"] = PD
        wos_documents_dict["PY"] = PY
        wos_documents_dict["VL"] = VL
        wos_documents_dict["IS"] = IS
        wos_documents_dict["PN"] = PN
        wos_documents_dict["SU"] = SU
        wos_documents_dict["SI"] = SI
        wos_documents_dict["MA"] = MA
        wos_documents_dict["BP"] = BP
        wos_documents_dict["EP"] = EP
        wos_documents_dict["AR"] = AR
        wos_documents_dict["DI"] = DI
        wos_documents_dict["D2"] = D2
        wos_documents_dict["EA"] = EA
        wos_documents_dict["PG"] = PG
        wos_documents_dict["WC"] = WC
        wos_documents_dict["SC"] = SC
        wos_documents_dict["GA"] = GA
        wos_documents_dict["UT"] = UT
        wos_documents_dict["PM"] = PM
        wos_documents_dict["OA"] = OA
        wos_documents_dict["HC"] = HC
        wos_documents_dict["HP"] = HP
        wos_documents_dict["DA"] = DA
        wos_documents.append(wos_documents_dict)
    return jsonify(wos_documents)
    #print(wos_documents)

#@app.route("/api/v1.0/wosdocumentsorgenhanced")
def wosDocumentsOrgEnhanced():
    # Query all data from the table
    results = session.query(
        WoSDocumentsOrgEnhanced.Organizations_Enhanced, 
        WoSDocumentsOrgEnhanced.records, 
        WoSDocumentsOrgEnhanced.percent).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_documents_org_enhanced = []
    for Organizations_Enhanced, records, percent in results:
        wos_documents_org_enhanced_dict = {}
        wos_documents_org_enhanced_dict["Organizations_Enhanced"] = Organizations_Enhanced
        wos_documents_org_enhanced_dict["records"] = records
        wos_documents_org_enhanced_dict["percent"] = percent
        wos_documents_org_enhanced.append(wos_documents_org_enhanced_dict)
    #return jsonify(wos_documents_org_enhanced)
    #print(wos_documents_org_enhanced)

wosDocumentsOrgEnhanced()

@app.route("/api/v1.0/wosdocumentsfundingagencies")
def wosDocumentsFundingAgencies():
    # Query all data from the table
    results = session.query(
        WoSDocumentsFundingAgencies.Funding_Agencies, 
        WoSDocumentsFundingAgencies.records, 
        WoSDocumentsFundingAgencies.percent).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_documents_funding_agencies = []
    for Funding_Agencies, records, percent in results:
        wos_documents_funding_agencies_dict = {}
        wos_documents_funding_agencies_dict["Funding_Agencies"] = Funding_Agencies
        wos_documents_funding_agencies_dict["records"] = records
        wos_documents_funding_agencies_dict["percent"] = percent
        wos_documents_funding_agencies.append(wos_documents_funding_agencies_dict)
    return jsonify(wos_documents_funding_agencies)
    #print(wos_documents_funding_agencies)

@app.route("/api/v1.0/wosdocumentscountries")
def wosDocumentsCountries():
    # Query all data from the table
    results = session.query(
        WoSDocumentsCountries.Countries_Regions, 
        WoSDocumentsCountries.records, 
        WoSDocumentsCountries.percent).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_documents_countries = []
    for Countries_Regions, records, percent in results:
        wos_documents_countries_dict = {}
        wos_documents_countries_dict["Countries_Regions"] = Countries_Regions
        wos_documents_countries_dict["records"] = records
        wos_documents_countries_dict["percent"] = percent
        wos_documents_countries.append(wos_documents_countries_dict)
    return jsonify(wos_documents_countries)
    #print(wos_documents_countries)

@app.route("/api/v1.0/wosdocumentsgrantnumbers")
def wosDocumentsGrantNumbers():
    # Query all data from the table
    results = session.query(
        WoSDocumentsGrantNumbers.Grant_Numbers, 
        WoSDocumentsGrantNumbers.records, 
        WoSDocumentsGrantNumbers.percent).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_documents_grant_numbers = []
    for Grant_Numbers, records, percent in results:
        wos_documents_grant_numbers_dict = {}
        wos_documents_grant_numbers_dict["Grant_Numbers"] = Grant_Numbers
        wos_documents_grant_numbers_dict["records"] = records
        wos_documents_grant_numbers_dict["percent"] = percent
        wos_documents_grant_numbers.append(wos_documents_grant_numbers_dict)
    return jsonify(wos_documents_grant_numbers)
    #print(wos_documents_grant_numbers)

@app.route("/api/v1.0/wosdocumentscitationreview")
def wosDocumentsCitationReview():
    # Query all data from the table
    results = session.query(
        WoSDocumentsCitationReview.Title,
        WoSDocumentsCitationReview.Authors,
        WoSDocumentsCitationReview.Corporate_Authors,
        WoSDocumentsCitationReview.Editors,
        WoSDocumentsCitationReview.Book_Editors,
        WoSDocumentsCitationReview.Source_Title,
        WoSDocumentsCitationReview.Publication_Date,
        WoSDocumentsCitationReview.Publication_Year,
        WoSDocumentsCitationReview.Volume,
        WoSDocumentsCitationReview.Issue,
        WoSDocumentsCitationReview.Part_Number,
        WoSDocumentsCitationReview.Supplement,
        WoSDocumentsCitationReview.Special_Issue,
        WoSDocumentsCitationReview.Beginning_Page,
        WoSDocumentsCitationReview.Ending_page,
        WoSDocumentsCitationReview.Article_Number,
        WoSDocumentsCitationReview.DOI,
        WoSDocumentsCitationReview.Conference_Title,
        WoSDocumentsCitationReview.Conference_Date,
        WoSDocumentsCitationReview.Total_Citations,
        WoSDocumentsCitationReview.Average_per_Year,
        WoSDocumentsCitationReview.y1900,
        WoSDocumentsCitationReview.y1901,
        WoSDocumentsCitationReview.y1902,
        WoSDocumentsCitationReview.y1903,
        WoSDocumentsCitationReview.y1904,
        WoSDocumentsCitationReview.y1905,
        WoSDocumentsCitationReview.y1906,
        WoSDocumentsCitationReview.y1907,
        WoSDocumentsCitationReview.y1908,
        WoSDocumentsCitationReview.y1909,
        WoSDocumentsCitationReview.y1910,
        WoSDocumentsCitationReview.y1911,
        WoSDocumentsCitationReview.y1912,
        WoSDocumentsCitationReview.y1913,
        WoSDocumentsCitationReview.y1914,
        WoSDocumentsCitationReview.y1915,
        WoSDocumentsCitationReview.y1916,
        WoSDocumentsCitationReview.y1917,
        WoSDocumentsCitationReview.y1918,
        WoSDocumentsCitationReview.y1919,
        WoSDocumentsCitationReview.y1920,
        WoSDocumentsCitationReview.y1921,
        WoSDocumentsCitationReview.y1922,
        WoSDocumentsCitationReview.y1923,
        WoSDocumentsCitationReview.y1924,
        WoSDocumentsCitationReview.y1925,
        WoSDocumentsCitationReview.y1926,
        WoSDocumentsCitationReview.y1927,
        WoSDocumentsCitationReview.y1928,
        WoSDocumentsCitationReview.y1929,
        WoSDocumentsCitationReview.y1930,
        WoSDocumentsCitationReview.y1931,
        WoSDocumentsCitationReview.y1932,
        WoSDocumentsCitationReview.y1933,
        WoSDocumentsCitationReview.y1934,
        WoSDocumentsCitationReview.y1935,
        WoSDocumentsCitationReview.y1936,
        WoSDocumentsCitationReview.y1937,
        WoSDocumentsCitationReview.y1938,
        WoSDocumentsCitationReview.y1939,
        WoSDocumentsCitationReview.y1940,
        WoSDocumentsCitationReview.y1941,
        WoSDocumentsCitationReview.y1942,
        WoSDocumentsCitationReview.y1943,
        WoSDocumentsCitationReview.y1944,
        WoSDocumentsCitationReview.y1945,
        WoSDocumentsCitationReview.y1946,
        WoSDocumentsCitationReview.y1947,
        WoSDocumentsCitationReview.y1948,
        WoSDocumentsCitationReview.y1949,
        WoSDocumentsCitationReview.y1950,
        WoSDocumentsCitationReview.y1951,
        WoSDocumentsCitationReview.y1952,
        WoSDocumentsCitationReview.y1953,
        WoSDocumentsCitationReview.y1954,
        WoSDocumentsCitationReview.y1955,
        WoSDocumentsCitationReview.y1956,
        WoSDocumentsCitationReview.y1957,
        WoSDocumentsCitationReview.y1958,
        WoSDocumentsCitationReview.y1959,
        WoSDocumentsCitationReview.y1960,
        WoSDocumentsCitationReview.y1961,
        WoSDocumentsCitationReview.y1962,
        WoSDocumentsCitationReview.y1963,
        WoSDocumentsCitationReview.y1964,
        WoSDocumentsCitationReview.y1965,
        WoSDocumentsCitationReview.y1966,
        WoSDocumentsCitationReview.y1967,
        WoSDocumentsCitationReview.y1968,
        WoSDocumentsCitationReview.y1969,
        WoSDocumentsCitationReview.y1970,
        WoSDocumentsCitationReview.y1971,
        WoSDocumentsCitationReview.y1972,
        WoSDocumentsCitationReview.y1973,
        WoSDocumentsCitationReview.y1974,
        WoSDocumentsCitationReview.y1975,
        WoSDocumentsCitationReview.y1976,
        WoSDocumentsCitationReview.y1977,
        WoSDocumentsCitationReview.y1978,
        WoSDocumentsCitationReview.y1979,
        WoSDocumentsCitationReview.y1980,
        WoSDocumentsCitationReview.y1981,
        WoSDocumentsCitationReview.y1982,
        WoSDocumentsCitationReview.y1983,
        WoSDocumentsCitationReview.y1984,
        WoSDocumentsCitationReview.y1985,
        WoSDocumentsCitationReview.y1986,
        WoSDocumentsCitationReview.y1987,
        WoSDocumentsCitationReview.y1988,
        WoSDocumentsCitationReview.y1989,
        WoSDocumentsCitationReview.y1990,
        WoSDocumentsCitationReview.y1991,
        WoSDocumentsCitationReview.y1992,
        WoSDocumentsCitationReview.y1993,
        WoSDocumentsCitationReview.y1994,
        WoSDocumentsCitationReview.y1995,
        WoSDocumentsCitationReview.y1996,
        WoSDocumentsCitationReview.y1997,
        WoSDocumentsCitationReview.y1998,
        WoSDocumentsCitationReview.y1999,
        WoSDocumentsCitationReview.y2000,
        WoSDocumentsCitationReview.y2001,
        WoSDocumentsCitationReview.y2002,
        WoSDocumentsCitationReview.y2003,
        WoSDocumentsCitationReview.y2004,
        WoSDocumentsCitationReview.y2005,
        WoSDocumentsCitationReview.y2006,
        WoSDocumentsCitationReview.y2007,
        WoSDocumentsCitationReview.y2008,
        WoSDocumentsCitationReview.y2009,
        WoSDocumentsCitationReview.y2010,
        WoSDocumentsCitationReview.y2011,
        WoSDocumentsCitationReview.y2012,
        WoSDocumentsCitationReview.y2013,
        WoSDocumentsCitationReview.y2014,
        WoSDocumentsCitationReview.y2015,
        WoSDocumentsCitationReview.y2016,
        WoSDocumentsCitationReview.y2017,
        WoSDocumentsCitationReview.y2018,
        WoSDocumentsCitationReview.y2019,
        WoSDocumentsCitationReview.y2020,
        WoSDocumentsCitationReview.y2021).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_documents_citation_review = []
    for Title,Authors,Corporate_Authors,Editors,Book_Editors,Source_Title,Publication_Date,Publication_Year,Volume,Issue,Part_Number,Supplement,Special_Issue,Beginning_Page,Ending_page,Article_Number,DOI,Conference_Title,Conference_Date,Total_Citations,Average_per_Year,y1900,y1901,y1902,y1903,y1904,y1905,y1906,y1907,y1908,y1909,y1910,y1911,y1912,y1913,y1914,y1915,y1916,y1917,y1918,y1919,y1920,y1921,y1922,y1923,y1924,y1925,y1926,y1927,y1928,y1929,y1930,y1931,y1932,y1933,y1934,y1935,y1936,y1937,y1938,y1939,y1940,y1941,y1942,y1943,y1944,y1945,y1946,y1947,y1948,y1949,y1950,y1951,y1952,y1953,y1954,y1955,y1956,y1957,y1958,y1959,y1960,y1961,y1962,y1963,y1964,y1965,y1966,y1967,y1968,y1969,y1970,y1971,y1972,y1973,y1974,y1975,y1976,y1977,y1978,y1979,y1980,y1981,y1982,y1983,y1984,y1985,y1986,y1987,y1988,y1989,y1990,y1991,y1992,y1993,y1994,y1995,y1996,y1997,y1998,y1999,y2000,y2001,y2002,y2003,y2004,y2005,y2006,y2007,y2008,y2009,y2010,y2011,y2012,y2013,y2014,y2015,y2016,y2017,y2018,y2019,y2020,y2021 in results:
        wos_documents_citation_review_dict = {}
        wos_documents_citation_review_dict["Title"] = Title
        wos_documents_citation_review_dict["Authors"] = Authors
        wos_documents_citation_review_dict["Corporate_Authors"] = Corporate_Authors
        wos_documents_citation_review_dict["Editors"] = Editors
        wos_documents_citation_review_dict["Book_Editors"] = Book_Editors
        wos_documents_citation_review_dict["Source_Title"] = Source_Title
        wos_documents_citation_review_dict["Publication_Date"] = Publication_Date
        wos_documents_citation_review_dict["Publication_Year"] = Publication_Year
        wos_documents_citation_review_dict["Volume"] = Volume
        wos_documents_citation_review_dict["Issue"] = Issue
        wos_documents_citation_review_dict["Part_Number"] = Part_Number
        wos_documents_citation_review_dict["Supplement"] = Supplement
        wos_documents_citation_review_dict["Special_Issue"] = Special_Issue
        wos_documents_citation_review_dict["Beginning_Page"] = Beginning_Page
        wos_documents_citation_review_dict["Ending_page"] = Ending_page
        wos_documents_citation_review_dict["Article_Number"] = Article_Number
        wos_documents_citation_review_dict["DOI"] = DOI
        wos_documents_citation_review_dict["Conference_Title"] = Conference_Title
        wos_documents_citation_review_dict["Conference_Date"] = Conference_Date
        wos_documents_citation_review_dict["Total_Citations"] = Total_Citations
        wos_documents_citation_review_dict["Average_per_Year"] = Average_per_Year
        wos_documents_citation_review_dict["1900"] = y1900
        wos_documents_citation_review_dict["1901"] = y1901
        wos_documents_citation_review_dict["1902"] = y1902
        wos_documents_citation_review_dict["1903"] = y1903
        wos_documents_citation_review_dict["1904"] = y1904
        wos_documents_citation_review_dict["1905"] = y1905
        wos_documents_citation_review_dict["1906"] = y1906
        wos_documents_citation_review_dict["1907"] = y1907
        wos_documents_citation_review_dict["1908"] = y1908
        wos_documents_citation_review_dict["1909"] = y1909
        wos_documents_citation_review_dict["1910"] = y1910
        wos_documents_citation_review_dict["1911"] = y1911
        wos_documents_citation_review_dict["1912"] = y1912
        wos_documents_citation_review_dict["1913"] = y1913
        wos_documents_citation_review_dict["1914"] = y1914
        wos_documents_citation_review_dict["1915"] = y1915
        wos_documents_citation_review_dict["1916"] = y1916
        wos_documents_citation_review_dict["1917"] = y1917
        wos_documents_citation_review_dict["1918"] = y1918
        wos_documents_citation_review_dict["1919"] = y1919
        wos_documents_citation_review_dict["1920"] = y1920
        wos_documents_citation_review_dict["1921"] = y1921
        wos_documents_citation_review_dict["1922"] = y1922
        wos_documents_citation_review_dict["1923"] = y1923
        wos_documents_citation_review_dict["1924"] = y1924
        wos_documents_citation_review_dict["1925"] = y1925
        wos_documents_citation_review_dict["1926"] = y1926
        wos_documents_citation_review_dict["1927"] = y1927
        wos_documents_citation_review_dict["1928"] = y1928
        wos_documents_citation_review_dict["1929"] = y1929
        wos_documents_citation_review_dict["1930"] = y1930
        wos_documents_citation_review_dict["1931"] = y1931
        wos_documents_citation_review_dict["1932"] = y1932
        wos_documents_citation_review_dict["1933"] = y1933
        wos_documents_citation_review_dict["1934"] = y1934
        wos_documents_citation_review_dict["1935"] = y1935
        wos_documents_citation_review_dict["1936"] = y1936
        wos_documents_citation_review_dict["1937"] = y1937
        wos_documents_citation_review_dict["1938"] = y1938
        wos_documents_citation_review_dict["1939"] = y1939
        wos_documents_citation_review_dict["1940"] = y1940
        wos_documents_citation_review_dict["1941"] = y1941
        wos_documents_citation_review_dict["1942"] = y1942
        wos_documents_citation_review_dict["1943"] = y1943
        wos_documents_citation_review_dict["1944"] = y1944
        wos_documents_citation_review_dict["1945"] = y1945
        wos_documents_citation_review_dict["1946"] = y1946
        wos_documents_citation_review_dict["1947"] = y1947
        wos_documents_citation_review_dict["1948"] = y1948
        wos_documents_citation_review_dict["1949"] = y1949
        wos_documents_citation_review_dict["1950"] = y1950
        wos_documents_citation_review_dict["1951"] = y1951
        wos_documents_citation_review_dict["1952"] = y1952
        wos_documents_citation_review_dict["1953"] = y1953
        wos_documents_citation_review_dict["1954"] = y1954
        wos_documents_citation_review_dict["1955"] = y1955
        wos_documents_citation_review_dict["1956"] = y1956
        wos_documents_citation_review_dict["1957"] = y1957
        wos_documents_citation_review_dict["1958"] = y1958
        wos_documents_citation_review_dict["1959"] = y1959
        wos_documents_citation_review_dict["1960"] = y1960
        wos_documents_citation_review_dict["1961"] = y1961
        wos_documents_citation_review_dict["1962"] = y1962
        wos_documents_citation_review_dict["1963"] = y1963
        wos_documents_citation_review_dict["1964"] = y1964
        wos_documents_citation_review_dict["1965"] = y1965
        wos_documents_citation_review_dict["1966"] = y1966
        wos_documents_citation_review_dict["1967"] = y1967
        wos_documents_citation_review_dict["1968"] = y1968
        wos_documents_citation_review_dict["1969"] = y1969
        wos_documents_citation_review_dict["1970"] = y1970
        wos_documents_citation_review_dict["1971"] = y1971
        wos_documents_citation_review_dict["1972"] = y1972
        wos_documents_citation_review_dict["1973"] = y1973
        wos_documents_citation_review_dict["1974"] = y1974
        wos_documents_citation_review_dict["1975"] = y1975
        wos_documents_citation_review_dict["1976"] = y1976
        wos_documents_citation_review_dict["1977"] = y1977
        wos_documents_citation_review_dict["1978"] = y1978
        wos_documents_citation_review_dict["1979"] = y1979
        wos_documents_citation_review_dict["1980"] = y1980
        wos_documents_citation_review_dict["1981"] = y1981
        wos_documents_citation_review_dict["1982"] = y1982
        wos_documents_citation_review_dict["1983"] = y1983
        wos_documents_citation_review_dict["1984"] = y1984
        wos_documents_citation_review_dict["1985"] = y1985
        wos_documents_citation_review_dict["1986"] = y1986
        wos_documents_citation_review_dict["1987"] = y1987
        wos_documents_citation_review_dict["1988"] = y1988
        wos_documents_citation_review_dict["1989"] = y1989
        wos_documents_citation_review_dict["1990"] = y1990
        wos_documents_citation_review_dict["1991"] = y1991
        wos_documents_citation_review_dict["1992"] = y1992
        wos_documents_citation_review_dict["1993"] = y1993
        wos_documents_citation_review_dict["1994"] = y1994
        wos_documents_citation_review_dict["1995"] = y1995
        wos_documents_citation_review_dict["1996"] = y1996
        wos_documents_citation_review_dict["1997"] = y1997
        wos_documents_citation_review_dict["1998"] = y1998
        wos_documents_citation_review_dict["1999"] = y1999
        wos_documents_citation_review_dict["2000"] = y2000
        wos_documents_citation_review_dict["2001"] = y2001
        wos_documents_citation_review_dict["2002"] = y2002
        wos_documents_citation_review_dict["2003"] = y2003
        wos_documents_citation_review_dict["2004"] = y2004
        wos_documents_citation_review_dict["2005"] = y2005
        wos_documents_citation_review_dict["2006"] = y2006
        wos_documents_citation_review_dict["2007"] = y2007
        wos_documents_citation_review_dict["2008"] = y2008
        wos_documents_citation_review_dict["2009"] = y2009
        wos_documents_citation_review_dict["2010"] = y2010
        wos_documents_citation_review_dict["2011"] = y2011
        wos_documents_citation_review_dict["2012"] = y2012
        wos_documents_citation_review_dict["2013"] = y2013
        wos_documents_citation_review_dict["2014"] = y2014
        wos_documents_citation_review_dict["2015"] = y2015
        wos_documents_citation_review_dict["2016"] = y2016
        wos_documents_citation_review_dict["2017"] = y2017
        wos_documents_citation_review_dict["2018"] = y2018
        wos_documents_citation_review_dict["2019"] = y2019
        wos_documents_citation_review_dict["2020"] = y2020
        wos_documents_citation_review_dict["2021"] = y2021
        wos_documents_citation_review.append(wos_documents_citation_review_dict)
    return jsonify(wos_documents_citation_review)
    #print(wos_documents_citation_review)

@app.route("/api/v1.0/woscitationswoscategory")
def wosCitationsWOSCategory():
    # Query all data from the table
    results = session.query(
        WoSCitationsWoSCategory.WOS_Category, 
        WoSCitationsWoSCategory.records, 
        WoSCitationsWoSCategory.percent).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_citations_wos_category = []
    for WOS_Category, records, percent in results:
        wos_citations_wos_category_dict = {}
        wos_citations_wos_category_dict["WOS_Category"] = WOS_Category
        wos_citations_wos_category_dict["records"] = records
        wos_citations_wos_category_dict["percent"] = percent
        wos_citations_wos_category.append(wos_citations_wos_category_dict)
    return jsonify(wos_citations_wos_category)
    #print(wos_citations_wos_category)

@app.route("/api/v1.0/woscitationsyears")
def wosCitationsYears():
    # Query all data from the table
    results = session.query(
        WoSCitationsYears.Publication_Year, 
        WoSCitationsYears.records, 
        WoSCitationsYears.percent).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_citations_year = []
    for Publication_Year, records, percent in results:
        wos_citations_year_dict = {}
        wos_citations_year_dict["Publication_Year"] = Publication_Year
        wos_citations_year_dict["records"] = records
        wos_citations_year_dict["percent"] = percent
        wos_citations_year.append(wos_citations_year_dict)
    return jsonify(wos_citations_year)
    #print(wos_citations_year)

@app.route("/api/v1.0/woscitationsorgenhanced")
#WoSCitationsOrgEnhanced = Base.classes.wos_citations_org_enhanced
def wosCitationsOrgEnhanced():
    # Query all data from the table
    results = session.query(
        WoSCitationsOrgEnhanced.Organization_Enhanced, 
        WoSCitationsOrgEnhanced.records, 
        WoSCitationsOrgEnhanced.percent).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_citations_org_enhanced = []
    for Organization_Enhanced, records, percent in results:
        wos_citations_org_enhanced_dict = {}
        wos_citations_org_enhanced_dict["Organization_Enhanced"] = Organization_Enhanced
        wos_citations_org_enhanced_dict["records"] = records
        wos_citations_org_enhanced_dict["percent"] = percent
        wos_citations_org_enhanced.append(wos_citations_org_enhanced_dict)
    return jsonify(wos_citations_org_enhanced)
    #print(wos_citations_org_enhanced)

@app.route("/api/v1.0/woscitationsfundingagencies")
#WoSCitationsFundingAgencies = Base.classes.wos_citations_funding_agencies
def wosCitationsFundingAgencies():
    # Query all data from the table
    results = session.query(
        WoSCitationsFundingAgencies.Funding_Agencies, 
        WoSCitationsFundingAgencies.records, 
        WoSCitationsFundingAgencies.percent).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_citations_funding_agencies = []
    for Funding_Agencies, records, percent in results:
        wos_citations_funding_agencies_dict = {}
        wos_citations_funding_agencies_dict["Funding_Agencies"] = Funding_Agencies
        wos_citations_funding_agencies_dict["records"] = records
        wos_citations_funding_agencies_dict["percent"] = percent
        wos_citations_funding_agencies.append(wos_citations_funding_agencies_dict)
    return jsonify(wos_citations_funding_agencies)
    #print(wos_citations_funding_agencies)

@app.route("/api/v1.0/woscitationsbookseriestitle")
#WoSCitationsBookSeriesTitle = Base.classes.wos_citations_book_series_title
def wosCitationsBookSeriesTitle():
    # Query all data from the table
    results = session.query(
        WoSCitationsBookSeriesTitle.Book_Series_Title, 
        WoSCitationsBookSeriesTitle.records, 
        WoSCitationsBookSeriesTitle.percent).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_citations_book_series_title = []
    for Book_Series_Title, records, percent in results:
        wos_citations_book_series_title_dict = {}
        wos_citations_book_series_title_dict["Book_Series_Title"] = Book_Series_Title
        wos_citations_book_series_title_dict["records"] = records
        wos_citations_book_series_title_dict["percent"] = percent
        wos_citations_book_series_title.append(wos_citations_book_series_title_dict)
    return jsonify(wos_citations_book_series_title)
    #print(wos_citations_book_series_title)

@app.route("/api/v1.0/woscitationsmeetingtitle")
#WoSCitationsMeetingTitle = Base.classes.wos_citations_meeting_title
def wosCitationsMeetingTitle():
    # Query all data from the table
    results = session.query(
        WoSCitationsMeetingTitle.Meeting_Title, 
        WoSCitationsMeetingTitle.records, 
        WoSCitationsMeetingTitle.percent).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_citations_meeting_title = []
    for Meeting_Title, records, percent in results:
        wos_citations_meeting_title_dict = {}
        wos_citations_meeting_title_dict["Meeting_Title"] = Meeting_Title
        wos_citations_meeting_title_dict["records"] = records
        wos_citations_meeting_title_dict["percent"] = percent
        wos_citations_meeting_title.append(wos_citations_meeting_title_dict)
    return jsonify(wos_citations_meeting_title)
    #print(wos_citations_meeting_title)

@app.route("/api/v1.0/woscitationscountries")
#WoSCitationsCountries = Base.classes.wos_citations_countries
def wosCitationsCountries():
    # Query all data from the table
    results = session.query(
        WoSCitationsCountries.Countries_Regions, 
        WoSCitationsCountries.records, 
        WoSCitationsCountries.percent).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_citations_countries = []
    for Countries_Regions, records, percent in results:
        wos_citations_countries_dict = {}
        wos_citations_countries_dict["Countries_Regions"] = Countries_Regions
        wos_citations_countries_dict["records"] = records
        wos_citations_countries_dict["percent"] = percent
        wos_citations_countries.append(wos_citations_countries_dict)
    return jsonify(wos_citations_countries)
    #print(wos_citations_countries)

@app.route("/api/v1.0/woscitationsgroupauthors")
#WoSCitationsGroupAuthors = Base.classes.wos_citations_group_authors

def wosCitationsGroupAuthors():
    # Query all data from the table
    results = session.query(
        WoSCitationsGroupAuthors.Group_Authors, 
        WoSCitationsGroupAuthors.records, 
        WoSCitationsGroupAuthors.percent).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_citations_group_authors = []
    for Group_Authors, records, percent in results:
        wos_citations_group_authors_dict = {}
        wos_citations_group_authors_dict["Group_Authors"] = Group_Authors
        wos_citations_group_authors_dict["records"] = records
        wos_citations_group_authors_dict["percent"] = percent
        wos_citations_group_authors.append(wos_citations_group_authors_dict)
    return jsonify(wos_citations_group_authors)
    #print(wos_citations_group_authors)

@app.route("/api/v1.0/woscitationslanguages")
#WoSCitationsLanguage = Base.classes.wos_citations_language
def wosCitationsLanguage():
    # Query all data from the table
    results = session.query(
        WoSCitationsLanguage.Language, 
        WoSCitationsLanguage.records, 
        WoSCitationsLanguage.percent).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_citations_language = []
    for Language, records, percent in results:
        wos_citations_language_dict = {}
        wos_citations_language_dict["Language"] = Language
        wos_citations_language_dict["records"] = records
        wos_citations_language_dict["percent"] = percent
        wos_citations_language.append(wos_citations_language_dict)
    return jsonify(wos_citations_language)
    #print(wos_citations_language)

@app.route("/api/v1.0/woscitationsgrantnumbers")
#WoSCitationsGrantNumbers = Base.classes.wos_citations_grant_numbers
def wosCitationsGrantNumbers():
    # Query all data from the table
    results = session.query(
        WoSCitationsGrantNumbers.Grant_Numbers, 
        WoSCitationsGrantNumbers.records, 
        WoSCitationsGrantNumbers.percent).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    wos_citations_grant_numbers = []
    for Grant_Numbers, records, percent in results:
        wos_citations_grant_numbers_dict = {}
        wos_citations_grant_numbers_dict["Grant Numbers"] = Grant_Numbers
        wos_citations_grant_numbers_dict["records"] = records
        wos_citations_grant_numbers_dict["percent"] = percent
        wos_citations_grant_numbers.append(wos_citations_grant_numbers_dict)
    return jsonify(wos_citations_grant_numbers)
    #print(wos_citations_grant_numbers)

@app.route("/api/v1.0/incitesdocuments")
#InCitesDocuments = Base.classes.incites_documents
def inCitesDocuments():
    # Query all data from the table
    results = session.query(
        InCitesDocuments.Accession_Number,
        InCitesDocuments.DOI,
        InCitesDocuments.Pubmed_ID,
        InCitesDocuments.Article_Title,
        InCitesDocuments.Link,
        InCitesDocuments.Authors,
        InCitesDocuments.Source,
        InCitesDocuments.Research_Area,
        InCitesDocuments.Document_Type,
        InCitesDocuments.Volume,
        InCitesDocuments.Issue,
        InCitesDocuments.Pages,
        InCitesDocuments.Publication_Date,
        InCitesDocuments.Times_Cited,
        InCitesDocuments.Journal_Expected_Citations,
        InCitesDocuments.Category_Expected_Citations,
        InCitesDocuments.Journal_Normalized_Citation_Impact,
        InCitesDocuments.Category_Normalized_Citation_Impact,
        InCitesDocuments.Percentile_in_Subject_Area,
        InCitesDocuments.Journal_Impact_Factor).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    incites_documents = []
    for Accession_Number,DOI,Pubmed_ID,Article_Title,Link,Authors,Source,Research_Area,Document_Type,Volume,Issue,Pages,Publication_Date,Times_Cited,Journal_Expected_Citations,Category_Expected_Citations,Journal_Normalized_Citation_Impact,Category_Normalized_Citation_Impact,Percentile_in_Subject_Area,Journal_Impact_Factor in results:
        incites_documents_dict = {}
        incites_documents_dict["Accession_Number"] = Accession_Number
        incites_documents_dict["DOI"] = DOI
        incites_documents_dict["Pubmed_ID"] = Pubmed_ID
        incites_documents_dict["Article_Title"] = Article_Title
        incites_documents_dict["Link"] = Link
        incites_documents_dict["Authors"] = Authors
        incites_documents_dict["Source"] = Source
        incites_documents_dict["Research_Area"] = Research_Area
        incites_documents_dict["Document_Type"] = Document_Type
        incites_documents_dict["Volume"] = Volume
        incites_documents_dict["Issue"] = Issue
        incites_documents_dict["Pages"] = Pages
        incites_documents_dict["Publication_Date"] = Publication_Date
        incites_documents_dict["Times_Cited"] = Times_Cited
        incites_documents_dict["Journal_Expected_Citations"] = Journal_Expected_Citations
        incites_documents_dict["Category_Expected_Citations"] = Category_Expected_Citations
        incites_documents_dict["Journal_Normalized_Citation_Impact"] = Journal_Normalized_Citation_Impact
        incites_documents_dict["Category_Normalized_Citation_Impact"] = Category_Normalized_Citation_Impact
        incites_documents_dict["Percentile_in_Subject_Area"] = Percentile_in_Subject_Area
        incites_documents_dict["Journal_Impact_Factor"] = Journal_Impact_Factor
        incites_documents.append(incites_documents_dict)
    return jsonify(incites_documents)
    #print(incites_documents)

@app.route("/api/v1.0/incitesdocumentsjournals")
#InCitesDocumentsJournals = Base.classes.incites_documents_journals
def inCitesDocumentsJournals():
    # Query all data from the table
    results = session.query(
        InCitesDocumentsJournals.Name,
        InCitesDocumentsJournals.Rank,
        InCitesDocumentsJournals.Web_of_Science_Documents,
        InCitesDocumentsJournals.Times_Cited,
        InCitesDocumentsJournals.Percent_Docs_Cited,
        InCitesDocumentsJournals.Quartile,
        InCitesDocumentsJournals.Five_Year_Impact_Factor,
        InCitesDocumentsJournals.Article_Influence,
        InCitesDocumentsJournals.Category_Normalized_Citation_Impact,
        InCitesDocumentsJournals.Cited_Half_Life,
        InCitesDocumentsJournals.Eigenfactor,
        InCitesDocumentsJournals.Immediacy_Index,
        InCitesDocumentsJournals.Impact_Factor_wo_Self_Cites,
        InCitesDocumentsJournals.Journal_Impact_Factor,
        InCitesDocumentsJournals.Journal_Normalized_Citation_Impact,
        InCitesDocumentsJournals.Percent_All_Open_Access_Documents,
        InCitesDocumentsJournals.Percent_Bronze_Documents,
        InCitesDocumentsJournals.Percent_DOAJ_Gold_Documents,
        InCitesDocumentsJournals.Percent_Green_Accepted_Documents,
        InCitesDocumentsJournals.Percent_Green_Published_Documents,
        InCitesDocumentsJournals.Percent_Other_Gold_Documents,
        InCitesDocumentsJournals.All_Open_Access_Documents,
        InCitesDocumentsJournals.Bronze_Documents,
        InCitesDocumentsJournals.DOAJ_Gold_Documents,
        InCitesDocumentsJournals.Green_Accepted_Documents,
        InCitesDocumentsJournals.Green_Published_Documents,
        InCitesDocumentsJournals.Other_Gold_Documents).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    incites_documents_journals = []
    for Name,Rank,Web_of_Science_Documents,Times_Cited,Percent_Docs_Cited,Quartile,Five_Year_Impact_Factor,Article_Influence,Category_Normalized_Citation_Impact,Cited_Half_Life,Eigenfactor,Immediacy_Index,Impact_Factor_wo_Self_Cites,Journal_Impact_Factor,Journal_Normalized_Citation_Impact,Percent_All_Open_Access_Documents,Percent_Bronze_Documents,Percent_DOAJ_Gold_Documents,Percent_Green_Accepted_Documents,Percent_Green_Published_Documents,Percent_Other_Gold_Documents,All_Open_Access_Documents,Bronze_Documents,DOAJ_Gold_Documents,Green_Accepted_Documents,Green_Published_Documents,Other_Gold_Documents in results:
        incites_documents_journals_dict = {}
        incites_documents_journals_dict["Name"] = Name
        incites_documents_journals_dict["Rank"] = Rank
        incites_documents_journals_dict["Web_of_Science_Documents"] = Web_of_Science_Documents
        incites_documents_journals_dict["Times_Cited"] = Times_Cited
        incites_documents_journals_dict["Percent_Docs_Cited"] = Percent_Docs_Cited
        incites_documents_journals_dict["Quartile"] = Quartile
        incites_documents_journals_dict["Five_Year_Impact_Factor"] = Five_Year_Impact_Factor
        incites_documents_journals_dict["Article_Influence"] = Article_Influence
        incites_documents_journals_dict["Category_Normalized_Citation_Impact"] = Category_Normalized_Citation_Impact
        incites_documents_journals_dict["Cited_Half_Life"] = Cited_Half_Life
        incites_documents_journals_dict["Eigenfactor"] = Eigenfactor
        incites_documents_journals_dict["Immediacy_Index"] = Immediacy_Index
        incites_documents_journals_dict["Impact_Factor_wo_Self_Cites"] = Impact_Factor_wo_Self_Cites
        incites_documents_journals_dict["Journal_Impact_Factor"] = Journal_Impact_Factor
        incites_documents_journals_dict["Journal_Normalized_Citation_Impact"] = Journal_Normalized_Citation_Impact
        incites_documents_journals_dict["Percent_All_Open_Access_Documents"] = Percent_All_Open_Access_Documents
        incites_documents_journals_dict["Percent_Bronze_Documents"] = Percent_Bronze_Documents
        incites_documents_journals_dict["Percent_DOAJ_Gold_Documents"] = Percent_DOAJ_Gold_Documents
        incites_documents_journals_dict["Percent_Green_Accepted_Documents"] = Percent_Green_Accepted_Documents
        incites_documents_journals_dict["Percent_Green_Published_Documents"] = Percent_Green_Published_Documents
        incites_documents_journals_dict["Percent_Other_Gold_Documents"] = Percent_Other_Gold_Documents
        incites_documents_journals_dict["All_Open_Access_Documents"] = All_Open_Access_Documents
        incites_documents_journals_dict["Bronze_Documents"] = Bronze_Documents
        incites_documents_journals_dict["DOAJ_Gold_Documents"] = DOAJ_Gold_Documents
        incites_documents_journals_dict["Green_Accepted_Documents"] = Green_Accepted_Documents
        incites_documents_journals_dict["Green_Published_Documents"] = Green_Published_Documents
        incites_documents_journals_dict["Other_Gold_Documents"] = Other_Gold_Documents
        incites_documents_journals.append(incites_documents_journals_dict)
    return jsonify(incites_documents_journals)
    #print(incites_documents_journals)

@app.route("/api/v1.0/incitescitations")
#InCitesCitations = Base.classes.incites_citations

def inCitesCitations():
    # Query all data from the table
    results = session.query(
        InCitesCitations.Accession_Number,
        InCitesCitations.DOI,
        InCitesCitations.Pubmed_ID,
        InCitesCitations.Article_Title,
        InCitesCitations.Link,
        InCitesCitations.Authors,
        InCitesCitations.Source,
        InCitesCitations.Research_Area,
        InCitesCitations.Document_Type,
        InCitesCitations.Volume,
        InCitesCitations.Issue,
        InCitesCitations.Pages,
        InCitesCitations.Publication_Date,
        InCitesCitations.Times_Cited,
        InCitesCitations.Journal_Expected_Citations,
        InCitesCitations.Category_Expected_Citations,
        InCitesCitations.Journal_Normalized_Citation_Impact,
        InCitesCitations.Category_Normalized_Citation_Impact,
        InCitesCitations.Percentile_in_Subject_Area,
        InCitesCitations.Journal_Impact_Factor).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    incites_citations = []
    for Accession_Number,DOI,Pubmed_ID,Article_Title,Link,Authors,Source,Research_Area,Document_Type,Volume,Issue,Pages,Publication_Date,Times_Cited,Journal_Expected_Citations,Category_Expected_Citations,Journal_Normalized_Citation_Impact,Category_Normalized_Citation_Impact,Percentile_in_Subject_Area,Journal_Impact_Factor in results:
        incites_citations_dict = {}
        incites_citations_dict["Accession_Number"] = Accession_Number
        incites_citations_dict["DOI"] = DOI
        incites_citations_dict["Pubmed_ID"] = Pubmed_ID
        incites_citations_dict["Article_Title"] = Article_Title
        incites_citations_dict["Link"] = Link
        incites_citations_dict["Authors"] = Authors
        incites_citations_dict["Source"] = Source
        incites_citations_dict["Research_Area"] = Research_Area
        incites_citations_dict["Document_Type"] = Document_Type
        incites_citations_dict["Volume"] = Volume
        incites_citations_dict["Issue"] = Issue
        incites_citations_dict["Pages"] = Pages
        incites_citations_dict["Publication_Date"] = Publication_Date
        incites_citations_dict["Times_Cited"] = Times_Cited
        incites_citations_dict["Journal_Expected_Citations"] = Journal_Expected_Citations
        incites_citations_dict["Category_Expected_Citations"] = Category_Expected_Citations
        incites_citations_dict["Journal_Normalized_Citation_Impact"] = Journal_Normalized_Citation_Impact
        incites_citations_dict["Category_Normalized_Citation_Impact"] = Category_Normalized_Citation_Impact
        incites_citations_dict["Percentile_in_Subject_Area"] = Percentile_in_Subject_Area
        incites_citations_dict["Journal_Impact_Factor"] = Journal_Impact_Factor
        incites_citations.append(incites_citations_dict)
    return jsonify(incites_citations)
    #print(iincites_citations)

if __name__ == "__main__":
    app.debug = True
    app.run()
