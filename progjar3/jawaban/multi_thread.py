from library import download_bc_gambar,get_url_list
import time
import datetime
import threading

TARGET_IP = '255.255.255.255'
TARGET_PORT = 5005


def download_bc_semua():
    texec = dict()
    urls = get_url_list()

    catat_awal = datetime.datetime.now()
    for k in urls:
        print(f"mendownload {urls[k]}")
        waktu = time.time()
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multithread
        texec[k] = threading.Thread(target=download_bc_gambar, args=(urls[k],True,TARGET_IP, TARGET_PORT))
        texec[k].start()

    #setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan join
    for k in urls:
        texec[k].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


#fungsi download_bc_gambar akan dijalankan secara multithreading

if __name__=='__main__':
    download_bc_semua()