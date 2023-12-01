# Simple-DNS-Resolver-Python
Um simples script em Python que utiliza a biblioteca dnspython para realizar consultas de resolução de DNS para um domínio específico. Este código tem como objetivo obter registros de tipo 'A' de um domínio, oferecendo uma ferramenta prática para realizar consultas de DNS de forma eficiente e direta.

# Pré-requisitos
Certifique-se de que o Python esteja instalado em seu ambiente. Para utilizar este script, é necessário ter a biblioteca 'dnspython' instalada. Caso não a tenha, você pode instalá-la utilizando o terminal com o comando: pip install dnspython.

# Funcionamento
O script cria uma instância do resolver DNS e tenta resolver o domínio especificado. Se bem-sucedido, ele imprime os registros 'A' correspondentes ao domínio. 
Atenção ao inserir o domínio corretamente na variável "alvo".

# Notas
Este script foi desenvolvido como uma ferramenta simples para consultar registros DNS de um domínio específico, visando auxiliar em testes de penetração (pentest). Ele permite a obtenção de registros de tipo 'A' para um domínio fornecido, facilitando a análise e a investigação de informações relevantes durante testes de segurança.
Utilize-o com responsabilidade e em conformidade com os regulamentos e políticas de uso de redes e sistemas. APENAS PARA FINS DE ESTUDO.
