from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

#BHobbs
#SNHU CS-340
#Sept 21, 2021
#Example code found at w3schools.com/python/python_mongodb_fid.asp

class AnimalShelter(object):

    #constructor to init the mongodb
    #to do: this should be a singleton
    def __init__(self):
        
        #URI must be percent escaped as per pymongo documentation
        userName = urllib.parse.quote_plus('aacUser')
        password = urllib.parse.quote_plus('abc123')
        
        self.client = MongoClient('mongodb://%s:%s@localhost:41439/?authSource=AAC' % (userName, password))
        self.dataBase = self.client['AAC']
       
    #Mehtod to create a record
    #Input data formatted as per the Pymongo API
    #Example: ({""name": "Rex", 'age_upon_outcome': '2 months'})
    def createRecord(self, data):
        if data is not None:
            insertValid = self.dataBase.animals.insert_one(data)
            #check the status of the inserted value 
            return True if insertValid.acknowledged else False
	
        else:
            raise Exception("No document to save. Data is empty.")
    
    #todo implement the R
    #get documents by the GUID
    #This is more for a test but could be used after the createRecord
    #Since the document returned by insert_one contains the newly created _id
    def getRecordId(self, postId):
        _data = self.dataBase.find_one({'_id': ObjectId(postId)})
                                  
        return _data
    
    #Get records with criteria
    #All records are returned if criteria is None
    #Default is None
    #Example: ({""name": "Rex", 'age_upon_outcome': '2 months'})
    #do not return the _id
    def getRecordCriteria(self, criteria = None):
        if criteria is not None:
            _data = self.dataBase.animals.find(criteria, {'_id' : 0})
                                 
        else:
            _data = self.dataBase.animals.find({}, {'_id' : 0})
                                  
        return _data
