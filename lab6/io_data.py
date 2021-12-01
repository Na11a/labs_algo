def input_data(file_name):
    with open(file_name, 'r') as file:
        count=int(file.readline())
        words = []
        for line in file.readlines():
            words.append(line.replace("\n", ""))

    return {'words':words,'count':count}

def output_data(file_name,value_to_write):
    with open(file_name,'w') as file:
        file.write(str(value_to_write))