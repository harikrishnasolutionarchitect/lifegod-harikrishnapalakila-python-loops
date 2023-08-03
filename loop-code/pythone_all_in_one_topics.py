def pythontutorial():
 print("=================>>> Python Tutorial <<<=========================")
 print("")
 print("Learning Python")
 print("")
 print("python is a popular programming language ")
 print("python can be used on server to implement and create web applications")
 print("")
 print("Learning python with examples")
 print("")
 print("we have python free online compliers so just we need to search on internet for pythone compliers")
 print("")

pythontutorial()

def pythontopics():
    print("1) python variables handling...!")
    print("2) python datatypes handling...!")
    print("3) python Numbers handling...!")
    print("4) pythone strings handling...!")
    print("5) python list handling ...!")
    print("python tuples handling ...!")
    print("pythone set handling ...!")
    print("python dictionaries..!")
    print("python if..elif..if handling..!")
    print("python loops - for , while , case handling...!")
    print("python function....!")
    print("python Arrarys...!")
    print("python file-handling...!")
    print("python Database - mysql + mongodb - handling...!")


pythontopics()

def start():
    print("")
    print("Program started...")
    print("Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule. Python is dynamically typed and garbage-collected")
    print("")

def usage():
    print("")
    print("Usage: kindly pass atleast 2 arguments and values")
    print()

def space():
    print("")
    print("")
    print("")


def end():
    print("")
    print("Program ended...")
    print("=========== END ===============")

start()
usage()
def add(n1, n2):
    add = n1 + n2
    return add
result = add(1, 2)
print(result)
end()
space()
space()

start()
usage()
def sub(n1, n2):
    sub = n1 - n2
    return sub
result = sub(1, 2)
print(result)
end()



pythontutorial()

pythontopics()

print("")
print("===========================> 4) python strings handling <===========================")
print("")
print("Usage:")
print("")
print("  1) Use Total / combine Method -- Total String Name                            : ")
print("  2) Use Reverse Method - Last Index of the string is                           : ")
print("  3) Use Last Index find Method - Last character of the string is               : ")
print("  4) Use Len Method to print length of string - Total Length of the string is   : ")
print("")

def stringshandling():
 name="hari"
 print("")
 print("Total String Name               : ", name[0]+name[1]+name[2]+name[3])
 print("Last Index of the string is     : ", name[-1]+name[-2]+name[-3]+name[-4])
 print("Last character of the string is : ", name[-1])
 print("Total Length of the string is   : ", len(name))
 print("")
 print("")
 print("=============> Using Add operator to combine strings <==============")
 print("")
 print("Usage:")
 print("Add operator")
 print("")
 a="hari"
 b="krishna"

 print("Adding character by character :", a[0]+a[1]+a[2]+a[3]+b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+a[3]+a[3]+a[3]+a[3]+a[3]+a[3]+a[3]+a[3]+a[3]+b[2]+b[3]+b[4]+b[5]+b[6]+a[3]+a[3]+a[3]+a[3]+a[3])
 print("Adding word Strings           :", b[-8:-1]+a[0:3]+a+b+a+b+a+b+a+b+a+b+a+b+a+b+a+b+a+b+a+b+a+b+a+b+a[0]+a[1]+a[2]+a[3]+b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+a[3]+a[3]+a[3]+a[3]+a[3]+a[3])
 print("Adding words Strings           :", a+b+b+a)
stringshandling()




print("")
print("===========================> 5) python list handling <===========================")
print("")
print("Usage:")
print("")


def listhandling():
    l = ["hari", "krishna", "deloitte"]
    l1=["Hyndai-creta1", "BMW1", "AUDI1"]
    l1.insert(4, 'venue')
    l1.append('i20')
    print(l1)
    print(l)
    print("Add Operator on list : ", l[0]+l[1])
    print("Adding word by word : ", l[0]+l[1]+l[2])
    print("Adding 2 list using extend:", l.extend(l1), l)

listhandling()


print("=================== fruits list handling ========================")

"""
fruit_list = ["Apple", "Banana"]

print(f'      Current Fruits List            :  {fruit_list}   ')

new_fruit = input("Please enter a fruit name:   ")

fruit_list.append(new_fruit)

print(f'Updated Fruits List {fruit_list}')


print("=================== END ========================")

print("")
print("")
"""
"""
print("=================== cars list handling ========================")

cars_list = ["audi", "bmw", "venue"]
print(f' All cars list : {cars_list} ')

new_car = input("Please enter a new car name:    ")
cars_list.append(new_car)

print(f' Updated cars list: {cars_list} ' )


print("=================== END ========================")
print("")
print("")


print("=================== EMI  list handling ========================")
emi = ["2000", "10000", "30000"]

print (f' Total EMI List : {emi} ')


new_emi_details=input("Enter New EMI Details : ")

emi.append(new_emi_details)

print(f' Updated emi list details:  {emi}')

print("=================== END ========================")
print("")
print("")


print("=================== AXIS BANK LOAN EMI  list handling ========================")

emi_details = ["10000", "20000", "30000"]
print(f' Total EMI Details : {emi_details}' )
new_emi_details = input("enter new emi details : ")
emi_details.append(new_emi_details)
print(f' Update emi details list : {emi_details}')
print("")
print("")

print("=================== END ========================")
print("")
print("")

"""
"""
print("=================== Gold Loan list Details ========================")

gold_rings_list = ["plain circle ring", "2 stone way ring", "10k-rings-2"]

print(f' Total Gold Rings list : {gold_rings_list}')

new_ring = input("Enter new ring details : ")

gold_rings_list.append(new_ring)

print(f'{gold_rings_list}')

gold_rings_list.insert(4, "sliver-ring")

print(f'{gold_rings_list}')

gold_rings_list.insert(5, "platinum-ring")

print(f'{gold_rings_list}')

index=int(input(f"Please enter index number between 0 and {len(gold_rings_list) - 1} :  "))
name=input("Please enter new ring new:  ")
gold_rings_list.insert(index, name)
print(f'{gold_rings_list}')
"""

print("=========================  Bike list handling ====================")
print("")

bikes_list=["KTM", "Harley Davidson x440","Suzuki Gixxer"]
new_bikes_list=[]

print(f' ALL Bikes List : {bikes_list}')

bikes_list.append("Ducati")
print(f'Updated bike list : {bikes_list}')
bikes_list.append("Yamaha")
bikes_list.append("2023 Hero Xpulse 200 4V")
bikes_list.append("Honda Shine 100")
bikes_list.append("Yamaha FZ-X")
print(f'Update all Cheap Bikes List : {bikes_list}')
bikes_list.insert(8, "2023 Yamaha YZF-R15")
print(f' Update all Cheap Bikes list ----- : {bikes_list}')
print(" Length of the Bikes list ", len(bikes_list))
print("")
print("")






"""
new_bike_position=int(input("Enter bike number :"))
new_bike_name=input("Enter new bike Name : ")
new_bikes_list.insert(new_bike_position, new_bike_name)
print(f' New Bikes list : {new_bikes_list}')

for a in range(0,new_bike_position):
    print(f'Adding New Bike Details')
    new_bikes_list.insert(new_bike_position, new_bike_name)

print(f'Updated New Bike List : {new_bikes_list}')
"""
"""
a=int(input("Enter the No. of Bikes : "))
b=input("Enter Bike Name: ")

for c in range(0,a):
 new_bikes_list.insert(a, b)
 bikes_list.extend(new_bikes_list)
 bikes_list.append(b)

print(f'{new_bikes_list}')
print(f'{bikes_list}')
"""

"""
a=input("Enter elements : ")
b=a.split()
print('list : ' ,b)

for c in range(len(b)):
    b[c]=int(b[c])
print(c)
"""

'''
list=[]
print(len(list))
'''


list1=[1,2,3,4]
list3=[5,6,7,8]
cars=["Audi A4,Audi a4 2021,Audi A40", "A4"]
bikes=["KTM","DUKE", "GIXXER"]
print(len(list1))
print(list1[0])
print(list1[-3])
print(list1[0:-2])
print(list)
list1[0:1]=[10,11]
print(list1)
print(1 in list1)
print(2 in list1)
print(3 in list1)
print(4 in list1)
print(5 in list1)
list1.append(5)
print(list1)
for a in list1: 
    print("List of Number are :", a) 
    '''
    list1.insert(6, 6)
    list1.insert(7, 7)
    list1.remove(7)
    list1.remove(6)
    list1.remove(5)
    list1.remove(4)
    '''
    a += 1
    a += 2
    print(list1)
    print("for loop output: ",a)
    list2=list1.copy()
    print(" Copied Listed Details are : ",list2)
    list4=list3.extend(list1)
    print("Combine all list details : ",list3)
    newcars=cars.copy()
    print("New cars - List5  details : ", newcars)
    vizagcars=cars.copy()
    print("Vizag Audi Cars List : ", vizagcars)
    Mumbaicarslist=cars.copy()
    print("Mumbai Audi Cars List: ", Mumbaicarslist)
    Vizagbikes=bikes.copy()
    print("Vizag Bike List : ", Vizagbikes)
    Vizagbikes=cars.copy()
    print("Car and bike list:", Vizagbikes)
    Vizagbikes=bikes.remove("KTM")
    print("Removed KTM Bike from List:", Vizagbikes)

    break

print("====hari====")


list2=[0.1,1.0,1.1,1.2,]
print(len(list2))
print(list2[0])
print(list2[-3])
print(list2[-1])

















print("")
print("===========================> 6) python Tuple handling =====================")
print("")
print("Usage:")
print("")

def tupleshandling():
    t = ("hari", "krishna", "deloitte", "apple")
    f=("apple","kiwi")
    c=("Hyndai-creta", "BMW", "AUDI")
    print(t)
    print("Add Operator on tuple: ", t[0]+t[1])
    print("Adding words by words :", c[0]+c[1]+t[3]+t[2]+t[0]+t[2]+t[3]+f[1])

tupleshandling()




print("")
print("")
print("")
print("=========== Strings Operations ==================")