write = open("Assembled.txt", "w")
write.close()
write = open("Assembled.txt", "a")
with open("Assembly.txt", "r") as read:
    data = read.readlines()
    for line in data:
        instruction = line.split()
        opcode = instruction[0]
        if opcode == "search":
            operand1 = instruction[1]
            write.write("copy " + operand1 +" x \n")
            write.write("seek -9999 \n")
            write.write("mark search \n")
            write.write("test EOF \n")
            write.write("tjmp terminate \n")
            write.write("test x = f \n")
            write.write("fjmp search \n")
