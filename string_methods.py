# string and character methods

chr(65) # 'A'
ord('A') # 65

"hello".capitalize() # 'Hello'
"hello".upper() # 'HELLO'
"HELLO".lower() # 'hello'   
" hello ".strip() # 'hello'
"hello".replace('e', 'a') # 'hallo'
"hello".split('e') # ['h', 'llo']
"hello".find('e') # 1

greeting = "hello"
for c in greeting:
    print(c)

print(greeting[1]) # 'e'

# string testing functions
"hello".isalpha() # True
"hello123".isalpha() # False
"123".isdigit() # True
"hello123".isdigit() # False
"hello123".isalnum() # True
"hello".isalnum() # True
"123".isalnum() # True
"123! #".isalnum() # False
"hello".islower() # True
"HELLO".isupper() # True
"hello".startswith("he") # True
"hello".endswith("lo") # True
"hello".isascii() # True
    