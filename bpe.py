# BPE: merge par mais frequente, repete K vezes
import re

vocab = {
    'l o w </w>': 5,
    'l o w e r </w>': 2,
    'n e w e s t </w>': 6,
    'w i d e s t </w>': 3
}
N_MERGES = 5


def get_stats(vocab):
    pairs = {}
    for word, freq in vocab.items():
        syms = word.split()
        for i in range(len(syms) - 1):
            p = (syms[i], syms[i + 1])
            pairs[p] = pairs.get(p, 0) + freq
    return pairs


def merge_vocab(pair, v_in):
    v_out = {}
    bigram = re.escape(pair[0]) + r' ' + re.escape(pair[1])
    pat = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word, freq in v_in.items():
        new = pat.sub(pair[0] + pair[1], word)
        v_out[new] = freq
    return v_out


if __name__ == "__main__":
    print("vocab inicial:")
    for w, f in vocab.items():
        print(f"  {w}: {f}")
    print()
    for i in range(N_MERGES):
        stats = get_stats(vocab)
        best = max(stats, key=stats.get)
        print(f"merge {i + 1}: {best} (freq {stats[best]})")
        vocab = merge_vocab(best, vocab)
        for w, f in vocab.items():
            print(f"  {w}: {f}")
        print()
