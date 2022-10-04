#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 02:49:10 2022

@author: brandonhobbs_snhu
"""
#Driver for testing CRUD 
import datetime
from CRUD import AnimalShelter
animals = AnimalShelter('abc123')

#query for a random record that is known to exist
print("Read Test. 1 record should be returned. \n")
query = animals.getRecordCriteria({"name": "Rex", 'animal_id': 'A714450'})
for docs in query:
    print(docs)

print("\nCreate Test. 1 record should be written and True returned. \n")
#True for success
#False for failed
print(animals.createRecord({
          'age_upon_outcome': "1 year",
          'animal_id': 'test_id', 
          'animal_type': 'test', 
          'breed': 'test breed', 
          'color': 'color', 
          'date_of_birth': '1900-01-01', 
          'datetime': '1900-01-01 12:00:00', 
          'monthyear': '1900-01-24T12:00:00', 
          'name': 'name', 
          'outcome_subtype': '', 
          'outcome_type': 'test', 
          'sex_upon_outcome': 'test', 
          'location_lat': 10.10, 
          'location_long': -10.10, 
          'age_upon_outcome_in_weeks': 123.123
          })
      )
 
print("\nRead Test of name:name. 1 record should be returned. \n")
query = animals.getRecordCriteria({"name": "name", 'age_upon_outcome': '1 year'})
for docs in query:
    print(docs)
    
print("\nUpdate Test. False should be returned. \n")
print(animals.updateRecord(
        {"name": "  ", 'age_upon_outcome': '-99 year'},
    {'datetime': "12"}
    )
    )
    
print("\nUpdate Test of name:name. True should be returned. \n")
_newDateTime = str(datetime.datetime.now())
print(animals.updateRecord(
        {"name": "name", 'age_upon_outcome': '1 year'},
    {'datetime': _newDateTime}
    )
    )
   
print("\nRead Test of name:name. datetime should be {}. \n".format(_newDateTime))
query = animals.getRecordCriteria({"name": "name", 'age_upon_outcome': '1 year'})
for docs in query:
    print(docs)

print("\nProperties should be 1 and 1\n")  
print("The records matched were {} and updated were {}".format(animals.records_matched, animals.records_updated))

print("\nDelete Test of name:name. True should be returned. \n")  
print(animals.deleteRecord({
        "name": "name", 'age_upon_outcome': '1 year'
        })
    )

print("\nThe deleted documents should be 1\n")
print("The documents deleted were {}".format(animals.records_deleted))

print("\nDelete Test of name:name. Exception should be raised. \n")  
print(animals.deleteRecord({}))