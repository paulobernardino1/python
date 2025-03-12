# Calculadora de Regra de Três Direta

Este é um projeto simples de calculadora utilizando **Tkinter** para calcular a regra de três direta. A interface gráfica permite ao usuário inserir três valores e calcular o quarto valor com base na fórmula da regra de três direta:

\[
\frac{b}{a} = \frac{c}{x} \Rightarrow x = \frac{b \times c}{a}
\]

## Funcionalidades

- Entrada de valores para `a`, `b` e `c`.
- Cálculo do valor de `x` automaticamente.
- Exibição do resultado de forma rápida e simples.
- Validação dos campos para garantir que apenas números válidos sejam inseridos.

## Como usar

1. **Instalação do Python**: Certifique-se de ter o Python instalado na sua máquina. Você pode fazer o download em [python.org](https://www.python.org/downloads/).
   
2. **Instalar as dependências**:
    O código utiliza a biblioteca **Tkinter**, que já é fornecida com o Python, então não é necessário instalar pacotes adicionais.

3. **Executando o código**:
   - Baixe o arquivo `.py` do projeto.
   - Abra o terminal ou prompt de comando.
   - Navegue até o diretório onde o arquivo está localizado.
   - Execute o comando:

     ```bash
     python nome_do_arquivo.py
     ```

4. **Usando a calculadora**:
   - Preencha os campos com os valores de `a`, `b` e `c`.
   - O valor de `x` será calculado automaticamente após pressionar o botão "Calcular".
   - O resultado será exibido no campo `x`, com fundo azul e texto branco.

## Estrutura do Projeto


## Detalhes Técnicos

- **Tkinter**: Utilizado para criar a interface gráfica do usuário (GUI).
- **ttk.Entry**: Para os campos de entrada de texto (para os valores de `a`, `b`, `c` e o resultado).
- **Botões e Labels**: Organizados para permitir uma fácil interação com o usuário.
- **Tratamento de erros**: Caso o usuário insira valores não numéricos, o sistema exibe uma mensagem de erro solicitando valores válidos.

## Licença

Este projeto é de código aberto e pode ser utilizado e modificado conforme necessário.


