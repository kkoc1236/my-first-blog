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
print(listlize)
for i in range(len(listlize)):

    line = listlize[i]
    result_1 = re.sub('["'"'"'\t\n=#/;\[\]"("")"""""?:$*/,}a-df-mo-rt-vx-zA-DF-MO-RT-VX-XZ]', ' ', str(line))
    # print(result_1)
    result = result_1.replace('-', ' ').replace('N', ' N ').replace('S', ' S ').replace('n', ' N ').replace('s',
                                                                                                            ' S ')
    #print(result)
    result_a = " ".join(result.split())
    result_b = result_a.split() #### ['00', '00.0', 'N', '00', '00.0', 'N']
    str_result_b = ' '.join(result_b)
    #print('aaa', str_result_b)
    result2 = re.sub('[a-zA-Z]', '', str_result_b)
    location_num = result2.split(' ')
    location_num1 = ' '.join(location_num)
    location_num2 = ' '.join(location_num1.split())
    location_num3 = location_num2.split()
    #print(location_num3)
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
            bool(is_number(str(location_num3[0])) and is_number(str(list_location_num_d[1])) and str(
                list_location_s[0]).replace('S', 'N') == 'N' and is_number(str(location_num3[2])) and is_number(
                str(list_location_num_d[3])) and str(list_location_s[1]).replace('W', 'E') == 'E')
            return True
        except IndexError:  # num을 float으로 변환할 수 없는 경우
            return False

    print(len(result_b))
    blank_list = [[], [], [], [], [], []]
    o = 0
    while o < len(result_b):
        o = o + 1
        read_list_w = result_b[-o+1:]
        str_result_b_w = ' '.join(read_list_w)
        print('aaa', str_result_b_w)
        result2_w = re.sub('[a-zA-Z]', '', str_result_b_w)
        print('bbb', result2_w)
        location_num_w = result2_w.split(' ')
        location_num1_w = ' '.join(location_num_w)
        location_num2_w = ' '.join(location_num1_w.split())
        location_num3_w = location_num2_w.split()
        # print(location_num3)
        list_location_num_w = list(map(float, location_num3_w))
        # print(list_location_num)
        list_location_num_d_w = list(round(x, 1) for x in list_location_num_w)  # 방향제외 좌표완성
        # print(list_location_num_d)

        location_s_w = re.sub('[0-9.-]', '', str_result_b_w)
        location_s2_w = ' '.join(location_s_w.split())
        list_location_s_w = location_s2_w.split()
        print(read_list_w)
        blank_list[o].append(read_list_w[-o+1])
        print('kkk', blank_list)

        def matchingcheck_w():
            try:
                bool(is_number(str(location_num3_w[0])) and is_number(str(list_location_num_d_w[1])) and str(
                    list_location_s_w[0]).replace('S', 'N') == 'N' and is_number(str(location_num3_w[2])) and is_number(
                    str(list_location_num_d_w[3])) and str(list_location_s_w[1]).replace('W', 'E') == 'E')
                return True
            except IndexError:
                return False
        print('xxx', matchingcheck_w())


        if matchingcheck_w():
            final_result = str(location_num3_w[0]).zfill(2) + '-' + str(list_location_num_d_w[1]).zfill(4) + \
                           list_location_s_w[
                               0] + ' ' + str(location_num3_w[2]).zfill(3) + '-' + str(list_location_num_d_w[3]).zfill(4) + \
                           list_location_s_w[1]
            print('ccc', final_result)

            Totallist.append(final_result)

            # print(final_result)

        # below code is checking for matching





    data = '\n'.join(Totallist)
print('zzz', data)






