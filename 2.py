
raw_data = open("2.in").read()
ranges = raw_data.replace("\n", "").split(",")
invalids = 0
found_ids = []
for item in ranges:
    if not item.strip():
        continue
        
    start, end = map(int, item.split("-"))
    
    for j in range(start, end + 1):
        s = str(j)
        length = len(s)
        if length % 2 != 0:
            continue
        
        mid = length // 2
        if s[:mid] == s[mid:]:
            invalids += j
            found_ids.append(j)

            
print(f"Calculated Sum: {invalids}")
