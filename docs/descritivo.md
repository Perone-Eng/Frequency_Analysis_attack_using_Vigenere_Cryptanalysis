# Funcionamento da Cifra de Vigenère
A cifra de Vigenère é um método de criptografia simétrica baseada em substituição polialfabética, ou seja, utiliza vários alfabetos cifrantes em sequência para aumentar a segurança da mensagem. Para isso, é usada uma palavra-chave (chave) que determina o deslocamento de cada letra da mensagem original (texto claro).
A cifra opera sobre letras do alfabeto (geralmente de A a Z). Cada letra da mensagem é cifrada com base na letra correspondente da chave, repetida ciclicamente até cobrir toda a extensão do texto. Para cada posição, soma-se o valor numérico da letra do texto e da letra da chave (considerando A=0, B=1, ..., Z=25), e o resultado é reduzido módulo 26 para se manter dentro do alfabeto. O valor resultante é convertido de volta em uma letra, formando o texto cifrado.
Por exemplo, para cifrar a letra "E" com a letra da chave "B", somamos 4 (E) + 1 (B) = 5, o que resulta na letra "F". Esse processo é repetido para todas as letras da mensagem.
A decifragem segue o processo inverso: subtrai-se o valor da letra da chave do valor da letra cifrada, também módulo 26, recuperando a letra original. A segurança da cifra depende da aleatoriedade e do comprimento da chave: se a chave for curta ou previsível, a cifra torna-se vulnerável à criptoanálise por frequência.

# Funcionamento do Ataque por Análise de Frequência
O ataque por análise de frequência é uma técnica clássica de criptoanálise utilizada para quebrar cifras baseadas em substituição, especialmente aquelas que mantêm uma correspondência direta entre letras do texto claro e do texto cifrado. O princípio central do ataque é que, mesmo após cifrada, uma mensagem tende a preservar padrões estatísticos do idioma original, como a frequência de aparecimento das letras.
Por exemplo, em português, letras como "A", "E" e "O" são muito comuns, enquanto "Z" e "X" são raras. O atacante coleta uma amostra suficiente do texto cifrado e conta a frequência de cada letra ou grupo de letras (como bigramas ou trigramas). Em seguida, compara essa distribuição com a frequência típica da língua-alvo.
A partir dessa comparação, o atacante faz hipóteses sobre o mapeamento entre letras cifradas e letras reais. Suponha que a letra mais frequente do texto cifrado seja "P". Sabendo que "E" é geralmente a letra mais frequente em português, pode-se supor que "P" representa "E" na cifra. Com base nessa e em outras correspondências prováveis, o atacante constrói uma chave parcial de substituição e testa se o texto decifrado faz sentido. O processo é iterativo, combinando tentativa e erro com ajustes baseados no contexto linguístico.
Esse tipo de ataque é especialmente eficaz contra cifras monoalfabéticas (como a cifra de César), mas também pode ser adaptado para cifras polialfabéticas, como a de Vigenère, desde que o comprimento da chave seja curto ou possa ser estimado. Neste caso, a análise de frequência é aplicada separadamente a cada posição da chave repetida.

# Funções-chave de Cifrador.py
- Função `limpar_texto`
	   Remove acentos e caracteres não alfabéticos de uma string. Para cada caractere $c$ do texto de entrada (em maiúsculas), Se $c \in$ acentos, substitui por `acentos[c]`, se $c$ é letra (A–Z), mantém. O resultado é uma string contendo apenas letras sem acento.
- Função `Cifrar`
	    A função Cifrar aplica a cifra de Vigenère sobre um texto qualquer, utilizando uma chave composta apenas por letras. Antes da cifragem, tanto o texto quanto a chave são convertidos para letras maiúsculas, e caracteres acentuados são substituídos por suas versões sem acento. Durante o processo, cada letra do texto é deslocada no alfabeto de acordo com a posição correspondente da chave, de forma cíclica, aplicando a fórmula $c_i = (m_i + k_i) \bmod 26$, onde $m_i$ e $k_i$ são os índices da letra da mensagem e da chave no alfabeto. Caracteres fora do alfabeto (como pontuação, espaços ou letras com acento) são preservados sem alteração. A função também respeita a capitalização original das letras cifradas.
# Funções-chave de Decifrador.py
- Função `limpar_texto`
A função recebe uma string e retorna apenas as letras maiúsculas de A a Z, substituindo caracteres acentuados por suas versões sem acento. Para cada caractere $c$, se $c \in$ acentos, ele é trocado por `acentos[c]`; se $c$ for uma letra, é mantido.  
- Função `Decifrador`
  A função reverte a cifra de Vigenère aplicada a um texto, utilizando a mesma chave usada na cifragem. A chave é previamente limpa, mantendo apenas letras maiúsculas sem acento. Para cada letra $c_i$ do criptograma presente no alfabeto, calcula-se a letra original com a fórmula: $$ m_i = (c_i - k_i + 26) \bmod 26 $$ em que $c_i$ é o índice da letra cifrada e $k_i$ o da chave. O resultado mantém letras acentuadas e símbolos inalterados, e preserva a capitalização original.
# Funções-chave de Ataque_de_recuperação_de_senha.py
- Função `limpar_texto`
  O texto é primeiro convertido para maiúsculas, depois remove todos os caracteres não alfabéticos (exceto letras maiúsculas de A a Z) do texto.
- Função `encontrar_repeticoes`
   Procura repetições de trigramas (sequências de 3 letras consecutivas) em texto. Para cada trigrama que aparece mais de uma vez, calcula as distâncias (em posições) entre ocorrências consecutivas. Retorna uma lista com todas essas distâncias
- Função `fatores_comuns_top3`
    A função fatores_comuns_top3(distancias) identifica os três fatores mais frequentes (entre 2 e 20) das distâncias fornecidas, sugerindo possíveis tamanhos de chave `k`.
k com base na análise de repetição de trigramas no ataque por frequência.
- Função `fatiar_texto`
   A função divide texto em `k` fatias intercaladas, onde `k` = tamanho_chave , agrupando os caracteres que presumivelmente foram cifrados com a mesma letra da chave em um ciframento do tipo Vigenère.
- Função `calcular_frequencia`
  Calcula a frequência percentual de cada letra do alfabeto no texto, retornando um dicionário com a distribuição relativa em %.
- Função `descobrir_chave`
  Estima a chave de cifra por análise de frequência, buscando para cada fatia o deslocamento $\( d \in [0, 25] \)$ que minimiza o erro absoluto entre a frequência da fatia decifrada com $d$ e a frequência típica do idioma, construindo assim a provável chave de um ciframento de Vigenère.
- Função `chave_com_melhor_erro`
  A função seleciona a melhor chave candidata para um ciframento do tipo Vigenère ao testar os três tamanhos de chave mais prováveis, obtidos a partir das distâncias entre trigramas repetidos. Para cada tamanho, a função calcula uma chave por análise de frequência, decifra o texto com essa chave e avalia o erro total entre a distribuição de frequência da decifragem e a frequência esperada da língua. A melhor chave é aquela que minimiza o erro total.
- Função `ataque`
  A função tenta descobrir a chave de uma cifra de Vigenère aplicada a dois textos (em português e em inglês) por meio de análise de frequência. Ela identifica padrões repetidos para estimar o tamanho da chave, fatia o texto conforme essas estimativas e compara a frequência das letras com as frequências típicas de cada idioma. A melhor chave é aquela que, ao ser usada na decifragem, produz um texto com frequência mais próxima da esperada. Ao final, retorna as chaves estimadas para cada idioma.
