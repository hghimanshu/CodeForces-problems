def replaceWords(dictionary, sentence):
    sentence = sentence.split(' ')
    for i in range(len(sentence)):
        curr_prefix = None
        for prefix in dictionary:
            if prefix in sentence[i]:
                if not curr_prefix:
                    curr_prefix = prefix
                else:
                    if len(prefix)<len(curr_prefix):
                        curr_prefix =prefix
        if curr_prefix:
            sentence[i] = curr_prefix
    
    return " ".join(sentence)

if __name__ == "__main__":
    dictionary = ["a","b","c"]
    sentence = "aadsfasf absbs bbab cadsfafs"
    print(replaceWords(dictionary,sentence))


