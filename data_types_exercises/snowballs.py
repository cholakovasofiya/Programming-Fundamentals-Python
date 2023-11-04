count_snowballs = int(input())
best_ball = 0
best_weight = 0
best_time = 0
best_quality = 0

for ball in range(count_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int((snowball_weight / snowball_time) ** snowball_quality)
    if snowball_value > best_ball:
        best_ball = snowball_value
        best_weight = snowball_weight
        best_time = snowball_time
        best_quality = snowball_quality
print(f"{best_weight} : {best_time} = {best_ball} ({best_quality})")
