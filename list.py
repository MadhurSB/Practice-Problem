if __name__ == '__main__':
    N = int(input())  # Number of elements or commands
    
    list_N = []  # Initialize an empty list
    
    for _ in range(N):
        command = input().split()  # Read each command and split into parts
        
        # Process commands based on the input
        if command[0] == "insert":
            list_N.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(list_N)
        elif command[0] == "remove":
            list_N.remove(int(command[1]))
        elif command[0] == "append":
            list_N.append(int(command[1]))
        elif command[0] == "sort":
            list_N.sort()
        elif command[0] == "pop":
            list_N.pop()
        elif command[0] == "reverse":
            list_N.reverse()
