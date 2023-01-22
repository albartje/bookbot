def count_chars(file_contents):
    dic = {}
    for char in file_contents:        
        char = char.lower()
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return dic

def count_words(file_contents):
    return len(file_contents.split())

def print_report(rel_path, words, chars):
    print(f"--- Begin report of {rel_path} ---")
    print(f"{words} wordds found in the document\n")
    for char in chars:
        print(f"The {char} character was found {chars[char]} times")
    
    print("--- End report ---")



with open('./books/frankenstein.txt') as f:
    file_contents = f.read()
    count_w = count_words(file_contents)
    count_c = count_chars(file_contents)

    print_report(f.name, count_w, count_c)



