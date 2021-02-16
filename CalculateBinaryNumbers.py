def calculateBinaryNumbers(binaryString: str):
    outputInteger: int = 0
    counter: int = 0

    if len(binaryString) < 8:
        return

    if len(binaryString) > 8:
        return

    for i in binaryString:
        if not i == "1" and not i == "0":
            return

        if counter == 0:
            if i == "1":
                outputInteger += 128
            else:
                outputInteger += 0

        if counter == 1:
            if i == "1":
                outputInteger += 64
            else:
                outputInteger += 0

        if counter == 2:
            if i == "1":
                outputInteger += 32
            else:
                outputInteger += 0

        if counter == 3:
            if i == "1":
                outputInteger += 16
            else:
                outputInteger += 0

        if counter == 4:
            if i == "1":
                outputInteger += 8
            else:
                outputInteger += 0

        if counter == 5:
            if i == "1":
                outputInteger += 4
            else:
                outputInteger += 0

        if counter == 6:
            if i == "1":
                outputInteger += 2
            else:
                outputInteger += 0

        if counter == 7:
            if i == "1":
                outputInteger += 1
            else:
                outputInteger += 0

        counter += 1

    return outputInteger
