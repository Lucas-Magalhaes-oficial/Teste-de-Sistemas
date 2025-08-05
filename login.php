<?php
//definer os dados de login (futuramente será via bd)
$usuario_correto = "admin";
$senha_correta = "123456";

//dados do formulario
$usuario = $_POST['username'] ?? '';
$senha = $_POST['password'] ?? '';

//verifica se estão corretos
if($usuario === $usuario_correto && $senha === $senha_correta) {
    header("Location: index.html");
    exit;
} else {
    //redireciona de volta com erro
    header("location: login.html?error=1");
    exit;
}
?>