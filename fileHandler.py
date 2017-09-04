def getDataFromFile(inputFilePath):
    days_file = open(inputFilePath, 'r')

    text = days_file.readlines()
    res = []

    for line in text:
        res.append(line.replace('\n', '').split(', '))

    return res
