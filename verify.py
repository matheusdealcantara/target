def verify(string):
    string = string.lower()
    if "a" in string:
        count = string.count("a")
        return [True, count]

    return [False, 0]


if __name__ == "__main__":
    string = input("Enter a string: ")
    result = verify(string)
    if result[0]:
        print(f"A string contém a letra 'a' {result[1]} vezes")
    else:
        print("A string não contém a letra 'a'")
