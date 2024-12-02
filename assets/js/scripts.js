document.addEventListener("DOMContentLoaded", () => {
    const menuData = {
        Segunda: ["Arroz", "Feijão", "Carne Assada"],
        Terça: ["Macarrão", "Frango", "Salada"],
        Quarta: ["Feijoada", "Couve", "Farofa"],
        Quinta: ["Arroz", "Peixe", "Legumes"],
        Sexta: ["Lasagna", "Salada", "Pudim"],
        Sábado: ["Churrasco", "Batata Frita", "Arroz Carreteiro"],
        Domingo: ["Frango Assado", "Purê de Batata", "Salada"]
    };
    
    // Navegar para a página do estudante ou funcionário
    document.getElementById("student-button").addEventListener("click", (event) => {
        event.preventDefault();
        window.location.href = "../index.html"; // Substitua pelo caminho real
    });

    // Navegar para a página do administrador
    document.getElementById("admin-button").addEventListener("click", (event) => {
        event.preventDefault();
        window.location.href = "../admin.html"; // Substitua pelo caminho real
    });
});
