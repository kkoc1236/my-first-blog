from django.shortcuts import render, get_object_or_404
import re
from xml.etree.ElementTree import parse





def is_number(num):
    try:
        float(num)
        return True #num을 float으로 변환할 수 있는 경우
    except ValueError: #num을 float으로 변환할 수 없는 경우
        return False


def home(request):
    return render(request, 'blog/xml_file_extractor.html')


def extracting(request):
    xmlfile = request.FILES['xmlfile']
    tree = parse(xmlfile)# reading xml file
    root = tree.getroot()

    RTPoint = root.findall("FutureRouteInfo/RouteInfo/ComparisonRPMs/ComparisonRPM/DRRoute/DrPoints/DrPoint/RTPoint")
    '''
    print(root.tag)
    print("break")
    print(root.attrib)
    print(RTPoint)

    for child in root: print(child.tag, child.attrib)
    '''
    Totallist = []

    for PointType in RTPoint:
        Typename = PointType.findtext("PointTypeName")
        Point_Lat = PointType.findtext("Point/Lat")
        Point_Lon = PointType.findtext("Point/Lon")
        NavTrack = PointType.findtext("NavTrack")
        if Typename == "WayPoint":
            if float(Point_Lat) >= 0:
                NS_Direction = "N"
            else:
                NS_Direction = "S"

            if float(Point_Lon) >= 0:
                EW_Direction = "E"
            else:
                EW_Direction = "W"

            GPS_Lat = abs((float(Point_Lat) / 5400) * 90)
            GPS_Lat_D = int(GPS_Lat)
            GPS_Lat_M = int((GPS_Lat - GPS_Lat_D) * 60)
            GPS_Lat_S = format(int((((GPS_Lat - GPS_Lat_D) * 60) - int((GPS_Lat - GPS_Lat_D) * 60)) * 10) * 0.1, '.1f')
            GPS_Lat_DMS = NavTrack + ' ' + str(GPS_Lat_D) + '-' + str(GPS_Lat_M + float(GPS_Lat_S)) + NS_Direction

            GPS_Lon = abs((float(Point_Lon) / 10800) * 180)
            GPS_Lon_D = int(GPS_Lon)
            GPS_Lon_M = int((GPS_Lon - GPS_Lon_D) * 60)
            GPS_Lon_S = format(int((((GPS_Lon - GPS_Lon_D) * 60) - int((GPS_Lon - GPS_Lon_D) * 60)) * 10) * 0.1, '.1f')
            GPS_Lon_DMS = str(GPS_Lon_D) + '-' + str(GPS_Lon_M + float(GPS_Lon_S)) + EW_Direction

            Totallist.append(GPS_Lat_DMS + ' ' + GPS_Lon_DMS)


        else:
            pass



        data = '\n'.join(Totallist)

    return render(request, 'blog/xml_file_extractor.html', {'data': data})








