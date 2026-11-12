# Cifra de Vigenère e Ataque por Análise de Frequência

Implementação em Python da **cifra de Vigenère** (cifragem e decifragem) e de um **ataque de recuperação de chave** que combina o **método de Kasiski** (repetição de trigramas) com **análise de frequência** de letras, para textos em **português** e **inglês**.

Projeto 1 da disciplina **Segurança Computacional** — Universidade de Brasília (UnB), 2025.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
![Dependências](https://img.shields.io/badge/depend%C3%AAncias-nenhuma-brightgreen)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🎥 Apresentação em vídeo

[Assista à explicação do projeto no YouTube](https://www.youtube.com/watch?v=2BVwqRQtI5w&t=130s)

📄 Descrição detalhada de cada função: [`docs/descritivo.md`](docs/descritivo.md)

---

## Sumário

- [Funcionalidades](#funcionalidades)
- [Como funciona](#como-funciona)
- [Como executar](#como-executar)
- [Exemplo](#exemplo)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Limitações](#limitações)

---

## Funcionalidades

| Opção | Descrição |
|---|---|
| **1 — Cifrar** | Cifra uma mensagem com uma chave alfabética |
| **2 — Decifrar** | Recupera a mensagem original a partir do criptograma e da chave |
| **3 — Ataque** | Descobre a chave de dois criptogramas (um em português e outro em inglês) sem conhecê-la |

Detalhes do tratamento de texto:

- letras acentuadas e `Ç` são normalizadas na chave;
- espaços, pontuação e letras acentuadas da mensagem são preservados sem cifragem;
- a capitalização original (maiúsculas/minúsculas) é mantida.

## Como funciona

### Cifra de Vigenère

Cada letra da mensagem é deslocada pela letra correspondente da chave, repetida ciclicamente (A = 0, …, Z = 25):

$$c_i = (m_i + k_i) \bmod 26 \qquad\qquad m_i = (c_i - k_i + 26) \bmod 26$$

### Ataque de recuperação da chave

1. **Limpeza** — o criptograma é reduzido às letras A–Z.
2. **Tamanho da chave (Kasiski)** — trigramas repetidos são localizados e as distâncias entre ocorrências são fatoradas; os **3 fatores mais frequentes** entre 2 e 20 viram candidatos a tamanho de chave.
3. **Fatiamento** — para cada tamanho `k`, o texto é dividido em `k` fatias com as letras cifradas pela mesma letra da chave.
4. **Análise de frequência** — em cada fatia, testa-se os 26 deslocamentos e escolhe-se o que minimiza o erro absoluto entre a frequência observada e a frequência típica do idioma.
5. **Escolha final** — entre os candidatos, vence a chave cuja decifragem completa fica mais próxima da distribuição de letras do idioma.

## Como executar

Requer apenas **Python 3** — sem dependências externas.

```bash
git clone https://github.com/Perone-Eng/Projeto_1_Seg_Comp.git
cd Projeto_1_Seg_Comp
python src/main.py
```

Testes automatizados:

```bash
python -m unittest discover -s tests
```

> Um executável para Windows (`main.exe`) está disponível na aba **Releases**.

## Exemplo

```text
$ python src/main.py
Selecione uma opção:
 1 - Cifrar uma mensagem
 2 - Decifrar uma mensagem
 3 - Obter senha por ataque de análise de frequência
1
Digite a mensagem: Ataque ao amanhecer!
Digite a chave: LIMAO
Lbmqip ia aalvteqpz!
```

No ataque (opção 3), com textos de algumas centenas de letras cifrados com as chaves `SENHA` (português) e `LEMON` (inglês), o programa recupera as duas chaves corretamente — cenário coberto em [`tests/test_vigenere.py`](tests/test_vigenere.py).

## Estrutura do repositório

```
Projeto_1_Seg_Comp/
├── src/
│   ├── main.py                # interface de linha de comando (autocontida)
│   ├── cifrador.py            # função Cifrar
│   ├── decifrador.py          # função Decifrador
│   └── ataque_frequencia.py   # Kasiski + análise de frequência
├── tests/
│   └── test_vigenere.py
├── docs/
│   └── descritivo.md          # teoria e descrição de cada função
├── .gitignore
├── LICENSE
└── README.md
```

## Limitações

- O ataque depende de textos razoavelmente longos; com poucas letras, a estatística de frequência não é confiável.
- Tamanhos de chave são buscados apenas entre 2 e 20.
- Quando o tamanho real da chave é um divisor de um candidato, o ataque pode devolver a chave repetida (ex.: `SENHASENHA`).

## Autor

**Felipe Perone**

## Licença

Distribuído sob a licença MIT. Veja [`LICENSE`](LICENSE).
