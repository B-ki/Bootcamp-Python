import random

option_list = ['shuffle', 'unique', 'ordered']


def generator(text, sep=" ", option=None):
    if not isinstance(text, str):
        print("ERROR")
        raise TypeError("text is not a string")
    if option is not None:
        if option not in option_list:
            print("ERROR")
            raise ValueError("Option is not correct")
    x = text.split(sep)
    if option is not None:
        if option == "shuffle":
            for i in range(len(x)-1, 0, -1):
                j = random.randint(0, i + 1)
                x[i], x[j] = x[j], x[i]
            for i in x:
                yield i
        elif option == "unique":
            for i in list(set(x)):
                yield i
        elif option == "ordered":
            for i in sorted(x):
                yield i
    else:
        for i in x:
            yield i


text = "Le Lorem Ipsum est simplement du faux texte. Lorem Ipsum Lorem Ipsum"

mygenerator = generator(text, sep=" ")
print(mygenerator)
for i in mygenerator:
    print(i)
for i in mygenerator:
    print(i)
print()
list2 = generator(text, sep=" ", option="shuffle")
for w1 in list2:
    print(w1)
print()
for w2 in generator(text, sep=" ", option="ordered"):
    print(w2)
print()
for w3 in generator(text, sep=" ", option="unique"):
    print(w3)
