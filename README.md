# LEET_CODE
[![GitHub last commit](https://img.shields.io/github/last-commit/dhyanpatel110/LEET_CODE)](https://github.com/dhyanpatel110/LEET_CODE/commits/master)
[![GitHub repo size](https://img.shields.io/github/repo-size/dhyanpatel110/LEET_CODE)](https://github.com/dhyanpatel110/LEET_CODE/archive/master.zip)


| # | Title | Solution | Difficulty |Basic idea (One line) |
|---| ----- | -------- | ---------- |--------------------- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python](https://github.com/dhyanpatel110/LEET_CODE/blob/master/python/001_Two_Sum.py)|Easy|1. Hash O(n) and O(n) space.<br>2. Sort and search with two points O(n) and O(1) space. |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | [Python](https://github.com/dhyanpatel110/LEET_CODE/blob/master/python/002_Add_Two_Numbers.py)|Medium |Take care of the carry from lower digit. |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/003_Longest_Substring_Without_Repeating_Characters.py)| Medium |1. Check every possible substring O(n^2) <br>2. Remember the character index and current check pos, if character index >= current pos, then there is duplicate |
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/004_Median_of_Two_Sorted_Arrays.py)|	Hard | 1. Merge two sorted lists and compute median, O(m + n) and O(m + n)<br>2. An extension of median of two sorted arrays of equal size problem|
| 5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/005_Longest_Palindromic_Substring.py)|	Medium |[Background knowledge](http://en.wikipedia.org/wiki/Longest_palindromic_substring)<br>1. DP if s[i]==s[j] and P[i+1, j-1] then P[i,j]<br>2. A palindrome can be expanded from its center<br>3. Manacher algorithm|

