countryname = input()
timevisits = int(input())
list_of_cities = eval(input())

travel_log = [
    {
        "country":"France",
        "numbertimes":12,
        "cities_visited":["Paris","Little","Dijon"],
        
    },
    {
        "country":"Germany",
        "numbertimes":132,
        "cities_visited":["Berlin","Hamburg","Stuttard"],
    },
] 

def addnewcountry(name, times, cities):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times
    new_country["cities"] = cities
    travel_log.append(new_country)

addnewcountry(countryname, timevisits , list_of_cities)
print(f"Ive been to {travel_log[2]['country']}") #kalo dictionary, pengarahnya adalah namanya sendiri, 
#sedangkan kalo list, pengarahnya adalah nomor index disini 2 karena list, kalo 2 : baba baru pake 2





