# PYCOR-41: Design the playlist and sample data
# Created a playlist with alt/rock and rap tracks.
# This list is used for slicing, negative indices, reverse slicing, and membership checks.

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

# Basic slice tests
print(playlist[1:4])
print(playlist[-4:-1])
print(playlist[::-1])
print("Post Malone - Rockstar" in playlist)

# PYCOR-42: Prompt user for slice indices and handle input safely
# PYCOR-43: Reverse preview and display the preview slice
# PYCOR-44: Membership check
try:
    start = int(input("Enter start index (can be negative, e.g., -3): "))
    end = int(input("Enter end index (exclusive, can be negative, e.g., -1): "))
    step = int(input("Enter step (e.g., 1 for normal, -1 for reverse): "))

    preview_slice = playlist[start:end:step]

    print("\nFull playlist:")
    print(f"You entered: start={start}, end={end}, step={step}")
    print("\nPreview slice:")
    print(preview_slice)

    reverse = input("Reverse preview? (y/n): ").lower()
    if reverse == "y":
        preview_slice = preview_slice[::-1]
        print("\nReversed preview slice:")
        print(preview_slice)

    song_to_check = input("Enter a song name to check: ")
    if song_to_check in preview_slice:
        print(f"'{song_to_check}' is in the preview!")
    else:
        print(f"'{song_to_check}' is NOT in the preview.")

except ValueError:
    print("Invalid input! Please enter integer values only.")
