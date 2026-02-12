user_id = [10,12,11,13,14,15] 

# Continue

for i in user_id:
    if i in [13,14,15]:
        continue
    print(i, "Email sent to this user.")


i = 0

while True:
    print(i)
    if i == 15:
        break
    i += 1