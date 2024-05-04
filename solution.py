

# filename: string
# return string
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return None
    
# like get words between brackets
# example: <DOC>HI</DOC> -> HI
# return the number of words and a dictionary with the words and their frequency
def get_words_between_tags(text):
    start = text.find("<")
    while start != -1:
        end = text.find(">", start)
        text = text[:start] + " " + text[end + 1:]
        start = text.find("<")
    cleaned_text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    words = cleaned_text.split()
    word_dict = {}
    word_count = 0
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
        word_count += 1
    return word_count, word_dict

# print the dictionary descending by frequency, top 10
# print the total number of words
# print the total number of unique words
# print the number of words with frequency less than 3
# print the number of words that contain the word "tani"
def print_words(words, total_words):
    # print the dictionary descending by frequency, top 10
    words = {k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)}
    top_10 = list(words.items())[:10]
    freq_lt_3 = {k: v for k, v in words.items() if v < 3}
   
    print("\nDAFTAR 10 KATA UNIK DENGAN FREKUENSI PALING TINGGI URUT BERDASARKAN FREKUENSI TINGGI")
    for i, (word, freq) in enumerate(top_10):
       print(f"{i+1}. {word} - {freq}")
        
        
    print(f"\nJUMLAH SELURUH KATA\n{total_words}\n")

    print(f"\nBANYAKNYA KATA UNIK DALAM DOKUMEN\n{len(words)}\n")

    print(f"\nJUMLAH KATA YANG FREKUENSINYA KURANG DARI 3\n{len(freq_lt_3)}\n")

    print("\nBANYAKNYA KATA UNIK YANG MENGANDUNG KATA tani")
    print(words.get("tani", 0))

    

def main():
    file = "korpus.txt"
    text = read_file(file)
    if text is None:
        print(f"File {file} not found")
        return
    
    word_count, word_dict = get_words_between_tags(text)
    print_words(word_dict, word_count)


if __name__ == "__main__":
    main()
