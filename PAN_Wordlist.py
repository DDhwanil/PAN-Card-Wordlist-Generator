Dictionary = open("PAN.txt", "a")
Fourthchar=['C','H','F','A','T','B','L','J','G','P']

print ("Wait for sometime to generate wordlist in Python")
for one in range(65,90,1):
    for two in range(65,90,1):
        for three in range(65,90,1):
            for four in Fourthchar:
                for five in range(65,90,1):
                    for six in range(0,9,1):
                        for seven in range(0,9,1):
                            for eight in range(0,9,1):
                                for nine in range(0,9,1):
                                    for ten in range(65,90,1):
                                        string='%s%s%s%s%s%s%s%s%s%s'%(chr(one),chr(two),chr(three),four,chr(five),six,seven,eight,nine,chr(ten))
                                        Dictionary.write(string)
                                        Dictionary.write('\n')
print ("Please find the wordlist (PAN.txt) in the same directory.")
