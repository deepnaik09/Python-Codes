text = "X-DSPAM-Confidence:    0.8475"
n = text.find('.')
print(float(text[n-1:]))