def reverse_string(str1):
    return str1[::-1]

def flip(sentence):
    lst1 = sentence.split()
    lst2 = [reverse_string(a) for a in lst1]
    new_sentence = " ".join(lst2)
    return new_sentence

# Driver code
test_str = "junyiacademy"
test_sentence = "flipped class room is important"
print(reverse_string(test_str))
print(flip(test_sentence))