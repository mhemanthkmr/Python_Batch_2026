# AND, OR, NOT

value_A = True
value_B = False

print(value_A and value_B)  # False
print(value_A or value_B)  # True
print(value_A and (not value_B))  #

print(
    True
    and False
    or (True and not False)
    or False
    and (not True and not True)
    or not True
)

# True and False or ( True and not False ) or False and (not True and not True) or not True

# True and False or ( True ) or False and ( False ) or not True

# True and False or ( True ) or False and ( False ) or not True

# True and False or ( True ) or False and ( False ) or False

# False or ( True ) or False and ( False ) or False

# False or ( True ) or False and ( False ) or False

# True or False and ( False ) or False

# True or False

# True
