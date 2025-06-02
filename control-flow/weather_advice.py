weather=input("what's the weather like today?(sunny/rainy/cold): ").lower()
if weather=="sunny":
    print("wear a tshirt and sunglasses.")
elif weather=="rainy":
    print("don't forget your umbrella and a raincoat")
elif weather=="cold":
    print("make sure to wear  a warm coat and a scarf")
else:
    print("sorry ,I don't have recommendations for this weather.")
