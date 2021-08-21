import pandas

data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("SampleData2.txt")
data1And2 = pandas.concat([data1, data2])
data1And2.to_csv("SampleData12.txt", index=None)

