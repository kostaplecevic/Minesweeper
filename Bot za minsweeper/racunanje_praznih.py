
with open('cetiri_ugla.txt','r') as f:
    data = f.readlines()

for line in data:
    words = line.split()
print(words)
x = len(words)

konacno = []
for i in words:
    i = int(i)
    konacno.append(i)
print(konacno)