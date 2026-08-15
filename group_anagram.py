"""
Group Anagram Module

This module provides functionality to group anagrams together.
An anagram is a word or phrase formed by rearranging the letters of another word or phrase.
"""

from typing import List, Dict


def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Group a list of words into groups of anagrams.
    
    Args:
        words: A list of words to be grouped
        
    Returns:
        A list of lists, where each inner list contains anagrams
        
    Example:
        >>> group_anagrams(['eat', 'tea', 'ate', 'bat', 'tab', 'cat'])
        [['eat', 'tea', 'ate'], ['bat', 'tab'], ['cat']]
    """
    anagram_dict: Dict[str, List[str]] = {}
    
    for word in words:
        # Sort the characters in the word to create a key
        # Anagrams will have the same sorted key
        sorted_word = ''.join(sorted(word.lower()))
        
        # Add word to the appropriate anagram group
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)
    
    # Return list of anagram groups
    return list(anagram_dict.values())


def group_anagrams_sorted(words: List[str]) -> List[List[str]]:
    """
    Group a list of words into groups of anagrams, with sorted output.
    
    Args:
        words: A list of words to be grouped
        
    Returns:
        A list of lists, where each inner list contains sorted anagrams,
        and the outer list is sorted by the first element of each group
        
    Example:
        >>> group_anagrams_sorted(['eat', 'tea', 'ate', 'bat', 'tab', 'cat'])
        [['ate', 'eat', 'tea'], ['bat', 'tab'], ['cat']]
    """
    anagram_dict: Dict[str, List[str]] = {}
    
    for word in words:
        # Sort the characters in the word to create a key
        sorted_word = ''.join(sorted(word.lower()))
        
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)
    
    # Sort each group and then sort the groups
    result = [sorted(group) for group in anagram_dict.values()]
    result.sort()
    
    return result


if __name__ == "__main__":
    # Test cases
    test_words = ['eat', 'tea', 'ate', 'bat', 'tab', 'cat', 'dog', 'god']
    
    print("Test 1: Basic anagram grouping")
    print(f"Input: {test_words}")
    result1 = group_anagrams(test_words)
    print(f"Output: {result1}")
    print()
    
    print("Test 2: Sorted anagram grouping")
    print(f"Input: {test_words}")
    result2 = group_anagrams_sorted(test_words)
    print(f"Output: {result2}")
    print()
    
    # Additional test case with mixed cases
    test_words_mixed = ['Listen', 'Silent', 'Enlist', 'Hello', 'World']
    print("Test 3: Mixed case anagrams")
    print(f"Input: {test_words_mixed}")
    result3 = group_anagrams_sorted(test_words_mixed)
    print(f"Output: {result3}")
