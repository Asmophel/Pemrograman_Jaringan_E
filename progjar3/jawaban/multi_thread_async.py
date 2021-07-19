from library import download_bc_gambar,get_url_list
import time
import datetime
import concurrent.futures

TARGET_IP = '255.255.255.255'
TARGET_PORT = 5005


def download_bc_semua():
    texec = dict()
    urls = get_url_list()
    status_task = dict()
    task = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    catat_awal = datetime.datetime.now()
    for k in urls:
        print(f"mendownload {urls[k]}")
        waktu = time.time()
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download dan broadcast gambar secara multithread
        texec[k] = task.submit(download_bc_gambar, urls[k],True, TARGET_IP, TARGET_PORT)

    #setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan memanggil result
    for k in urls:
        status_task[k]=texec[k].result()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("hasil task yang dijalankan")
    print(status_task)


#fungsi download_bc_gambar akan dijalankan secara multithreading

if __name__=='__main__':
    download_bc_semua()