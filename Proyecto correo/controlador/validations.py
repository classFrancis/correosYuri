from controlador.dto_trabajador import TrabajadorDTO
from controlador.dto_usuario import UsuarioDTO
from controlador.dto_datosLaborales import DatosLaboralesDTO
from controlador.dto_cargasFamiliares import CargasFamiliaresDTO
from controlador.dto_contactosDeEmergencia import ContactosDeEmergenciaDTO

def validarLogin():
    usuarioTrabajador = input("Ingrese Nombre de Usuario:\n")
    claveTrabajador = input("Ingrese su Clave de Usuario:\n")
    resultado = TrabajadorDTO().validarLogin(usuarioTrabajador,claveTrabajador)
    return resultado

def validarRutTrab():
    while True:
        rutTrab = input("ingrese el rut del trabajador\n")
        if len(rutTrab) > 0 and rutTrab not in [" "]:
            resultado = TrabajadorDTO().validarRut(rutTrab)
            if resultado is None:
                break
            else:
                print("El rut ingresado ya existe en el registro")
        else:
            print("No se permite un rut vacio")
    return rutTrab

def validarNombreUsuario():
    while True:
        nombreUsuario = input('ingrese el nombre para el Usuario\n')
        if len(nombreUsuario) > 0 and nombreUsuario not in [" "]:
            resultado = UsuarioDTO().validarNombreUsuario(nombreUsuario)
            if resultado is None:
                break
            else:
                print('El nombre de usuario ya existe')
        else:
            print("Debe ingresar un nombre de usuario valido")
    return nombreUsuario
        
    
def addTrabajadorAlSistema():
    rutTrab = validarRutTrab()
    nombTrab = input("Ingrese el nombre\n").capitalize()
    apellTrab = input("Ingrese el apellido\n").capitalize()
    nombComp = nombTrab +" "+apellTrab
    generoTrab = input("Ingrese el genero, use (M) o (F)\n").upper()
    telefonoTrab = input('Ingrese el telefono\n')
    direccionTrab = input('Ingrese la direccion\n')
    TrabajadorDTO().addTrabajador(rutTrab,nombComp,generoTrab,telefonoTrab,direccionTrab)
    addUsuario(rutTrab)
    addDatosLaborales(rutTrab)
    addCargasFamiliares(rutTrab)
    addContactosDeEmergencia(rutTrab)
    print("\nDatos registrados con exito\n")
        
def addUsuario(rutTrab):   
    print('Ahora debe crear las credenciales de Usuario para el trabajador')
    nombUsuario = validarNombreUsuario()
    password = input('Ingrese el password para el usuario\n')
    UsuarioDTO().addUsuario(nombUsuario,password,rutTrab)

       
def addDatosLaborales(rutTrab):
    print('Ahora ingrese los datos laborales')
    fechaCont = input('Ingrese la fecha de contratacion (AA-MM-DD Ej:1999-05-25)\n')
    cargo = input("Ingrese el cargo\n").capitalize()
    depto = input("Ingrese el Departamento\n").capitalize()
    if depto in ['Rrhh', 'Recursos humanos', 'Recursoshumanos', 'Recursos Humanos']:
        depto = 'RRHH'
    DatosLaboralesDTO().addDatosLaborales(fechaCont,cargo,depto,rutTrab)
    
def addCargasFamiliares(rutTrab):
    while True:
        tieneCarga = input("¿El trabajador tiene cargas familiares? (Y/N)\n").upper()
        if tieneCarga in ['Y', 'N']:
            break
        print("Por favor, ingrese Y para sí, o N para no.")
    
    if tieneCarga == 'Y':
        while True:
            print("Ahora debe ingresar las cargas familiares\n")
            rutCarga = input("Ingrese el rut de la carga familiar\n")
            nombCarga = input("Ingrese el nombre de la carga familiar\n").capitalize()
            apellCarga = input("Ingrese el apellido de la carga familiar\n").capitalize()
            nombCompCarga = nombCarga+" "+apellCarga
            parentesco = input("Ingrese el parentesco\n").capitalize()
            generoCarga = input("Ingrese el genero de la carga familiar, use (M) o (F)\n").upper()
            CargasFamiliaresDTO().addCargasFamiliares(rutCarga,nombCompCarga,parentesco,generoCarga,rutTrab)
            
            while True:
                otraCarga = input("¿Desea agregar otra carga familiar? (Y/N)\n").upper()
                if otraCarga in ['Y', 'N']:
                    break
                print("Por favor, ingrese Y para si, o N para no.")
            if otraCarga == 'N':
                break

        
def addContactosDeEmergencia(rutTrab):
    while True:
        print("Ahora ingrese contactos de emergencia")
        rutContact = input("ingrese el rut del contacto\n")
        nombContact = input("Ingrese el nombre del contacto\n").capitalize()
        apellContact = input("Ingrese el apeelido del contacto\n").capitalize()
        nombreCompContact = nombContact+" "+apellContact
        relacionContact = input("Ingrese la relacion del contacto con el trabajador\n").capitalize()
        telefonoContact = input("Ingrese el telefono del contacto de emergencia\n")
        ContactosDeEmergenciaDTO().addContactosDeEmergencia(rutContact,nombreCompContact,relacionContact,telefonoContact,rutTrab)
        
        while True:
            otroContacto = input("¿Desea agregar otro contacto de emergencia? (Y/N)\n").upper()
            if otroContacto in ['Y', 'N']:
                break
            print("Por favor, ingrese Y para si, o N para no.")
        if otroContacto == 'N':
            break

        
def modificarDatosPersonales(rut):
    resultado = TrabajadorDTO().validarRut(rut)
    print('Por motivos de seguridad el rut no se puede modificar desde el aplicativo')
    print("Para modificar el rut de un trabajador debe contactarse con el encargado de la base de datos")
    print(f"Sus datos personales actuales son: {resultado}")
    nombre = input("Ingrese el nuevo nombre\n").capitalize()
    apellido = input("ingrese el nuevo apellido\n").capitalize()
    nombreComp = nombre+" "+apellido
    genero = input("Ingrese el genero use (F) si es femenino o (M) si es masculino\n").upper()
    telefono = input("Ingrese el nuevo numero de telefono\n")
    direccion = input("Ingrese la nueva direccion\n")
    TrabajadorDTO().modificarDatosPersonales(nombreComp,genero,telefono,direccion,rut)

def modificarCargasFamiliares(rutTrab):
    resultado = CargasFamiliaresDTO().obtenerDatosDeCargas(rutTrab)
    print("Estas son las cargas familiares asociadas:")
    for x in resultado:
        print(x)
    rutCar = input("Ingrese el rut de la carga familiar a modificar\n")
    rutCarga = input("Ingrese el nuevo rut de la carga familiar\n")
    nombCarga = input("Ingrese el nuevo nombre de la carga familiar\n").capitalize()
    apellCarga = input("Ingrese el nuevo apellido de la carga familiar\n").capitalize()
    nombCompCarga = nombCarga+" "+apellCarga
    parentesco = input("Ingrese el parentesco\n").capitalize()
    generoCarga = input("Ingrese el genero de la carga familiar, use (M) o (F)\n").upper()
    CargasFamiliaresDTO().modificarCargasFamiliares(rutCarga,nombCompCarga,parentesco,generoCarga,rutTrab,rutCar)

def modificarContactosDeEmergencia(rutTrab):
    resultado = ContactosDeEmergenciaDTO().obtenerDatosDeContactos(rutTrab)
    print("Estos son los contactos de emergencia asociados:")
    for x in resultado:
        print(x)
    rutCont = input("Ingrese el rut del contacto a modificar\n")
    rutContact = input("ingrese el rut del contacto\n")
    nombContact = input("Ingrese el nombre del contacto\n").capitalize()
    apellContact = input("Ingrese el apeelido del contacto\n").capitalize()
    nombreCompContact = nombContact+" "+apellContact
    relacionContact = input("Ingrese la relacion del contacto con el trabajador\n").capitalize()
    telefonoContact = input("Ingrese el telefono del contacto de emergencia\n")
    ContactosDeEmergenciaDTO().modificarContactosDeEmergencia(rutContact,nombreCompContact,relacionContact,telefonoContact,rutTrab,rutCont)

def listGender(gender):
    print("Listado empleados por género")
    resultado = TrabajadorDTO().showDataGender(gender)
    if len(resultado) > 0:
        for u in resultado:
            print("<------------------------------------->")
            print(u)
            print("<------------------------------------->")
    else:
        print("no hay resultados")

def listCargo(cargo):
    print("Listado empleados por cargo")
    resultado = TrabajadorDTO().showDataCargo(cargo)
    if len(resultado) > 0:
        for u in resultado:
            print("<------------------------------------->")
            print(u)
            print("<------------------------------------->")
    else:
        print("no hay resultados")

def listAreaDep(area, dep):
    print("Listado empleados por cargo y departamento")
    resultado = TrabajadorDTO().showDataAreaDep(area, dep)
    if len(resultado) > 0:
        for u in resultado:
            print("<------------------------------------->")
            print(u)
            print("<------------------------------------->")
    else:
        print("no hay resultados")

def listCargFam(rutTrab):
    resultado = CargasFamiliaresDTO().obtenerDatosDeCargas(rutTrab)
    print("Estas son las cargas familiares asociadas:")
    for x in resultado:
        print(x)

def listaContEmer(rutTrab):
    resultado = ContactosDeEmergenciaDTO().obtenerDatosDeContactos(rutTrab)
    print("Estos son los contactos de emergencia asociados:")
    for x in resultado:
        print(x)

def listAllWorkers():
    resultado = TrabajadorDTO().showAll()
    if len(resultado) > 0:
        for u in resultado:
            print("<------------------------------------->")
            print(u)
            print("<------------------------------------->")
    else:
        print("no hay resultados")

def deleteSpecificData(dato, rut):
    print("Buscando el dato especificado a eliminar")
    resul = TrabajadorDTO().deleteDatoTrabajador(dato, rut)
    return resul

def deleteCargaFam(dato):
    print("Buscando el dato especificado a eliminar")
    resul = CargasFamiliaresDTO().deleteCargaFam(dato)
    return resul

def deleteContactEmer(dato):
    print("Buscando el dato especificado a eliminar")
    resul = ContactosDeEmergenciaDTO().deleteContactEmer(dato)
    return resul

def inicio(user):
    tipoUser = TrabajadorDTO().tipoDeUsuario(user[0],user[1])
    if tipoUser[0] == 'Administrador'.capitalize() and tipoUser[1] == 'RRHH'.upper():
        menuAdministradorRRHH(user)
    elif tipoUser[0] == 'Gerente'.capitalize() and tipoUser[1] == 'Gerencia'.capitalize():
        menuGerencia(user)
    else:
        menuTrabajadores(user)
        
def modificarMisDatosPersonales(rut):
    resultado = TrabajadorDTO().validarRut(rut)
    print(resultado)
    if resultado is not None:
        while True:
            print("\nPor favor elige una opción del siguiente menú:")
            print("1. Modificar Datos Personales")
            print("2. Modificar Cargas Familiares")
            print("3. Modificar Contactos de Emergencia")
            print("4. Volver al menu anterior")

            try:
                choice = int(input("\nTu elección: "))
            except ValueError:
                print("\n¡Error! Por favor, introduce un número.")
                continue

            if choice == 1:
                print("\nHas elegido la opción 1")
                option = input(
                    "Si desea ingresar una modificación ingrese 1, sino ingrese 2 para eliminar un dato. Para volver ingrese 3\n")
                if option == "1":
                    modificarDatosPersonales(rut)
                elif option == "2":
                    print("Puede eliminar nombre, género, teléfono o dirección")
                    print("Ingrese [N] para nombre, [G], para género, [T] para teléfono o [D] para dirección")
                    dato = input("Elija qué dato personal desea eliminar\n").upper()
                    deleteSpecificData(dato, rut)
                else:
                    print("\nHas elegido volver al menu anterior")
                    break
            elif choice == 2:
                print("\nHas elegido la opción 2")
                option = input(
                    "Si desea ingresar una modificación ingrese 1, sino ingrese 2 para eliminar un dato. Para volver ingrese 3\n")
                if option == "1":
                    modificarCargasFamiliares(rut)
                elif option == "2":
                    listCargFam(rut)
                    dato = input("Elija qué carga familiar desea eliminar ingresando el rut de dicha carga\n")
                    deleteCargaFam(dato)
                else:
                    print("\nHas elegido volver al menu anterior")
                    break
            elif choice == 3:
                print("\nHas elegido la opción 3")
                option = input(
                    "Si desea ingresar una modificación ingrese 1, sino ingrese 2 para eliminar un dato. Para volver ingrese 3\n")
                if option == "1":
                    modificarContactosDeEmergencia(rut)
                elif option == "2":
                    listaContEmer(rut)
                    dato = input(
                        "Elija qué contacto de emergencia desea eliminar ingresando el rut de dicho contacto\n")
                    deleteContactEmer(dato)
                else:
                    print("\nHas elegido volver al menu anterior")
                    break
            elif choice == 4:
                print("\nHas elegido volver al menu anterior")
                break
            else:
                print("\n¡Error! Por favor, elige una opción válida.")
    else:
        print("El rut ingresado no esta registrado")
    
def modificarDatosTrabajador():
    ciclo = True
    while ciclo:
        rut = input("Ingrese el rut del trabajador a modificar\n")
        if len(rut) > 0 and rut not in [" "]:
            resultado = TrabajadorDTO().validarRut(rut)
            if resultado is not None:
                while True:
                    print("\nPor favor elige una opción del siguiente menú:")
                    print("1. Modificar Datos Personales")
                    print("2. Modificar Cargas Familiares")
                    print("3. Modificar Contactos de Emergencia")
                    print("4. Volver al menu anterior")

                    try:
                        choice = int(input("\nTu elección: "))
                    except ValueError:
                        print("\n¡Error! Por favor, introduce un número.")
                        continue

                    if choice == 1:
                        print("\nHas elegido la opción 1")
                        option = input(
                            "Si desea ingresar una modificación ingrese 1, sino ingrese 2 para eliminar un dato. Para volver ingrese 3\n")
                        if option == "1":
                            modificarDatosPersonales(rut)
                        elif option == "2":
                            print("Puede eliminar nombre, género, teléfono o dirección")
                            print("Ingrese [N] para nombre, [G], para género, [T] para teléfono o [D] para dirección")
                            dato = input("Elija qué dato personal desea eliminar\n").upper()
                            deleteSpecificData(dato, rut)
                        else:
                            print("\nHas elegido volver al menu anterior")
                            ciclo = False
                            break
                    elif choice == 2:
                        print("\nHas elegido la opción 2")
                        option = input(
                            "Si desea ingresar una modificación ingrese 1, sino ingrese 2 para eliminar un dato. Para volver ingrese 3\n")
                        if option == "1":
                            modificarCargasFamiliares(rut)
                        elif option == "2":
                            listCargFam(rut)
                            dato = input("Elija qué carga familiar desea eliminar ingresando el rut de dicha carga\n")
                            deleteCargaFam(dato)
                        else:
                            print("\nHas elegido volver al menu anterior")
                            ciclo = False
                            break
                    elif choice == 3:
                        print("\nHas elegido la opción 3")
                        option = input(
                            "Si desea ingresar una modificación ingrese 1, sino ingrese 2 para eliminar un dato. Para volver ingrese 3\n")
                        if option == "1":
                            modificarContactosDeEmergencia(rut)
                        elif option == "2":
                            listaContEmer(rut)
                            dato = input(
                                "Elija qué contacto de emergencia desea eliminar ingresando el rut de dicho contacto\n")
                            deleteContactEmer(dato)
                        else:
                            print("\nHas elegido volver al menu anterior")
                            ciclo = False
                            break
                    elif choice == 4:
                        print("\nHas elegido volver al menu anterior")
                        ciclo = False
                        break
                    else:
                        print("\n¡Error! Por favor, elige una opción válida.")
            else:
                print("El rut ingresado no esta registrado")
        else:
            print("Ingrese un rut valido")

def menuAdministradorRRHH(user):
     while True:
        print("\nBienvenid@ al Menu de Administrador")
        print("\nPor favor elige una opción del siguiente menú:")
        print("1. Ver Mis Datos")
        print("2. Registrar Trabajador en el sistema")
        print("3. Modificar datos de trabajador")
        print("4. Listar trabajadores por género")
        print("5. Listar trabajadores por cargo")
        print("6. Listar trabajadores área y departamento")
        print("7. Salir")
        
        try:
            choice = int(input("\nTu elección: "))
        except ValueError:
            print("\n¡Error! Por favor, introduce un número.")
            continue
            
        if choice == 1:
            print("\nHas elegido la opción 1")
            datosUser = TrabajadorDTO().mostrarDatosPorUseryPass(user[0],user[1])
            print(f'\n-----------------------------------\n|Estos son tus datos en el sistema:\n-----------------------------------\n{datosUser}')
        elif choice == 2:
            print("\nHas elegido la opción 2")
            addTrabajadorAlSistema()
        elif choice == 3:
            print("\nHas elegido la opción 3")
            modificarDatosTrabajador()
        elif choice == 4:
            print("\nHas elegido la opción 4")
            gender = input("Elija el género a buscar [M] o [F]\n").upper()
            print(f'\n-----------------------------------\n|Estos son tus datos en el sistema:\n----------------------------------\n')
            listGender(gender)
        elif choice == 5:
            print("\nHas elegido la opción 5")
            cargo = input("Coloque el cargo a buscar\n").capitalize()
            print(f'\n-----------------------------------\n|Estos son tus datos en el sistema:\n----------------------------------\n')
            listCargo(cargo)
        elif choice == 6:
            print("\nHas elegido la opción 6")
            area = input("Coloque el cargo a buscar\n").capitalize()
            departamento = input("Coloque el departamento a buscar\n").upper()
            print(f'\n-----------------------------------\n|Estos son tus datos en el sistema:\n----------------------------------\n')
            listAreaDep(area, departamento)
        elif choice == 7:
            print("\nHas elegido salir. ¡Hasta luego!")
            break
        else:
            print("\n¡Error! Por favor, elige una opción válida.")

def menuGerencia(user):
    while True:
        print("\nBienvenid@ al Menu Gerencial")
        print("\nPor favor elige una opción del siguiente menú:")
        print("1. Ver Mis Datos")
        print("2. Listar todos los trabajadores")
        print("3. Salir")
        
        try:
            choice = int(input("\nTu elección: "))
        except ValueError:
            print("\n¡Error! Por favor, introduce un número.")
            continue
            
        if choice == 1:
            print("\nHas elegido la opción 1")
            datosUser = TrabajadorDTO().mostrarDatosPorUseryPass(user[0],user[1])
            print(f'\n-----------------------------------\n|Estos son tus datos en el sistema:\n----------------------------------\n{datosUser}')
        elif choice == 2:
            print("\nHas elegido la opción 2")
            listAllWorkers()
        elif choice == 3:
            print("\nHas elegido salir. ¡Hasta luego!")
            break
        else:
            print("\n¡Error! Por favor, elige una opción válida.")
    
def menuTrabajadores(user):
    while True:
        print('\nBienvenid@ al Menu Principal')
        print("\nPor favor elige una opción del siguiente menú:")
        print("1. Ver Mis Datos")
        print("2. Modificar o eliminar datos de trabajador")
        print("3. Salir")
        
        try:
            choice = int(input("\nTu elección: "))
        except ValueError:
            print("\n¡Error! Por favor, introduce un número.")
            continue
            
        if choice == 1:
            print("\nHas elegido la opción 1")
            datosUser = TrabajadorDTO().mostrarDatosPorUseryPass(user[0],user[1])
            print(f'\n-----------------------------------\n|Estos son tus datos en el sistema:\n-----------------------------------\n{datosUser}')
        elif choice == 2:
            print("\nHas elegido la opción 2")
            trabajador = TrabajadorDTO().mostrarDatosPorUseryPass(user[0],user[1])
            rutTrab = trabajador.getRutTrabajador()
            modificarMisDatosPersonales(rutTrab)
        elif choice == 3:
            print("\nHas elegido salir. ¡Hasta luego!")
            break
        else:
            print("\n¡Error! Por favor, elige una opción válida.")
    
    
