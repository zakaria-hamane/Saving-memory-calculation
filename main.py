msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def components_of_oper():
    calc = input(msg_0).split()
    oper = calc[1]
    if calc[0] == 'M':
        x = float(memory)
        x = int(x) if '.0' in str(x) else x
    else:
        x = float(calc[0])
        x = int(x) if '.0' in str(x) else x
    if calc[2] == 'M':
        y = float(memory)
        y = int(y) if '.0' in str(y) else y

    else:
        y = float(calc[2])
        y = int(y) if '.0' in str(y) else y
    return x, y, oper


def is_one_digit(v):
    return type(v) == int and (-10 < v < 10)


def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y) is True:
        msg += msg_6
    if (x == 1 or y == 1) and oper == '*':
        msg += msg_7
    if (x == 0 or y == 0) and (oper in "* + -"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
    return msg


def operations(x, y, oper):
    operations = {"*": float(x * y), "+": float(x + y), "-": float(x - y)}
    return operations.pop(oper) if oper in operations else x / y


def check_msg_index(msg_index):
    msgs = [msg_10, msg_11, msg_12]
    msg_ = list(enumerate(msgs, 10))
    for index, msg in msg_:
        if index == msg_index:
            return msg


def check_result_one_digit(memory, result):
    result = int(result) if '.0' in str(result) else float(result)
    if is_one_digit(result) is False:
        memory = result
    elif is_one_digit(result) is True:
        msg_index = 10
        while msg_index <= 12:
            msg = check_msg_index(msg_index)
            if input(msg) == "y":
                msg_index += 1
            else:
                break
        else:
            memory = result
    return memory
            

memory = 0
while True:
    x, y, oper = components_of_oper()
    msg = check(x, y, oper)
    print(msg)
    try:
        result = operations(x, y, oper)
        print(result)

        if input(msg_4) == "y":
            memory = check_result_one_digit(memory, result)
        else:
            memory
        if input(msg_5) == "n":
            break

    except ZeroDivisionError:
        print(msg_3)
    except ValueError:
        print(msg_1)
    except KeyError:
        print(msg_2)
