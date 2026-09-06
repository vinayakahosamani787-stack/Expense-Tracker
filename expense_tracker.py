print("$$$$$$<<<<EXPENSE TRACKER>>>>$$$$$$")
expense=[]
def menu():
    print("1. Add Expense\n2. View Expense\n3. Search Expense\n4. Update Expense\n5. Delete Expense\n6. Show Total Expense\n7. Exit")
while True:
    menu()
    try:
        choice=int(input("Enter the choice: "))
    except ValueError:
        print("Enter valid choice")
        continue
    if choice==1:
        exp_name=input("Enter the expense name: ")
        try:
            amount=int(input("Enter the amount: "))
        except ValueError:
            print("Enter valid amount")
            continue
        category=input("Enter the category: ")
        expense.append([exp_name,amount,category])
        print(expense)
    elif choice==2:
        for index,exp in enumerate(expense):
            print(f"{index} : {exp}")
    elif choice==3:
        cat_search=input("Enter the category you want to search: ")
        found=False
        for exp in expense:
            if cat_search==exp[2]:
                print(exp)
                found=True
        if not found:
            print("Category not found")
    elif choice==4:
        try:
            index=int(input("Enter the expense index: "))
        except ValueError:
            print("Enter valid index")
            continue
        if index in range(0,len(expense)):
            new_exp=input("Enter the expense name: ")
            try:
                new_amount=int(input("Enter the amount: "))
            except ValueError:
                print("Enter valid amount")
                continue
            new_cat=input("Enter the category: ")
            expense[index]=[new_exp,new_amount,new_cat]
            print(expense[index])
    elif choice==5:
        try:
            index=int(input("Enter the expense index: "))
        except ValueError:
            print("Enter valid index")
            continue
        if index in range(0,len(expense)):
            expense.pop(index)
            print(expense)
        else:
            print("Invalid index")
    elif choice==6:
        total=0
        for exp in expense:
            total+=exp[1]
        print(f"Total:{total}")
    elif choice==7:
        print("Exit")
        break
    else:
        print("Invalid choice")


        
    







    
    