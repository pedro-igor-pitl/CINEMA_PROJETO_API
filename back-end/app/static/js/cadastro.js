function BtnLimpar(){
document.querySelector('.BtnLimpar').addEventListener('click', function() {
        const nome = document.getElementById('nome').value = '';
        const cpf = document.getElementById('cpf').value = '';
        const email = document.getElementById('email').value = '';
        const senha = document.getElementById('senha').value = '';
})};

BtnLimpar();

/*
document.querySelector('.FormCadastro').addEventListener('submit', function(event) {
    event.preventDefault();
    const nome = document.getElementById('nome').value;
    const cpf = document.getElementById('cpf').value;
    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;

    if (cpf.length !== 11) {
        alert('O CPF deve ter exatamente 11 dígitos.');
        return; 
    }
});
*/