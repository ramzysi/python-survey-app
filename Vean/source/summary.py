#---------------------------------------------------------------
def sumScreenTime():
    global totalST
    global maksST
    global minST
    global rataanST

    f = open("data/screenTime.txt")
    isi = f.readlines()
    index = 0
    for i in isi:
        i = i.rstrip("\n")
        i = int(i)
        isi[index] = i
        index += 1
    
    totalST = sum(isi)
    maksST = max(isi)
    minST = min(isi)
    rataanST = totalST/len(isi)
    # print(minST)
    # print(maksST)
    # print("%.2f" %rataanST)
    f.close()

#---------------------------------------------------------------
def sumDataUsed():
    global totalDU
    global maksDU
    global minDU
    global rataanDU

    f = open("data/dataUsed.txt")
    isi = f.readlines()
    index = 0
    for i in isi:
        i = i.rstrip("\n")
        i = int(i)
        isi[index] = i
        index += 1
    
    totalDU = sum(isi)
    maksDU = max(isi)
    minDU = min(isi)
    rataanDU = totalDU/len(isi)
    # print(minDU)
    # print(maksDU)
    # print("%.2f" %rataanDU)
    f.close()


#---------------------------------------------------------------
def sumWifiUsed():
    global totalWU
    global maksWU
    global minWU
    global rataanWU

    f = open("data/wifiUsed.txt")
    isi = f.readlines()
    index = 0
    for i in isi:
        i = i.rstrip("\n")
        i = int(i)
        isi[index] = i
        index += 1
    
    totalWU = sum(isi)
    maksWU = max(isi)
    minWU = min(isi)
    rataanWU = totalWU/len(isi)
    # print(minWU)
    # print(maksWU)
    # print("%.2f" %rataanWU)
    f.close()


#---------------------------------------------------------------
def sumCostData():
    global totalCD
    global maksCD
    global minCD
    global rataanCD

    f = open("data/costData.txt")
    isi = f.readlines()
    index = 0
    for i in isi:
        i = i.rstrip("\n")
        i = int(i)
        isi[index] = i
        index += 1
    
    totalCD = sum(isi)
    maksCD = max(isi)
    minCD = min(isi)
    rataanCD = totalCD/len(isi)
    # print(minCD)
    # print(maksCD)
    # print("%.2f" %rataanCD)
    f.close()


#---------------------------------------------------------------
def sumCostWifi():
    global totalCW
    global maksCW
    global minCW
    global rataanCW

    f = open("data/costWifi.txt")
    isi = f.readlines()
    index = 0
    for i in isi:
        i = i.rstrip("\n")
        i = int(i)
        isi[index] = i
        index += 1
    
    totalCW = sum(isi)
    maksCW = max(isi)
    minCW = min(isi)
    rataanCW = totalCW/len(isi)
    # print(minCW)
    # print(maksCW)
    # print("%.2f" %rataanCW)
    f.close()

#---------------------------------------------------------------
def sumToData():
    sumScreenTime()
    sumDataUsed()
    sumWifiUsed()
    sumCostData()
    sumCostWifi()
    
    f = open("data/dataSum.txt","w")
    f.writelines(["Terkecil"+","+str(minST)+","+str(minDU)+","+str(minWU)+","+str(minCD)+","+str(minCW)+"\n"])
    f.writelines(["Terbesar"+","+str(maksST)+","+str(maksDU)+","+str(maksWU)+","+str(maksCD)+","+str(maksCW)+"\n"])
    f.writelines(["Total"+","+str(totalST)+","+str(totalDU)+","+str(totalWU)+","+str(totalCD)+","+str(totalCW)+"\n"])
    f.writelines(["Rata-Rata"+","+str(round(rataanST, 2))+","+str(round(rataanDU, 2))+","+str(round(rataanWU, 2))+","+str(int(rataanCD))+","+str(int(rataanCW))+"\n"])
    f.close

#---------------------------------------------------------------
def headSum():
    no = "No"
    na = "Indikator"
    pk = "Pekerjaan"
    ku = "Penggunaan Kuota"
    by = "Biaya"
    dt = "Data"
    wf = "WiFi"
    sc = "Screen Time"
    Id = "ID"
        
        
    print(no.ljust(3)+" | "+na.ljust(13)+" | "+
    sc.center(7)+" |"+ku.center(26)+" | "+by.center(32)+" |")

    print("| ".rjust(6)+"| ".rjust(16)+"| ".rjust(14)+
    dt.center(11)+" | "+wf.center(11)+" |"+dt.center(16)+"| "+wf.center(15)+" |")

    print(98*"-")
