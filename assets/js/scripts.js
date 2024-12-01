document.addEventListener("DOMContentLoaded", () => {
    // Ação do botão de login
    document.getElementById("login-button").addEventListener("click", function (event) {
        event.preventDefault(); // Evita o comportamento padrão do formulário

        // Redireciona para o index.html
        window.location.href = "../index.html"; // Caminho relativo para o index.html
    });

    // Ação do botão "Esqueci a senha"
    const forgotPasswordButton = document.getElementById("forgot-password-button");
    forgotPasswordButton.addEventListener("click", () => {
        window.location.href = "./forgot-password.html"; // Redireciona para a tela de redefinição de senha
    });

    const recoverPasswordButton = document.getElementById("recover-password");
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

    document.getElementById('ver-cardapio').addEventListener('click', () => {
        const restaurante = document.getElementById('restaurante').value;
        const data = document.getElementById('data').value;
        const tipoRefeicao = document.getElementById('tipo_refeicao').value;
    
        // Simula a busca do cardápio (pode ser adaptado para consumir uma API)
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
    
});
