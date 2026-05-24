# Défi 1 : Tri
words = input("Entrez des mots séparés par des virgules : ").split(",")
sorted_words = sorted([word for word in words])
print(",".join(sorted_words))

# Défi 2 : Le mot le plus long
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Tests
print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))