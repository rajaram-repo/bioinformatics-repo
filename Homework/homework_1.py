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
print('fast_complement:::For input ACTG the o/p is :',result_complemet)

def remove_interval(s, start, stop):
    """
    Removes the interval of characters from a string or list inclusively, 0 based
    EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    :param s: a string
    :param start: a non-negative integer
    :param stop: a non-negative integer greater than the start integer.
    :return: a string
    """
    #s[:start] will get the string from start of string to 'start'->value stored in start
    #s[stop:] will get the string from 'stop'->value stored in the stop to end of the string
    temp_list = s[:start] + s[stop+1:]
    return temp_list
result_remove_interval = remove_interval('Rajaram',2,4)
print('result for remove_interval(Rajaram,2,4): ',result_remove_interval)

def kmer_list(s, k):
    """
    Generates all kmers of size k for a string s and store them in a list
    :param s: any string
    :param k: any integer greater than zero
    :return: a list of strings
    """
    kmer = []
    n = len(s)
    # n-k+1 is the available range of values or probablities.
    for x in range(0, n-k+1):
        kmer.append(s[x:x+k])
    return kmer
result_kmer_list = kmer_list('rajaram',3)
print('Result for kmer_list(rajaram,3)',result_kmer_list)
def kmer_set(s, k):
    """
    Generates all kmers of size k for a string s and store them in a set
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    kmer =  set([])
    n = len(s)
    #n-k+1 is the available range of values or probablities.
    for x in range(0, n - k + 1):
        kmer.add(s[x:x + k])
    return kmer
result_kmer_set = kmer_set('rajaram',3)
print('result of kmer_set(rajaram,3)',result_kmer_set)
def kmer_dict(s, k):
    """
    Generates all kmers of size k for a string s and store them in a dictionary with the
    kmer(string) as the key and the number of occurances of the kmer as the value(int).
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    kmer = {}
    #calculating the length as n.
    n = len(s)
    for x in range(0, n - k + 1):
        #checking if the entry alread in the dictionary kmer
        if s[x:x+k] in kmer:
            #if the entry is available then increament 1
            kmer[s[x:x + k]] += 1
        else:
            #else initialize the kmer value as 1
            kmer[s[x:x+k]] = 1
    return kmer
result_kmer_dict = kmer_dict('rajaram',2)
print('Result for kmer_dict(rajaram,2)',result_kmer_dict)

# Reading Files
def head(file_name):
    """
    Prints the FIRST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    #from itertools import islice
    with open('../test_files/' + file_name, 'r') as infile:
        list = infile.readlines()
    #printing the 1st 10 lines
    print('list of first 10 lines',list[:10])

head('test.fasta')
def tail(file_name):
    """
    Prints the LAST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    with open('../test_files/' + file_name, 'r') as infile:
        list = infile.readlines()
    #calculating the last 10 lines using len(list)-10:len(list)
    print('list of last 10 lines',list[len(list)-10:len(list)])
tail('test.fasta')

def print_even(file_name):
    """
    Prints the even numbered lines of a file
    :param file_name: a string
    :return: None
    """
    with open('../test_files/' + file_name, 'r') as infile:
        #initialising 1 to 1 so that it evaluate from line 1
        i = 1
        for x in infile.readlines():
            #performing operation to find the even number entry
            if i%2 == 0:
                #actual printing of lines
                print(x)
            #increamenting
            i+=1
print_even('test.fasta')
def csv_list(file_name):
    """
    Read in a CSV file to a 2D array (In python it is a list of lists)
    :param file_name: a string
    :return: a list of lists
    """
    listoflist = []
    with open('../test_files/' + file_name, 'r') as infile:
        for x in infile.readlines():
            x = x.replace('\n','')
            #splitting based on ',' that are encountered in csv files.
            #splitted vale will be a list, that inturn is stored into another main list
            #making it list of lists or 2D array.
            listoflist.append(x.split(','))
    return listoflist
result_csv_list = csv_list('test_csv.csv')
print('Result for csv_list(test_csv.csv)',result_csv_list)

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
            x = x.replace('\n', '')
            # splitting based on ',' that are encountered in csv files.
            #column-1 because the range start from 0 , so if user enters 1st column then its 0th column we need to fetch
            list.append(x.split(',')[column - 1])
    return list
print('Result for get_csv_column(test_csv.csv, 3)',get_csv_column('test_csv.csv', 3))


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
                # sequence will be stored in x[1], and i am removing nextline '\n' characters that comes with it.
                list.append(x[1].replace('\n', ''))
            except:
                pass
    return list
result_fasta_seqs = fasta_seqs('proper_fasta.fasta')
print('Result for fasta_seqs(proper_fasta.fasta)',result_fasta_seqs)

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
                    #x[0] contains only headers
                    list.append(x[0])
            except:
                pass
    return list
result_fasta_headers = fasta_headers('proper_fasta.fasta')
print('Result for fasta_headers(proper_fasta.fasta)',result_fasta_headers)

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
                #Entering values into the dictionary using dict[key]=value
                dict[x[0]] =  x[1].replace('\n', '')
            except:
                pass
    return dict
result_fasta_dict = fasta_dict('proper_fasta.fasta')
print('Result for fasta_dict(proper_fasta.fasta)',result_fasta_dict)

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
print('Result for reverse_complement(ACTG)',result_reverse_complement)

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
            #converting only of the valid string is encountered
            #then the string is converted accordingly
            str = str + dict[char]
        #the case for incalid string, it throws only the error
        else :
            str = 'invalid character entered, please check the input'
            break
    return str
result_transcribe = transcribe('ACTG')
print('Result for transcribe(ACTG):',result_transcribe)

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
        #checks if x is in key of RNA_CODON_TABLE
        if x in RNA_CODON_TABLE:
            #appends only if the value for the  given key is not *
            if RNA_CODON_TABLE[x] != '*':
                str = str + RNA_CODON_TABLE[x]
        #if only one char is extra(meaning apart form the 3 pair characters available in dictionary)
        #checks if the char is in following
        elif len(x) == 1 and x in ['A','G','C','U']:
            str = str + x
        #if the char is of length 2 i.e, 2 words extra
        elif len(x) == 2 and x[0] in ['A','G','C','U'] and x[1] in ['A','G','C','U']:
            #Then appending the char to the actually converted string
            str = str + x[0]
            str = str + x[1]
        #if the char is not in the above characters then it is a unrecognised character.
        else:
            print("Unrecognised character:",x)
    return str
result_translate = translate('UUUUUCUUAGGAUGAGAGUAAUA')
print('Result for translate(UUUUUCUUAGGAUGAGAGUAAUA):',result_translate)

def reading_frames(dna):
    """
    Generates a list of all 6 possible reading frames for a given strand of DNA
    For the non-biologists: https://en.wikipedia.org/wiki/Open_reading_frame
    :param dna: a string containing only the characters C, T, A, and G
    :return: a list of 6 strings containing only C, T, A, and G
    """
    #the 6 types are as follows
    # the actual string and the reverse complement
    list = []
    #this is the actual string
    list.append(dna)
    #this is the reverse complement of the string
    # done reusing the fastcomplement() method that was already available.
    #others are done likewise
    list.append(fast_complement(dna[::-1]))
    list.append(dna[1:len(dna)])
    list.append(fast_complement(dna[1:len(dna)][::-1]))
    list.append(dna[2:len(dna)])
    list.append(fast_complement(dna[2:len(dna)][::-1]))
    return list
result_reading_frames = reading_frames('GGCAGATTCTAA')
print('Result for reading_frames(GGCAGATTCTAA):',result_reading_frames)