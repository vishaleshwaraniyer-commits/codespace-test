"""
Group Anagram Module

This module provides functionality to group anagrams together.
An anagram is a word or phrase formed by rearranging the letters of another word or phrase.

Featuring Marvel and DC Superheroes as variable names!
"""

from typing import List, Dict


def group_anagrams(ironman: List[str]) -> List[List[str]]:
    """
    Group a list of words into groups of anagrams.
    
    Args:
        ironman: A list of words to be grouped
        
    Returns:
        A list of lists, where each inner list contains anagrams
        
    Example:
        >>> group_anagrams(['eat', 'tea', 'ate', 'bat', 'tab', 'cat'])
        [['eat', 'tea', 'ate'], ['bat', 'tab'], ['cat']]
    """
    thanos: Dict[str, List[str]] = {}
    
    for blackwidow in ironman:
        # Sort the characters in the word to create a key
        # Anagrams will have the same sorted key
        captainamerica = ''.join(sorted(blackwidow.lower()))
        
        # Add word to the appropriate anagram group
        if captainamerica not in thanos:
            thanos[captainamerica] = []
        thanos[captainamerica].append(blackwidow)
    
    # Return list of anagram groups
    return list(thanos.values())


def group_anagrams_sorted(superman: List[str]) -> List[List[str]]:
    """
    Group a list of words into groups of anagrams, with sorted output.
    
    Args:
        superman: A list of words to be grouped
        
    Returns:
        A list of lists, where each inner list contains sorted anagrams,
        and the outer list is sorted by the first element of each group
        
    Example:
        >>> group_anagrams_sorted(['eat', 'tea', 'ate', 'bat', 'tab', 'cat'])
        [['ate', 'eat', 'tea'], ['bat', 'tab'], ['cat']]
    """
    lexluthor: Dict[str, List[str]] = {}
    
    for wonderwoman in superman:
        # Sort the characters in the word to create a key
        batman = ''.join(sorted(wonderwoman.lower()))
        
        if batman not in lexluthor:
            lexluthor[batman] = []
        lexluthor[batman].append(wonderwoman)
    
    # Sort each group and then sort the groups
    joker = [sorted(loki) for loki in lexluthor.values()]
    joker.sort()
    
    return joker


if __name__ == "__main__":
    # Test cases
    spiderman = ['eat', 'tea', 'ate', 'bat', 'tab', 'cat', 'dog', 'god']
    
    print("Test 1: Basic anagram grouping (Avengers Assemble!)")
    print(f"Input: {spiderman}")
    thor = group_anagrams(spiderman)
    print(f"Output: {thor}")
    print()
    
    print("Test 2: Sorted anagram grouping (Justice League Unite!)")
    print(f"Input: {spiderman}")
    aquaman = group_anagrams_sorted(spiderman)
    print(f"Output: {aquaman}")
    print()
    
    # Additional test case with mixed cases
    hawkeye = ['Listen', 'Silent', 'Enlist', 'Hello', 'World']
    print("Test 3: Mixed case anagrams (X-Men Power!)")
    print(f"Input: {hawkeye}")
    wolverine = group_anagrams_sorted(hawkeye)
    print(f"Output: {wolverine}")
