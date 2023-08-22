import csv

# filename = "Criminal_count.csv"
# num=0
# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow([5])
"""def insertData(data):
    field=['Name', "Father's Name", "Gender", "DOB","Crimes"]
    x=[data['Name'], data["Father's Name"], data['Gender'], data['DOB(yyyy-mm-dd)'], data['Crimes Done']]
    filen = "Criminal.csv"
    with open(filen, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(field)
        csvwriter.writerow(x)"""




import csv

def insertData(data):
    field=['Name', "Father's Name", 'Gender', 'DOB', 'Crimes']
    x=[data['Name'], data["Father's Name"], data['Gender'], data['DOB(yyyy-mm-dd)'], data['Crimes Done']]
    filen = "Criminal.csv"
    with open(filen, 'a', newline='') as csvfile:  # Open the file in append mode ('a') instead of write mode ('w')
        csvwriter = csv.writer(csvfile)
        if csvfile.tell() == 0:  # Check if the file is empty (no previous rows)
            csvwriter.writerow(field)  # Write the field (column headers) only once
        csvwriter.writerow(x)  # Write the row of data



# def insertData(data):
#     print(data['Name'])
#     rowId=0
#     db=sqlite3.connect('profile.db')
#     cursor=db.cursor()
#     print("Opened Database")

#     query = "INSERT INTO criminaldata VALUES(NAME,FATHER NAME, GENDER, DOB, CRIMES);" % \
#             (data['Name'], data["Father's Name"], data['Gender'],
#              data['DOB(yyyy-mm-dd)'], data['Crimes Done'])

#     cursor.execute(query)
#     db.commit()
#     rowId=cursor.lastrowid
#     print("RowId %d" % rowId)

#     print("Record Created")
#     db.close()
#     return rowId



# def insertData(data):
#     # print(data)
# 	rowId = 0
# 	db = sqlite3.connect('test.db')
#     cursor = db.cursor()
#     # cursor=db.cursor()
# 	print("Opened database Succesfully")

# 	query = "INSERT INTO criminaldata VALUES(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
#             (data["Name"], data["Father's Name"], data["Mother's Name"], data["Gender"],
#              data["DOB(yyyy-mm-dd)"], data["Blood Group"], data["Identification Mark"],
#              data["Nationality"], data["Religion"], data["Crimes Done"])

#     cursor.execute(query)
#     db.commit()
#     rowId = cursor.lastrowid
#     print("data stored on row %d" % rowId)

#     db.commit()
# 	print ("Records created successfully");
# 	db.close()
# 	return rowId
