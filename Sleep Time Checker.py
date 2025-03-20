minimum_sleep_hours = int(input())
maximum_sleep_hours = int(input())
user_sleep_hours = int(input())

if minimum_sleep_hours <= user_sleep_hours <= maximum_sleep_hours:
    print("Normal")
if user_sleep_hours < minimum_sleep_hours:
    print("Deficiency")
if user_sleep_hours > maximum_sleep_hours:
    print("Excess")
