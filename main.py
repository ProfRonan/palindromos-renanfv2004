

import re

def is_palindrome(string: str) -> bool:
    
    n = string
    n = n.lower()
    n = n.replace(" ", "")
    n = re.sub(r'[^\w\s]','',n)
    n2 = n[::-1]

    if n == n2:
