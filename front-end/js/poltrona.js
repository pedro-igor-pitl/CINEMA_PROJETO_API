document.getElementById("UsuarioIcon").addEventListener("click", function() {
    var usuarioMenu = document.getElementById("UsuarioMenu");
    if (usuarioMenu.style.display === "none" || usuarioMenu.style.display === "") {
        usuarioMenu.style.display = "block";
    } else {
        usuarioMenu.style.display = "none";
    }
});

window.onclick = function(event) {
    var usuarioMenu = document.getElementById("UsuarioMenu");
    if (!event.target.matches('#UsuarioIcon')) {
        if (usuarioMenu.style.display === "block") {
            usuarioMenu.style.display = "none";
        }
    }
};

const valorPorPoltrona = 15;
let quantidadePoltronas = 0;
let valorTotal = 0;

const qtPoltronaElement = document.getElementById("QtPoltrona");
const valorTotalElement = document.getElementById("ValorTotalPoltrona");

function atualizarValores() {
    qtPoltronaElement.textContent = quantidadePoltronas;
    valorTotalElement.textContent = valorTotal.toFixed(2).replace('.', ',');
}

const poltronas = document.querySelectorAll(".circuloPoltrona");
poltronas.forEach(poltrona => {
    poltrona.addEventListener("click", () => {
        if (poltrona.classList.contains("selecionada")) {
            poltrona.classList.remove("selecionada");
            quantidadePoltronas--;
            valorTotal -= valorPorPoltrona;
        } else {
            poltrona.classList.add("selecionada");
            quantidadePoltronas++;
            valorTotal += valorPorPoltrona;
        }

        atualizarValores();
    });
});

atualizarValores();

