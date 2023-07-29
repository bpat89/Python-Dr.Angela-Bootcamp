# ("🌳")  "💰"

row1 = ["🌳", "🌳", "🌳"]
row2 = ["🌳", "🌳", "🌳"]
row3 = ["🌳", "🌳", "🌳"]
print("Welcome to the treasure map")
print(f"{row1}\n{row2}\n{row3}")

position = input("Mark the coordinates of your treasure : ")
x_axis = int(position[0])
y_axis = int(position[1])
full_map = [row1, row2, row3]
selected_row = full_map[x_axis-1]
selected_row[y_axis-1] = "💰"
print(f"{row1}\n{row2}\n{row3}")
