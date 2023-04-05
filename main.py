# friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]

# print(f"lenth of friends is {len(friends)}")

# first = friends[0]
# mid = friends[1]
# last = friends[-1]

# print(f"First friend is: {first}")
# print(f"Mid friend is: {mid}")
# print(f"Last friend is: {last}")

# print(type(first))
# print(type(mid))
# print(type(last))

# friend_name = input("Enter your name: ")
# gender = input("Your sex (Male or Female): ")
# friend_tuple = (friend_name, gender)
# friends.append(friend_tuple)
# print(friends)

# student = {
#     "name": "Toan",
#     "age": "21",
#     "grades": [15, 25, 23, 10]
# }
# info = {
#         "id": "SV001",
#         "gender": "male"
# }
# student.update(info)
# key = list(student.keys())
# print(key)

# value = list(student.values())
# print(value)

# items = list(student.items())
# print(items)

# student.clear()
# print(student)

# set_a = {"John", "Max", "Anna", "Bob", "Obito"}
# set_m = {"Max", "Mery", "David", "Anna", "Naruto", "John"}

# # Tìm bạn học vẽ + toán
# set_a_m = set_a.intersection(set_m)
# print(set_a_m)

# # Tìm bạn học vẽ - toán
# set_art = set_a.difference(set_m)
# print(set_art)

# # Tìm bạn học toán - vẽ
# set_math = set_m.difference(set_a)
# print(set_math)

# # Tìm bạn học chỉ học 1 môn
# set_only = set_a.symmetric_difference(set_m)
# print(set_only)

# # Tìm tất cả
# set_all = set_a.union(set_m)
# print(set_all)

lst = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_years": 1973,
    "track_list": [
    "Speak to me",
    "Breathe",
    "On The Run",
    "Time",
    "The Great Gig in the Sky",
    "Money",
    "Us and Them",
    "Any colour you like",
    "Brain Damage",
    "Eclipse",
    ]}
print(lst["album_name"])
print(lst.get("album_name"))

print(lst["release_years"])
print(lst.get("release_years"))

lst["release_years"] = 1971
print(lst)

del lst["track_list"]
print(lst)

lst["amount"] = 2000
lst.update(amount=2000)
print(lst)

lst.clear()
print(lst)
