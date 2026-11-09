def reverse_string(word):
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
        print(i, word[i], reversed_word)


def reverse_string_recursion(sentence):
    if len(sentence) <= 1:
        return sentence
    return sentence[-1] + reverse_string_recursion(sentence[:-1])

if __name__ == "__main__":
    print(reverse_string("GABRIEL"))
    print(reverse_string_recursion("GABRIEL"))
