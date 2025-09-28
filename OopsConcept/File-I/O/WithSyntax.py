with open("hiiii.txt","r") as f:
    data=f.read()
    print(data)


with open("hiiii.txt","w") as f:
    f.write("new data")