from bpe import get_stats, merge_vocab, vocab


def test_par_mais_frequente():
    stats = get_stats(vocab)
    best = max(stats, key=stats.get)
    assert best == ('e', 's'), f"par errado: {best}"
    assert stats[best] == 9, f"freq errada: {stats[best]}"
    print("ok: par mais frequente")


def test_todos_pares_positivos():
    stats = get_stats(vocab)
    for p, f in stats.items():
        assert f > 0, f"freq negativa: {p}"
    print("ok: todos pares positivos")


if __name__ == "__main__":
    test_par_mais_frequente()
    test_todos_pares_positivos()
    print("\ntodos os testes passaram")
