#Group: Alejandro, Michael, and Sydney
#Oct 30 2024
#BINF6250

#no imports

def validate_DNA_characters(dna_string):
    if not isinstance(dna_string, str):
        raise ValueError("Input must be a string")
    # Check for valid characters
    valid_characters = {'A', 'T', 'C', 'G', '-'}
    for letter in dna_string:
        if letter not in valid_characters:
            raise ValueError("Invalid characters in input string list. Valid chars are ATCG-")
    #valid
    return True


def validate_list_input(dna_list):
    #check if dna_list is a list and/or empty 
    if not isinstance(dna_list, list) or len(dna_list) == 0:
        raise ValueError("dna_list must be a non-empty list")
    
    #check if dna_list contains only "ATCG-" character, call validate_DNA_characters
    for dna in dna_list:
        validate_DNA_characters(dna)
    return True


def validate_input(dna_list, k):
    """Validate the input DNA sequences and k value."""
    # TODO: Implement input validation
    # Raise appropriate exceptions for invalid inputs
    validate_list_input(dna_list)
    if not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer")
    return True



def hamming_distance(s1, s2):
    """Calculate the Hamming distance between two strings."""
    # TODO: Implement the Hamming distance calculation

    #----------CHECKS----------
    # Check validity of input strings
    # Size should be equal
    if len(s1) != len(s2):
        raise ValueError("Strings are of different lengths")
    # Check characters
    validate_DNA_characters(s1+s2)

    # -------- \CHECKS --------- 

    
    # Counter for differences
    ham_counter = 0
    # Loop through both strings of same len
    for i in range(len(s1)):
        # if different, increment counter
        if s1[i] != s2[i]:
            ham_counter += 1
        # else don't
        else:
            continue
    #return counter
    return ham_counter


def total_distance(pattern, dna_list):
    """Calculate the total distance between a pattern and a list of DNA sequences."""
    # TODO: Implement the total distance calculation

    #----------CHECKS---------
    # check if dna_list is a list and/or empty
    validate_list_input(dna_list)

    # check if pattern is a string of ATCGs
    if len(pattern) == 0:
        raise ValueError("Pattern is an empty string")

    validate_DNA_characters(pattern)

    # -------- \CHECKS --------- 


    # Total disatnce counter
    total_dist = 0
    # Iterate through dna_list and call hamming_distance
    for dna in dna_list:
        hamm_distance = hamming_distance(pattern, dna)
        total_dist += hamm_distance
    # Return total distance
    return total_dist


def branch_and_bound(prefix, k, dna_list, best_distance):
    """
    Recursive branch and bound algorithm for median string search. The algo starts with base case of k being  
    
    Args:
        prefix: Current prefix of the pattern being built.
        k: Remaining length to complete the pattern.
        dna_list: List of DNA sequences.
        best_distance: Current best distance found.
    
    Returns:
        A tuple containing the best pattern found and its distance.
    """
    # TODO: Implement the branch and bound algorithm
    # Branch and bound info from Chapter 4 section 6 https://www.bioinformaticsalgorithms.org/bioinformatics-chapter-4

    #------------CHECKS----------------
    #other checks in median_string()
    if not isinstance(best_distance, list) or len(best_distance) != 2:
        raise ValueError("best_distance must be a list of length 2") 
    # -------- \CHECKS --------- 


    # Base case: when k is 0
    # Calculate total distance by calling helper fx
    if k == 0:
        t_distance = total_distance(prefix, dna_list)
        # Compare against provided best distance
        if t_distance <= best_distance[0]:
            # if t_distance is smaller, it is the best distance
            best_distance[0] = t_distance
            best_distance[1] = prefix
            # Return best distance for next call
            return best_distance
        else:
            return best_distance
    
    # Recursive case: when there's still remaining length to complete the pattern, aka k > 0
    # Check all possible DNA bases
    nucs = ['A', 'T', 'C', 'G']
    for nuc in nucs:
        # extend prefix with current nucleotide
        new_prefix = prefix + nuc
        # Call total_distance with new prefix
        t_distance = total_distance(new_prefix, dna_list)

        # If the t_distance is <= to the current best_distance, recursively call branch_and_bound with new prefix and length of k - 1
        if t_distance <= best_distance[0]:
            best_distance = branch_and_bound(new_prefix, k - 1, dna_list, best_distance)
        
    return best_distance


def median_string(dna_list, k):
    """
    Find the median string of length k for a list of DNA sequences using branch and bound.
    
    Args:
        dna_list: List of DNA sequences.
        k: Length of the median string to find.
    
    Returns:
        A tuple containing the median string of length k and its total distance.
    """
    # TODO: Implement the median string search using the branch_and_bound function
    # -------- CHECKS --------- 
    # DNA_list validation
    validate_input(dna_list, k)
    
    # -------- \CHECKS --------- 


    # Before calling branch_and_bound, initialize best_distance and prefix
    # Initiating a lis t length 2 to pass the test. Empty string leads to issues when median is not found.
    best_distance = [float("inf"), None]
    prefix = ""

    # call branch_and_bound
    best_median_string = branch_and_bound(prefix, k, dna_list, best_distance)

    # make the tuple of best pattern and distance and return
    tuple_return = (best_median_string[1], best_median_string[0])
    return tuple_return

