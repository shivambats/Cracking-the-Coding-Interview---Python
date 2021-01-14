input = 'aabbccddee'

current = input[0]
current_count = 0

output = str()
small = True

for each in input:
    if each == current:
        current_count += 1
    else:
        if current_count != 2:
            small = False
        output += f"{current}{current_count}"
        current_count = 1
        current = each

if small:
    output = input
