import csv

def lab(x, y):       
    data = (str(x), str(y))

    exists = False
    with open('data.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if tuple(row) == data:
                exists = True
                break
            
    if not exists:
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)




         