import os

with open('salmonella_spi1_region.fna', 'r') as f, open('salmonella.txt', 'w') as f_out:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        if len(line) <= 80:
            f_out.write(line)
