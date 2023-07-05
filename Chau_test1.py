#OPEN AND READ FILE
def openread_file(filename):
    file = open(filename, mode = 'r')
    content = file.readlines()
    file.close()  
    return content


#PROCESS DATA
def process_data(data):
    list_content = []
    for row in data:
        list_row = row.split()
        if len(list_row) == 1:
            continue
        else:
            list_content.append(list_row)

    #Number of column
    number_of_column = len(list_content[0])

    #Padding for each column
    padding = []
    max_len_column = 0
    for index in range(number_of_column):
        padding_each_column = max(len(list[index]) for list in list_content)
        padding.append(padding_each_column)

    #Max length line
    sum_padding = 0
    for pad in padding:
        sum_padding += pad
    max_length_line = sum_padding + (number_of_column - 1)*3

    #Formatting
    formatted_lines = []
    for line in list_content:
        if line == list_content[0]:
            formatted_line = ' | '.join(f'{col:^{width}}' if col else ' ' * width for col, width in zip(line, padding))
        else:
            formatted_line = ' | '.join(f'{col:>{width}}' if col else ' ' * width for col, width in zip(line, padding))
        formatted_lines.append(formatted_line)
    formatted_lines.insert(0, '-' * max_length_line)
    formatted_lines.insert(2, '-' * max_length_line)   
    final_result = '\n'.join(formatted_lines)
    return final_result


#WIRTE IN NEW FILE
def write_file(filename,final_result):
    file = open(filename, "w")
    file.write(final_result)


#MAIN
def main():
    content = openread_file('test.txt')
    data = process_data(content)
    write_file('Chau_test1_result.txt',data)
    
    
if __name__ == "__main__":
    main()   


    