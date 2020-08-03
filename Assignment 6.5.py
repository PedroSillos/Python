text = "X-DSPAM-Confidence:    0.8475"
char_pos = text.find(":")
stretch = text[char_pos+1 :]
striped = stretch.strip()
print(striped)