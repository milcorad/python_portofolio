def custom_function(data):
    for i in range(len(data)):
        if i % 2 == 0:
            data[i] = True
        else:
            data[i] = False
    return data

print(custom_function([0, 0, 0, 0, 0]))