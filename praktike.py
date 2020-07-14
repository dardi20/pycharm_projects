def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


#print (is_even(15))

def is_palindrome(num):
    num_str = str(num)
    num_str1 = num_str[:int(len(num_str)/2)]
    num_str2 = ""
    index = len(num_str)-1

    while index > len(num_str)/2:
        num_str2 += num_str[index]
        index -= 1

    if num_str1 == num_str2 :
        return "Is a palindrome"
    else:
        return "It's not a palindrome"

#print(is_palindrome(121))

def is_pow_of_2(num):
    if num % 2 != 0:
        return "Its not power of 2"
    num = int(num / 2)
    if num == 1:
        return "Its power of 2"
    is_pow_of_2(num)

#print(is_pow_of_2(4))
fjale = "lalalala"
fjale.capitalize()

def to_upper_case(str):

    for index in range(0, 4):
        if (str[index]+"").isupper():
            return str.upper()
        else:
            return str

#print(to_upper_case("dJaLi"))

def divisible_by5(numbers):
    filtered_numbers = [];
    for var in numbers:
        if(var > 150):
            continue
        if var % 5 != 0:
            continue
        else:
            filtered_numbers.append(var)

    return filtered_numbers

#print(divisible_by5([35, 25, 160, 120, 100]))

def list_to_dictionary(words):
    result = dict()
    sorted_result = dict()
    for word in words:
        if result.get(len(word)) != None:
            result[len(word)].append(word)
        else:
            result[len(word)] = [word]
    for i in list(sorted(result.keys())):
        sorted_result[i] = result.get(i)

    return sorted_result
print(list_to_dictionary(["ghjkk","hjjkk", "u", "sfd", "jk", "oooooooo"]))


