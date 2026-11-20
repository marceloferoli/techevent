<?php
// Importa a classe que você acabou de criar
require_once "Usuario.php";

// Verifica se o formulário foi enviado via POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome  = $_POST["nome"];
    $idade = $_POST["idade"];
    $email = $_POST["email"];
    $cpf   = $_POST["cpf"];

    // Instancia o objeto Usuario usando o molde da sua classe
    $novoUsuario = new Usuario($nome, $idade, $email, $cpf);
    
    // Manda gravar direto no MySQL!
    $novoUsuario->salvarNoBanco();

    echo "<h2>Usuário cadastrado via Web com sucesso!</h2>";
    echo "<a href='index.html'>Voltar ao cadastro</a>";
}
