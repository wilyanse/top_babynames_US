old_data = "raw_data_2007.txt"

old_males = []
old_females = []
old_both = []

with open(old_data, "r") as file:
    lines = file.readlines()
    for line in lines[1:]:
        male_name = line.split()[1]
        female_name = line.split()[2]
        old_males.append(male_name)
        old_females.append(female_name)

        old_both.append(male_name)
        old_both.append(female_name)

print("Old data:")
print(old_males)
print(old_females)
print(old_both)

new_data = "raw_data_2020.txt"

new_males = []
new_females = []
new_both = []

with open(new_data, "r") as file:
    lines = file.readlines()
    for line in lines[1:]:
        male_name = line.split()[1]
        female_name = line.split()[2]
        new_males.append(male_name)
        new_females.append(female_name)

        new_both.append(male_name)
        new_both.append(female_name)

print("New data:")
print(new_males)
print(new_females)
print(new_both)

# Find the names that are in the old data but not in the new data
most_popular_boys = [name for name in old_males if name not in new_males][:10]
print(most_popular_boys)

most_popular_girls = [name for name in old_females if name not in new_females][:10]
print(most_popular_girls)

most_popular_boys = [name for name in old_males if name not in new_both[:100]][:10]
print(most_popular_boys)

most_popular_girls = [name for name in old_females if name not in new_both[:100]][:10]
print(most_popular_girls)