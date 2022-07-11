def startup(): # this is unnecessary but cool
    e = open("main/cli-app/cli-app.txt", "r")
    value = (e.read())
    e.close()
    return value