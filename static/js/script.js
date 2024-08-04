document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById("meuFormulario");
  
    formulario.addEventListener("submit", function(event) {
  
      // Coleta os dados do formulário
      const formData = new FormData(formulario);
  
      // Envia os dados para o servidor usando AJAX
      fetch("{{ url_for('add_user') }}", {
        method: "POST",
        body: formData
      })
      .then(response => {
        // Limpa os campos do formulário após o envio bem-sucedido
        const inputs = formulario.querySelectorAll("input");
        inputs.forEach(input => input.value = "");
      })
      .catch(error => {
        console.error("Erro ao enviar o formulário:", error);
      });
  });
});