name = input("whats your name")

match name:
    case "baluku" | "EDGAR" | "SAM":
        print("Gryffindor")
    case "Dev":
        print("Slytherin")   

    case _:
        print("who")
     