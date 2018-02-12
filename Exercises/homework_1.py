"""
Homework 01
DO NOT RENAME THIS FILE OR ANY DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".
"""


# String Functions
import os
def fast_complement(dna):
    """
    Uses a dictionary to convert a DNA sequence into the complement strand.  C <--> G,  T <--> A
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    str = ''
    dict = {'C':'G','G':'C','A':'T','T':'A'}
    for char in dna:
        if char == 'C' or char == 'G' or char == 'T' or char == 'A':
            str = str + dict[char]
        else :
            str = 'invalid character entered, please check the input'
            break
    return str

result_complemet=fast_complement('ACTG')
print('For input ACTG the o/p is :',result_complemet)

def remove_interval(s, start, stop):
    """
    Removes the interval of characters from a string or list inclusively, 0 based
    EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    :param s: a string
    :param start: a non-negative integer
    :param stop: a non-negative integer greater than the start integer.
    :return: a string
    """
    temp_list = s[:start] + s[stop:]
    return temp_list
result_remove_interval = remove_interval('Rajaram',1,5)
print('The result for Rajaram : ',result_remove_interval)

def kmer_list(s, k):
    """
    Generates all kmers of size k for a string s and store them in a list
    :param s: any string
    :param k: any integer greater than zero
    :return: a list of strings
    """
    kmer = []
    n = len(s)
    for x in range(0, n-k+1):
        kmer.append(s[x:x+k])
    return kmer
result_kmer_list = kmer_list('rajaram',3)
print('result of kmer_list',result_kmer_list)
def kmer_set(s, k):
    """
    Generates all kmers of size k for a string s and store them in a set
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    kmer =  set([])
    n = len(s)
    for x in range(0, n - k + 1):
        kmer.add(s[x:x + k])
    return kmer
result_kmer_set = kmer_list('rajaram',3)
print('result of kmer_set',result_kmer_set)
def kmer_dict(s, k):
    """
    Generates all kmers of size k for a string s and store them in a dictionary with the
    kmer(string) as the key and the number of occurances of the kmer as the value(int).
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    kmer = {}
    n = len(s)
    for x in range(0, n - k + 1):
        if s[x:x+k] in kmer:
            kmer[s[x:x + k]] += 1
        else:
            kmer[s[x:x+k]] = 1
    return kmer
result_kmer_dict = kmer_dict('rajaram',2)
print(result_kmer_dict)

# Reading Files
def head(file_name):
    """
    Prints the FIRST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    #from itertools import islice
    with open('../test_files/' + file_name, 'r') as infile:
        #print(list(islice(infile, 10)))
        list = infile.readlines()
    print('list of first 10 lines',list[:10])

head('test.fasta')
def tail(file_name):
    """
    Prints the LAST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    with open('../test_files/' + file_name, 'r') as infile:
        #print(list(islice(infile, 10)))
        list = infile.readlines()
    print('list of last 10 lines',list[len(list)-10:len(list)])
tail('test.fasta')

def print_even(file_name):
    """
    Prints the even numbered lines of a file
    :param file_name: a string
    :return: None
    """
    with open('../test_files/' + file_name, 'r') as infile:
        #print(list(islice(infile, 10)))
        i = 1
        for x in infile.readlines():
            if i%2 == 0:
                print(x)
            i+=1
#print_even('test.fasta')
def csv_list(file_name):
    """
    Read in a CSV file to a 2D array (In python it is a list of lists)
    :param file_name: a string
    :return: a list of lists
    """
    listoflist = []
    with open('../test_files/' + file_name, 'r') as infile:
        for x in infile.readlines():
            listoflist.append(x.split(','))
    return listoflist
result_csv_list = csv_list('test_csv.fasta')
print(result_csv_list)

def get_csv_column(file_name, column):
    """
    Reads in a CSV file and returns a list of values belonging to the column specified
    :param file_name: a string
    :param column: a positive integer
    :return: a list
    """
    list = []
    with open('../test_files/' + file_name, 'r') as infile:
        for x in infile.readlines():
            list.append(x.split(',')[column - 1])
    return list
print(get_csv_column('test_csv.fasta', 3))


def fasta_seqs(file_name):
    """
    Reads in a FASTA file and returns a list of only the sequences
    :param file_name: a string
    :return: a list of strings
    """
    list = []
    with open('../test_files/' + file_name, 'r') as infile:
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            try:
                x = seq.split('\n', 1)
                # header = x[0]
                list.append(x[1].replace('\n', ''))
            except:
                pass
    return list
result_fasta_seqs = fasta_seqs('proper_fasta.fasta')
print(result_fasta_seqs)

def fasta_headers(file_name):
    """
    Reads in a FASTA file and returns a list of only the headers (Lines that start with ">")
    :param file_name: a string
    :return: a list of strings
    """
    list = []
    with open('../test_files/' + file_name, 'r') as infile:
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            try:
                x = seq.split('\n', 1)
                if x[0] != '':
                    list.append(x[0])
            except:
                pass
    return list
result_fasta_headers = fasta_headers('proper_fasta.fasta')
print(result_fasta_headers)

def fasta_dict(file_name):
    """
    Reads in a FASTA file and returns a dictionary of the format {header: sequence, ...}, where
    the sequence headers are keys and the sequence is the value
    :param file_name: a string
    :return: a dictionary
    """
    dict = {}
    with open('../test_files/' + file_name, 'r') as infile:
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            try:
                x = seq.split('\n', 1)
                dict[x[0]] =  x[1].replace('\n', '')
            except:
                pass
    return dict
result_fasta_dict = fasta_dict('proper_fasta.fasta')
print(result_fasta_dict)

def fastq_to_fasta(file_name, new_name=None):
    """
    Reads in a FASTQ file and writes it to a new FASTA file. This definition should also
    keep the same file name and change the extension to from .fastq to .fasta if new_name is not specified.
    EX: fastq_to_fasta('ecoli.fastq') should write to a new file called ecoli.fasta
    :param file_name: a string
    :param new_name: a string
    :return: None
    """
    if(file_name.endswith('.fastq')):
        with open('../test_files/' + file_name, 'r') as infile:
            text = infile.read()
            if new_name == None:
                f = open('../test_files/'+file_name.split('.')[0]+'.fasta','w+')
                print('New file created : '+file_name.split('.')[0]+'.fasta')
            else:
                f = open('../test_files/' + new_name + '.fasta', 'w+')
                print('New file created : ' + new_name + '.fasta')
            f.write(text)
            f.close()
    return
fastq_to_fasta('proper_fastq.fastq','blah')
# Transcription and Translation
def reverse_complement(dna):
    """
    Returns the strand of DNA that is the reverse complement of the sequence given
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    str = ''
    dict = {'C': 'G', 'G': 'C', 'A': 'T', 'T': 'A'}
    for char in dna:
        if char == 'C' or char == 'G' or char == 'T' or char == 'A':
            str = str + dict[char]
        else :
            str = 'invalid character entered, please check the input'
            break
    return str[::-1]
result_reverse_complement = reverse_complement('ACTG')
print(result_reverse_complement)

def transcribe(dna):
    """
    Transcribes a string of DNA into RNA
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, U, A, and G
    """
    str = ''
    dict = {'C': 'C', 'G': 'G', 'A': 'A', 'T': 'U'}
    for char in dna:
        if char == 'C' or char == 'G' or char == 'T' or char == 'A':
            str = str + dict[char]
        else :
            str = 'invalid character entered, please check the input'
            break
    return str
result_transcribe = transcribe('ACTG')
print(result_transcribe)

def translate(rna):
    """
    Translates the strand of RNA given into its amino acid composition.
    DO NOT INCLUDE * IN YOUR RETURN STRING
    :param rna: a string containing only the characters C, U, A, and G
    :return: a string containing only the characters G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    """
    RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
           "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
           "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
           "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
           "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
           "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
           "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
           "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
           "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
           "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
           "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
           "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
           "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
           "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
           "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
           "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
    str = ''
    list = [rna[i:i+3] for i in range(0,len(rna),3)]
    for x in list:
        if RNA_CODON_TABLE[x] != '*':
            str = str + RNA_CODON_TABLE[x]
    return str
result_translate = translate('UUUUUCUUAGGAUGAGAGUAA')
print(result_translate)

def reading_frames(dna):
    """
    Generates a list of all 6 possible reading frames for a given strand of DNA
    For the non-biologists: https://en.wikipedia.org/wiki/Open_reading_frame
    :param dna: a string containing only the characters C, T, A, and G
    :return: a list of 6 strings containing only C, T, A, and G
    """
    list = []
    list.append(dna)
    list.append(dna[::-1])
    list.append(dna[1:len(dna) - 2])
    list.append(dna[1:len(dna) - 2][::-1])
    list.append(dna[2:len(dna) - 1])
    list.append(dna[2:len(dna) - 1][::-1])
    return list
result_reading_frames = reading_frames('GGCAGATTCTAA')
print(result_reading_frames)