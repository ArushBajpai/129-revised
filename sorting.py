import csv

data = []

with open("bright_stars.csv","r") as f :
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
star_data = data[1:]

# print(moon_data.__sizeof__)

for data_point in star_data:
    data_point[2] = data_point[2].lower()


# moon_data.sort()
star_data.sort(key = lambda moon_data: moon_data[2])

with open("star_data1.csv","a+") as f :
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)

with open('star_data1.csv') as input, open('sorted.csv','w',newline = '') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row) 
