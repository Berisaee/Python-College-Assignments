def main():
    word=input("Enter the word: ")

    count_letters={}
    for letter in word:
        if letter in count_letters:
            count_letters[letter]+=1
        else:
            count_letters[letter]=1
    sorted_words = dict(sorted(count_letters.items(), key=lambda x: x[1],reverse=True))

    print(sorted_words)
    
if __name__=="__main__":
    main()