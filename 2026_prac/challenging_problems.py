"""
5 Challenging Python Coding Problems
=====================================
Fill in each function below. Run this file to test your solutions
against the provided test cases (uncomment the test calls in main()
as you go).
"""

from typing import List
from statistics import median
# ---------------------------------------------------------------------------
# 1. MEDIAN OF TWO SORTED ARRAYS
# ---------------------------------------------------------------------------
# Given two sorted arrays nums1 and nums2, return the median of the two
# arrays combined. Target time complexity: O(log(min(m, n))).
#
# Example:
#   nums1 = [1, 3], nums2 = [2]        -> 2.0
#   nums1 = [1, 2], nums2 = [3, 4]     -> 2.5

def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    # TODO: implement using binary search on the smaller array
    nums1.extend(nums2)
    return median(nums1)


# ---------------------------------------------------------------------------
# 2. N-QUEENS
# ---------------------------------------------------------------------------
# Place n queens on an n x n chessboard so that no two queens attack each
# other. Return all distinct solutions, where each solution is a list of
# strings representing the board ('Q' for queen, '.' for empty).
#
# Example: n = 4 -> 2 solutions

def solve_n_queens(n: int) -> List[List[str]]:
    # TODO: implement using backtracking
    # Initialize containers to track under-attack paths
    cols = set()
    pos_diag = set()  # Tracks (r + c)
    neg_diag = set()  # Tracks (r - c)

    solutions = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r: int):
        # Base case: All queens are successfully placed
        if r == n:
            copy = ["".join(row) for row in board]
            solutions.append(copy)
            return

        for c in range(n):
            # Check if the current position is under attack
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            # Place the queen and flag the paths
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"

            # Move to the next row
            backtrack(r + 1)

            # Backtrack: Remove the queen and clear flags
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."

    # Start backtracking from the first row (index 0)
    backtrack(0)
    return solutions



# ---------------------------------------------------------------------------
# 3. LONGEST INCREASING PATH IN A MATRIX
# ---------------------------------------------------------------------------
# Given an m x n integers matrix, return the length of the longest
# strictly increasing path. You may move up, down, left, or right (no
# diagonals, no wraparound).
#
# Example:
#   matrix = [[9,9,4],
#             [6,6,8],
#             [2,1,1]]
#   -> 4  (path: 1 -> 2 -> 6 -> 9)

def longest_increasing_path(matrix: List[List[int]]) -> int:
    # TODO: implement using DFS + memoization
    pass


# ---------------------------------------------------------------------------
# 4. WORD LADDER
# ---------------------------------------------------------------------------
# Given beginWord, endWord, and a wordList, return the length of the
# shortest transformation sequence from beginWord to endWord such that
# only one letter is changed at a time, and each transformed word exists
# in wordList. Return 0 if no such sequence exists.
#
# Example:
#   beginWord = "hit", endWord = "cog"
#   wordList = ["hot","dot","dog","lot","log","cog"]
#   -> 5  ("hit" -> "hot" -> "dot" -> "dog" -> "cog")

def ladder_length(beginWord: str, endWord: str, wordList: List[str]) -> int:
    # TODO: implement using BFS
    pass


# ---------------------------------------------------------------------------
# 5. REGULAR EXPRESSION MATCHING
# ---------------------------------------------------------------------------
# Implement regular expression matching supporting '.' and '*' (no other
# regex features, and no use of the `re` module):
#   '.' matches any single character.
#   '*' matches zero or more of the preceding element.
# The match should cover the ENTIRE input string.
#
# Example:
#   is_match("aa", "a")     -> False
#   is_match("aa", "a*")    -> True
#   is_match("ab", ".*")    -> True
#   is_match("mississippi", "mis*is*p*.") -> False

def is_match(s: str, p: str) -> bool:
    # TODO: implement using dynamic programming
    pass


# ---------------------------------------------------------------------------
# TEST CASES — uncomment as you implement each function
# ---------------------------------------------------------------------------

def main():
    # --- 1. Median of Two Sorted Arrays ---
    print(find_median_sorted_arrays([1, 3], [2]))          # 2.0
    print(find_median_sorted_arrays([1, 2], [3, 4]))       # 2.5

    # --- 2. N-Queens ---
    solutions = solve_n_queens(4)
    print(len(solutions))                                   # 2
    for sol in solutions:
        print('\n'.join(sol), '\n')

    # --- 3. Longest Increasing Path ---
    # matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    # print(longest_increasing_path(matrix))                  # 4

    # --- 4. Word Ladder ---
    # print(ladder_length("hit", "cog",
    #                      ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5

    # --- 5. Regular Expression Matching ---
    # print(is_match("aa", "a"))                              # False
    # print(is_match("aa", "a*"))                              # True
    # print(is_match("ab", ".*"))                              # True
    # print(is_match("mississippi", "mis*is*p*."))             # False

    pass


if __name__ == "__main__":
    main()
