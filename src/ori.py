# Crawler for CCTV
# MAM JogjaProv ATCS-Kota endpoint is: "https://mam.jogjaprov.go.id:1937/atcs-kota/"
# CCTV ATCS Jogja endpoint is: "https://cctvjss.jogjakota.go.id/atcs/" and it uses ".stream/chunklist_w128673376.m3u8" instead of ".stream/playlist.m3u8"
# When capturing from another endpoint category, you can change the path behind https://mam.jogjaprov.go.id:1937. Example https://mam.jogjaprov.go.id:1937/{another endpoint}
import cv2
import time
import os

count = 1
capturing = True
# # You can add more location in here
# location = [
#     "ATCS_Simpang_Wirosaban_View_Selatan",
#     "ATCS_Simpang_Basen",
#     "ATCS_Lampu_Merah_JlMentriSupeno",
#     "ATCS_Simpang_Demangan_View_Selatan",
#     "ATCS_Simpang_Gondomanan_View_Selatan",
#     "ATCS_Lampu_Merah_PasarGading2"
# ]
# for idx, a in enumerate(location):
#     print(str(idx + 1) + ". " + a)
# i = input("Pilih lokasi: ")
count_pic = int(input("Jumlah gambar: "))

directory = "husein"

# vcap = cv2.VideoCapture("https://cctvjss.jogjakota.go.id/atcs/" + location[int(i) - 1] + ".stream/playlist.m3u8")
vcap = cv2.VideoCapture("https://pelindung.bandung.go.id:3443/video/HIKSVISION/" + directory + ".m3u8")
fps = vcap.get(cv2.CAP_PROP_FPS)
wt = 1 / fps

# Create directory based on location
# directory = location[int(i) - 1]

complete_dir = 'images/' + directory
if not os.path.exists(complete_dir):
    os.makedirs(complete_dir)

while capturing:
    start_time = time.time()
    # Capture frame-by-frame
    ret, frame = vcap.read()

    if frame is not None:
        # Construct image path
        filename = os.path.join(complete_dir, str(time.time()) + ".jpg")
        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Save image every n seconds
        n = 1
        if count == n*fps:
            cv2.imwrite(filename, frame)
            print("Image: " + filename)
            count = 1
            count_pic -= 1
        else:
            count += 1
        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q') or count_pic == 0:
            break
        dt = time.time() - start_time
        if wt - dt > 0:
            time.sleep(wt - dt)
    else:
        print("Frame is None")
        # break

# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print("Video stop. Remaining images: " + str(count_pic))