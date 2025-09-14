while True:
    answer = input("сделал лабу по элтеху? (Y/N)\n").strip().upper()
    if answer == 'Y':
        print("скинь")
        break
    elif answer == 'N':
        print("соболезную")
        break
    else:
        print("Y/N!!!!")