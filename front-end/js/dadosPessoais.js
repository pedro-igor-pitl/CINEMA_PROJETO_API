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