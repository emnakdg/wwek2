p = True
q = False

left_s = not(p or q)
right_s = (not p) and (not q)
print(left_s == right_s)



p = False
q = True

left_s = not(p or q)
right_s = (not p) and (not q)
print(left_s == right_s)
