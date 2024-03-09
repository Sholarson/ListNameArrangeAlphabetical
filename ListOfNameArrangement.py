nameList = {}
a = []
i = 0

try:
    textFileName = input("Enter the textFile name you want to store along with the extention '.txt': ")

    if not textFileName.endswith(".txt") :
        raise Exception("'.txt' not added! ")
    
    while True:
        nameInput = input("Enter the name or enter 'Q' if you want to quit: ")
        if nameInput.istitle() == False:
            print("First, second and last name should start with capital letter")
            continue
        elif nameInput.lower() == "q":
            break
        a.insert(i,nameInput)
        i+=1

    a.sort()

    def textFile(n):
        with open(n, 'w') as file:
            for key, value in nameList.items():
                file.write(f'{key}: {value}\n')

    for i in range(len(a)):
        nameList[i+1] = a[i]

    textFile(textFileName)
    print(nameList)

except Exception as err:
    print(f"An error has occured: {err}")


    
