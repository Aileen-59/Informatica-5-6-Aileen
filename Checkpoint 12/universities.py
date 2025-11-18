universities = {
    "Eastern Arizona College":{"distance":"404.4","num_majors": "90","price":"8370"},
    "UACJ":{"distance":"11.3","num_majors":"60","price":"2250"},
    "Tecmilenio":{"distance":"202.1","num_majors":"43","price":"30000"},
    "LaSalle":{"distance":"299.7","num_majors":"42","price":"60000"},
    "UTP":{"distance":"8.8","num_majors":"4","price":"2505"}
}
def main():
    name = input("Type the name of the university: ")
    if name not in universities:
        print("Sorry, that university is not in our list.")
    else:
        uni = universities[name]
        print(uni)
    api = requests.get("http://universities.hipolabs.com/search?name="+universities[uni]["officiald_name"])
    print(api.json())
    
main()