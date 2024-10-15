const imagens = document.querySelectorAll('.FilmeImgDiv');
const circulos = document.querySelectorAll('.CirculoFilme');
let currentImg = 0;

function atualizarImagem() {
    imagens.forEach((img, index) => {
        img.classList.toggle('active', index === currentImg);
    });

    circulos.forEach((circulo, index) => {
        circulo.classList.toggle('active', index === currentImg);
    });
}

function proximaImagem() {
    currentImg = (currentImg + 1) % imagens.length;
    atualizarImagem();
}

function anteriorImagem() {
    currentImg = (currentImg - 1 + imagens.length) % imagens.length;
    atualizarImagem();
}

document.querySelector('.BtnProximoEmAlta').addEventListener('click', proximaImagem);
document.querySelector('.BtnAnteriorEmAlta').addEventListener('click', anteriorImagem);

circulos.forEach((circulo, index) => {
    circulo.addEventListener('click', () => {
        currentImg = index;
        atualizarImagem();
    });
});

atualizarImagem();

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
