# Automate Send

Esse projeto consiste em um programa simples para que seja possível enviar automaticamente a mesma mensagem para diversos contatos.O programa faz um pequeno tratamento do numero de telefone(removendo hífen, espaço, parenteses e adicionando o DD), e realizando o envio de uma mensagem com o nome do contato e a mensagem que esta no arquivo [mensage.txt](mensage.txt).

O software e livre e sinta-se a vontade para adapta-lo a sua necessidade.Não me responsabilizo pela utilização do mesmo.

## Como utilizar

Primeiro passo e realizar a atualizacao dos arquivos [book](book.csv) e [mensagem](mensage.txt) com os contatos que receberão a mensagem respectivamente.
Posteriormente, utilize o comando no seu terminal(linux,mac ou windows):

    python Automate_send.py

o navegador sera aberto automaticamente para realização do login no whatsapp web, realize o login e o software ira automaticamente começar o envio das mensagens.
outra possibilidade e a execução através do notebook [Automate_send.ipynb](Automate_send.ipynb), o resultado final será o mesmo.

## Requisitos

-   Os telefones de contato devem estar no formato:
    -   (DD) 9xxxx-xxxx;
    -   (DD) xxxx-xxxx;
    -   DD9xxxx-xxxx ou
    -   DDxxxx-xxxx;
-   O contato deve ser preenchido na tabela book.csv que esta contido nessa pasta.
-   A mensagem deve ser escrita no arquivo mensage.txt , utilizando "{}" no local da mensagem que gostaria de substituir pelo nome da empresa ou pessoa que voce gostaria de enviar a mensagem.
-   Navegador Safari(é possivel realizar a troca pelo chrome [nessa linha](Automate_send.py#L38) do arquivo)

## Limitações

-   Este software esta inicialmente configurado para mandar mensagem somente para o Brasil(DDI +55), porem com uma pequena alterações no arquivo .py e no csv, ele pode enviar para qualquer outro numero valido do WPP.
-   Não e possível fazer o envio de anexos (audio,video, fotos,arquivos e etc) na mensagem.
-   O software não faz a validação do numero antes do envio. De forma que caso o numero nao exista ou não tenha WhatsApp o sistema trava o envio e nao realiza o fechamento do browser.
-   O software faz a inserção do nono digito( o digito 9 apos o DDD) através da conta se o numero armazenado tem 10 algarismos(8 do numero + 2 do ddd).
-   O sistema foi testado somente com o safari.

## Links uteis

[Format String in python](https://docs.python.org/3/library/string.html#format-examples)

[Selenium python documentation](https://selenium-python.readthedocs.io)
