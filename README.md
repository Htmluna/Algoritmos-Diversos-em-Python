# Projeto de Algoritmos Diversos

## Descrição do Projeto

Este repositório contém a implementação de quatro algoritmos distintos solicitados por diferentes clientes e contextos. Cada tarefa envolve a criação de um programa específico para resolver problemas únicos. Abaixo está uma descrição detalhada de cada um dos quatro algoritmos implementados.

### 1. Cálculo de Bônus de Serviço de Estúdio de Gravação

Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.

#### Funcionalidades
- Receber o tipo de assinatura do cliente.
- Receber o faturamento anual do cliente.
- Calcular e exibir o valor do bônus que o cliente deve pagar ao serviço.

#### Tabela de Porcentagens
| Nível    | Porcentagem sobre o faturamento |
|----------|---------------------------------|
| Basic    | 30%                             |
| Silver   | 20%                             |
| Gold     | 10%                             |
| Platinum | 5%                              |

### 2. Votação do Melhor Dia para Lives

Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.

### 3. Cálculo de Média de Notas para Turmas Grandes

A escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.

#### Requisitos Especiais
- Exibir uma mensagem indicando se o professor está digitando as notas dos alunos pares ou ímpares.
- Mensagem ao inserir cada nota:

VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.


### 4. Desbloqueio de Servidor Após Ataque Hacker

Um grande cliente sofreu um ataque hacker: o servidor foi sequestrado por um software malicioso que criptografou todos os discos e pede a digitação de uma senha para a liberação da máquina. A senha é composta pela palavra “LIBERDADE” seguida do fatorial dos minutos que a máquina estiver marcando no momento da digitação da senha.

#### Funcionalidades
- Receber os minutos atuais da máquina.
- Calcular o fatorial dos minutos utilizando loop (não é permitido o uso de funções prontas para o cálculo do fatorial).
- Exibir a senha necessária para o desbloqueio.

## Como Executar

Cada algoritmo está implementado em um arquivo Python separado. Para executar qualquer um dos programas, basta rodar o script correspondente utilizando Python 3.x.

### Exemplo
Para executar o cálculo de bônus:
```bash
python calculo_bonus.py
