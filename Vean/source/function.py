from source.summary import *
import os

#---------------------------------------------------------------
def menu():
    os.system("cls")
    print(5*"=", "SELAMAT DATANG DI VEAN", 5*"=","\n")
    print("MENU")
    print("1. Melihat data")
    print("2. Menambah data baru")
    print("3. Mencari data")
    print("4. Mengupdate data")
    print("5. Menghapus data")
    print("6. Ringkasan data")
    print("7. Keluar dari program")
    do = input("Apa yang ingin anda lakukan ? (No. Menu) :  ")
    pilihan(do)

#---------------------------------------------------------------
def pilihan(do):
    os.system("cls")
    if do == "1":
        lihatData()
    elif do == "2":
        addData()
    elif do == "3":
        searchData()
    elif do == "4":
        updateData()
    elif do == "5":
        deleteData()
    elif do == "6":
        sumToTable()
    elif do == "7":
        keluar()
    else:
        print("\nMaaf, layanan tidak tersedia")
        print("\nTekan [Enter] untuk kembali ke menu")
        input()
        menu()


#---------------------------------------------------------------
def lihatData():
    os.system("cls")
    print("\n# ANDA DI DALAM MENU MELIHAT DATA #")
    print("\n"+" DATA SURVEI ".center(104,"=")+"\n")

    f = open("data\semuaData.txt", "r")

    lis = f.readlines()
    x = sorted(lis)

    if len(x) == 0:
        print("DATA MASIH KOSONG")
        print("TIDAK BISA MENAMPILKAN DATA")
    else:
        head()
        j = 1
        for i in x:
            i = i.rstrip("\n")
            i = i.split(",")
            no = str(j)+"."

            i[2] +=" Jam"
            i[3] +=" GB"
            i[4] +=" GB"

            print(no.ljust(3)+" | "+i[0].ljust(10)+" | "+ i[1].ljust(10)+" | "+i[2].ljust(11)+
            " | "+i[3].ljust(9)+" | "+i[4].ljust(8)+" | "+"Rp."+i[5].rjust(7)+" | "+
            "Rp."+i[6].rjust(8)+" | "+i[7].rjust(6)+" |",end="\n")

            j += 1
        
        keterangan()
    
    f.close()
    print("\nTekan [Enter] untuk kembali ke menu")
    input()
    menu()


#---------------------------------------------------------------
def addData():
    os.system("cls")
    print("\n# ANDA DI DALAM MENU MENAMBAH DATA BARU #")
    print("\n")

    print(" TAMBAH DATA SURVEI ".center(53,"="))
    print("\n")

    nama  = input("Nama Depan   : ")
    job   = input("Pekerjaan    : ")
    sTime = input("Gadget screen time (jam/hari) *hanya angka     : ")
    useD  = input("Penggunaan kuota data (GB/bulan) *hanya angka  : ")
    useW  = input("Penggunaan kuota WiFi (GB/bulan) *hanya angka  : ")
    costD = input("Biaya kuota data (Rp/bulan) *hanya angka       : ")
    costW = input("Biaya langganan WiFi (Rp/bulan) *hanya angka   : ")

    from random import randint
    iD = ""
    for i in range(3):
        x = randint(0,9)
        iD += str(x)

    if len(nama) == 0:
        nama="-"
    if len(job) == 0:
        job="-"
    if len(sTime) == 0:
        sTime="0"
    if len(useD) == 0:
        useD="0"
    if len(useW) == 0:
        useW="0"
    if len(costD) == 0:
        costD="0"
    if len(costW) == 0:
        costW="0"

    f = open("data\semuaData.txt", "a")
    f.writelines([nama.title()+","+job.title()+","+sTime+","+useD+","+useW+","+costD+","+costW+","+iD+"\n"])
    f.close()

    f = open("data\screenTime.txt", "a")
    f.writelines([sTime+"\n"])
    f.close()

    f = open("data\dataUsed.txt", "a")
    f.writelines([useD+"\n"])
    f.close()

    f = open("data\wifiUsed.txt", "a")
    f.writelines([useW+"\n"])
    f.close()

    f = open("data\costData.txt", "a")
    f.writelines([costD+"\n"])
    f.close()

    f = open("data\costWifi.txt", "a")
    f.writelines([costW+"\n"])
    f.close()

    print("\n")
    print("Data berhasil ditambahkan dengan ID:", iD)
    
    print("\nTekan [Enter] untuk kembali ke menu")
    input()
    menu()


#---------------------------------------------------------------
def searchData():
    os.system("cls")
    print("\n# ANDA DI DALAM MENU MENCARI DATA #")
    print("\n")

    print(" CARI DATA SURVEI ".center(53,"="))
    print("\n")

    f = open("data\semuaData.txt","r")
    lis = f.readlines()

    if len(lis) == 0:
        print("DATA MASIH KOSONG")
        print("PENCARIAN TIDAK DAPAT DILAKUKAN")
    else:
        print("MENU\n"+"1. Nama Depan\n"+"2. ID")
        pil = input("Cari data berdasarkan: ")
        if pil == "1":
            item = input("Masukan Nama Depan: ")
        elif pil == "2":
            item = input("Masukan ID: ")
        else:
            print("\nMaaf, layanan tidak tersedia")
            print("\nTekan [Enter] untuk kembali ke menu")
            input()
            menu()

        for i in lis:
            if item.title() in i:
                print("\n")
                headNo()
                i = i.rstrip("\n")
                i = i.split(",")

                i[2] +=" Jam"
                i[3] +=" GB"
                i[4] +=" GB"

                print(i[0].ljust(10)+" | "+ i[1].ljust(10)+" | "+i[2].ljust(11)+
                " | "+i[3].ljust(9)+" | "+i[4].ljust(8)+" | "+"Rp."+i[5].rjust(7)+
                " | "+"Rp."+i[6].rjust(8)+" | "+i[7].rjust(6)+" |",end="")
                cek = True
                break
            else:
                cek = False
                continue

        if cek == False:
            print("\nMaaf, data yang anda cari tidak ada")
        f.close()

    print("\n")
    print("Tekan [Enter] untuk kembali ke menu")
    input()
    menu()
           

#---------------------------------------------------------------
def updateData():
    os.system("cls")
    print("\n# ANDA DI DALAM MENU MENGUPDATE DATA #")
    print("\n"+" UPDATE DATA SURVEI ".center(53,"=")+"\n")

    f = open("data\semuaData.txt","r")
    isi = f.readlines()

    if len(isi) == 0:
        print("DATA MASIH KOSONG")
        print("UPDATE DATA TIDAK DAPAT DILAKUKAN")
    else:
        print("MENU\n"+"1. Nama Depan\n"+"2. ID")
        pil = input("Cari data yang ingin di update berdasarkan: ")
        if pil == "1":
            item = input("Masukan Nama Depan: ")
            print("\n")
        elif pil == "2":
            item = input("Masukan ID: ")
            print("\n")
        else:
            print("\nMaaf, layanan tidak tersedia")
            print("\nTekan [Enter] untuk kembali ke menu")
            input()
            menu()

        index = 0
        for x in isi:
            x = x.rstrip("\n")
            xp = x.split(",")

            if item.title() in x:
                headNo()
                xp[2] +=" Jam"
                xp[3] +=" GB"
                xp[4] +=" GB"
                print(xp[0].ljust(10)+" | "+ xp[1].ljust(10)+" | "+xp[2].ljust(11)+
                " | "+xp[3].ljust(9)+" | "+xp[4].ljust(8)+" | "+"Rp."+xp[5].rjust(7)+
                " | "+"Rp."+xp[6].rjust(8)+" | "+xp[7].rjust(6)+" |",end="")

                print("\n")
                sure = input("Ingin update data ini (Y/N)?")

                if sure.upper() == "Y":
                    nb  = input("Nama Depan   : ")
                    jb  = input("Pekerjaan    : ")
                    stb = input("Gadget screen time (jam/hari) *hanya angka     : ")
                    udb = input("Penggunaan kuota data (GB/bulan) *hanya angka  : ")
                    uwb = input("Penggunaan kuota WiFi (GB/bulan) *hanya angka  : ")
                    cdb = input("Biaya kuota data (Rp/bulan) *hanya angka       : ")
                    cwb = input("Biaya langganan WiFi (Rp/bulan) *hanya angka   : ")

                    if len(nb) == 0:
                        nb="-"
                    if len(jb) == 0:
                        jb="-"
                    if len(stb) == 0:
                        stb="0"
                    if len(udb) == 0:
                        udb="0"
                    if len(uwb) == 0:
                        uwb="0"
                    if len(cdb) == 0:
                        cdb="0"
                    if len(cwb) == 0:
                        cwb="0"

                    xp[0] = nb.title()
                    xp[1] = jb.title()
                    xp[2] = stb
                    xp[3] = udb
                    xp[4] = uwb
                    xp[5] = cdb
                    xp[6] = cwb
                    xp[7]+= "\n"
                    iJoin = ",".join(xp)

                    isi[index] = iJoin

                    # Screen Time
                    f = open("data\screenTime.txt","r")
                    ubah = f.readlines()
                    x = ubah[index]
                    x = stb+"\n"
                    ubah[index] = x
                    f.close()
                    
                    f = open("data\screenTime.txt", "w")
                    ubah = f.writelines(ubah)
                    f.close()

                    # Data Used
                    f = open("data\dataUsed.txt","r")
                    ubah = f.readlines()
                    x = ubah[index]
                    x = udb+"\n"
                    ubah[index] = x
                    f.close()
                    
                    f = open("data\dataUsed.txt", "w")
                    ubah = f.writelines(ubah)
                    f.close()

                    # WiFi Used
                    f = open("data\wifiUsed.txt","r")
                    ubah = f.readlines()
                    x = ubah[index]
                    x = uwb+"\n"
                    ubah[index] = x
                    f.close()
                    
                    f = open("data\wifiUsed.txt", "w")
                    ubah = f.writelines(ubah)
                    f.close()

                    # Cost Data
                    f = open("data\costData.txt","r")
                    ubah = f.readlines()
                    x = ubah[index]
                    x = cdb+"\n"
                    ubah[index] = x
                    f.close()
                    
                    f = open("data\costData.txt", "w")
                    ubah = f.writelines(ubah)
                    f.close()

                    # Cost Wifi
                    f = open("data\costWifi.txt","r")
                    ubah = f.readlines()
                    x = ubah[index]
                    x = cwb+"\n"
                    ubah[index] = x
                    f.close()
                    
                    f = open("data\costWifi.txt", "w")
                    ubah = f.writelines(ubah)
                    f.close()

                    print("\nData berhasil di update")
                elif sure.upper() == "N":
                    cek = True
                    break
                else:
                    print("Maaf, kunci tidak valid")
            
                cek = True
                break
            else:
                cek = False
                index += 1
                continue
        
        if cek == False:
            print("Maaf, data yang anda cari tidak ada")

        f.close()

        f = open("data\semuaData.txt", "w")
        isi = f.writelines(isi)
        f.close()

    print("\nTekan [Enter] untuk kembali ke menu")
    input()
    menu()


#---------------------------------------------------------------
def deleteData():
    os.system("cls")
    print("\n# ANDA DI DALAM MENU MENGHAPUS DATA #")
    print("\n")

    print(" HAPUS DATA SURVEI ".center(53,"="))
    print("\n")

    f = open("data\semuaData.txt","r")
    isi = f.readlines()

    if len(isi) == 0:
        print("DATA MASIH KOSONG")
        print("HAPUS DATA TIDAK DAPAT DILAKUKAN")
    else:
        print("MENU\n"+"1. Nama Depan\n"+"2. ID")
        pil = input("Cari data yang ingin di hapus berdasarkan: ")
        if pil == "1":
            item = input("Masukan Nama Depan: ")
            print("\n")
        elif pil == "2":
            item = input("Masukan ID: ")
            print("\n")
        else:
            print("\nMaaf, layanan tidak tersedia")
            print("\nTekan [Enter] untuk kembali ke menu")
            input()
            menu()

        index = 0
        for x in isi:
            x = x.rstrip("\n")
            xp = x.split(",")
            if item.title() in x:
                headNo()
                xp[2] +=" Jam"
                xp[3] +=" GB"
                xp[4] +=" GB"
                print(xp[0].ljust(10)+" | "+ xp[1].ljust(10)+" | "+xp[2].ljust(11)+
                " | "+xp[3].ljust(9)+" | "+xp[4].ljust(8)+" | "+"Rp."+xp[5].rjust(7)+
                " | "+"Rp."+xp[6].rjust(8)+" | "+xp[7].rjust(6)+" |",end="")

                print("\n")
                cek = input("Ingin menghapus data ini (Y/N)? ")

                if cek.upper() == "Y":
                    del isi[index]

                    # Screen Time
                    f = open("data\screenTime.txt","r")
                    ubah = f.readlines()
                    del ubah[index]
                    f.close()
                    
                    f = open("data\screenTime.txt", "w")
                    ubah = f.writelines(ubah)
                    f.close()

                    # Data Used
                    f = open("data\dataUsed.txt","r")
                    ubah = f.readlines()
                    del ubah[index]
                    f.close()
                    
                    f = open("data\dataUsed.txt", "w")
                    ubah = f.writelines(ubah)
                    f.close()

                    # Wifi Used
                    f = open("data\wifiUsed.txt","r")
                    ubah = f.readlines()
                    del ubah[index]
                    f.close()
                    
                    f = open("data\wifiUsed.txt", "w")
                    ubah = f.writelines(ubah)
                    f.close()

                    # Cost Data
                    f = open("data\costData.txt","r")
                    ubah = f.readlines()
                    del ubah[index]
                    f.close()
                    
                    f = open("data\costData.txt", "w")
                    ubah = f.writelines(ubah)
                    f.close()

                    # Cost Wifi
                    f = open("data\costWifi.txt","r")
                    ubah = f.readlines()
                    del ubah[index]
                    f.close()
                    
                    f = open("data\costWifi.txt", "w")
                    ubah = f.writelines(ubah)
                    f.close()

                    print("Data berhasil dihapus")
                elif cek.upper() == "N":
                    break
                else:
                    print("Maaf, kunci tidak valid")

                cek = True
                break
            else:
                cek = False
                index += 1
                continue
        
        if cek == False:
            print("Maaf, data yang anda cari tidak ada")

        f.close()

        f = open("data\semuaData.txt", "w")
        isi = f.writelines(isi)
        f.close()

    print("\nTekan [Enter] untuk kembali ke menu")
    input()
    menu()


#---------------------------------------------------------------
def keluar():
    os.system("cls")
    print("\nTERIMA KASIH SUDAH MENGGUNAKAN VEAN\n")


#---------------------------------------------------------------
def head():
    no = "No"
    na = "Nama Depan"
    pk = "Pekerjaan"
    ku = "Penggunaan Kuota"
    by = "Biaya"
    dt = "Data"
    wf = "WiFi"
    sc = "Screen Time"
    Id = "ID"
        
        
    print(no.ljust(3)+" | "+na.center(10)+" | "+ pk.center(10)+" | "+
    sc.center(7)+" | "+ku.center(20)+" | "+by.center(24)+" | "+Id.center(6)+" |")

    print("| ".rjust(6)+"| ".rjust(13)+"| ".rjust(13)+"| ".rjust(14)+
    dt.center(10)+"| "+wf.center(8)+" |"+dt.center(12)+"| "+wf.center(12)+"| "+" |".rjust(8))

    print(104*"-")


#---------------------------------------------------------------
def headNo():
    na = "Nama"
    pk = "Pekerjaan"
    ku = "Penggunaan Kuota"
    by = "Biaya"
    dt = "Data"
    wf = "WiFi"
    sc = "Screen Time"
    Id = "ID"
        
        
    print(na.ljust(10)+" | "+ pk.center(10)+" | "+
    sc.center(7)+" | "+ku.center(20)+" | "+by.center(24)+" | "+Id.center(6)+" |")

    print("| ".rjust(13)+"| ".rjust(13)+"| ".rjust(14)+
    dt.center(10)+"| "+wf.center(8)+" | "+dt.center(11)+"| "+wf.center(12)+"| "+" |".rjust(8))

    print(98*"-")


#---------------------------------------------------------------
def keterangan():
    print("\n")
    print("Screen Time      : Durasi waktu seseorang terpapar layar gadget dalam 1 hari")
    print("Penggunaan Kuota : Penggunaan kuota data atau WiFi dalam 1 bulan")
    print("Biaya            : Pengeluaran biaya layanan internet data atau WiFi dalam 1 bulan")


#---------------------------------------------------------------
def sumToTable():
    os.system("cls")
    sumToData()
    print("\n# ANDA DI DALAM MENU RINGKASAN DATA #")
    print("\n"+" DATA SUMMARY ".center(98,"=")+"\n")
    f = open("data\dataSum.txt")

    lis = f.readlines()
    
    if len(lis) == 0:
        print("DATA MASIH KOSONG")
        print("TIDAK BISA MENAMPILKAN DATA")
    else:
        headSum()
        j = 1
        for i in lis:
            i = i.rstrip("\n")
            i = i.split(",")
            no = str(j)+"."
            
            i[1] +=" Jam"
            i[2] +=" GB"
            i[3] +=" GB"
            
            print(no.ljust(3)+" | "+i[0].ljust(13)+" | "+ i[1].rjust(11)+" | "+i[2].rjust(11)+
            " | "+i[3].rjust(11)+" | "+"Rp."+i[4].rjust(11)+" | "+
            "Rp."+i[5].rjust(12)+" |",end="\n")
            j += 1
        

        f = open("data\semuaData.txt")
        isi = f.readlines()

        total_resp = 0
        for i in isi:
            total_resp += 1
        
        f.close()

        print("\nJumlah Responden :", total_resp)
        keterangan()
        
    f.close()
    print("\nTekan [Enter] untuk kembali ke menu")
    input()
    menu()