from conex import conn 
import traceback

class daoTrabajador:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "correosyuri")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn
    
    
    def validarLogin(self,nombreUsuario, claveUsuario):
        sql = "SELECT nombre_de_usuario, clave_accesos FROM usuario WHERE nombre_de_usuario = %s AND clave_accesos = %s;"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombreUsuario, claveUsuario))

            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def validarRut(self,rut):
        sql = 'select * from trabajador where rut = %s;'
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (rut,))
            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def tipoDeUsuario(self,nombreUsuario,claveUsuario):
        sql ="SELECT dl.cargo, dl.departamento FROM usuario u JOIN datosLaborales dl ON u.rut_trabajador = dl.rut_trabajador JOIN trabajador t ON dl.rut_trabajador = t.rut WHERE u.nombre_de_usuario = %s AND u.clave_accesos = %s;"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombreUsuario, claveUsuario))

            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def mostrarDatosPorUseryPass(self,nombreUsuario, claveUsuario):
        sql ="""SELECT 
                    t.rut, 
                    t.nombre, 
                    t.genero, 
                    t.telefono, 
                    t.direccion, 
                    u.id as id_usuario,
                    u.nombre_de_usuario, 
                    u.clave_accesos, 
                    d.id as id_datosLaborales,
                    d.fecha_contratacion, 
                    d.cargo, 
                    d.departamento, 
                    c.id as id_cargasFamiliares,
                    c.rut_carga,
                    c.nombre_carga, 
                    c.parentesco, 
                    c.genero_carga, 
                    e.id as id_contactosEmergencia,
                    e.rut_contacto,
                    e.nombre_contacto, 
                    e.relacionTrabajador, 
                    e.telefono_contacto 
                FROM usuario u
                LEFT JOIN trabajador t ON u.rut_trabajador = t.rut
                LEFT JOIN datosLaborales d ON d.rut_trabajador = t.rut
                LEFT JOIN cargasFamiliares c ON c.rut_trabajador = t.rut
                LEFT JOIN contactosEmergencia e ON e.rut_trabajador = t.rut
                WHERE u.nombre_de_usuario = %s AND u.clave_accesos = %s;"""
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombreUsuario, claveUsuario))

            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado

    def showDataGender(self, gender):
        sql ="""SELECT 
                    t.rut, 
                    t.nombre, 
                    t.genero, 
                    t.telefono, 
                    t.direccion, 
                    u.id as id_usuario,
                    u.nombre_de_usuario, 
                    u.clave_accesos, 
                    d.id as id_datosLaborales,
                    d.fecha_contratacion, 
                    d.cargo, 
                    d.departamento, 
                    c.id as id_cargasFamiliares,
                    c.rut_carga,
                    c.nombre_carga, 
                    c.parentesco, 
                    c.genero_carga, 
                    e.id as id_contactosEmergencia,
                    e.rut_contacto,
                    e.nombre_contacto, 
                    e.relacionTrabajador, 
                    e.telefono_contacto 
                FROM usuario u
                LEFT JOIN trabajador t ON u.rut_trabajador = t.rut
                LEFT JOIN datosLaborales d ON d.rut_trabajador = t.rut
                LEFT JOIN cargasFamiliares c ON c.rut_trabajador = t.rut
                LEFT JOIN contactosEmergencia e ON e.rut_trabajador = t.rut where genero = %s;"""
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (gender,))

            resultado = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado

    def showDataCargo(self, cargo):
        sql ="""SELECT 
                    t.rut, 
                    t.nombre, 
                    t.genero, 
                    t.telefono, 
                    t.direccion, 
                    u.id as id_usuario,
                    u.nombre_de_usuario, 
                    u.clave_accesos, 
                    d.id as id_datosLaborales,
                    d.fecha_contratacion, 
                    d.cargo, 
                    d.departamento, 
                    c.id as id_cargasFamiliares,
                    c.rut_carga,
                    c.nombre_carga, 
                    c.parentesco, 
                    c.genero_carga, 
                    e.id as id_contactosEmergencia,
                    e.rut_contacto,
                    e.nombre_contacto, 
                    e.relacionTrabajador, 
                    e.telefono_contacto 
                FROM usuario u
                LEFT JOIN trabajador t ON u.rut_trabajador = t.rut
                LEFT JOIN datosLaborales d ON d.rut_trabajador = t.rut
                LEFT JOIN cargasFamiliares c ON c.rut_trabajador = t.rut
                LEFT JOIN contactosEmergencia e ON e.rut_trabajador = t.rut
                WHERE cargo = %s;"""
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo,))

            resultado = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado

    def showDataAreaDep(self, area, dep):
        sql = """SELECT 
                    t.rut, 
                    t.nombre, 
                    t.genero, 
                    t.telefono, 
                    t.direccion, 
                    u.id as id_usuario,
                    u.nombre_de_usuario, 
                    u.clave_accesos, 
                    d.id as id_datosLaborales,
                    d.fecha_contratacion, 
                    d.cargo, 
                    d.departamento, 
                    c.id as id_cargasFamiliares,
                    c.rut_carga,
                    c.nombre_carga, 
                    c.parentesco, 
                    c.genero_carga, 
                    e.id as id_contactosEmergencia,
                    e.rut_contacto,
                    e.nombre_contacto, 
                    e.relacionTrabajador, 
                    e.telefono_contacto 
                FROM usuario u
                LEFT JOIN trabajador t ON u.rut_trabajador = t.rut
                LEFT JOIN datosLaborales d ON d.rut_trabajador = t.rut
                LEFT JOIN cargasFamiliares c ON c.rut_trabajador = t.rut
                LEFT JOIN contactosEmergencia e ON e.rut_trabajador = t.rut
                WHERE d.cargo = %s and d.departamento = %s;"""
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (area, dep))

            resultado = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def addTrabajador(self,rutTrab,nombTrab,generoTrab,telefonoTrab,direccionTrab):
        sql = """INSERT INTO trabajador(rut, nombre, genero, telefono, direccion)
                    VALUES(%s, %s, %s, %s, %s);"""
        c = self.getConex()
        mensaje = "Datos Registrados con exito"  # Mensaje por defecto
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (rutTrab, nombTrab,generoTrab ,telefonoTrab ,direccionTrab))
            c.getConex().commit()
            print(mensaje)
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def showAll(self):
        sql = """SELECT 
                    t.rut, 
                    t.nombre, 
                    t.genero, 
                    t.telefono, 
                    t.direccion, 
                    u.id as id_usuario,
                    u.nombre_de_usuario, 
                    u.clave_accesos, 
                    d.id as id_datosLaborales,
                    d.fecha_contratacion, 
                    d.cargo, 
                    d.departamento, 
                    c.id as id_cargasFamiliares,
                    c.rut_carga,
                    c.nombre_carga, 
                    c.parentesco, 
                    c.genero_carga, 
                    e.id as id_contactosEmergencia,
                    e.rut_contacto,
                    e.nombre_contacto, 
                    e.relacionTrabajador, 
                    e.telefono_contacto 
                FROM usuario u
                LEFT JOIN trabajador t ON u.rut_trabajador = t.rut
                LEFT JOIN datosLaborales d ON d.rut_trabajador = t.rut
                LEFT JOIN cargasFamiliares c ON c.rut_trabajador = t.rut
                LEFT JOIN contactosEmergencia e ON e.rut_trabajador = t.rut;"""
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            resultado = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def modificarDatosPersonales(self,nombre,genero,telefono,direccion,rut):
        sql = """UPDATE trabajador 
                    SET nombre = %s, genero = %s, telefono = %s, direccion = %s 
                    WHERE rut = %s;"""
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombre,genero,telefono,direccion,rut))
            c.getConex().commit()
            print("Datos Personales modificados")
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def deleteDatoTrabajador(self, dato, rut):
        if dato == 'N':
            sql = "UPDATE trabajador SET nombre = '' WHERE rut = %s;"
        elif dato == 'G':
            sql = "UPDATE trabajador SET genero = '' WHERE rut = %s;"
        elif dato == 'T':
            sql = "UPDATE trabajador SET telefono = '' WHERE rut = %s;"
        else:
            sql = "UPDATE trabajador SET direccion = '' WHERE rut = %s;"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (rut,))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos modificados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje