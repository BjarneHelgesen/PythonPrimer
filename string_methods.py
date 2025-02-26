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