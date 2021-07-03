lucky_numbers= [4,6,5,7,12,43,22]
friends = ["Allan","Mary","Pam","Simon","Brady","Jim"]
# friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1,"Chris")
friends.remove("Jim") #removes Jim
friends.pop() #removes last item off the list
lucky_numbers.sort()
year= input("Enter your year of birth:")
month= input("Enter your birth month:")
date= input("Enter the date of birth:")
password= ("Your Password is: " "#"+year+"#"+month+"#"+date)
print(password)


#print(friends.index("Mary")) #shows the index of Mary
#print(friends)
#print(lucky_numbers)

