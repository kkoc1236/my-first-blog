from django.shortcuts import render
import re




def home(request):
    return render(request, 'blog/report.html')




def report(request):
    fulltextarea = request.POST['fulltextarea']
    listlize = fulltextarea.split('\r\n')

    #print(listlize)

    Faillist = []
    NoonReport = [['*DATE / TIME', ' '], ['*POSITION', ' '], ['COURSE', ' '], ['STEAMING TIME', ' '],
                  ['STEAMING DISTANCE', ' '], ['*SPEED', ' '], ['SLIP', ' '], ['SET RPM', ' '],
                  ['*OBS. RPM', ' '], ['WIND DIR', ' '], ['B/F', ' '], ['WAVE DIR', ' '], ['WAVE Ht', ' '],
                  ['SWELL DIR', ' '], ['SWELL Ht', ' '], ['*FUEL cons', ' '], ['DISEL cons', ' '],
                  ['GASS cons', ' '], ['ULS cons', ' '], ['*FUEL BROB', ' '], ['DISEL BROB', ' '],
                  ['GASS BROB', ' '], ['ULS BROB', ' ']]

    Index = {'DATETIMEGMT': 1001, 'REPORTDATETIME': 1006, 'TIMEATNOON': 1003, 'DATE': 1004, 'TIMEUTC': 1005, 'POSITIONDATE': 1007, 'NOONPOSITIONLATITUDELONGITUDE': 2001, 'POSITION': 2002, 'POSITIONATNOON': 2003, 'POS': 2004, 'NOONPOSITION': 2005, 'PRESENTCOURSEHEADING': 3001, 'COURSEDEG': 3002, 'GYROCOURSEATNOON': 3003, 'GYROSET': 3004, 'SETGYRO': 3005, 'SETGYROATNOON': 3006, 'COURSE': 3007, 'TIMELASTREPORT': 4001, 'REPORTDURATION': 4002, 'STEAMINGTIMEFROMLASTREPORT': 4003, 'STEAMINGDISTNMTIMEH': 4004, 'TIMESLR': 4005, 'DISTANCETRAVELEDSINCELASTREPORTDISTANCEREMAININGFORCURRENTTRANSITTOPLOCE': 5001, 'DISTLASTREPORT': 5002, 'DISTANCEOVERGROUND': 5003, 'STEAMINGDISTANCEFROMLASTREPORTOG': 5004, 'DISTSLR': 5005, 'STEAMINGDISTANCE': 5006, 'PRESENTSPEEDAVERAGESPEEDSINCELASTREPORT': 6001, 'SPEEDKTS': 6002, 'AVESPD': 6003, 'AVERAGESPEEDFROMLASTREPORTTOTHISNOON': 6004, 'SPEED': 6005, 'AVGSPDSLR': 6006, 'AVERAGESPEEDFROMLASTREPORTTOTHISNOONOG': 6007, 'SLIP': 7004, 'AVESLIPFROMLASTREPORT': 7002, 'AVERAGESLIPFROMLASTREPORT': 7003, 'SLIPSLR': 7005, 'SETRPM': 8002, 'SETTINGRPMAFTERTHISNOON': 8003, 'SETRPMAFTERTHISNOON': 8004, 'RPMMELOADSLIPSINCELASTREPORT': 9001, 'AVERAGERPM': 9006, 'AVERPM': 9003, 'AVERPMOFMAINENGINE': 9004, 'AVERAGERPMFROMLASTREPORTTOTHISNOON': 9005, 'AVGRPMSLR': 9007, 'PREVAILINGWINDDIRECTIONANDSPEEDBFSWELLSIRECTIONANDHEIGHTMTRS': 10001, 'WIND': 10002, 'WINDDIRECTION': 10003, 'WINDDIRECTIONTRUE': 10004, 'WINDDIRKTS': 10005, 'WINDDIRESE': 10006, 'WINDSPD': 11001, 'WINDSPEEDTRUE': 11002, 'WINDBF': 11003, 'WAVEDIRECTION': 12001, 'WINDSEADIRECTION': 12002, 'WAVEHEIGHTDIRM': 12003, 'WAVEHEIGHT': 13001, 'WAVEHGHT': 13002, 'WINDSEAHEIGHT': 13003, 'WAVEHEIGHTDIR': 13004, 'SEASHT': 13005, 'SWELLDIRECTIONTRUE': 14001, 'SWELLDIRECTION': 14002, 'SWELLDIR': 14003, 'SWELLHEIGHT': 15001, 'SWELLHT': 15002, 'HSFOCONSUMPTIONSINCELASTREPORTNOTINCLUDINGANYCONSUMPTIONFORBALLASTINGORDEBALLASTINGMT': 16001, 'MECONSUMPTIONIFOHSDOLSGOULSFUELMT': 16002, 'FOCONSUMPTIONOFMEFROMLASTREPORT': 16006, 'FOCONSUMPTIONOFMAINENGINE': 16005, 'MECONSUMPTION': 16007, 'MECONSUMPTIONHSFOLSGO': 16008, 'MECONSIFO': 16009, 'MDOORMGOCONSUMPTION': 17001, 'DOCONSUMPTIONOFMEFROMLASTREPORT': 17002, 'LSMGOCONSUMPTIONSINCELASTREPORTNOTINCLUDINGANYCONSUMPTIONFORBALLASTINGORDEBALLASTINGMT': 18001, 'GOCONSUMPTIONOFMEFROMLASTREPORT': 18003, 'MECONSLSMDO': 18004, 'ULSCONSUMPTIONOFMEFROMLASTREPORT': 19001, 'HSFOANDLSMGOROBMT': 20001, 'BROBMT': 20002, 'ROB': 20003, 'FOROB': 20004, 'FOROBATNOON': 20005, 'BROB': 20006, 'BROBMTHSFOLSGO': 20007, 'BROBIFO': 20008, 'MDOORMGOROBATNOON': 21001, 'DOROBATNOON': 21002, 'BROBMDO': 21003, 'BROBLSMDO': 21004, 'GOROB': 22001, 'GOROBATNOON': 22002, 'ULSROBATNOON': 23001}

    ori_index = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','' ,'' , '', '', '', '', '', '','' ,'' ,'' ,'' ,'' , '', '', '', '','' ,'' ,'' , '', '', '', '', '', '', '', '','' ,'' , '', '']

    for i in range(len(listlize)):
        line = listlize[i]
        line2 = line.replace('\n', '')
        list_noon = line2.split(':')
        print(list_noon[0])
        print(line)
        if len(list_noon) > 1:
            index = "".join(re.findall("[a-zA-Z]+", list_noon[0])).upper()

            # print(index)
            def TorF():
                try:
                    Index[index]
                    return True
                except KeyError:
                    return False

            if TorF():
                value = Index[index]
                #print(value)
                if 1000 < value < 2000:
                    # print(('DATE / TIME : '), ''.join(list_noon[1:]))
                    NoonReport[0][1] = ''.join(list_noon[1:])
                    ori_index[0] = list_noon[0]
                elif 2000 < value < 3000:  # 7) 단어 정수 범위 설정 (1000단위로)
                    NoonReport[1][1] = ''.join(list_noon[1:])  # 8) NoonReport[x][1] <<< x를 수정할것
                    ori_index[1] = list_noon[0] # 9) original index 가 들어감
                elif 3000 < value < 4000:
                    NoonReport[2][1] = ''.join(list_noon[1:])
                    ori_index[2] = list_noon[0]
                elif 4000 < value < 5000:
                    NoonReport[3][1] = ''.join(list_noon[1:])
                    ori_index[3] = list_noon[0]
                elif 5000 < value < 6000:
                    NoonReport[4][1] = ''.join(list_noon[1:])
                    ori_index[4] = list_noon[0]
                elif 6000 < value < 7000:
                    NoonReport[5][1] = ''.join(list_noon[1:])
                    ori_index[5] = list_noon[0]
                elif 7000 < value < 8000:
                    NoonReport[6][1] = ''.join(list_noon[1:])
                    ori_index[6] = list_noon[0]
                elif 8000 < value < 9000:
                    NoonReport[7][1] = ''.join(list_noon[1:])
                    ori_index[7] = list_noon[0]
                elif 9000 < value < 10000:
                    NoonReport[8][1] = ''.join(list_noon[1:])
                    ori_index[8] = list_noon[0]
                elif 10000 < value < 11000:
                    NoonReport[9][1] = ''.join(list_noon[1:])
                    ori_index[9] = list_noon[0]
                elif 11000 < value < 12000:
                    NoonReport[10][1] = ''.join(list_noon[1:])
                    ori_index[10] = list_noon[0]
                elif 12000 < value < 13000:
                    NoonReport[11][1] = ''.join(list_noon[1:])
                    ori_index[11] = list_noon[0]
                elif 13000 < value < 14000:
                    NoonReport[12][1] = ''.join(list_noon[1:])
                    ori_index[12] = list_noon[0]
                elif 14000 < value < 15000:
                    NoonReport[13][1] = ''.join(list_noon[1:])
                    ori_index[13] = list_noon[0]
                elif 15000 < value < 16000:
                    NoonReport[14][1] = ''.join(list_noon[1:])
                    ori_index[14] = list_noon[0]
                elif 16000 < value < 17000:
                    NoonReport[15][1] = ''.join(list_noon[1:])
                    ori_index[15] = list_noon[0]
                elif 17000 < value < 18000:
                    NoonReport[16][1] = ''.join(list_noon[1:])
                    ori_index[16] = list_noon[0]
                elif 18000 < value < 19000:
                    NoonReport[17][1] = ''.join(list_noon[1:])
                    ori_index[17] = list_noon[0]
                elif 19000 < value < 20000:
                    NoonReport[18][1] = ''.join(list_noon[1:])
                    ori_index[18] = list_noon[0]
                elif 20000 < value < 21000:
                    NoonReport[19][1] = ''.join(list_noon[1:])
                    ori_index[19] = list_noon[0]
                elif 21000 < value < 22000:
                    NoonReport[20][1] = ''.join(list_noon[1:])
                    ori_index[20] = list_noon[0]
                elif 22000 < value < 23000:
                    NoonReport[21][1] = ''.join(list_noon[1:])
                    ori_index[21] = list_noon[0]
                elif 23000 < value < 24000:
                    NoonReport[22][1] = ''.join(list_noon[1:])
                    ori_index[22] = list_noon[0]

            else:
                Faillist.append(line)


        else:
            Faillist.append(line)
            pass

    Faillist_data = '\n'.join(Faillist)

    shoot = {'date_index' : NoonReport[0][0], 'date_ori' : ori_index[0], 'date_data' : NoonReport[0][1],
             'position_index' : NoonReport[1][0], 'position_ori' : ori_index[1], 'position_data' : NoonReport[1][1],
             'course_index': NoonReport[2][0], 'course_ori': ori_index[2], 'course_data': NoonReport[2][1],
             'steamingtime_index': NoonReport[3][0], 'steamingtime_ori': ori_index[3], 'steamingtime_data': NoonReport[3][1],
             'steamingdistance_index': NoonReport[4][0], 'steamingdistance_ori': ori_index[4], 'steamingdistance_data': NoonReport[4][1],
             'speed_index': NoonReport[5][0], 'speed_ori': ori_index[5], 'speed_data': NoonReport[5][1],
             'slip_index': NoonReport[6][0], 'slip_ori': ori_index[6], 'slip_data': NoonReport[6][1],
             'setrpm_index': NoonReport[7][0], 'setrpm_ori': ori_index[7], 'setrpm_data': NoonReport[7][1],
             'obsrpm_index': NoonReport[8][0], 'obsrpm_ori': ori_index[8], 'obsrpm_data': NoonReport[8][1],
             'winddir_index': NoonReport[9][0], 'winddir_ori': ori_index[9], 'winddir_data': NoonReport[9][1],
             'bf_index': NoonReport[10][0], 'bf_ori': ori_index[10], 'bf_data': NoonReport[10][1],
             'wavedir_index': NoonReport[11][0], 'wavedir_ori': ori_index[11], 'wavedir_data': NoonReport[11][1],
             'waveht_index': NoonReport[12][0], 'waveht_ori': ori_index[12], 'waveht_data': NoonReport[12][1],
             'swelldir_index': NoonReport[13][0], 'swelldir_ori': ori_index[13], 'swelldir_data': NoonReport[13][1],
             'swellht_index': NoonReport[14][0], 'swellht_ori': ori_index[14], 'swellht_data': NoonReport[14][1],
             'fuelcons_index': NoonReport[15][0], 'fuelcons_ori': ori_index[15], 'fuelcons_data': NoonReport[15][1],
             'diselcons_index': NoonReport[16][0], 'diselcons_ori': ori_index[16], 'diselcons_data': NoonReport[16][1],
             'gasscons_index': NoonReport[17][0], 'gasscons_ori': ori_index[17], 'gasscons_data': NoonReport[17][1],
             'ulscons_index': NoonReport[18][0], 'ulscons_ori': ori_index[18], 'ulscons_data': NoonReport[18][1],
             'fuelbrob_index': NoonReport[19][0], 'fuelbrob_ori': ori_index[19], 'fuelbrob_data': NoonReport[19][1],
             'diselbrob_index': NoonReport[20][0], 'diselbrob_ori': ori_index[20], 'diselbrob_data': NoonReport[20][1],
             'gassbrob_index': NoonReport[21][0], 'gassbrob_ori': ori_index[21], 'gassbrob_data': NoonReport[21][1],
             'ulsbrob_index': NoonReport[22][0], 'ulsbrob_ori': ori_index[22], 'ulsbrob_data': NoonReport[22][1],
             'Faillist': Faillist_data}

    return render(request, 'blog/report.html', shoot)










