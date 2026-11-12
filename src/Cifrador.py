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
