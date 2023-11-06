# https://www.codingninjas.com/studio/problems/check-if-the-string-is-a-palindrome_1062633

import re
check = input()

def palindrome(s):
    text = re.sub(r"[^A-Za-z0-9]","",s)
    s = text.lower().replace(' ','')
    return s == s[::-1]

print(palindrome(check))