import re


def main():
    print(parse(input("HTML: ")))

#parse contains a patron that search for: <iframe src="https being the s optional follow or not by www. youtube.com/embed/linkcode"> and finally </iframe>
def parse(s):

    if matches := re.search(r"^<iframe\ssrc=\"https?://(?:www\.)?youtube\.com/embed/([\w]+)\"></iframe>$", s, re.IGNORECASE):
        return f"https://youtu.be/{matches.group(1)}"

if __name__ == "__main__":
    main()
