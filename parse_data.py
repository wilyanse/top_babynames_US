old_data = "raw_data_2007.txt"

with open(old_data, "r") as file:
    lines = file.readlines()
    print("".join(lines))  # Join to avoid extra newlines
    print(lines[0].split())
