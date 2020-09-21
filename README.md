# Atividade Mastertech


## 1 - Cadastro de usuário
### Requisição
Requisição para listar todos os hotéis do sistema, podendo opcionalmente receber filtros personalizados via path, de forma que se o cliente não definir nenhum parâmetro de consulta (nenhum filtro), os parâmetros receberão os valores padrão. 

![Image](/image/cadastro_usuario.png)


### Resposta

![Image](/image/resposta_Cadastro.png)


### Requisição
Com o campo cpf faltando no corpo da requisição

![Image](/image/cadastro_error.png)


### Resposta
Como resposta, resposta notifica a falta do campo cpf

![Image](/image/respota_cadastro_error.png)


## 2 - Listar Usuários
### Requisição
Requisição para visualizar todos os usuários com as suas informações

![Image](/image/lista_usuario.png)

### Resposta
Retorna a lista de todos os usuários cadastrados comas informações

![Image](/image/resposta_lista_usuario.png)


## 3 - Listar um único Usuário
## Requisição
requisição retorna os dados de um usuário especifico: users{id_user}
![Image](/image/lista_usuario_unico.png)

### Resposta
Como resposta, obtém-se uma mensagem de erro, dizendo que o hotel não foi encontrado.

![Image](/image/resposta_usuario_unico.png)


## Requisição
Usuário que não existe na base de dados 

![Image](/image/lista_usuario_unico_error.png)


### Resposta
Para um usuário não cadastrado é exibido a massagem “User not found”

![Image](/image/resposta_alterar_usuario_erro.png)


## 4 - Alterar de Usuário
### Requisição
Nessa requisição os campos que podem ser alterados são nome_completo, cpf e email

![Image](/image/alterar_usuario.png)

### Antes
![Image](/image/antes.png)



### Resposta
A reposta retorna o cadastro do usuário atualizado

![Image](/image/atualizado.png)

### Requisição
Usuário não cadastrado

![Image](/image/alterar_usuario_error.png)

### Resposta
Para um usuário não cadastrado é exibido a massagem “User not found”

![Image](/image/resposta_alterar_usuario_erro.png)

## 5 - Bater Ponto

### Requisição
Nessa requisição, é feita o restiro da batida de ponto de um usuário fornecendo : {id_user}


![Image](/image/bater_ponto_start.png)


### Resposta
Retorna as informações do ponto que foi batido

![Image](/image/Resposta_bater_ponto.png)

### Apenas as opções (Entrada e Saida) são permitidas

![Image](/image/request_erro.png)

### Resposta

![Image](/image/Bater_ponto_error_opc.png)

### Requisição
Caso seja informado um usuario não cadastrado na base de dados 

![Image](/image/requisao_erro_user.png)

### Resposta
Retorna o status code 404

![Image](/image/erro_404_opcao.png)




