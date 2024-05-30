const instrumentosPrincipales = ['Guitarra', 'Tambor', 'Bateria', 'Caja de haija', 'Charango'];

const imagenes = {
    'Guitarra': 'images/guitarra.jpg',
    'Tambor': 'images/tambor.jpg',
    'Bateria': 'images/bateria.jpg',
    'Caja de haija': 'images/caja_de_haija.jpg',
    'Charango': 'images/charango.jpg'
};

let userInteracted = false;
const sonidoReproducido = {};

function playSound(instrument, sound) {
    const soundId = `${instrument.toLowerCase().replace(/ /g, '')}${sound.replace(/ /g, '')}`;
    const audioElement = document.getElementById(soundId);
    if (audioElement) {
        audioElement.play().catch(error => {
            console.log(`No se pudo reproducir el sonido: ${error}`);
        });
    }
}

function fetchInstrumentData() {
    if (!userInteracted) return;

    const xhr = new XMLHttpRequest();
    xhr.open("GET", "../php/get_data.php", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const instrumentos = JSON.parse(xhr.responseText);
            instrumentosPrincipales.forEach(nombre => {
                const instrumentoData = instrumentos.find(instr => instr.nombre_instrumento === nombre);
                const valor = instrumentoData ? instrumentoData.valor : 1;
                const sonido = instrumentoData ? instrumentoData.sonido : '';
                const instrumentoDiv = document.getElementById(nombre.replace(/ /g, ''));

                if (instrumentoDiv) {
                    instrumentoDiv.className = 'instrumento ' + (valor == 2 ? 'tocado' : 'no-sonido');
                    instrumentoDiv.textContent = `${nombre} - ${valor == 2 ? sonido : 'No Emite Sonido'}`;
                    instrumentoDiv.style.backgroundImage = `url(${imagenes[nombre]})`;
                    
                    if (valor == 2 && sonido) {
                        if (!sonidoReproducido[nombre]) {
                            sonidoReproducido[nombre] = {};
                        }
                        if (!sonidoReproducido[nombre][sonido]) {
                            playSound(nombre, sonido);
                            sonidoReproducido[nombre][sonido] = true;
                        }
                    } else if (valor == 1 && sonidoReproducido[nombre]) {
                        sonidoReproducido[nombre][sonido] = false;
                    }
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
        instrumentoDiv.id = nombre.replace(/ /g, '');
        instrumentoDiv.className = 'instrumento no-sonido';
        instrumentoDiv.textContent = `${nombre} - No Emite Sonido`;
        container.appendChild(instrumentoDiv);
    });

    setInterval(fetchInstrumentData, 1000); // Fetch data every 1 second

    // Esperar la primera interacción del usuario
    document.body.addEventListener('click', () => {
        if (!userInteracted) {
            userInteracted = true;
            console.log("Usuario interactuó, reproducción de audio habilitada.");
        }
    }, { once: true });
});
