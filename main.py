S = "Xavier2.0"

print("True" if len([s for s in S if s.isalnum()]) > 0 else "False")
print("True" if len([s for s in S if s.isalpha()]) > 0 else "False")
print("True" if len([s for s in S if s.isdigit()]) > 0 else "False")
print("True" if len([s for s in S if s.islower()]) > 0 else "False")
print("True" if len([s for s in S if s.isupper()]) > 0 else "False")
