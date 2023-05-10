bad_chars = ".-:,'&/1234567890"

with open("words.txt", "r") as input:
    with open("words_fixed.txt", "w") as output:
        for idx, line in enumerate(input):
            bad = False

            # check for illegal characters
            for c in bad_chars:
                if c in line:
                    bad = True

            # check for length
            if not 4 < len(line):
                bad = True

            if not bad:
                output.write(line)
