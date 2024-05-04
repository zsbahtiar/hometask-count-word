
import xml.etree.ElementTree as ET 
import re

# filename: string
# return string
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return None

def print_stats(total_article,total_word, word_dict):
    words = {k: v for k, v in sorted(word_dict.items(), key=lambda item: item[1], reverse=True)}
    top_10 = list(words.items())[:10]
    freq_lt_3 = {k: v for k, v in words.items() if v < 3}
   
    print(f"\nJUMLAH BERITA DALAM KORPUS\n{total_article}\n")

    print("\nDAFTAR 10 KATA UNIK DENGAN FREKUENSI PALING TINGGI URUT BERDASARKAN FREKUENSI TINGGI")
    for i, (word, freq) in enumerate(top_10):
       print(f"{i+1}. {word} - {freq}")
        
        
    print(f"\nJUMLAH SELURUH KATA\n{total_word}\n")

    print(f"\nBANYAKNYA KATA UNIK DALAM DOKUMEN\n{len(words)}\n")

    print(f"\nJUMLAH KATA YANG FREKUENSINYA KURANG DARI 3\n{len(freq_lt_3)}\n")

    print("\nBANYAKNYA KATA UNIK YANG MENGANDUNG KATA tani")
    print(words.get("tani", 0))

    
def get_stats_word(text):
    tree = ET.fromstring(f"<DOCS>{text}</DOCS>")
    total_article = len(tree.findall("DOC"))
    total_word = 0
    word_dict = {}
    for _ in tree.findall("DOC"):
        for __ in _.findall("TEXT"):
            text = __.text
            cleaned_text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
            words = cleaned_text.split()
            for word in words:
                if len(word) < 3:
                    continue

                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
                total_word += 1
   
    return total_article,total_word, word_dict

def main():
    file = "korpus.txt"
    text = read_file(file)
    if text is None:
        print(f"File {file} not found")
        return
    
    total_article,total_word, word_dict = get_stats_word(text)
    print_stats( total_article,total_word, word_dict)


if __name__ == "__main__":
    main()




   