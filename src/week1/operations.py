
def palindrome(word):
    start_i = 0
    end_i = len(word)-1
    palin = True
    while start_i < end_i:
        start_char = word[start_i]
        end_char = word[end_i]
        if start_char != end_char:
            palin = False
            break
        start_i += 1
        end_i += -1
    print(palin)



def odd_numbers(lim):
    for i in range(lim):
        if i % 2 != 0:
            print(i)


def main():
    palindrome("test")

# TODO: test todo function.
# Entry point. This explicitly tells the file that we want to execute it. This cuts down on import errors
if __name__ == "__main__":
    main()