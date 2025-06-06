menu_item = ["pen","pencil","book"]
prices= [2.99,6.2, 13.33]


for item , price in zip(menu_item,prices):
    print(f"{item:<12} {price:>5.2f}$")
