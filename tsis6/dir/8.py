import os
path = r"/Users/madinayelmuratova/Desktop/pp2-22B030343/tsis6/dir/copy.txt"
if not os.path.exists(path=path):
    print("Doesnt exist")

os.remove(path)