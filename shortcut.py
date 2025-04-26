def find_list(list_search, finder):

    for x in range(len(list_search) - 1):

        if list_search[x] == finder:
            return x

    return -1