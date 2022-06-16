from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps    # Ensures results are in JSON format


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:55525/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']

    # Complete this create method to implement the C in CRUD using insert().
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            return True
        else:
            raise Exception("False")

    # Complete this method to implement the R in CRUD using find()
    def read(self, data):
        if data is not None:
            return self.database.animals.find(data, { '_id': False} )     
        else:
             raise Exception("Nothing to find, because data parameter is empty.")
                
    # Update item based on parameter, which is the U in CRUD using update_many().
    def update(self, data, query):
        if data is not None and query is not None:
            # Check that document subject to change exists in collection using count_documents()
            if self.database.animals.count_documents(data) != 0:
                # data is the key value pair of document subject to change and $set to update document field.
                update_result = self.database.animals.update_many(data, {"$set": query})
                result = update_result.raw_result   # returns raw result from MongoDB Driver in JSON format
            else:
                result = "Document not found."
            return result
        else:
            raise Exception("Nothing to update, because data parameter is empty.")
                
            
    # Delete record based on parameter, which is the D in CRUD using delete_many().
    def delete(self, data):
        if data is not None:
            # Check that document subject to change exists in collection using count_documents()
            if self.database.animals.count_documents(data) != 0:
                remove_result = self.database.animals.delete_many(data) # data should be dictionary
                result = remove_result.raw_result    # returns raw result from MongoDB Driver in JSON format    
            else:
                result = "Document not found."
            return result
        else:
            raise Exception("Nothing to delete, because data parameter is empty.")

      
        
        


