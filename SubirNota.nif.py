def nif():
    resto=0
    numero= input("Dime tu NIF: ")
    letra="TRWAGMYFPDXBNJZSQVHLCKE"
    resto=numero%23
    print "Tu letra de DNI es; ",letra[resto]

nif()

    
