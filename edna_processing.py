
from Bio import SeqIO

def parse_edna_fastq(filepath):
    species_detected = set()
    for record in SeqIO.parse(filepath, "fastq"):
        if len(record.seq) > 100:
            species_detected.add("sample_fish_species")
    print(f"Species detected: {species_detected}")
    return species_detected

if __name__ == "__main__":
    parse_edna_fastq("sample.fastq")
