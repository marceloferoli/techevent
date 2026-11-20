<?php

class Usuario {
    public $nome;
    public $idade;
    public $email;
    public $cpf;

    // Método construtor (igual ao __init__ do Python!)
    public function __construct($nome, $idade, $email, $cpf) {
        $this->nome = $nome;
        $this->idade = $idade;
        $this->email = $email;
        $this->cpf = $cpf;
    }

    public function salvarNoBanco() {
        // Conexão PDO moderna e segura com o MySQL do XAMPP
        $pdo = new PDO("mysql:host=localhost;dbname=techevent;charset=utf8", "root", "");
        
        // SUA VEZ: Complete o comando SQL INSERT INTO usuarios (...) VALUES (?, ?, ?, ?)
        $sql = "INSERT INTO usuarios (nome, idade, email, cpf) VALUES (?, ?, ?, ?)";
        
        $stmt = $pdo->prepare($sql);
        $stmt->execute([$this->nome, $this->idade, $this->email, $this->cpf]);
    }
}
