def last_line(words, diff, i, j):
    space_needed = j - i - 1
    spaces_on_right = diff - space_needed

    word = "".join(words[i])
    k = i + 1
    while k < j:
        word += " " + words[k]
        k += 1

    return word


def justifying(words, diff, i, j):
    space_needed = j - i - 1
    spaces = diff // space_needed
    extra_spaces = diff % space_needed

    word = "".join(words[i])
    k = i + 1
    while k < j:
        if extra_spaces > 0:
            spaces_to_apply = spaces + 1
        else:
            spaces_to_apply = spaces + 0
        extra_spaces -= 1

        word += (" " * spaces_to_apply) + words[k]
        k += 1
    return word


def dynamic_algorithm(text_input, max_width):

    texts = text_input.split("\n")
    out = []
    for text in texts:
        if len(text):
            words = text.split(" ")
            i = 0
            n = len(words)
            while i < n:
                j = i + 1
                line_length = len(words[i])
                while j < n and ((line_length + len(words[j]) + (j - i - 1)) < max_width):
                    line_length += len(words[j])
                    j += 1

                diff = max_width - line_length
                number_of_words = j - i
                result = ""
                if number_of_words == 1:
                    result += (last_line(words, diff, i, j))
                else:
                    result += (justifying(words, diff, i, j))
                out.append(result)
                i = j
        else:
            out.append("\n")

    return out


def greedy_algorithm(text_input, max_width):

    texts = text_input.split("\n")
    out = []
    for text in texts:
        if len(text):
            words = text.split(" ")
            i = 0
            n = len(words)
            while i < n:
                j = i + 1
                line_length = len(words[i])
                while j < n and ((line_length + len(words[j]) + (j - i - 1)) < max_width):
                    line_length += len(words[j])
                    j += 1

                spaces = (j - i - 1)
                line_length += spaces
                diff = max_width - line_length
                number_of_words = (j - i)
                result = ""
                if number_of_words == 1:
                    result += words[j - 1]
                else:
                    for k in range(i, j):
                        result += words[k]
                        if spaces > 0:
                            result += " "
                        spaces -= 1

                out.append(result)
                i = j
        else:
            out.append('\n')

    return out


def read_file_in(filename_in):
    with open(f'inputs/{filename_in}.txt') as file_in:
        ret = file_in.read()
    return ret


def write_file_out(filename_out, text_output):
    with open(f'outputs/{filename_out}_out.txt', 'w') as file_out:
        file_out.write(text_output)


if __name__ == '__main__':
    option_1 = 2
    while option_1 != 0:
        try:
            option_1 = int(input("\nSelect a formatting type:\n" + "1 - Greedy Algorithm (Basic)\n" +
                                 "2 - Dynamic Algorithm (Intermediary)\n" + "0 - Exit\n"))
            if option_1 == 0:
                break
            elif option_1 == 1 or option_1 == 2:
                filename = input("Enter the filename (without the extension): \n")
                try:
                    text_in = read_file_in(filename)
                    try:
                        line_width = int(input("Enter the number of characters per line:\n"))
                        if line_width > 0:
                            if option_1 == 1:
                                text_out = greedy_algorithm(text_in, line_width)
                            else:
                                text_out = dynamic_algorithm(text_in, line_width)

                            for idx, line in enumerate(text_out):
                                if line != '\n':
                                    text_out[idx] += '\n'

                            write_file_out(filename, "".join(text_out))
                        else:
                            print("Invalid number")
                    except ValueError:
                        print("Invalid number!")
                except FileNotFoundError:
                    print("\nFile does not exist!\n")
            else:
                print("\nInvalid Option\n")
        except ValueError:
            print("\nInvalid Option\n")
