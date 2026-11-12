#Função Cifrar
def Cifrar(texto, key):
  abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
       "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

  acentos = {'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 'Ä': 'A',
           'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
           'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
           'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O', 'Ö': 'O',
           'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
           'Ç': 'C'}

  def limpar_texto(texto):
      texto_novo = ''
      for c in texto.upper():
          if c in acentos:
              texto_novo += acentos[c]
          elif c.isalpha():
              texto_novo += c
      return texto_novo

  # Limpa chave (a chave deve ser só letras)
  key = limpar_texto(key)

  # Processo de cifra
  criptograma = ""
  key_index = 0

  for c in texto:
      c_maiusculo = c.upper()

      # Verifica se a letra é do alfabeto sem acento
      if c_maiusculo in abc:
          n = abc.index(c_maiusculo)
          k = abc.index(key[key_index % len(key)])
          new_letter = (n + k) % 26
          # Mantém minúsculo se a letra original era minúscula
          letra_cifrada = abc[new_letter].lower() if c.islower() else abc[new_letter]
          criptograma += letra_cifrada
          key_index += 1

      # Se for letra com acento, mantém inalterada
      elif c_maiusculo in acentos.keys():
          criptograma += c

      # Se for espaço, vírgula, ponto ou outro caractere especial, mantém inalterado
      else:
          criptograma += c

  return criptograma

#Função de Decifrar
def Decifrador(criptograma, key):
       abc = ["A","B","C","D","E","F", "G", "H", "I", "J", "K", "L",
              "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y","Z"]

       acentos = {'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 'Ä': 'A',
                  'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
                  'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
                  'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O', 'Ö': 'O',
                  'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
                  'Ç': 'C'}

       def limpar_texto(texto):
           texto_novo = ''
           for c in texto.upper():
               if c in acentos:
                   texto_novo += acentos[c]
               elif c.isalpha():
                   texto_novo += c
           return texto_novo


       # Limpa chave (só letras, sem espaços)
       key = limpar_texto(key)

       # Processo de decifra
       mensagem = ""
       key_index = 0

       for c in criptograma:
           c_maiusculo = c.upper()

           # Se for letra sem acento
           if c_maiusculo in abc:
               n = abc.index(c_maiusculo)
               k = abc.index(key[key_index % len(key)])
               msg_letter = ((n - k) + 26) % 26
               letra_decifrada = abc[msg_letter].lower() if c.islower() else abc[msg_letter]
               mensagem += letra_decifrada
               key_index += 1

           # Se for letra com acento, mantém inalterada
           elif c_maiusculo in acentos.keys():
               mensagem += c

           # Se for espaço, vírgula, ponto ou outro caractere especial, mantém inalterado
           else:
               mensagem += c

       return mensagem

#Função de Ataque
def ataque(texto_pt, texto_en):
    import re
    from collections import Counter

    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    frequencia_portugues = {'A': 14.63, 'B': 1.04, 'C': 3.88, 'D': 4.99, 'E': 12.57, 'F': 1.02, 'G': 1.30,
        'H': 1.28, 'I': 6.18, 'J': 0.40, 'K': 0.02, 'L': 2.78, 'M': 4.74, 'N': 5.05,
        'O': 10.73, 'P': 2.52, 'Q': 1.20, 'R': 6.53, 'S': 7.81, 'T': 4.34, 'U': 4.63,
        'V': 1.67, 'W': 0.01, 'X': 0.21, 'Y': 0.01, 'Z': 0.47}

    frequencia_ingles = {'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.70, 'F': 2.23, 'G': 2.02,
        'H': 6.09, 'I': 6.97, 'J': 0.15, 'K': 0.77, 'L': 4.03, 'M': 2.41, 'N': 6.75,
        'O': 7.51, 'P': 1.93, 'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06, 'U': 2.76,
        'V': 0.98, 'W': 2.36, 'X': 0.15, 'Y': 1.97, 'Z': 0.07}

    def limpar_texto(texto):
        return re.sub(r'[^A-Z]', '', texto.upper())

    def encontrar_repeticoes(texto):
        trigrams = {}
        for i in range(len(texto) - 2):
            trigram = texto[i:i + 3]
            if trigram in trigrams:
                trigrams[trigram].append(i)
            else:
                trigrams[trigram] = [i]

        distancias = []
        for positions in trigrams.values():
            if len(positions) > 1:
                for i in range(len(positions) - 1):
                    distancia = positions[i + 1] - positions[i]
                    distancias.append(distancia)
        return distancias

    def fatores_comuns_top3(distancias):
        if not distancias:
            return [1]

        fatores = []
        for d in distancias:
            for i in range(2, 21):  # testamos tamanhos de chave até 20
                if d % i == 0:
                    fatores.append(i)

        contagem = Counter(fatores).most_common(3)
        return [f[0] for f in contagem] if contagem else [1]

    def fatiar_texto(texto, tamanho_chave):
        return [texto[i::tamanho_chave] for i in range(tamanho_chave)]

    def calcular_frequencia(texto):
        contador = Counter(texto)
        total = sum(contador.values())
        return {letra: (contador.get(letra, 0) / total) * 100 for letra in abc}

    def descobrir_chave(fatias, freq_idioma):
        chave = ''
        for fatia in fatias:
            menor_erro = float('inf')
            melhor_deslocamento = 0

            for deslocamento in range(26):
                texto_deslocado = ''.join(abc[(abc.index(c) - deslocamento) % 26] for c in fatia)
                freq_texto = calcular_frequencia(texto_deslocado)

                erro = sum(abs(freq_texto.get(l, 0) - freq_idioma.get(l, 0)) for l in abc)

                if erro < menor_erro:
                    menor_erro = erro
                    melhor_deslocamento = deslocamento

            chave += abc[melhor_deslocamento]
        return chave

    def chave_com_melhor_erro(texto, freq_idioma):
        distancias = encontrar_repeticoes(texto)
        candidatos = fatores_comuns_top3(distancias)

        melhor_chave = None
        menor_erro_total = float('inf')

        for tamanho_chave in candidatos:
            fatias = fatiar_texto(texto, tamanho_chave)
            chave = descobrir_chave(fatias, freq_idioma)

            texto_decodificado = Decifrador(texto, chave) #Decifrador aqui é o mesmo da outra file!
            freq_texto_dec = calcular_frequencia(texto_decodificado)
            erro_total = sum(abs(freq_texto_dec[l] - freq_idioma[l]) for l in abc)

            if erro_total < menor_erro_total:
                menor_erro_total = erro_total
                melhor_chave = chave

        return melhor_chave

    # Limpa os textos
    texto_pt_limpo = limpar_texto(texto_pt)
    texto_en_limpo = limpar_texto(texto_en)

    # Descobre as chaves
    chave_pt = chave_com_melhor_erro(texto_pt_limpo, frequencia_portugues)
    chave_en = chave_com_melhor_erro(texto_en_limpo, frequencia_ingles)

    # Mostra as chaves
    x = f"Chave descoberta para o texto em Português: {chave_pt}"
    y = f"Chave descoberta para o texto em Inglês: {chave_en}"
    chaves = [x,y]
    return chaves

#Interface
print("Selecione uma opção:\n 1 - Cifrar uma mensagem \n 2 - Decifrar uma mensagem \n 3 - Obter senha por ataque de análise de frequência")
opcao = int(input())
if opcao == 1:
  texto = input("Digite a mensagem: ")
  key = input("Digite a chave: ")
  xl = Cifrar(texto, key)
  print(xl)
elif opcao == 2:
  criptograma = input("Digite a mensagem cifrada: ")
  key = input("Digite a chave: ")
  xl = Decifrador(criptograma,key)
  print(xl)
elif opcao == 3:
  texto_pt = input("Digite a mensagem em português cifrada: ")
  texto_en  = input("Digite a mensagem em inglês cifrada: ")
  xli = ataque(texto_pt, texto_en)
  print(xli[0])
  print(xli[1])
else: 
  print("Opção inválida!")
