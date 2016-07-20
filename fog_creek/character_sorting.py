# http://www.fogcreek.com/jobs/supportengineer
from collections import Counter

if __name__ == "__main__":
    with open("character_sorting_text.txt") as f:
        text = "".join(f.readlines())
        sorted_string = ""
        for letter, count in Counter(text).most_common():
            sorted_string += letter
        result = sorted_string.split("_")[0]
        print(result)
