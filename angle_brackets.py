class Angles:

    def check(self, angles):
        angles = list(angles)
        # print(angles)
        counter = 0
        for i in angles:
            if i == "<":
                counter += 1
            else:
                counter -= 1
        print("Counter:", counter)
        if angles[-1] == "<" and angles[0] == ">":
                angles.insert(0, "<")
                angles.append(">")
                print("printing angles 3", "".join(angles))
                # return "".join(angles)

        if counter > 0:
            angles.append(">" * counter)
            print("printing angles 1", "".join(angles))
            return "".join(angles)
        elif counter < 0:
            counter = abs(counter)
            for i in range(counter):
                angles.insert(0, "<")
                print("printing angles 2", "".join(angles))
                return "".join(angles)
        else:
            print("printing angles 3", "".join(angles))
            return "".join(angles)





    # left = []
    # right = []
    # for i in angles:
    #     if i == "<":
    #         left.append("<")
    #     elif i == ">":
    #         right.append(">")
    # print(left)
    # print(right)
    # left_brackets = left.count("<")
    # right_brackets = right.count(">")
    # if left_brackets % 2 == 0 and right_brackets % 2 == 0:
    #     if angles[-1] == "<":
    #         angles.append(">")
    #         print("printing angles 1", angles)
    #         return angles
    #     elif angles[0] == ">":
    #         angles.insert(0, "<")
    #         print("printing angles 2", angles)
    #         return angles
    #     else:
    #         print("printing angles 3", angles)
    #         return angles
    # else:
    #     print("lol no")
    #     return "no"

# checking this: "<<>><"