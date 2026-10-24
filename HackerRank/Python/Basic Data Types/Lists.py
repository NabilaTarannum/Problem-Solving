if __name__ == "__main__":
    N = int(input())
    my_list = []

    commands = {
        "insert": lambda x, y: my_list.insert(x, y),
        "print": lambda: print(my_list),
        "remove": lambda x: my_list.remove(x),
        "append": lambda x: my_list.append(x),
        "sort": lambda: my_list.sort(),
        "pop": lambda: my_list.pop(),
        "reverse": lambda: my_list.reverse(),
    }

    for _ in range(N):
        command = input().split()
        action = command[0]
        if action in commands:
            if action in ["insert"]:
                commands[action](int(command[1]), int(command[2]))
            elif action in ["remove", "append"]:
                commands[action](int(command[1]))
            else:
                commands[action]()
