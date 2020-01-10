import re
import xlwt


if __name__=='__main__':
    with open("PressurePushTimeArriveTest_2020-01-10_14_11_49.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    lines1 = []
    lines2 = []
    for i, line in enumerate(lines):
        if re.search(r'成功', line):
            pattern1 = re.compile(r'第 \d*')
            # print(pattern1.findall(line)[0].split(' ')[1])
            pattern2 = re.compile(r'是：\d*')
            # print(pattern2.findall(line)[0].split('：')[1])
            lines1.append(pattern1.findall(line)[0].split(' ')[1] + ' ' + pattern2.findall(line)[0].split('：')[1] + '\n')

        if re.search(r'到达', line):
            pattern1 = re.compile(r'第 \d*')
            # print(pattern1.findall(line)[0].split(' ')[1])
            pattern2 = re.compile(r'是：\d*')
            # print(pattern2.findall(line)[0].split('：')[1])
            lines2.append(pattern1.findall(line)[0].split(' ')[1] + ' ' + pattern2.findall(line)[0].split('：')[1] + '\n')

    fl = open('send.txt', 'w')
    for ii in lines1:
        fl.write(ii)
    fl.close()

    f2 = open('receive.txt', 'w')
    for ii in lines2:
        f2.write(ii)
    f2.close()

    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('test')

    worksheet.write(0, 0, 'num')
    worksheet.write(0, 1, 'time')

    sendFile =  open("send.txt", "r")
    receiveFile =  open("receive.txt", "r")
    
    index = 1
    missing = []
    while True: 
        receiveLine = receiveFile.readline()
        read = True
        if len(missing) > 0:
            for item in missing:
                if (receiveLine and receiveLine.strip().split(" ")[0] == item.strip().split(" ")[0]):
                    sendLine = item
                    print("find missing: ", item)
                    missing.remove(item)
                    read = False
                    break

        if read:
            sendLine = sendFile.readline()
            

        if sendLine and receiveLine:
            sendArray = sendLine.strip().split(" ")
            receiveArray = receiveLine.strip().split(" ")

            while sendArray[0] != receiveArray[0]:
                missing.append(sendLine)
                sendLine = sendFile.readline()
                sendArray = sendLine.strip().split(" ")

            print(sendArray[0], receiveArray[0])
            worksheet.write(index, 0, int(sendArray[0]))
            worksheet.write(index, 1, int(receiveArray[1]) - int(sendArray[1]))

            index = index + 1
        else:
            break
    
    workbook.save("arrive_test.xls")
    print("missing " + str(len(missing)) + " elements")
    print("missing elements are: ", missing)