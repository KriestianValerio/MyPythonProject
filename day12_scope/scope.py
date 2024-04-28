# enemies = 1

# def increased_enemies():
#         enemies = 2
#         print(f"there are {enemies}")
        
# increased_enemies()
# print(f"enemies outside function {enemies}")

# Local Scope
# def drink_potion():
#         potion_strength = 2 # define variabel ini hanya berlaku di dalem def, jadi diluar ini ga terdefinisi
#         print(potion_strength)

# Global Scope


# drink_potion() # kalo kek gini dia jadi lokal, does not work

# # There is no Block Scope

# if 3>2:
#         a_variable = 10

# print(a_variable) #ini bisa work, jadi block hanya ada di def function, kalo if or for or while, bs tembus

# pengaruh global
# enemies = 1

# def increase_enemies(): 
# #     global enemies # memasukkan global var enemies ke local
# #     enemies2 = enemies + 1
#     global enemies # kalo gaada ini, dia bingung enemies nya ditambah terus masukin ke mana, gaada varnya
#     enemies += 1
#     print(enemies)

# increase_enemies()

# player_health = 10 # this has global scope, bisa masuk ke def

# def drink_potion():
#         potion_strength = 2 # this is local variable
#         print(player_health)

# drink_potion()

enemies = 1
def increase_enemies():
    print(enemies)
    return enemies + 1

print(increase_enemies())













                        

