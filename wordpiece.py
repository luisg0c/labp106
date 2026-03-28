from transformers import AutoTokenizer

tok_multi = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
tok_pt = AutoTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")

frase = "Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."

tokens_multi = tok_multi.tokenize(frase)
tokens_pt = tok_pt.tokenize(frase)

print("frase:", frase)
print()
print("multilingual:", tokens_multi)
print("bertimbau:   ", tokens_pt)
print()
print("tokens multi:", len(tokens_multi))
print("tokens pt:   ", len(tokens_pt))
