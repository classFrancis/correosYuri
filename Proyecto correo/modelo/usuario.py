

class Usuario():
    """
    La clase Usuario representa un usuario en el sistema. 
    Almacena la identificación del usuario, su nombre y la clave de acceso.
    
    Atributos:
        idUsuario (str): La identificación del usuario en el sistema.
        nombre (str): El nombre del usuario.
        claveAcceso (str): La clave de acceso del usuario para autenticación.
        
    Métodos:
        getIdUsuario: Retorna la identificación del usuario.
        setIdUsuario: Establece la identificación del usuario.
        
        getNombre: Retorna el nombre del usuario.
        setNombre: Establece el nombre del usuario.
        
        getClaveAcceso: Retorna la clave de acceso del usuario.
        setClaveAcceso: Establece la clave de acceso del usuario.
        
        __str__: Retorna una representación en cadena de caracteres del usuario.
    """
    def __init__(self,idUsuario,nombre,claveAcceso):
        self.__idUsuario = idUsuario
        self.__nombre = nombre
        self.__claveAcceso = claveAcceso
        
    def __str__(self):
        return f'|ID: {self.__idUsuario} \n|Nombre: {self.__nombre}'

    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario

    def getIdUsuario(self):
        return self.__idUsuario

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setClaveAcceso(self, claveAcceso):
        self.__claveAcceso = claveAcceso

    def getClaveAcceso(self):
        return self.__claveAcceso
        
        
        