# Lab 6 - Tokenizador BPE e WordPiece

Implementação do BPE (Byte Pair Encoding) do zero em Python puro e exploração do WordPiece via BERT multilingual e BERTimbau.

## BPE: o que ele faz

A cada iteração, o BPE conta os pares adjacentes de símbolos no vocabulário e funde o par mais frequente em um único token. Após K iterações, formam-se sub-palavras morfológicas estáveis (sufixos como `est</w>`, raízes como `low`).

## WordPiece: o `##`

Tokens com `##` na frente (`##mente`, `##etros`) são pedaços que continuam a palavra anterior, não tokens novos. Quando o tokenizer encontra uma palavra fora do vocabulário, ele quebra em sub-palavras conhecidas — assim o modelo nunca trava com OOV. O BERTimbau (só português, vocab 29k) quebra menos que o multilingual (119k vocab, 100+ línguas) porque tem mais palavras portuguesas inteiras no vocab.

## Como rodar

    pip install transformers
    python bpe.py
    python wordpiece.py
    python test_bpe.py

## Saída

BPE em 5 iterações sobre o corpus do enunciado:

```
merge 1: ('e', 's') -> es  freq=9
merge 2: ('es', 't') -> est  freq=9
merge 3: ('est', '</w>') -> est</w>  freq=9
merge 4: ('l', 'o') -> lo  freq=7
merge 5: ('lo', 'w') -> low  freq=7

vocab final:
  low </w>: 5
  low e r </w>: 2
  n e w est</w>: 6
  w i d est</w>: 3
```

WordPiece comparando os dois tokenizadores na frase do enunciado:

```
frase: Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar.

multilingual (27 tokens):
  ['Os', 'hip', '##er', '-', 'par', '##âm', '##etros', 'do', 'transform', '##er',
   'são', 'in', '##cons', '##tit', '##uc', '##ional', '##mente', 'di', '##f', '##í',
   '##cei', '##s', 'de', 'aj', '##usta', '##r', '.']

bertimbau (16 tokens):
  ['Os', 'hiper', '-', 'parâmetros', 'do', 'transform', '##er', 'são', 'incons',
   '##titu', '##cionalmente', 'difíceis', 'de', 'ajus', '##tar', '.']
```

`parâmetros` fica inteiro no BERTimbau, mas vira `par ##âm ##etros` no multilingual — o vocab português dedicado evita quase metade dos splits.

## Uso de IA

Ferramenta usada: Claude Sonnet 4.6

- Padrão regex com lookarounds no `merge_vocab` para evitar fundir tokens que são prefixo de outros
- Sugestão do tokenizer `neuralmind/bert-base-portuguese-cased` (BERTimbau) para comparar com o multilingual
- Estruturação do README (organização das seções, blocos de exemplo)
