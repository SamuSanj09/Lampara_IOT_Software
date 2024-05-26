<?php
$nombreServidor = "localhost";
$nombreUsuario = "root";
$contraseña = "";
$nombreBD = "instrumentos";

$conn = new mysqli($nombreServidor, $nombreUsuario, $contraseña, $nombreBD);

if ($conn->connect_error) {
  die(json_encode(["error" => "Fallo en la conexión: " . $conn->connect_error]));
}
?>
