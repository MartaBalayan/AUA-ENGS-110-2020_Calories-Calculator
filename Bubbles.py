import pprint


def Book_sort(smth):
    checked = True

    while checked:

        checked = False

        for i in range(len(smth) - 1):

            if smth[i]["year"] > smth[i + 1]["year"]:
                smth[i], smth[i + 1] = smth[i + 1], smth[i]

                checked = True
    return smth


books = [{"title": "Harry Potter and the Prisoner of Azkaban", "year": 1999, "month": "July"},
         {"title": "Harry Potter and the Chamber of Secrets", "year": 1998, "month": "July"},
         {"title": "Harry Potter and the Philosopher's Stone", "year": 1997, "month": "June"}]

print(Book_sort(books))

for i in books:
    pprint.pprint(i)