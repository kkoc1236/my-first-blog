from django.shortcuts import render
import re



def is_number(num):
    try:
        float(num)
        return True #num을 float으로 변환할 수 있는 경우
    except ValueError: #num을 float으로 변환할 수 없는 경우
        return False



fulltextarea = "[1st Waypoint : 30-07.45N 088-04.70W]%n[Navigation Type (1st - 2nd) : RL]%n[2nd Waypoint : 30-06.11N 088-02.55W]%n"

listlize = fulltextarea.split('%n')

    #pattern model
p_num = re.compile('\d')
p_hi = re.compile('-')
p_dot = re.compile('.')
p_ch = re.compile('[a-zA-Z]')
Totallist = []

for i in range(len(listlize)):
    line = listlize[i]
    result_1 = re.sub('["'"'"'\t\n=+/;\[\]"("")"""""?:$/,*}a-df-mo-rt-vx-zA-DF-MO-RT-VX-XZ]', ' ', str(line))
    # print(result_1)
    result = result_1.replace('-', ' ').replace('N', ' N ').replace('S', ' S ').replace('n', ' N ').replace('s',' S ').replace('W', ' W ').replace('E', ' E ').replace('w', ' W ').replace('e',' E ')
    # print(result_list)
    result_a = " ".join(result.split())
    result_f = result_a.split()  #### ['00', '00.0', 'N', '00', '00.0', 'N']
    print('bbb', result_f)
    result_b = result_f[-6:]
    str_result_b = ' '.join(result_b)
    print('aaa', result_b)
    result2 = re.sub('[a-zA-Z]', '', str_result_b)
    location_num = result2.split(' ')
    location_num1 = ' '.join(location_num)
    location_num2 = ' '.join(location_num1.split())
    location_num3 = location_num2.split()
    # print(location_num3)
    list_location_num = list(map(float, location_num3))
    # print(list_location_num)
    list_location_num_d = list(round(x, 1) for x in list_location_num)  # 방향제외 좌표완성
    # print(list_location_num_d)

    location_s = re.sub('[0-9.-]', '', str_result_b)
    location_s2 = ' '.join(location_s.split())
    list_location_s = location_s2.split()


    # print(list_location_s)
    # print(str(list_location_s[0]).isalpha())
    # print(is_number(str(location_num3[0])))

    def matchingcheck():

        try:
            bool(is_number(str(result_b[0])) and is_number(str(result_b[1])) and str(
                result_b[2]).replace('S', 'N') == 'N' and is_number(str(result_b[3])) and is_number(
                str(result_b[4])) and str(result_b[5]).replace('W', 'E') == 'E')
            return True
        except IndexError:  # num을 float으로 변환할 수 없는 경우
            return False

    print('xxx', matchingcheck())
    if matchingcheck() and bool(is_number(str(result_b[0])) and is_number(str(result_b[1])) and str(
                result_b[2]).replace('S', 'N') == 'N' and is_number(str(result_b[3])) and is_number(
                str(result_b[4])) and str(result_b[5]).replace('W', 'E') == 'E'):
        final_result = str(result_b[0]).zfill(2) + '-' + str(result_b[1]).zfill(4) + \
                       result_b[
                           2] + ' ' + str(result_b[3]).zfill(3) + '-' + str(result_b[4]).zfill(4) + \
                       result_b[5]

        Totallist.append(final_result)

        # print(final_result)

    # below code is checking for matching

    else:
        Totallist.append(line + "<<------- Couldn't be converted")
        pass





data = '\n'.join(Totallist)
print('zzz', data)






