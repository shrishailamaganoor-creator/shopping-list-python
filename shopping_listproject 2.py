print("="*62)
print( """Make your shopping list""" )
print("="*62)
shopping_list = [ ]
while True:
    add = input("tell me if u want to add an item to your list y/n:").lower().strip
    if add in ["yes","y"]:
             item = input("Enter the item:").strip()
             shopping_list.append(item)
    elif add in ["no","n"]:
             break
    else:
        print("please enter yes or no")
    
print('Your shopping list would be')
count= 1
for item in shopping_list:
    print(count,".",item)
    count+=1
print("thank you") 
