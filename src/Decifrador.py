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
