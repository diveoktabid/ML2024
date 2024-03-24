# Latihan Basic -1
print('Latihan Basic -1 :')
print("Hello, Python!")
print("Nama Saya Adalah")
print('Dive Oktabid Fikhri')
print('=================================')

# Latihan Formatting dengan spesial character
print('# Latihan Formatting dengan spesial character : ')
print("\nNama saya","Dive", end=" ")
print("Fikhri")
print('\n==================================')

# Latihan membuat formatting pola bintang
print()
print('Latihan membuat formatting pola bintang : ')
print()
print("    *    "*2)
print("   * *   "*2)
print("  *   *  "*2)
print(" *     * "*2)
print("***   ***"*2)
print("  *   *  "*2)
print("  *   *  "*2)
print("  *****  "*2)
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n"*2)
print('\n====================================')

# Membuat bangun datar persegi dengan replication
print()
print('Membuat bangun datar persegi dengan replication :')
print("+" + 10*"-" + "+")
print(("|" + 10*" " + "|\n") * 5, end="")
print("+" + 10*"-" + "+")
print('\n====================================')

# cara berbicara ke komputer
print()
print('cara berbicara ke komputer :')
print("Katakan sesuatu...")
sesuatu = input()
print("mmmmm", sesuatu, " Oke")
print('\n====================================')

# latihan variables
print()
print('latihan variable :')
kilometer = 12.25
mil = 7.38

miles_to_kilometers = mil * 1.61
kilometers_to_miles = kilometer / 1.61

print(mil, "1 mil adalah", round(miles_to_kilometers, 2), "kilometer")
print(kilometer, "1 kilometer adalah", round(kilometers_to_miles, 2), "mil")