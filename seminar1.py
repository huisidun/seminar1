while True:
    answer = input("сделал лабу по элтеху? (Y/N)\n").strip().upper()
    if answer == 'Y':
        print("\033[93mскинь пж\033[0m")
        break
    elif answer == 'N':
        print("соболезную..")
    else:
        print("\033[91mY/N!!!\033[0m")