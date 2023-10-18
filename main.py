
with open("books/frankestein.txt") as f:
    file_contents = f.read()
    chars = {}
    for word in file_contents:
        
        lower = word.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
       

