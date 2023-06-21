from controlador.dto_trabajador import TrabajadorDTO

def validarLogin():
    usuarioTrabajador = input("Ingrese Nombre de Usuario:\n")
    claveTrabajador = input("Ingrese su Clave de Usuario:\n")
    resultado = TrabajadorDTO().validarLogin(usuarioTrabajador,claveTrabajador)
    return resultado


def inicio(user):
    tipoUser = TrabajadorDTO().tipoDeUsuario(user[0],user[1])
    if tipoUser[0] == 'Administrador'.capitalize() and tipoUser[1] == 'RRHH'.upper():
        menuAdministradorRRHH(user)
    elif tipoUser[0] == 'Gerente'.capitalize() and tipoUser[1] == 'Gerencia'.capitalize():
        menuGerencia(user)
    else:
        menuTrabajadores(user)
        
        
def menuAdministradorRRHH(user):
     while True:
        print("Bienvenid@ al Menu de Administrador")
        print("\nPor favor elige una opción del siguiente menú:")
        print("1. Ver Mis Datos")
        print("2. Registrar Trabajador")
        print("3. Opción 3")
        print("4. Opción 4")
        print("5. Opción 5")
        print("6. Salir")
        
        try:
            choice = int(input("\nTu elección: "))
        except ValueError:
            print("\n¡Error! Por favor, introduce un número.")
            continue
            
        if choice == 1:
            print("\nHas elegido la opción 1")
            datosUser = TrabajadorDTO().mostrarDatosPorUseryPass(user[0],user[1])
            print(f'Estos son tus datos en el sistema: \n{datosUser}')
            
        elif choice == 2:
            print("\nHas elegido la opción 2")
        elif choice == 3:
            print("\nHas elegido la opción 3")
        elif choice == 4:
            print("\nHas elegido la opción 4")
        elif choice == 5:
            print("\nHas elegido la opción 5")
        elif choice == 6:
            print("\nHas elegido salir. ¡Hasta luego!")
            break
        else:
            print("\n¡Error! Por favor, elige una opción válida.")
    
      
def menuGerencia(user):
    while True:
        print("Bienvenid@ al Menu Gerencial")
        print("\nPor favor elige una opción del siguiente menú:")
        print("1. Ver Mis Datos")
        print("2. Opción 2")
        print("3. Opción 3")
        print("4. Opción 4")
        print("5. Opción 5")
        print("6. Salir")
        
        try:
            choice = int(input("\nTu elección: "))
        except ValueError:
            print("\n¡Error! Por favor, introduce un número.")
            continue
            
        if choice == 1:
            print("\nHas elegido la opción 1")
            datosUser = TrabajadorDTO().mostrarDatosPorUseryPass(user[0],user[1])
            print(datosUser)
        elif choice == 2:
            print("\nHas elegido la opción 2")
        elif choice == 3:
            print("\nHas elegido la opción 3")
        elif choice == 4:
            print("\nHas elegido la opción 4")
        elif choice == 5:
            print("\nHas elegido la opción 5")
        elif choice == 6:
            print("\nHas elegido salir. ¡Hasta luego!")
            break
        else:
            print("\n¡Error! Por favor, elige una opción válida.")
    
def menuTrabajadores(user):
    while True:
        print('Bienvenid@ al Menu Principal')
        print("\nPor favor elige una opción del siguiente menú:")
        print("1. Ver Mis Datos")
        print("2. Opción 2")
        print("3. Opción 3")
        print("4. Opción 4")
        print("5. Opción 5")
        print("6. Salir")
        
        try:
            choice = int(input("\nTu elección: "))
        except ValueError:
            print("\n¡Error! Por favor, introduce un número.")
            continue
            
        if choice == 1:
            print("\nHas elegido la opción 1")
            datosUser = TrabajadorDTO().mostrarDatosPorUseryPass(user[0],user[1])
            print(datosUser)
        elif choice == 2:
            print("\nHas elegido la opción 2")
        elif choice == 3:
            print("\nHas elegido la opción 3")
        elif choice == 4:
            print("\nHas elegido la opción 4")
        elif choice == 5:
            print("\nHas elegido la opción 5")
        elif choice == 6:
            print("\nHas elegido salir. ¡Hasta luego!")
            break
        else:
            print("\n¡Error! Por favor, elige una opción válida.")
    
    
