import csv
import psycopg2 as pgsql


connection=pgsql.connect(host="localhost", dbname="postgres", user="postgres",password="mmnf98040517", port=5432)
cur=connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS PhoneBook (
    surname VARCHAR(255),
    name VARCHAR(255),
    number INT
);
""")

def update(sn, mode, newv):
    cur.execute("""UPDATE PhoneBook
    SET {} = '{}'
    WHERE surname = '{}'
    """.format(mode,newv,sn))

def delete(sn):
    cur.execute("""DELETE FROM Phonebook
    WHERE surname='{}'
    """.format(sn))

#Вставка данных

mode="enter";
while True:
    print("Type 'enter' if you want to add more data and type 'stop' to break")
    mode=input()
    if mode=="stop":
        break
    mytuple=[]
    print("enter surname:")
    mytuple.append(input())
    print("enter name:")
    mytuple.append(input())
    print("enter number:")
    mytuple.append(input())
    mytuple=tuple(mytuple)
    cur.execute("""INSERT INTO PhoneBook (surname, name ,number) VALUES
    {};
    """.format(mytuple))


#Обновление данных
while True:
    print("Type 'update' to update some data or 'stop' to break")
    mode=input()
    if mode=="stop":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Enter surname")
    idtochange=input()
    print("What you want to change? name/number")
    mode=input()
    print("Enter new name/number")
    newvalue=input()
    update(idtochange, mode, newvalue)

#Удаление
while True:
    print("want to delete some data? yes or no")
    mode=input()
    if mode=="no":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Enter surname")
    idtodelete=input()
    delete(idtodelete)


connection.commit()
cur.close()
connection.close()