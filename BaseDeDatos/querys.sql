-- Consultar todos los datos de un usuario con el rut--

SELECT 
    t.rut, t.nombre, t.genero, t.telefono, t.direccion,
    u.id AS id_usuario, u.nombre_de_usuario, u.clave_accesos,
    d.id AS id_datosLaborales, d.fecha_contratacion, d.cargo, d.departamento,
    c.id AS id_cargasFamiliares, c.nombre_carga, c.parentesco, c.genero_carga,
    e.id AS id_contactosEmergencia, e.nombre_contacto, e.relacionTrabajador, e.telefono_contacto
FROM 
    trabajador t
LEFT JOIN 
    usuario u ON t.rut = u.rut_trabajador
LEFT JOIN 
    datosLaborales d ON t.rut = d.rut_trabajador
LEFT JOIN 
    cargasFamiliares c ON t.rut = c.rut_trabajador
LEFT JOIN 
    contactosEmergencia e ON t.rut = e.rut_trabajador
WHERE 
    t.rut = '1-1';

-- Eliminar datos de usuario de todas las tablas a traves del rut --

DELETE FROM usuario WHERE rut_trabajador = '1-1';
DELETE FROM datosLaborales WHERE rut_trabajador = '1-1';
DELETE FROM cargasFamiliares WHERE rut_trabajador = '1-1';
DELETE FROM contactosEmergencia WHERE rut_trabajador = '1-1';
DELETE FROM trabajador WHERE rut = '1-1';







