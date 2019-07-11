from django.shortcuts import render
import re



def is_number(num):
    try:
        float(num)
        return True #num을 float으로 변환할 수 있는 경우
    except ValueError: #num을 float으로 변환할 수 없는 경우
        return False


Totallist = []

fulltextarea = "09*	59.7'	S	077*	59.7'	E%n 06*	12.5'	N	094*	42.4E%n 06*	11.4'	N	097*	36.0'	E"

listlize = fulltextarea.split('%n')

    #pattern model
p_num = re.compile('\d')
p_hi = re.compile('-')
p_dot = re.compile('.')
p_ch = re.compile('[a-zA-Z]')

for i in range(len(listlize)):
    line = listlize[i]
    result_1 = re.sub('["'"'"'\t\n=#/;\[\]"("")"""""?:$*}a-df-mo-rt-vx-zA-DF-MO-RT-VX-XZ]', ' ', str(line))
    # print(result_1)
    result = result_1.replace('-', ' ').replace('N', ' N ').replace('S', ' S ').replace('n', ' N ').replace('s',
                                                                                                            ' S ')
    result_list = list(result)
    print(result)
    result_a = " ".join(result.split())
    result_b = result_a.split()
    print(result_b)
    result2 = re.sub('[a-zA-Z]', '', result)
    location_num = result2.split(' ')
    location_num1 = ' '.join(location_num)
    location_num2 = ' '.join(location_num1.split())
    location_num3 = location_num2.split()
    #print(location_num3)
    list_location_num = list(map(float, location_num3))
    # print(list_location_num)
    list_location_num_d = list(round(x, 1) for x in list_location_num)  # 방향제외 좌표완성
    # print(list_location_num_d)

    location_s = re.sub('[0-9.-]', '', result_1)
    location_s2 = ' '.join(location_s.split())
    list_location_s = location_s2.split()

    # print(list_location_s)
    # print(str(list_location_s[0]).isalpha())
    # print(is_number(str(location_num3[0])))

    def matchingcheck():

        try:
            bool(is_number(str(location_num3[0])) and is_number(str(list_location_num_d[1])) and str(
                list_location_s[0]).replace('S', 'N') == 'N' and is_number(str(location_num3[2])) and is_number(
                str(list_location_num_d[3])) and str(list_location_s[1]).replace('W', 'E') == 'E')
            return True
        except IndexError:  # num을 float으로 변환할 수 없는 경우
            return False


    if matchingcheck() and bool(is_number(str(location_num3[0])) and is_number(str(list_location_num_d[1])) and str(
            list_location_s[0]).replace('S', 'N') == 'N' and is_number(str(location_num3[2])) and is_number(
            str(list_location_num_d[3])) and str(list_location_s[1]).replace('W', 'E') == 'E'):
        final_result = str(location_num3[0]).zfill(2) + '-' + str(list_location_num_d[1]).zfill(4) + \
                       list_location_s[
                           0] + ' ' + str(location_num3[2]).zfill(3) + '-' + str(list_location_num_d[3]).zfill(4) + \
                       list_location_s[1]

        Totallist.append(final_result)

        # print(final_result)

    # below code is checking for matching

    else:
        Totallist.append(line + "<<------- Couldn't be converted")
        pass

    data = '\n'.join(Totallist)
print(data)






