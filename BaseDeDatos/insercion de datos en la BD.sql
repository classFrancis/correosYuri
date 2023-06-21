
INSERT INTO trabajador(rut, nombre, genero, telefono, direccion)
VALUES('1-1', 'Francisco Sánchez', 'M', '123456789', 'Siempre viva 743');

-- la clave es 123, la que aparece registrada en la BD es asi luego de pasar por el encoder --
INSERT INTO usuario(nombre_de_usuario, clave_accesos, rut_trabajador)
VALUES('fsanchez', '202cb962ac59075b964b07152d234b70', '1-1'); 

INSERT INTO datosLaborales(fecha_contratacion, cargo, departamento, rut_trabajador)
VALUES('2023-01-01', 'Administrador', 'RRHH', '1-1');

INSERT INTO cargasFamiliares(nombre_carga, parentesco, genero_carga, rut_trabajador)
VALUES('Diana Sanchez', 'Hija', 'F', '1-1');

INSERT INTO contactosEmergencia(nombre_contacto, relacionTrabajador, telefono_contacto, rut_trabajador)
VALUES('Tiare Alarcon', 'Esposa', '987654321', '1-1');

 