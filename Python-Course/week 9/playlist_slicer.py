# PYCOR-41: Design the playlist and sample data
# Created a playlist with alt/rock and rap tracks.
# This list is used for slicing, negative indices, reverse slicing, and membership checks as required by the assignment.

playlist = [
    "Linkin Park - Numb",
    "The Neighbourhood - Sweater Weather",
    "Imagine Dragons - Believer",
    "Arctic Monkeys - Do I Wanna Know?",
    "Nirvana - Smells Like Teen Spirit",
    "Thirty Seconds to Mars - Stuck",
    "Red Hot Chili Peppers - Californication",
    "Fall Out Boy - Centuries",
    "Green Day - American Idiot",
    "Eminem - Lose Yourself",
    "2Pac - California Love",
    "NF - Destiny",
    "NF - Statement",
    "Kendrick Lamar - HUMBLE.",
    "Post Malone - Rockstar"
]
print(playlist[1:4])
print(playlist[-4:-1])
print(playlist[::-1])
print("Post Malone - Rockstar" in playlist)

# PYCOR-42: Prompt user for slice indices and handle input safely
# Prompts the user for start, end, and step values, converts them to integers,
# and handles potential invalid or negative inputs.
try:
    start = int(input("Enter the index (can negative, e.g, -3): "))
    end = int(input("Enter end index (exclusive, can be negative, e.g, -1): "))
    step = int(input("Enter step (e.g, 1 for normal, -1 for reverse): "))

    print(f"\nYou entered: start={start}, end={end}, step={step}")
except ValueError:
    print("Invalid input! Please enter integer values only.")
