from application import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
#from sqlalchemy.orm import Session, scoped_session, sessionmaker
#from sqlalchemy import create_engine, func, inspect



#db = SQLAlchemy(app)
#db.Model.metadata.reflect(db.engine)

####################################
## Access tables in existing database
####################################

#wosdocuments = db.Table('wos_documents', db.metadata, autoload=True, autoload_with=db.engine)

#####################
## Using Flask-SQLAlchemy with Automap base
####################
# produce our own MetaData object
metadata = MetaData()

# we can then produce a set of mappings from this MetaData.
Base = automap_base(metadata=metadata)

# reflect the tables
Base.prepare(db.engine, reflect=True )

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

# reflect all of the classes mapped to the Base
Base.classes.keys()

# class WoSDocuments(db.Model):
#     __tablename__ = 'wos_documents'
#     __table_args__ = { 'extend_existing': True }
#     id = db.Column(db.Integer, primary_key=True)
#     # LOC_CODE = db.Column(db.Text, primary_key=True)   


# inspector = inspect(db.engine)
# table_name = WoSDocuments
# def table(table_name):
#     names = []
#     for table_name in inspector.get_table_names():
#         for column in inspector.get_columns(table_name):
#             names.append(column)
#             return(str(names))       







