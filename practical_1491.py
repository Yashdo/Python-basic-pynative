# 1491. Average Salary Excluding the Minimum and Maximum Salary
salary = [1000, 2000, 3000]

"""First Method"""

# minimum=min(salary)
# maximum=max(salary)
# avg= (minimum + maximum)/2
# print(avg)

"""Secound Method"""

lenth = len(salary)
min_salary = salary[0]
max_salary = salary[0]
mini=0
maxi=0
for i in range(lenth):

    if min_salary < salary[i]:
        salary[i] = min_salary
        # mini = salary[i]
    
    if max_salary > salary[i]:
        salary[i] = max_salary
        # maxi = salary[i]
print(salary)

# print(minimum)
# print(maximum)

# avg = (minimum + maximum) / 2
# print(avg)
