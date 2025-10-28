def top_n(word_counts, n):
    return sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))[:n]
