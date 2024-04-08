import re


def main():
    print(count(input("Text: ")))

   #findall, looks for any match given a pattern and returns it as a list, the pattern is (um) and anything that is not an alphanumeric character before or after it.
def count(s):
     if matches := re.findall(r"(\bum\b)", s, re.IGNORECASE):
        return len(matches)
     else: return 0

if __name__ == "__main__":
    main()
