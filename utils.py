def read_fasta(file_name):
    with open(file_name) as file:
        text_content = file.read()
        begin = text_content.find("\n")
        head = text_content[0:begin]
        genome = text_content[begin + 1:].replace("\n", "")
        return head, genome


def reverse_complement(s):
    ans = ""
    d = {"A": "T", "T": "A", "G": "C", "C": "G"}
    for letter in s:
        ans += d[letter]
    return ans[::-1]


def hamming_distance(s1, s2):
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1
    return dist


def find_pattern_with_mismatches(text, pattern, d):
    k = len(pattern)
    n = len(text)
    count = 0
    for i in range(n - k):
        if hamming_distance(text[i:i + k], pattern) <= d:
            count += 1
    return count


def neighborhood(pattern, d):
    neighbors = []
    k = len(pattern)

    def recurse(s, diffs):
        if len(s) < k:
            if diffs > 0:
                for letter in ['A', 'T', 'G', 'C']:
                    if letter == pattern[len(s)]:
                        recurse(s + letter, diffs)
                    else:
                        recurse(s + letter, diffs - 1)
            else:
                recurse(s + pattern[len(s)], 0)
        else:
            neighbors.append(s)

    recurse('', d)
    return neighbors


def frequent_matches_with_mismatches(genome, k, d):
    freq_map = {}
    n = len(genome)
    for i in range(n - k + 1):
        pattern = genome[i:i + k]
        neighbors = neighborhood(pattern, d)
        c_pattern = reverse_complement(pattern)
        neighbors += neighborhood(c_pattern, d)
        for nb in neighbors:
            if nb not in freq_map:
                freq_map[nb] = 1
            else:
                freq_map[nb] += 1
    max_val = max(freq_map.values())
    ans = [key for key in freq_map if freq_map[key] == max_val]
    return ans, max_val