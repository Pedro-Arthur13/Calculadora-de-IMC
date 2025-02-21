---

# Calculadora de IMC
<img src="https://memes.memedrop.io/production/Dk613ekq8ymR/source.gif" alt="Yokuso" width="1050" height="auto"/>

Este projeto implementa uma calculadora de Índice de Massa Corporal (IMC) utilizando a biblioteca Tkinter, com uma interface gráfica simples. O programa permite ao usuário inserir seu nome, peso e altura, calcular o IMC e salvar os dados em um arquivo de texto.

## Autores
- [Pedro Arthur](https://github.com/Pedro-Arthur13)
- [Emanuel Rodrigues](https://github.com/wManell)
- Miguel Sthevão

## Instalação

Para rodar o projeto em seu computador, você pode optar por utilizar o executável fornecido ou seguir os passos abaixo para rodar o código diretamente:

### Usando o Executável
Você pode baixar o executável para rodar o aplicativo diretamente sem precisar configurar o ambiente Python. O executável está disponível na página de releases do repositório.

1. Acesse a [Release 1.0](https://github.com/Pedro-Arthur13/Calculadora-de-IMC/releases/tag/Calculator).
2. Baixe o arquivo executável compatível com seu sistema operacional.
3. Após o download, basta executar o arquivo para iniciar o aplicativo.

### Usando o Código-Fonte
Se preferir rodar o código-fonte, siga as etapas abaixo:

1. Clone o repositório:
    ```bash
    git clone https://github.com/Pedro-Arthur13/Calculadora-de-imc.git
    ```

2. Navegue até a pasta do projeto:
    ```bash
    cd Calculadora-de-imc
    ```

3. Verifique se o Python 3.x está instalado em seu computador. Caso não tenha, instale-o a partir de [python.org](https://www.python.org/downloads/).

4. Instale a biblioteca Tkinter (se necessário). Em sistemas baseados em Debian/Ubuntu, você pode instalar Tkinter com:
    ```bash
    sudo apt-get install python3-tk
    ```

5. Execute o código:
    ```bash
    python3 imc_calculadora.py
    ```

### No Arch Linux
Para usuários do Arch Linux, você pode baixar o executável e rodar diretamente ou instalar o pacote via AUR, caso esteja disponível.

1. Instale o **python-tk** se não o tiver:
    ```bash
    sudo pacman -S python-tk
    ```



## Como Usar

1. Abra a aplicação.
2. Preencha seu **Nome**, **Peso** (em kg) e **Altura** (em metros) nos campos correspondentes.
3. Clique no botão **Calcular** para calcular seu IMC.
4. O IMC será exibido abaixo, junto com uma mensagem indicando o resultado.
5. Todas as informações inseridas serão salvas em um arquivo de texto com nome `info.txt`.

## Funcionalidades

- **Cálculo do IMC:** O IMC é calculado com a fórmula: IMC = peso/altura^2
- **Validação de Entrada:** O programa verifica se o peso e a altura são valores positivos e se são números válidos.
- **Salvar Dados:** Os dados (Nome, Peso, Altura, IMC) são salvos em um arquivo de texto.

## Exceções Tratadas

- **NegativeValueError:** Caso o peso ou altura sejam menores ou iguais a zero, uma exceção personalizada será gerada, exibindo uma mensagem de erro.
- **ValueError:** Caso o peso ou a altura não sejam números válidos, uma exceção será gerada, indicando que as entradas precisam ser numéricas.

  
## Projeto na Disciplina de Programação Orientada a Objetos
- Este projeto faz parte da matéria de **Programação Orientada a Objetos**, ministrada pelo professor [Michel da Silva](https://github.com/MichelZero).
--- 
