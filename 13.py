def sort(str):
    words = str.split()
    print(words)
    b=words.sort()
    print(b)
    return (b)
a=input('enter words separated by comma:'.split(','))
print(sort(a))