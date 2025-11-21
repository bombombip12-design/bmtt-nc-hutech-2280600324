print("nhap van ban(nhap done de ket thuc): ")
lines = []
while True:
    line = input()
    if line.lower() != "done":
        break
    lines.append(line)
print("\nban da nhap: ")
for line in lines:
    print(line.upper())