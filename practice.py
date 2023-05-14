from amy import *
new = open("new.txt", "r") 
print(new.read())
new.close()
c='y'
while c=='y':   
    print("\n\nlist of practicals: ")
    print("1. To count the number of vowels")
    print("2. To count the number of blank spaces")
    print("3. To count a specific word")
    print("4. To the replace specific word")
    print("5. To copy the content of one file to another")
    d= int(input("what do you wanna do: "))      
    if d==1:
        count1()
    elif d==2:
        coblank()
    elif d==3:
        cospecific()
    elif d==4:
        replace()
        
    elif d==5:
        copy()
    else:
        print("invalid")
        break 
        
        




