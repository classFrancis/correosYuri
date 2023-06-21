CREATE TABLE trabajador (
    rut VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    genero varchar (20) NOT NULL,
    telefono VARCHAR(15),
    direccion VARCHAR(255)
);
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_de_usuario VARCHAR(100) NOT NULL,
    clave_accesos VARCHAR(255) NOT NULL,
    rut_trabajador VARCHAR(10)
);
ALTER TABLE usuario
ADD FOREIGN KEY (rut_trabajador) REFERENCES trabajador(rut);
CREATE TABLE datosLaborales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_contratacion DATE NOT NULL,
    cargo VARCHAR(100),
    departamento VARCHAR(100),
    rut_trabajador VARCHAR(10)
);
ALTER TABLE datosLaborales
ADD FOREIGN KEY (rut_trabajador) REFERENCES trabajador(rut);
CREATE TABLE cargasFamiliares (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_carga VARCHAR(100) NOT NULL,
    parentesco VARCHAR(100),
    genero_carga Varchar(20),
    rut_trabajador VARCHAR(10)
);
ALTER TABLE cargasFamiliares
ADD FOREIGN KEY (rut_trabajador) REFERENCES trabajador(rut);
CREATE TABLE contactosEmergencia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_contacto VARCHAR(100) NOT NULL,
    relacionTrabajador VARCHAR(100),
    telefono_contacto VARCHAR(15),
    rut_trabajador VARCHAR(10)
);
ALTER TABLE contactosEmergencia
ADD FOREIGN KEY (rut_trabajador) REFERENCES trabajador(rut);


