function sendData(nombre_instrumento, valor, sonido) {
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "../php/data_debug.php", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            alert(xhr.responseText);
            setTimeout(() => {
                resetData(nombre_instrumento, sonido);
            }, 2000);
        }
    };
    xhr.send(`nombre_instrumento=${nombre_instrumento}&valor=${valor}&sonido=${sonido}`);
}

function resetData(nombre_instrumento, sonido) {
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "../php/data_debug.php", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log(xhr.responseText);
        }
    };
    xhr.send(`nombre_instrumento=${nombre_instrumento}&valor=1&sonido=${sonido}`);
}
