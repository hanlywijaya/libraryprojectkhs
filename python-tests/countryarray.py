countries = ['Australia', 'China', 'Japan', 'New Zealand', 'United States of America']
capitals = ['Canberra', 'Beijing', 'Tokyo', 'Wellington', 'Washington']
askedcountry = input("Enter a country's name: ")
for i in range(len(countries)):
    if(askedcountry) == countries[i]:
        print("The capital of", countries[i], "is", capitals[i])
        break
    else:
        print("Country not found, please try again")
        break