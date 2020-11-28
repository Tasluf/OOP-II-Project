Doctor = [("191-45041", "Jasim", "admin"), ("191-45042", "karim", "admin"), ("191-45043", "Rahim", "admin"), ("191-4504", "Masum", "admin"), ("191-4505", "Jon", "admin")]
Patient = [("192-65441", "Jasim", "admin"), ("192-65442", "karim", "admin"), ("192-65443", "Rahim", "admin"), ("192-65444", "Masum", "admin"), ("192-65445", "Jon", "admin")]


def Authentication(id, password):
    id_first = id.split("-")
    if id_first[0] == "191":
        for i in Doctor:
            if i[0] == id and i[2] == password:
                print("-----------Doctor profile-----------")
                print("Welcome Mr. {}".format(i[1]))
                return
        else:
            print("Id or Password is incorrect")
    elif id_first[0] == "192":
        for i in Patient:
            if i[0] == id and i[2] == password:
                print("-----------Patient profile-----------")
                print("Welcome {}".format(i[1]))
                return
        else:
            print("Id or Password is incorrect")
    else:
        print("Your Id is incorrect")


if __name__ == '__main__':
    print("---------------------------------------Log In Page---------------------------------------")
    id = input("Enter your Id: ")
    password = input("Enter your Password: ")
    Authentication(id, password)