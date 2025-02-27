day_number = [1,2,3,4,5,6,7]
day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
zero_to_19 = range(20)

for day in day_name:
    print(day)
    
i = 0
while i < 7:
    print(day_name[i])
    i +=  1 



for i in range(20):
    if i % 2:
        print(i)