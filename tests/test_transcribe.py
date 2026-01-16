# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Test that the following mapping is true:
    G --> C
    C --> G
    T --> A
    A --> U
    """
    # assert transcribe("GCTA") == "CGAU"
    assert transcribe("ACTGAACCC") == "UGACUUGGG"

def test_reverse_transcribe():
    """
    Test that the input string gets transcribed and then reversed, i.e.:
    GCTA --> CGAU --> UAGC
    """
    # assert reverse_transcribe("GCTA") == "UAGC"
    assert reverse_transcribe("ACTGAACCC") == "GGGUUCAGU"
