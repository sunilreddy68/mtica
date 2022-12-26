def extract_vowel(s):
    temp_vowel=''
    for i in s:
        if i in 'AEIOBaeiou':
            temp_vowel+=i
            #print('temp_vowel:',temp_vowel)
    return temp_vowel
str1=input()
a=extract_vowel(str1)
print('vowels:',a)
