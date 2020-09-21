# Atividade Mastertech


## 1 - Cadastro de usuário
### Requisição
Requisição para listar todos os hotéis do sistema, podendo opcionalmente receber filtros personalizados via path, de forma que se o cliente não definir nenhum parâmetro de consulta (nenhum filtro), os parâmetros receberão os valores padrão. 

![Image Cadastro usuário](/image/cadastro_usuario.png)


### Resposta

![Image Cadastro usuário](/image/resposta_Cadastro.png)


### Requisição
Com o campo cpf faltando no corpo da requisição

![Image Cadastro usuário](/image/cadastro_error.png)


### Resposta
Como resposta, resposta notifica a falta do campo cpf

![Image Cadastro usuário](/image/respota_cadastro_error.png)


## 2 - Listar Usuários
### Requisição
Requisição para visualizar todos os usuários com as suas informações

![Image Cadastro usuário](/image/lista_usuario.png)

### Resposta
Retorna a lista de todos os usuários cadastrados comas informações

![Image Cadastro usuário](/image/resposta_lista_usuario.png)


## 3 - Listar um único Usuário
## Requisição
requisição retorna os dados de um usuário especifico: users{id_user}
![Image Cadastro usuário](/image/lista_usuario_unico.png)

### Resposta
Como resposta, obtém-se uma mensagem de erro, dizendo que o hotel não foi encontrado.

![Image Cadastro usuário](/image/resposta_usuario_unico.png)


## Requisição
Usuário que não existe na base de dados 

![Image Cadastro usuário](/image/lista_usuario_unico_error.png)


### Resposta
Para um usuário não cadastrado é exibido a massagem “User not found”

![Image Cadastro usuário](/image/resposta_alterar_usuario_erro.png)


## 4 - Alterar de Usuário
### Requisição
Nessa requisição os campos que podem ser alterados são nome_completo, cpf e email

![Image Cadastro usuário](/image/alterar_usuario.png)

### Antes
![Image Cadastro usuário](/image/antes.png)



### Resposta
A reposta retorna o cadastro do usuário atualizado

![Image Cadastro usuário](/image/atualizado.png)

### Requisição
Usuário não cadastrado

![Image Cadastro usuário](/image/alterar_usuario_error.png)

### Resposta
Para um usuário não cadastrado é exibido a massagem “User not found”

![Image Cadastro usuário](/image/resposta_alterar_usuario_erro.png)
















