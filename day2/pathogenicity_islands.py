def gc_blocks(seq, block_size):

    seq_list = ()

    for i in range(len(seq) // block_size):
        seq_list = seq_list + (seq[(i * block_size):((i * block_size) + block_size)],)

    return seq_list
