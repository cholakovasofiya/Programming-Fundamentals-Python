list_body_parts = []
for _ in range(3):
    body_part = input()
    list_body_parts.append(body_part)
list_body_parts[0], list_body_parts[2] = list_body_parts[2], list_body_parts[0]
print(list_body_parts)
