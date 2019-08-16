from django.shortcuts import render
import re



def home(request):
    return render(request, 'blog/sky_gps.html')


def sky_gps(request):
    fulltextarea = request.POST['fulltextarea']
    listlize = fulltextarea.split('\r\n')
    listlize2 = [x for x in listlize if x]
    #print(listlize2)

    f_list = []
    Filteredlist = []
    Totallist = []

    '''CLB 가 리스트 몇번째에 있는지를 찾는 인덱싱'''
    for i in range(30):
        list_line0 = listlize2[i].split(' ')
        if ' '.join(list_line0).find('CLB') >= 0:
            indexing_CLB = list_line0.index('CLB')
            break

    for i in range(len(listlize2)):
        line = listlize2[i]
        list_line = line.split(' ')
        if len(list_line) > 8:
            t_list = list_line[:indexing_CLB + 1]

            if len(t_list) is 3 and len(''.join(t_list)) > 11:  # 주어진 리스트 숫자가 딱 맞아 떨어지는 경우
                f_list.append(t_list)

            if len(t_list) > 3 and len(''.join(t_list)) > 12:  # 리스트 숫자가 많은경우.. 좀더 연구가 필요 할 것...
                latlon = t_list[1] + t_list[2]
                f2_list = [t_list[0], latlon, t_list[-1]]
                f_list.append(f2_list)

        else:
            Filteredlist.append(line)
            pass
    print(f_list)
    i = 0
    while True:
        numbering = str(int(i / 2) + 1)
        wp_name = ''.join(re.findall(r"\d*\.\d+|\d+|\w", f_list[i][0])) + ' ' + ''.join(
            re.findall(r"\d*\.\d+|\d+|\w", f_list[i + 1][0]))
        Lat = str(f_list[i][1].replace('N', '').replace('S', '-'))
        Lon = str(f_list[i + 1][1].replace('E', '').replace('W', '-'))
        Alt = str(f_list[i][2].replace('CLB', 'CL').replace('DSC', 'DS'))
        Totallist.append(' '.join([numbering, wp_name, Lat, Lon, Alt]))
        i += 2
        if f_list[i] is f_list[-2]:
            numbering = str(int(i / 2) + 1)
            wp_name = ''.join(re.findall(r"\d*\.\d+|\d+|\w", f_list[i][0])) + ' ' + ''.join(
                re.findall(r"\d*\.\d+|\d+|\w", f_list[i + 1][0]))
            Lat = str(f_list[i][1].replace('N', '').replace('S', '-'))
            Lon = str(f_list[i + 1][1].replace('E', '').replace('W', '-'))
            Alt = str(f_list[i][2].replace('CLB', 'CL').replace('DSC', 'DS'))
            Totallist.append(' '.join([numbering, wp_name, Lat, Lon, Alt]))
            i += 2
            break

        # print(f_list)





        else:
            pass
    #print(Totallist)

    data = '\n'.join(Totallist)
    Faillist_data = '\n'.join(Filteredlist)


    return render(request, 'blog/sky_gps.html', {'data': data, 'Filteredlist':Faillist_data})


'''
조건 1. CLB가 무조건 마지막에 배치되어 있어야 한다.
'''




