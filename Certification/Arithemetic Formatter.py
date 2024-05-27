def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    for problem in problems:
        first, operator, second = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        length = max(len(first), len(second)) + 2

        first_line.append(first.rjust(length))
        second_line.append(operator + second.rjust(length - 1))
        third_line.append('-' * length)

        if answer:
            if operator == '+':
                result = str(int(first) + int(second))
            else:
                result = str(int(first) - int(second))
            fourth_line.append(result.rjust(length))

    arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(third_line)
    if answer:
        arranged_problems += '\n' + '    '.join(fourth_line)

    return arranged_problems

# Test the function

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"], True)}')
print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True)}')
print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], True)}')
print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))