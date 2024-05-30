<?php
require_once 'db.php';

// Función para insertar datos en la tabla instrumento
function insert_data($data) {
    $conn = connect_db();

    
    $valor = $conn->real_escape_string($data['valor']);
    $sonido = $conn->real_escape_string($data['sonido']);
    $HoraFecha = $conn->real_escape_string($data['HoraFecha']);
    $nombre_instrumento = $conn->real_escape_string($data['nombre_instrumento']);

    // SQL para insertar datos
    $sql = "INSERT INTO instrumento ( valor, sonido, HoraFecha, nombre_instrumento) VALUES ('$valor', '$sonido', '$HoraFecha', '$nombre_instrumento')";

    // Ejecutar consulta
    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    // Cerrar conexión
    $conn->close();
}
?>
