word = str(input("saisissez votre texte : "))

def inverse_words(modality):
    len_word = len(modality)
    inverse = ""

    for i in range(len_word):
        inverse = inverse + modality[len_word-i-1]

    print(inverse, len(inverse))
    
print(inverse_words(word))