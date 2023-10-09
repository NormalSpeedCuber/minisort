def minisort(array=list):
    output = []

    while True:
        output.append(min(array))
        array.remove(min(array))

        if len(array) == 0:
            break

    return output

nums = [3, 1, 2]

print(minisort(nums))