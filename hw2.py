firt_name=input("write your name:")
last_name=input("write your last name:")
age=int(input("write your age:"))
year=int(input("write your date of year:"))

bilg_list=[]
bilg_list.append(firt_name)
bilg_list.append(last_name)
bilg_list.append(age)
bilg_list.append(year)


for i in bilg_list:
    if(i==age  and i<18):
        print("You can not go out because it's too dangerous")
    elif(i==age and i>18):
        print("You can go out the street")