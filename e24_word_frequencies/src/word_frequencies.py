#!/usr/bin/env python3

def word_frequencies(filename):
    with open(filename, 'r') as f:        
        s = f.read()
        words = s.split() 
        words = [w.strip("""!"#$%&'()*,-./:;?@[]_""") for w in words]
        wc = {w:0 for w in words}
        for w in words:
            wc[w] += 1
        items = sorted(wc.items(), key= lambda item : item[1])
        wc = dict(items)
        print(wc['Alice'])
    return wc

def main():
    print(word_frequencies(r"e24_word_frequencies\src\alice.txt"))

if __name__ == "__main__":
    main()