<?php
require_once 'insert_data.php';

// Leer datos JSON desde el cuerpo de la petición
$input = file_get_contents("php://input");
$data = json_decode($input, true);

if (!empty($data)) {
    insert_data($data);
} else {
    echo "No data received";
}
?>
