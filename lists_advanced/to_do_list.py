things_to_do = input().split("-")
to_do_list = []
sorted_tasks = []
while things_to_do[0] != "End":
    task_importance = int(things_to_do[0])
    task = things_to_do[1]
    to_do_list.append([task_importance, task])
    sorted_tasks = [data[1] for data in sorted(to_do_list)]
    things_to_do = input().split("-")
print(sorted_tasks)
