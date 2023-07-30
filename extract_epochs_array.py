import re

f = open("log_train.txt", "r").read()

epochs = [ int(i) for i in re.findall(r'\[(\d+)/\d+\]', f) ]

print(epochs)
