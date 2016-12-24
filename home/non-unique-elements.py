
def checkio(data):
    data = [i for i in data if data.count(i) > 1]
    return data