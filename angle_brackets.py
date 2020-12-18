class Angles:

    def check(self, angles):
        angles = list(angles)
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
