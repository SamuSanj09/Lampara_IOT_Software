<?php
include 'db.php';

$instrumentos = array();

$sql = "SELECT nombre_instrumento, valor, sonido FROM instrumento ORDER BY HoraFecha DESC";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $instrumentos[] = $row;
    }
} else {
    echo "No se encontraron datos";
}

$conn->close();

header('Content-Type: application/json');
echo json_encode($instrumentos);
error_log("Datos enviados: " . json_encode($instrumentos));
?>
