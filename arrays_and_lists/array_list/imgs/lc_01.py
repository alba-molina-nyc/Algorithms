"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

def duplicate_removal(s):
    s = list(s)
    print(s)
    left = s[0]
    right = s[1]

    for i in s:
        if left != right:
            print(f'{left} != {right}')
            i = s[i +1]
        else:
            print(f'{left} != {right}')
            

    # for i in s:
    #     left = s[0]
    #     right = s[1]
    #     if left != right:
    #         print(f'{left} != {right}')
    #         s[left] = left + 1
    # print(f'{left} == {right}')


        
            

if __name__ == '__main__':
    print(duplicate_removal('abbaca'))