import re
import sys

users = set()
groups = set()

# Process each line from stdin
for line in sys.stdin:
    match = re.search(r'\\([^\s]+) \((SidTypeUser|SidTypeGroup)\)', line)
    if match:
        name = match.group(1)
        sid_type = match.group(2)

        if sid_type == "SidTypeUser":
            users.add(name)
        elif sid_type == "SidTypeGroup":
            groups.add(name)

# Output sorted results
print("Users:")
for user in sorted(users):
    print(user)

print("\nGroups:")
for group in sorted(groups):
    print(group)