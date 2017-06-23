import bioinfo_dicts

def n_neg(seq):
    """Number of negative residues in a protein sequence"""

    # Check for a valid sequence
    for aa in seq:
        if aa not in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid.')

    # This line will magically make everything good
    seq = seq.upper().replace('E', 'ED').replace('D', 'ED')

    # Count E's and D's, since these are the negative residues
    return seq.count('ED')

