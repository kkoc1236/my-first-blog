from django.shortcuts import render
import re




def is_number(num):
    try:
        float(num)
        return True #num을 float으로 변환할 수 있는 경우
    except ValueError: #num을 float으로 변환할 수 없는 경우
        return False


def home(request):
    return render(request, 'blog/post_list.html')


def new_page(request):
    fulltextarea = request.GET['fulltextarea']
    listlize = fulltextarea.split('\r\n')
    listlize2 = [x for x in listlize if x]


    Totallist = []
    Faillist = []

    for i in range(len(listlize2)):
        line = listlize2[i]
        result_1 = re.sub('["'"'"'\t\n=+/;\[\]"("")"""""?><_:$\\\/,*}a-df-mo-rt-vx-zA-DF-MO-RT-VX-XZ"属"]', ' ', str(line))
        # print(result_1)
        result = result_1.replace('-', ' ').replace('N', ' N ').replace('S', ' S ').replace('n', ' N ').replace('s', ' S ').replace('W', ' W ').replace('E', ' E ').replace('w', ' W ').replace('e',' E ')
        # print(result_list)
        result_a = " ".join(result.split())
        result_f = result_a.split()  #### ['00', '00.0', 'N', '00', '00.0', 'N']
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
        print(list_location_num_d)


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
            final_result = str(result_b[0]).zfill(2) + '-' + str(list_location_num_d[1]).zfill(4) + \
                           result_b[
                               2] + ' ' + str(result_b[3]).zfill(3) + '-' + str(list_location_num_d[3]).zfill(4) + \
                           result_b[5]

            Totallist.append(final_result)

            # print(final_result)


        else:
            Faillist.append(line + "<<------- Couldn't be converted")
            pass



        data = '\n'.join(Totallist)
        Faillist_data = '\n'.join(Faillist)

    return render(request, 'blog/post_list.html', {'data': data, 'Faillist':Faillist_data})

'''
1. 분이 60을 넘겼을시 도로 환산하는 계산식이 필요함
2. Coppy button
3. 뒤에서부터 읽기 [x:] 개선해 보기
4. 자동 GC 입력 (일정 NM을 넘겼을시)
5. result_1 = re.sub('["'"'"'\t\n=+/;\[\]"("")"""""?><_:$\\\/,*}a-df-mo-rt-vx-zA-DF-MO-RT-VX-XZ"属"]', ' ', str(line)) 부분을 
re.findall(r"[-+]?\d*\.\d+|\d+|E|W|N|S|e|w|n|s", 대상)로 대체 가능할듯..
6. 반본에서 if문에 break 를 사용하면 반복을 중간에 멈출 수 있다
'''






