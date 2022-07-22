import csv, os

# path = os.path.join, img_file.filename)) 
# opening the CSV file
def read_csv(path):
    with open(path, mode ='r') as file:
        #print(path)
        # reading the CSV file
        csvFile = csv.reader(file)
        data = []
        # displaying the contents of the CSV file
        #print(type(csvFile))
        for lines in csvFile:
            data.append(lines)
        return data
