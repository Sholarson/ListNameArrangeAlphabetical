# nameList = {}
# a = []
# i = 0

# textFileName = input("Enter the textFile name you want to store along with the extention '.txt': ")
# while True:
#     nameInput = input("Enter the name or enter 'Q' if you want to quit: ")
#     if nameInput.istitle() == False:
#         print("First, second and last name should start with capital letter")
#         continue
#     elif nameInput.lower() == "q":
#         break
#     a.insert(i,nameInput)
#     i+=1
# a.sort()
# def textFile(n):
#     file = open(n, 'w')
#     for key, value in nameList.items():
#         file.write(f'{key}: {value}\n')
#     # file.write(str(nameList))
#     file.close()
# for i in range(len(a)):
#     nameList[i+1] = a[i]
# textFile(textFileName)
# print(nameList)


try:
    i = int(input(": "))
    raise Exception("no")
except Exception as er:
    print(er)
