<h1>Lista de exercícios de Programação I - Estrutura de Decisão</h1>

<h2>1 - Analise o programa abaixo e responda o que acontece se o primeiro e o segundo valores forem iguais? Explique.</h2>
<li>a = int(input("Primeiro valor: "))</li>
<li>b = int(input("Segundo valor: "))</li>
<li>if a > b: </li>
<li>print ("O primeiro número é o maior!") </li>
<li>if b > a: </li>
<li>print ("O segundo número é o maior!")</li>


<h2>2 - Escreva um programa que pergunte a velocidade do carro de um usuário.
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso,
exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.</h2>


<h2>3 - Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.</h2>

<h2>4 - Escreva um programa que receba o código de uma categoria ou subcategoria de um produto e exiba:
“O produto da categoria/subcategoria [digitada] é de R$ [valor identificado]”.
O valor está atrelado a categoria conforme regra abaixo:</h2>
<h3>Se for da categoria 1, o valor é de R$ 100,00</h3>
<h3>Se não for categoria 1 verifique qual é sua categoria</h3>

<h3 align="center">Categoria 2- Possui duas subcategorias:</h3>
<li>Subcategoria 3: R$ 50,00</li>
<li>Subcategoria 4: R$ 25,00</li>
<h3 align="center>Categoria 5- Possui duas subcategorias:</h3>
<li>Subcategoria 6: R$ 500,00</li>
<li>Subcategoria 7: R$ 800,00</li>
<li>Qualquer número o qual não tenha uma categoria registrada, deve exibir a mensagem: “Categoria inválida”
</li>

<h2>5 - Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
 Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.</h2> 

<h2>6 - Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário.
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.</h2>

<h2>7 - Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir</h2>



<h2>8 - Escreva um programa no qual o usuário informe o tipo de veículo dentre as opções: Carro, Moto, Caminhonete, Caminhão e Ônibus;
a distância a ser viajada, o consumo em Km por litro de combustível que o veículo faz e indique qual é o melhor combustível para utilizar, considerando os valores:</h2>
<li>Gasolina: R$ 7,45 por litro</li>
<li>Álcool: R$ 5,95 por litro</li>
<li>Diesel S10: R$ 6,65 por litro</li>
<li>Diesel S500: R$ 6,25 por litro</li>

<h3>Observe os tipos de combustíveis permitidos para os veículos informados:</h3>
<li>Carro: Gasolina e Álcool</li>
<li>Moto: Gasolina e Álcool</li>
<li>Caminhonete: Gasolina e Diesel S500</li>
<li>Caminhão e Ônibus: Diesel S500 e Diesel S10</li>
<h3>Para realizar o cálculo, o tipo de combustível selecionado deve ser compatível com o tipo do veículo, caso contrário, o programa deve exibir: “Veículos e Combustível incompatíveis”
Em caso de compatibilidade, o programa deverá exibir uma mensagem como: “O melhor combustível para o veículo [veículo informado] é o [combustível calculado], pois o valor dele é [valor calculado]. Já o combustível [combustível menos vantajoso], o valor dele é de [valor do combustível menos vantajoso].</h3>





<h2>9 - Fazer um programa que receba a dia e hora de início e do término de um jogo, em valores inteiros, exemplo:</h2>

<li>Dia Início: 2</li>
<li>Hora início: 10</li>
<li>Dia Término: 2</li>
<li>Hora Término: 15</li>
<h3>O Software deve calcular quanto tempo durou o jogo. Observa-se que um jogo pode começar em um dia e terminar em outro.
 O sistema deve exibir a quanto tempo durou o jogo e se começou e terminou no mesmo dia ou no dia seguinte.
 É impossível voltar no tempo, então o jogador não pode começar o jogo em dia após o término.</h3>

<h2>10 - Faça um programa que receba como entrada 5 registros contendo: O nome de um produto, seu valor unitário e quantidade comprada.
 O programa deve calcular o valor final dos produtos, se o valor final foi maior que 100, deve dar um desconto de 20% no valor total.
 No final o programa deve exibir a lista de produtos comprados, apresentando em linhas diferentes o nome, a quantidade, o valor unitário e valor total.
 Na última linha deve exibir: “Total: R$ … ; Valor do desconto: R$ … e Total com Desconto: R$ ….”</h2>
