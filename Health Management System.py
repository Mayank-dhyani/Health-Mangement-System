#HEALTH MANGEMENT SYSTEM
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        print("PRESS 1). DIET")
        print("PRESS 2). EXERCISE")
        num = int(input())
        if num == 1:
            f = open("rohan_lock.txt", "a")
            value = str(input("ENTER TO EDIT DIET"))
            x = str(datetime.date.today())
            f.write("1) " + x + ":- " + value.title() + "\n")
            f.close()
            print("SUCCESSFULLY WRITTEN")
        elif num==2:
            f = open("rohan_rt.txt", "a")
            value = str(input("ENTER TO EDIT EXERCISE"))
            x = str(datetime.date.today())
            f.write("1) " + x + ":- " + value.title() + "\n")
            f.close()
            print("SUCCESSFULLY WRITTEN")
        else:
            print("not present")

    elif k==2:
        print("PRESS 1). DIET")
        print("PRESS 2). EXERCISE")
        num = int(input())
        if num == 1:
            f = open("mayank_lock .txt", "a")
            value = str(input("ENTER TO EDIT DIET"))
            x = str(datetime.date.today())
            f.write("1) " + x + ":- " + value.title() + "\n")
            f.close()
            print("SUCESSFULLY WRITTEN")
        elif num == 2:
            f = open("mayank_rt.txt", "a")
            value = str(input("ENTER TO EDIT EXERCISE"))
            x = str(datetime.date.today())
            f.write("1) " + x + ":- " + value.title() + "\n")
            f.close()
            print("SUCESSFULLY WRITTEN")
        else:
            print("not presnt")

    elif k==3:
        print("PRESS 1). DIET")
        print("PRESS 2). EXERCISE")
        num = int(input())
        if num == 1:
            f = open("paras_lock.txt", "a")
            value = str(input("ENTER TO EDIT DIET"))
            x = str(datetime.date.today())
            f.write("1) " + x + ":- " + value.title() + "\n")
            f.close()
            print("SUCESSFULLY WRITTEN")
        elif num == 2:
            f = open("paras_rt.txt", "a")
            value = str(input("ENTER TO EDIT EXERCISE"))
            x = str(datetime.date.today())
            f.write("1) " + x + ":- " + value.title() + "\n")
            f.close()
            print("SUCESSFULLY WRITTEN")
        else:
            print("not present")

    else:
        print("not present")

def retrieve(k):
    if k==1:
        print("PRESS 1). DIET")
        print("PRESS 2). EXERCISE")
        num = int(input())
        if num==1:
            f = open("rohan_lock.txt", "rt")
            x = str(datetime.date.today())
            value=str(f.read())
            print("1) " + x + ":- " + value.title() + "\n")
            f.close()
            print("SUCESSFULLY WRITTEN")
        else:
            f = open("rohan_rt.txt", "rt")
            x = str(datetime.date.today())
            value = str(f.read())
            print("1) " + x + ":- " + value.title() + "\n")
            f.close()
            print("SUCESSFULLY WRITTEN")

    elif k==2:
        print("PRESS 1). DIET")
        print("PRESS 2). EXERCISE")
        num = int(input())
        if num==1:
            f = open("mayank_lock .txt", "rt")
            x = str(datetime.date.today())
            value = str(f.read())
            print("1) " + x + ":- " + value.title() + "\n")
            f.close()
            print("SUCESSFULLY WRITTEN")
        else:
            f = open("mayank_rt.txt", "rt")
            x = str(datetime.date.today())
            value = str(f.read())
            print("1) " + x + ":- " + value.title() + "\n")
            f.close()
            print("SUCESSFULLY WRITTEN")



    elif k==3:
        print("PRESS 1). DIET")
        print("PRESS 2). EXERCISE")
        num = int(input())
        if  num==1:
            f = open("paras_lock.txt", "rt")
            x = str(datetime.date.today())
            value = str(f.read())
            print("1) " + x + ":- " + value.title() + "\n")
            f.close()
            print("SUCESSFULLY WRITTEN")
        else:
            f = open("paras_rt.txt", "rt")
            x = str(datetime.date.today())
            value = str(f.read())
            print("1) " + x + ":- " + value.title() + "\n")
            f.close()
            print("SUCESSFULLY WRITTEN")


    else:
        print("not present")
print("PRESS 1). WRITE")
print("PRESS 2). RETRIEVE")
a=int(input())
if a==1:
    print("you have a 3 Options to Chosse:-")
    print("\t\t\t\t\t\t\t\t1):- ROHAN")
    print("\t\t\t\t\t\t\t\t2):- MAYANK")
    print("\t\t\t\t\t\t\t\t3):- PARAS")
    b=int(input())
    take(b)
else:
    print("you have 3 option to  choose :-")
    print("\t\t\t\t\t\t\t\t1):- ROHAN")
    print("\t\t\t\t\t\t\t\t2):- MAYANK")
    print("\t\t\t\t\t\t\t\t3):- PARAS")
    b=int(input())
    retrieve(b)


