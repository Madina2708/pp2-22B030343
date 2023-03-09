def string(s):
    k={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
           k["upper"]+=1
        elif c.islower():
           k["lower"]+=1
        else:
           pass
    print ("String : ", s)
    print ("Number of Upper case characters : ", k["upper"])
    print ("Number of Lower case Characters : ", k["lower"])

string('bfrbfHHJhb')