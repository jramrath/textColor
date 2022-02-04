from textColor import tc

def test():
    print("Starting test ...")

    print(tc.green("This should be green"))
    print(tc.red("This should be red"))
    print(tc.blue("This should be blue"))
    print(tc.yellow("This should be yellow"))
    
    print(tc.input("INPUT"))
    print(tc.info("INFO"))
    print(tc.error("ERROR"))
    print(tc.output("OUTPUT"))