# https://luteorg.github.io/lute-manual/usage/terms/bulk-term-import.html
import csv


def main():
    i_file = "bnc-coca.csv"
    o_file = "output.csv"

    with open(i_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        rows = list(reader)

    with open(o_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["language", "term", "translation", "parent", "tags"])
        for row in rows:
            term, forms, tags = row
            if "," in forms:
                forms = forms.split(", ")
                forms.insert(0, term)
                forms = list(dict.fromkeys(forms))
                for form in forms:
                    if form == term:
                        writer.writerow(["English", term, "", "", tags])
                    else:
                        writer.writerow(["English", form, "", term, tags])
            else:
                writer.writerow(["English", term, "", "", tags])

    print(f"Output written to {o_file}")


if __name__ == "__main__":
    main()
