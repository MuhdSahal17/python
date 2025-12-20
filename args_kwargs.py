def shopping(*price,**item):
    print("--ITEMS--")
    for k,v in item.items():
        print(k,v)

    print("\n--Amount--")
    for i in price:
        print(i)
    total = sum(price)
    print(f"Total=",total)

shopping(2500,1200,5220,220,
        Item1 = "Dress" ,
         Item2 = "Shoes" ,
         Item3 = "Belt" ,
         Item4 = "suglass" )