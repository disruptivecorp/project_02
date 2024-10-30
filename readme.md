Group members: Michael Bambha, Sydney Cole, Alejandro Scaffa
Date: Oct 30, 2024
Class: BINF6250
Project 02

Current file: README.md
Python files: gibbs.py, debruign.py, median_string.py


--------------- gibbs.py planning/pseudocode:

1. Choose 1 sequence to randomly be removed (call it sequence 'r')
	- Start of the system is a starting index for each sequence
2. Remove the sequence (DNAi)
3. Build PWM from all other sequences
4. Score each k-mer in the removed sequence
 - For each k-mer in DNA_i, calculate a score using the PWM.
 - Convert these scores into a probability distribution (higher-scoring k-mers have higher probability).
5. Update starting index for sequence 'r' based on a weighted random (distribution generated from score)
6. Repeat for 'x' iterations (10,000 in our case) or until PWM(x - 1) ~= PWN(x)


------------- debruign.py planning/pseudocode
DeBruign Algo. See also pictures dgb.png and PWM.png.

Build a De Bruijn graph from a string:
        
Updates graph attribute to add all valid edges from the string:
    define substring length k and input string
    For each k-length substring of input:
        split k mer into left and right k-1 mer
        add k-1 mers as nodes with a directed edge from left k-1 mer to right k-1 mer
    
    1. Extract k-mers from the input sequence.
    2. Use the (k-1)-mer prefixes and suffixes to define nodes.
    3. Create edges between nodes based on overlapping (k-1)-mers.
    4. Track the connections between nodes by using their row/col IDs.
    
    Node class uses (row, col) as ID; we can map each k-1-mer to a unique row/col pair
    (using indexes or hashing). Each edge will connect nodes whose k-1-mers overlap.




------------- median_string.py planning/pseudocode
Median String Algo

hamming_distance(s1, s2)
1. validate arg lengths being equal
2. iterate through strings
    - if different, increment counter
3. return hamming distance

total_distance(pattern, dna_list)
1. validate args
2. create distance counter
3. iterate through bases/strings in dna_list
    - call hamming distance 
    - add to total distance 
4. return total distance 


branch_and_bound(prefix, k, dna_list, best_distance)
1. base case k = 0 
    - call total_distance
    - if total_distance is smaller than best distance, update it
    - return best_distance
2. recursive case k > 0 
    - for nucs ATCG
    - new_prefix = nuc+prefix
    - if (totaldistance(new_prefix)) <= best_distance from dna_list
        - then call recurssion with new_prefix and k-1
3. return best_distance


median_string(dna_list, k)
1. validate inputs with validate_input(dna_list, k) (basic ATCG, len, k>0 checks)
2. Initialize best_distance (which contains total distance)
3. Call branch_and_bound(prefix, k, dna_list, best_distance) on an empty prefix
4. return the resulting total_distance and prefix within a tuple. 

Reflection:
This project was about solving for the median string. The median string here is a DNA sequence motif that minimizes the hamming distance to a set of DNA sequences. This motif finding is a useful tool in bioinformatics for finding the patterns of DNA that bind to protein, patterns of RNA, and with some manipulation protein primary structure motifs, phylogenetic studies, primer design, epigenetic studies, and more. The DNA sequences we are working with can come from experiments like ChIP-seq where a protein that binds to DNA is collected with the DNA piece still attached to it, those DNA bits are sequenced, and using the median string we find the "average" sequence motif that can then be used to create drugs that fit the lock just like the dna fits the protein. This project involved an input of DNA sequences and integer k which is the size of the motif being explored. The ouput is k-mer sized dna string motif. This project approaches this calculation in two ways, through brute force on all possible k-mers and through the branch-and-bound algorithm which is a recursive function that more efficiently looks for the best median string, although both have the same worst-case big O of O(4^k), by selecting a nucleotide at a time it shortens the search space considerably. We were able to implement the three scripts outlined earlier in the readme.md to calculate the median_string. The whole group tended towards the biology side of the background by previous training so it was interesting focusing on the coding side of things on this somewhat longer second project. We all agree that we should focus on using the Github ecosystem more than we did, we ended up meeting multiples times over Teams briging some of that gap and collaborating on the approaches and scripts. The median string algorithm project gives perspective as to how a great algorithm can literally change a large subset of the field of genetics as a whole. 

Gen AI statement: gen AI such as chatGPT was used to ask questions such as "What is the median string problem?", "Explain the problem like I'm 5, in high school, or in college", "What is the big O of brute force vs. branch-and-bound?", "What is the syntax for the import timeit in python3?". Github co-pilot was used for inline corrections when necessary.
