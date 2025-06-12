from pymongo import MongoClient
#create connection
client = MongoClient('localhost',27017)

#create or access database called new
mydatabase = client.new

#create or access collection called myTable
mycollection=mydatabase.myTable 

#sample document to be added in database
'''rec={'name':'nima',
     'modules':['HPC','OOPS','AI/ML'],
      'day':12
     }
mycollection.insert_one(rec)'''

#inserting many documents
'''rec=[{'name':'nima',
     'modules':['HPC','OOPS','AI/ML'],
      'day':12
     },{
     'name':'rosy',
     'modules':['OOPS','AI/ML'],
      'day':12,
      'challenge':'Leapfrog'
     }]
mycollection.insert_many(rec)'''

# To find() all the entries inside collection
'''result=mycollection.find()
for record in result:
    print(record)'''

#some mongodb queries
'''for i in mycollection.find({'name':'rosy'}):
 print(i)

print(mycollection.count_documents({'name':'rosy'}))'''

#update
update=mycollection.update_one(
 {'name':'nima'},
 {
 '$set':{'name':'susma'},
 "$currentDate":{"lastModified":True}
 })
print(update)