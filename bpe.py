# BPE: merge par mais frequente, repete K vezes

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
            pairs[p] = pairs.get(p, 0) + 1
    return pairs


if __name__ == "__main__":
    stats = get_stats(vocab)
    print("pares:", stats)
    best = max(stats, key=stats.get)
    print("melhor par:", best, stats[best])
