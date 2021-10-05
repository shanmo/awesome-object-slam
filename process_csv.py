import csv
# filename = "Deep_learning.csv"
filename = "Object_SLAM.csv"
with open(filename,"rb") as source:
    rdr= csv.reader(source)
    with open("result.csv","wb") as result:
        wtr= csv.writer(result)
        for r in rdr:
            wtr.writerow((r[0], r[1]))