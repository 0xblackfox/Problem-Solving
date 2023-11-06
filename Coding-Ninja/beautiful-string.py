#https://www.codingninjas.com/studio/problems/beautiful-string_1115625

def makeBeautiful(str):
    def flip(ch):
        return '1' if ch == '0' else '0'
    
    def get_flip(s, expected):
        flip_count = 0
        for ch in s:
            if ch != expected:
                flip_count += 1
            expected = flip(expected)
        return flip_count
    
    return min(get_flip(str, '0'),
               get_flip(str, '1'))
               

print(makeBeautiful(input()))