import os
l = [10, 20, 30, 40, 50]
with open("mm.txt", "w+") as f:
    for i in l:
        f.write(f"{str(i)} \n", )
for i in range(97, 123):
    f = open(f"/Users/madinayelmuratova/Desktop/pp2-22B030343/tsis6/dir/mm.txt{chr(i)}.txt", "w")
    f.close()


with open("mm.txt") as f:
    with open('copy2.txt', "w") as cop:
        for line in f:
            cop.write(line)

path = r"/Users/madinayelmuratova/Desktop/pp2-22B030343/tsis6/dir/copy2.txt"
if not os.path.exists(path=path):
    print("Doesn't exist")
else:
    print("Exists")
