#######################
# Test Processing II  #
#######################


def digits_to_words(input_string):
    digit_string = ''
    separator = ' '
    numsInString = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    selected = []
    for i in range(len(input_string)):
        if input_string[i].isdigit(): 
            selected.append(numsInString[int(input_string[i])])
    digit_string = separator.join(selected)
    return digit_string

"""
컴퓨터 프로그래밍에 많은 명명 규칙이 있지만, 두 규칙이 특히 흔히 쓰입니다. 
첫번째로는, 변수 이름을 'underscore'로 나눠준다거나, (ex. under_score_variable)
두번째로는, 변수 이름을 대소문자 구별해 구분자 (delimiter)없이 쓰는 경우가 있습니다. 
이 두번째의 경우에는 첫번째 단어는 소문자로, 그 후에 오는 단어들의 첫번째 글자들은 대문자로 쓰입니다 (ex. camelCaseVariable). 
"""


def to_camel_case(underscore_str):
    underscoring = False

    temp = ''
    if underscore_str.count('_') == 0:
        return underscore_str

    for i in range(len(underscore_str)):
        if not underscoring and underscore_str[i] == '_':
            underscoring = True
        elif underscoring and underscore_str[i] != '_':
            underscoring = False
            temp += underscore_str[i].upper()
        elif not underscoring and underscore_str[i] != '_':
            temp += underscore_str[i].lower()

    camelcase_str = temp[0].lower() + temp[1:]

    return camelcase_str

# underscore_str1 = "to_camel_case"
# print(to_camel_case(underscore_str1))
# underscore_str2 = "__EXAMPLE__NAME__"
# print(to_camel_case(underscore_str2))
# underscore_str3 = "alreadyCamel"
# print(to_camel_case(underscore_str3))