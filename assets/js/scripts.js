document.addEventListener("DOMContentLoaded", () => {
    const loginButton = document.getElementById("student-button");
    if (loginButton) {
        loginButton.addEventListener("click", function (event) {
            event.preventDefault();
            window.location.href = "../index.html";
        });
    } else {
        console.log("student-button não encontrado");
    }

    const payButton = document.getElementById("pay-button");
    if (payButton) {
        payButton.addEventListener("click", function (event) {
            event.preventDefault();
            window.location.href = "payment.html";
        });
    } else {
        console.log("pay-button não encontrado");
    }

    const forgotPasswordButton = document.getElementById("admin-button");
    if (forgotPasswordButton) {
        forgotPasswordButton.addEventListener("click", () => {
            window.location.href = "../admin.html";
        });
    } else {
        console.log("admin-button não encontrado");
    }

    const recoverPasswordButton = document.getElementById("recover-password");
    if (recoverPasswordButton) {
        recoverPasswordButton.addEventListener("click", (event) => {
            event.preventDefault();
            const usuario = document.getElementById("usuario").value;
            const email = document.getElementById("email").value;

            if (usuario && email) {
                alert(`Um link de recuperação foi enviado para o e-mail: ${email}`);
            } else {
                alert("Por favor, preencha todos os campos.");
            }
        });
    } else {
        console.log("recover-password não encontrado");
    }

    const verCardapioButton = document.getElementById('ver-cardapio');
    if (verCardapioButton) {
        verCardapioButton.addEventListener('click', () => {
            const restaurante = document.getElementById('restaurante').value;
            const data = document.getElementById('data').value;
            const tipoRefeicao = document.getElementById('tipo_refeicao').value;

            const cardapio = {
                restaurante1: {
                    almoco: "Arroz, Feijão, Frango Assado, Salada.",
                    jantar: "Sopa de Legumes, Pão, Sobremesa.",
                    cafe: "Pão com Manteiga, Café, Fruta."
                },
                restaurante2: {
                    almoco: "Macarrão, Carne Moída, Legumes Refogados.",
                    jantar: "Arroz, Feijão, Omelete, Salada.",
                    cafe: "Pão de Queijo, Chá, Suco."
                },
                restaurante3: {
                    almoco: "Risoto de Frango, Salada Mista, Fruta.",
                    jantar: "Lasanha, Salada de Alface, Pudim.",
                    cafe: "Bolo, Leite com Café, Torradas."
                }
            };

            const menuSelecionado = cardapio[restaurante]?.[tipoRefeicao];
            const detalhes = menuSelecionado
                ? `Cardápio para ${tipoRefeicao} em ${data}: ${menuSelecionado}`
                : "Cardápio não disponível.";

            const cardapioSection = document.getElementById('cardapio-section');
            cardapioSection.style.display = 'block';
            document.getElementById('cardapio-detalhes').innerText = detalhes;
        });
    } else {
        console.log("ver-cardapio não encontrado");
    }
});
