let menu = document.querySelector('#menu-icon');
let navlist = document.querySelector('.navlist');
let origem = document.getElementById('origem');
let destino = document.getElementById('destino');

function onClickBotao() {
    let valorOrigem = origem.value;
    let valorDestino = destino.value;
    let veiculo = document.querySelectorAll('input[name="veiculo"]:checked')

    if (veiculo) {
        alert(`Jau o veículo selecionado é o ${veiculo.value}`)
    }

    if (valorOrigem != null && valorDestino != null) {

        try {

            fetch("https//backend", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: {
                    valorDestino,
                    valorOrigem,
                }
            }).then(response => console.log(response))

        } catch (error) {
            console.log(error)
            'Foi não, mano :('
        }

    }


}

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navlist.classList.toggle('open');
};

let number = document.getElementById("number");
let counter = 0;
setInterval(() => {
    if (counter == 65) {
        clearInterval();
    } else {
        counter += 1;
        number.innerHTML = counter + "%";
    }
}, 25);
