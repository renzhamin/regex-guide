import re

f = open("log_train.txt", "r").read()

train_loss = re.findall(r'Train loss: (\d+\.\d+)', f)
valid_loss = re.findall(r'Valid loss: (\d+\.\d+)', f)

train_loss = [float(i) for i in train_loss]
valid_loss = [float(i) for i in valid_loss]

print("train_loss =", train_loss)
print("")
print("valid_loss =", valid_loss)
