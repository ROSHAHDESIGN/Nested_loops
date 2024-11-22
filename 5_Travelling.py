
while True:
    destination = input() #vseki pyt poluchavam destinacia

    if destination == "End":#ako vidi End spira
        break
    min_budget = float(input()) #vseki pyt poluchavam budget
    money = 0.0 #opredelyam money koito vseki edin pyt sa 0.0
    #vseki pyt money se RESTARTIRA,  zapochva ot nachalo

    while money < min_budget: #filter na WHILE
        new_income = float(input())
        money += new_income #new_income tryabva da se dobavi kym money
        #parite shte se trupat v money dokato stanat > min budget


    print(f"Going to {destination}!")


