def gc_blocks(seq, block_size):

    seq_list = ()

    #Generates subsequences
    for i in range(len(seq) // block_size):
        seq_list = seq_list + (seq[(i * block_size):((i * block_size) + block_size)],)

    #Finding GC content

    gc_list = ()

    for i in range(len(seq) // block_size):
        working_string = seq_list[i]
        count = 0
        for j in range(block_size):
            if working_string[j] == 'G':
                count += 1
            if working_string[j] == 'C':
                count += 1
        gc_content = count / block_size
        gc_list = gc_list + (gc_content,)

    return gc_list
