def binary_similarity(n, m):
    # Convert the numbers to binary strings
    n_bin = bin(n)[2:]
    m_bin = bin(m)[2:]
    
    # Make the binary strings the same length by padding with zeros
    max_len = max(len(n_bin), len(m_bin))
    n_bin = n_bin.zfill(max_len)
    m_bin = m_bin.zfill(max_len)
    
    # Compute the similarity
    similarity = 0
    for i in range(max_len):
        if n_bin[i] != m_bin[i]:
            similarity += 1
    
    return similarity
print(binary_similarity(4,2))