from controlador.validations import validarLogin,inicio

intentos = 1
print("Correos Yuri")
while intentos <=3:
    try:
        resu = validarLogin()
        if resu is not None:
            inicio(resu)
            break
        else:
            print("Los datos ingresados no existen, vuelva a ingresar sus credenciales de usuario")
            intentos += 1
    except:
        print("Vuelve a intentarlo")
if intentos == 4:
    print("Se ha superado el numero de intentos permitidos")