# 🎟️ TechEvent — Sistema Full Stack de Gestão de Eventos

Sistema integrado de gerenciamento de eventos, usuários e inscrições desenvolvido como projeto prático de Engenharia de Software. Combina um motor administrativo em linha de comando (CLI) e uma interface web conectados ao mesmo banco de dados relacional.

## 🛠️ Tecnologias Utilizadas
* **Backend CLI:** Python 3 (POO, manipulação de listas, busca e ordenação com `sorted`/`lambda`)
* **Backend Web:** PHP 8+ (POO, PDO para prevenção de SQL Injection)
* **Frontend:** HTML5
* **Banco de Dados:** MySQL (via XAMPP)

## 🗂️ Arquitetura do Projeto
* `/cli` — Aplicação de terminal em Python (`mysql-connector-python`).
* `/web` — Interface web em PHP e HTML5.
* `/database` — Script SQL (`schema.sql`) com a modelagem relacional (`usuarios`, `eventos`, `inscricoes`).
