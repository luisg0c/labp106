# Lab 6 - Tokenizador BPE e WordPiece

Implementacao do algoritmo BPE (Byte Pair Encoding) do zero e comparacao do WordPiece usando o BERT multilingual e o BERTimbau.

O BPE funde pares de simbolos mais frequentes iterativamente. Apos 5 rodadas no corpus de exemplo, formam-se tokens morfologicos como `est</w>` (sufixo superlativo) e `low` (raiz).

## Dependencias

    pip install transformers

## WordPiece

Tokens com `##` na frente (tipo `##mente`, `##etros`) sao pedacos que continuam a palavra anterior, nao palavras novas. O tokenizer WordPiece quebra palavras raras ou compridas em sub-palavras que ele conhece, entao o modelo nunca trava com vocabulario desconhecido. O BERTimbau (treinado so em portugues) quebra bem menos que o multilingual porque tem mais palavras portuguesas inteiras no vocabulario, por exemplo `parâmetros` fica inteiro no BERTimbau mas vira `par ##âm ##etros` no multilingual.

## Como rodar

    python bpe.py
    python wordpiece.py
    python test_bpe.py

## Uso de IA

Ferramenta usada: Claude Sonnet 4.6

- O padrao regex com lookahead/lookbehind no `merge_vocab` foi gerado com auxilio de IA e revisado manualmente
- Sugestao do tokenizer `neuralmind/bert-base-portuguese-cased` (BERTimbau) pra comparar com o multilingual
