# Calculadora de IMC

Programa simples em Python que calcula o Índice de Massa Corporal (IMC) a partir do peso e da altura informados pelo usuário, e classifica o resultado de acordo com as faixas oficiais.

## Como funciona

O programa pede ao usuário para digitar o peso (em kg) e a altura (em metros), calcula o IMC usando a fórmula:

```
IMC = peso / (altura * altura)
```

Em seguida, compara o resultado com faixas de referência usando estruturas `if / elif / else` e exibe a classificação correspondente.

## Tabela de classificação

| IMC             | Classificação        |
|-----------------|-----------------------|
| Menor que 18.5  | Abaixo do peso         |
| 18.5 a 24.9     | Peso normal             |
| 25 a 29.9       | Sobrepeso                |
| 30 a 34.9       | Obesidade grau I        |
| 35 a 39.9       | Obesidade grau II       |
| 40 ou mais      | Obesidade grau III      |

## Requisitos

- Python 3.x instalado

## Como executar

1. Clone ou baixe este repositório.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

```bash
python Imc.py
```

4. Digite seu peso e sua altura quando solicitado.

## Exemplo de uso

```
Coloque seu peso (kg): 70
Coloque sua altura (m): 1.75

Seu IMC é: 22.86
Resultado: Peso normal
```

## Observações

- A altura deve ser digitada usando ponto como separador decimal (ex: `1.75`), não vírgula.
- O comando `os.system('cls')` limpa a tela do terminal antes de iniciar; ele funciona no Windows. Em sistemas Linux/Mac, o comando equivalente seria `os.system('clear')`.

## Possíveis melhorias futuras

- Tratamento de erros para entradas inválidas (texto em vez de número).
- Permitir múltiplas consultas sem precisar reiniciar o programa.
- Interface gráfica (GUI) ou versão web.

## Autor

Projeto pessoal de estudo em Python.
