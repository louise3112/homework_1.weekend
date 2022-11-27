# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, change_in_cash):
    pet_shop["admin"]["total_cash"] += change_in_cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, increase):
    pet_shop["admin"]["pets_sold"] += increase

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets_by_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
    
    return None

def remove_pet_by_name(pet_shop, pet_name):
    pet_to_remove = find_pet_by_name(pet_shop, pet_name) #creates variable to hold relevant dictionary in pets list
    pet_shop["pets"].remove(pet_to_remove)

def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash_to_remove):
    customer["cash"] -= cash_to_remove

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet_to_add):
    customer["pets"].append(pet_to_add)

def customer_can_afford_pet(customer, pet):
    if get_customer_cash(customer) >= pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):
    #Check pet is in shop and customer can afford pet:
    if pet != None and customer_can_afford_pet(customer, pet) == True:    
        #Add pet to customer:
        add_pet_to_customer(customer, pet)

        #Remove pet from shop and increase count of pets sold by 1:
        pet_name = pet["name"]
        remove_pet_by_name(pet_shop, pet_name)
        increase_pets_sold(pet_shop, 1)

        #Remove cost of pet from customer:
        pet_cost = pet["price"]
        remove_customer_cash(customer, pet_cost)

        #Add cash from sale of pet to shop total cash:
        add_or_remove_cash(pet_shop, pet_cost)
