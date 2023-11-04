number = int(input())
char_percentage = number // 10
char_point = 10 - char_percentage

if number < 100:
    print(f"{number}% [{'%'* char_percentage}{'.'* char_point}]")
    print("Still loading...")
else:
    print("100% Complete!")
    print(f"[{'%'* char_percentage}]")
