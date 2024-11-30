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
});
