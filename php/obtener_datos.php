<?php
$nombreServidor = "localhost";
$nombreUsuario = "root";
$contraseña = "";
$nombreBD = "instrumentos";
$conn = new mysqli($nombreServidor, $nombreUsuario, $contraseña, $nombreBD);

if ($conn->connect_error) {
  die("Fallo: " . $conn->connect_error);
}

header('Content-Type: application/json');

$lampID = $_GET['nombre_instrumento']; 

$sqlLamp = "SELECT HOUR(HoraFecha) as Hora, COUNT(*) as Frecuencia 
FROM instrumento 
WHERE nombre_instrumento = '$lampID' 
GROUP BY HOUR(HoraFecha)";
$resultadoLamp = $conn->query($sqlLamp);
$Grafico1 = [];
while($fila = $resultadoLamp->fetch_assoc()) {
    $Grafico1[] = $fila;
}

$sqlTemp ="SELECT valor as valor1, Count(*) as Frecuencia FROM instrumento WHERE nombre_instrumento = '$lampID'  
GROUP BY valor";
$resultadoTemp = $conn->query($sqlTemp);
$Grafico2 = [];
while($fila = $resultadoTemp->fetch_assoc()) {
    $Grafico2[] = $fila;
}

$sqlLamp2 = "SELECT valor as valor2, Count(*) as Frecuencia2 
FROM instrumento 
WHERE nombre_instrumento = '$lampID'  
GROUP BY valor";
$resultadoLamp2 = $conn->query($sqlLamp2);
$Grafico3 = [];
while($fila = $resultadoLamp2->fetch_assoc()) {
    $Grafico3[] = $fila;
}

$sqlLamp3 = "SELECT valor AS valor3, id1 AS id_actual
FROM instrumento
WHERE nombre_instrumento = '$lampID'";
$resultadoLamp3 = $conn->query($sqlLamp3);
$Grafico4 = [];
while($fila = $resultadoLamp3->fetch_assoc()) {
    $Grafico4[] = $fila;
}

$resultados = [
    'Grafico1' => $Grafico1,
    'Grafico2' => $Grafico2,
    'Grafico3' => $Grafico3,
    'Grafico4' => $Grafico4
];

echo json_encode($resultados);

$conn->close();
?>