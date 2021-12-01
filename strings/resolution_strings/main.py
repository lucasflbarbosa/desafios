def dynamic(text, width):
    words = text.split()
    count = len(words)
    slack = [[0] * count for i in range(count)]
    for i in range(count):
        slack[i][i] = width - len(words[i])
        for j in range(i + 1, count):
            slack[i][j] = slack[i][j - 1] - len(words[j]) - 1

    minima = [0] + [10 ** 20] * count
    breaks = [0] * count
    for j in range(count):
        i = j
        while i >= 0:
            if slack[i][j] < 0:
                cost = 10 ** 10
            else:
                cost = minima[i] + slack[i][j] ** 2
            if minima[j + 1] > cost:
                minima[j + 1] = cost
                breaks[j] = i
            i -= 1

    lines = []
    j = count
    while j > 0:
        i = breaks[j - 1]
        lines.append(' '.join(words[i:j]))
        j = i
    lines.reverse()
    return lines


def dynamic_algorithm():
    pass


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

                if number_of_words == 1:
                    result = ""
                    result += words[j - 1]
                else:
                    result = ""
                    for k in range(i, j):
                        result += words[k]
                        if spaces > 0:
                            result += " "
                        spaces -= 1
                    # if j < n:
                    #     result += (" " * diff)

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
            option_1 = int(input("\nSelect a formatting type:\n" + "1 - Greedy Algorithm\n" +"2 - Dynamic Algorithm\n" + "0 - Exit\n"))
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
                                #text_out = dynamic_algorithm(text_in, line_width)
                                text_out = dynamic(text_in, line_width)
                            for idx, line in enumerate(text_out):
                                if line != '\n':
                                    text_out[idx] += '\n'
                            # print(text_out)
                            # print("\n".join(text_out))
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
