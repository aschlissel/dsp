#Q1.
def different_degrees(diff):
    #create two lists to perform operations
    diff_degrees = []
    new_diff_degrees = []

    #append faculty column to list
    [diff_degrees.append(col[1]) for col in csv_f]

    #remove column heading
    del diff_degrees[0]

    #remove the periods in degrees to make degrees uniform
    diff_degrees = map(lambda diff_degrees: diff_degrees.replace(".", ""), diff_degrees)

    #separate multiple-degree strings in that list
    [new_diff_degrees.extend(item.split()) for item in diff_degrees]

    #count the number of degrees in each category
    diff_degrees_count = collections.Counter(new_diff_degrees)
    return diff_degrees_count
