import csv
from projections import convertGeometry




def writer(header, data, filename, option):
        with open (filename, "w", newline = "") as csvfile:
            if option == "write":

                movies = csv.writer(csvfile)
                movies.writerow(header)
                for x in data:
                    movies.writerow(x)
            elif option == "update":
                writer = csv.DictWriter(csvfile, fieldnames = header)
                writer.writeheader()
                writer.writerows(data)
            else:
                print("Option is not known")

def updater(filename):
    with open(filename, newline= "") as file:
        readData = [row for row in csv.DictReader(file)]
        for r in readData :
            r['lon'], r['lat'] = convertGeometry(r['lon'], r['lat'], "israel", "wgs84")
            print(r)



    readHeader = readData[0].keys()
    writer(readHeader, readData, filename, "update")

if __name__ == '__main__':
    updater("geocode.csv")

