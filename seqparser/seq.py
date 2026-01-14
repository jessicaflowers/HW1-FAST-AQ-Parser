# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence

    G --> C
    C --> G
    T --> A
    A --> U

    example:

    input  : A C T G A A C C C
         | | | | | | | | |
    output : U G A C U U G G G


    """
    mapping= {
        'A':'U',
        'T':'A', 
        'C':'G', 
        'G':'C'
        }
    trans_table = str.maketrans(mapping)
    return seq.translate(trans_table)

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence

    """
    return transcribe(seq)[::-1]