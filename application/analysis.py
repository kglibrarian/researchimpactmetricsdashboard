
#from application.routes import wosDocuments
from application.models import *
from application import app, db
import json
from itertools import chain
#result = WoSDocuments

def readData(result):
    #print(results)
    # Create a dictionary from the row data and append to a list of all documents
    final_int = str(result)
    # for item in result:
    #     wos_documents.append(str(item.gettext()))
    return final_int
    #print(wos_documents)

def wosDocsdict(docs):
    # Create a dictionary from the row data and append to a list of all documents
    wos_documents = []
    # for dd in docs.values():
    #     wos_documents.append(dd)
    # wos_documents = pprint (vars(docs))
    # # wos_document = json.dumps(docs.__dict__)
    # for index in range(len(wos_document)):
    #     for key in wos_document[index]:
    #         wos_documents = wos_document[index][key]
    for e in chain.from_iterable(o.list for o in docs):
    # Do something for each element
        wos_documents.append(e)
    return (wos_documents)


# def names(tables):
#     name =  []
#     name.append(str(tables))
   
#     return json.dumps(names)

# wosCountry = []


# def normalizeCountries():
#     results = db.session.query(WoSDocumentsCountries).all()
#     for r in results:
