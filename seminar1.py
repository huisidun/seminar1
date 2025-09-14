while True:
    answer = input("сделал лабу по элтеху? (Y/N)\n").strip().upper()
    if answer == 'Y':
        print("скинь пж")
        break
    elif answer == 'N':
        print("соболезную..")
        break
    else:
        print("\033[91mY/N!!!\033[0m")