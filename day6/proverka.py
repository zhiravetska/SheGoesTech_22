food = "Kartupelis"
# count = 0
# bad_char = "S"
# clean_text = ""
# for c in food:
#     if c == bad_char:
#         count += 1
#         print("found a bad one", bad_char)
#     else:
#         clean_text += c  # create new string by adding char to old string
# print(f"There are {count} {bad_char}s in {food}")
# print(f"Cleaned {clean_text=}")

for c in food:
    print(c, end=":")  # so instead of default newline \n i used : as endpoint
print()
