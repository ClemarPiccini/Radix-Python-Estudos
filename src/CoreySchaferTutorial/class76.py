# Sets - Set Methods and Operations to Solve Common Problems

s4 = set([1, 2, 3, 4, 5])
s4.add(7)
s4.remove(1)

print(s4)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

s5 = s1.intersection(s2)

print(s5)

employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

if 'Corey' in developers:
    print('Found!')

# O(n) for list
# O(1) for a set