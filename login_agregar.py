"""
Login
"""

flag = True

usuarios_login = [{"user": "carlos", "password": "123"},{"user": "rodri", "password": "123"}]

uss = usuarios_login[0]
uss1 = usuarios_login[1]

while flag == True:

    user = input("\nIngrese su usuario --> ");
    contra = input("Ingrese su contraseña --> ")

    if user == uss["user"] and contra == uss["password"]:
        print("")