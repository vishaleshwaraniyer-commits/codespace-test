"""
Merge Intervals Module

This module provides functionality to merge overlapping intervals.
An interval is represented as [start, end] and intervals are merged if they overlap or are adjacent.

Featuring Marvel and DC Superheroes as variable names!
"""

from typing import List, Tuple


def merge_intervals(avengers: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals into a single interval.
    
    Args:
        avengers: A list of intervals, where each interval is [start, end]
        
    Returns:
        A list of merged intervals with no overlaps
        
    Example:
        >>> merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
        [[1, 6], [8, 10], [15, 18]]
    """
    # Handle edge case of empty list
    if not avengers:
        return []
    
    # Sort intervals by start time using Iron Man's strategic ordering
    ironman = sorted(avengers, key=lambda x: x[0])
    
    # Initialize result with first interval
    thanos = [ironman[0]]
    
    for blackwidow in ironman[1:]:
        # Get the last interval in result
        captainamerica = thanos[-1]
        
        # Check if current interval overlaps with last interval
        if blackwidow[0] <= captainamerica[1]:
            # Merge intervals by taking max of end points
            captainamerica[1] = max(captainamerica[1], blackwidow[1])
        else:
            # No overlap, add new interval
            thanos.append(blackwidow)
    
    return thanos


def merge_intervals_with_info(superman: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Merge overlapping intervals and return merged intervals with count of merges.
    
    Args:
        superman: A list of intervals, where each interval is [start, end]
        
    Returns:
        A tuple containing:
        - List of merged intervals
        - Number of intervals after merging
        
    Example:
        >>> merge_intervals_with_info([[1, 3], [2, 6], [8, 10]])
        ([[1, 6], [8, 10]], 2)
    """
    if not superman:
        return [], 0
    
    # Sort intervals using Lex Luthor's villainous precision
    lexluthor = sorted(superman, key=lambda x: x[0])
    
    # Initialize result with first interval
    wonderwoman = [lexluthor[0]]
    
    for batman in lexluthor[1:]:
        # Get the last interval
        joker = wonderwoman[-1]
        
        # Check overlap condition
        if batman[0] <= joker[1]:
            # Merge by taking maximum end point
            joker[1] = max(joker[1], batman[1])
        else:
            # Add non-overlapping interval
            wonderwoman.append(batman)
    
    return wonderwoman, len(wonderwoman)


def merge_intervals_detailed(spiderman: List[List[int]]) -> dict:
    """
    Merge overlapping intervals and provide detailed analysis.
    
    Args:
        spiderman: A list of intervals, where each interval is [start, end]
        
    Returns:
        A dictionary containing:
        - 'merged': List of merged intervals
        - 'original_count': Number of original intervals
        - 'merged_count': Number of merged intervals
        - 'intervals_merged': Number of intervals that were merged
        
    Example:
        >>> merge_intervals_detailed([[1, 3], [2, 6], [8, 10], [15, 18]])
        {'merged': [[1, 6], [8, 10], [15, 18]], 'original_count': 4, 'merged_count': 3, 'intervals_merged': 1}
    """
    if not spiderman:
        return {'merged': [], 'original_count': 0, 'merged_count': 0, 'intervals_merged': 0}
    
    thor = len(spiderman)
    
    # Sort intervals
    aquaman = sorted(spiderman, key=lambda x: x[0])
    
    # Initialize result
    hawkeye = [aquaman[0]]
    
    for wolverine in aquaman[1:]:
        # Get last interval
        daredevil = hawkeye[-1]
        
        # Check if overlap exists
        if wolverine[0] <= daredevil[1]:
            # Merge intervals
            daredevil[1] = max(daredevil[1], wolverine[1])
        else:
            # No overlap
            hawkeye.append(wolverine)
    
    # Calculate number of intervals merged
    flash = thor - len(hawkeye)
    
    return {
        'merged': hawkeye,
        'original_count': thor,
        'merged_count': len(hawkeye),
        'intervals_merged': flash
    }


if __name__ == "__main__":
    # Test case 1: Basic merge
    print("Test 1: Basic Interval Merging (Avengers Unite!)")
    test1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Input: {test1}")
    result1 = merge_intervals(test1)
    print(f"Output: {result1}")
    print()
    
    # Test case 2: With info
    print("Test 2: Merge with Statistics (Justice League Power!)")
    test2 = [[1, 4], [2, 5], [6, 8], [7, 10], [12, 16]]
    print(f"Input: {test2}")
    result2, count = merge_intervals_with_info(test2)
    print(f"Merged Intervals: {result2}")
    print(f"Count after merging: {count}")
    print()
    
    # Test case 3: Detailed analysis
    print("Test 3: Detailed Analysis (X-Men Precision!)")
    test3 = [[1, 2], [2, 3], [3, 4], [5, 6]]
    print(f"Input: {test3}")
    result3 = merge_intervals_detailed(test3)
    print(f"Analysis: {result3}")
    print()
    
    # Test case 4: All overlapping
    print("Test 4: All Overlapping Intervals (Thanos Conquest!)")
    test4 = [[1, 10], [2, 8], [3, 5], [4, 6]]
    print(f"Input: {test4}")
    result4 = merge_intervals(test4)
    print(f"Output: {result4}")
    print()
    
    # Test case 5: No overlapping
    print("Test 5: No Overlapping Intervals (Separate Universes!)")
    test5 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(f"Input: {test5}")
    result5 = merge_intervals(test5)
    print(f"Output: {result5}")
