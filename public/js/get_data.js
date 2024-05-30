const instrumentosPrincipales = ['Guitarra', 'Tambor', 'Bateria', 'Caja de Haija', 'Charango'];

function fetchInstrumentData() {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "../php/get_data.php", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const instrumentos = JSON.parse(xhr.responseText);
            instrumentosPrincipales.forEach(nombre => {
                const instrumentoData = instrumentos.find(instr => instr.nombre_instrumento === nombre);
                const valor = instrumentoData ? instrumentoData.valor : 1;
                const sonido = instrumentoData ? instrumentoData.sonido : '';
                const instrumentoDiv = document.getElementById(nombre);

                if (instrumentoDiv) {
                    instrumentoDiv.className = 'instrumento ' + (valor == 2 ? 'tocado' : 'no-sonido');
                    instrumentoDiv.textContent = `${nombre} - ${valor == 2 ? sonido : 'No Emite Sonido'}`;
                }
            });
        }
    };
    xhr.send();
}

document.addEventListener("DOMContentLoaded", function() {
    const container = document.getElementById('instrumentosContainer');
    instrumentosPrincipales.forEach(nombre => {
        const instrumentoDiv = document.createElement('div');
        instrumentoDiv.id = nombre;
        instrumentoDiv.className = 'instrumento no-sonido';
        instrumentoDiv.textContent = `${nombre} - No Emite Sonido`;
        container.appendChild(instrumentoDiv);
    });

    setInterval(fetchInstrumentData, 1000); // Fetch data every 1 second
});
