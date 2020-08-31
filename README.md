# Strongify password API 💻
Esta Api é capaz de analisar e modificar uma senha de forma randômica, a fim de deixá-la mais forte, se baseando nos seguintes critérios:

* Ter um tamanho mínimo de 8 caracteres
* Ter ao menos um número 
* Ter ao menos uma letra maiúscula  
* Ter ao menos uma letra minuscula 
* Ter ao menos um dos caracteres especiais, que são:  ('[@_!#$%^&*()<>?/\|}{~:]') 


### Partindo dos seguintes princípios

* A variação das senhas deve ser "pequena", apenas o necessário para atingir os critérios anteriores
* A alteração deve ser realizada de forma aleatória para evitar que seja possível prever
* Não deve ser possível prever quais caracteres serão alterados dado uma senha


### Custo 
O custo do algoritmo no pior caso é O(N), e no melhor caso ele é O(1).

### Heroku 
Disponibilizamos também essa api no heroku que pode ser acessado por: https://strongify-password.herokuapp.com/

* Para testar essa api basta fazer um post para: https://strongify-password.herokuapp.com/api/strongify-password. 
Passado como parâmetro o seguinte objeto: 

```js
{
    "password": "<Aqui você coloca a senha que quer testar>"
}
```



