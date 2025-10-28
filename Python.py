# Read the total number of country stamps
n = int(input())

# Initialize an empty set to store unique country names
stamps = set()

# Read each country name and add it to the set
for _ in range(n):
    stamps.add(input())

# Output the number of distinct country stamps
print(len(stamps))

         