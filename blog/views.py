from django.shortcuts import render
from .models import Post
from django.utils import timezone
import re

Totallist = []

def home(request):
    return render(request, 'blog/post_list.html')


def new_page(request):
    fulltextarea = request.GET['fulltextarea']
    listlize = fulltextarea.split('%n')

    # pattern model
    p_num = re.compile('\d')
    p_hi = re.compile('-')
    p_dot = re.compile('.')
    p_ch = re.compile('[a-zA-Z]')

    for i in range(len(listlize)):
        line = listlize[i]
        result_1 = re.sub('["'"'"'\t\n=#/\[\]"("")"""""?:$*}a-df-mo-rt-vx-zA-DF-MO-RT-VX-XZ]', ' ', str(line))
        # print(result_1)
        result = result_1.replace('-', ' ').replace('N', ' N ').replace('S', ' S ').replace('n', ' N ').replace('s',
                                                                                                                ' S ')
        result_list = list(result)
        # print(result_list)
        result2 = re.sub('[a-zA-Z]', '', result)
        location_num = result2.split(' ')
        location_num1 = ' '.join(location_num)
        location_num2 = ' '.join(location_num1.split())
        location_num3 = location_num2.split()
        # print(location_num3)
        list_location_num = list(map(float, location_num3))
        # print(list_location_num)
        list_location_num_d = list(round(x, 1) for x in list_location_num)  # 방향제외 좌표완성
        # print(list_location_num_d)

        location_s = re.sub('[0-9.-]', '', result_1)
        location_s2 = ' '.join(location_s.split())
        list_location_s = location_s2.split()
        # print(list_location_s)

        final_result = str(location_num3[0]).zfill(2) + '-' + str(list_location_num_d[1]).zfill(4) + list_location_s[
            0] + ' ' + str(location_num3[2]).zfill(3) + '-' + str(list_location_num_d[3]).zfill(4) + list_location_s[1]
        # print(final_result)

        # below code is checking for matching
        TorF = list(final_result)
        m = p_num.match(TorF[0]) and p_num.match(TorF[1]) and p_hi.match(TorF[2]) and p_num.match(
            TorF[3]) and p_num.match(
            TorF[4]) and p_dot.match(TorF[5]) and p_num.match(TorF[6]) and p_ch.match(TorF[7]) and \
            p_num.match(TorF[9]) and p_num.match(TorF[10]) and p_num.match(TorF[11]) and p_hi.match(
            TorF[12]) and p_num.match(TorF[13]) and p_num.match(TorF[14]) and p_dot.match(TorF[15]) and p_num.match(
            TorF[16]) and p_ch.match(TorF[17])

        if m:
            Totallist.append(final_result)
            #print(final_result)

        else :
            pass

    '\n'.join(Totallist)
    data = '<br />'.join(Totallist)
    return render(request, 'blog/Converted.html', {'data': data})







