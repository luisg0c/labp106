# Lab 6 - Tokenizador BPE e WordPiece

Implementacao do algoritmo BPE (Byte Pair Encoding) do zero e comparacao do WordPiece usando o BERT multilingual e o BERTimbau.

O BPE funde pares de simbolos mais frequentes iterativamente. Apos 5 rodadas no corpus de exemplo, formam-se tokens morfologicos como `est</w>` (sufixo superlativo) e `low` (raiz).

## Dependencias

    pip install transformers

## Como rodar

    python bpe.py
    python wordpiece.py
    python test_bpe.py
