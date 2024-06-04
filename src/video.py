import cv2
import os
import time

# Define video recording parameters
fps = 25  # Frames per second
duration = 30  # Recording duration in seconds

cntr = 0
capturing = True
# You can add more location in here
location = [
    "Gondomanan",
    "Wirobrajan",
    "Gramedia",
    "Jetis",
    "SimpangTerbanUtara",
    "Serangan",
    "SimpangDemanganUtara",
    "UKDW",
    "APMD",
    "SimpangTerbanTimur",
    "SimpangDemanganSelatan",
    "SimpangTerbanBarat",
    "SimpangBalaikotaTimur",
    "SimpangPingit1",
    "SimpangPingit3",
    "Warungboto1",
    "Simpang_KolSugiono2",
    "SimpangPasarTeloUtara",
    "KMNol",
    "BPK",
    "ViewSimpangTugu",
    "ViewBukitKlangon",
    "ViewAlunAlunKidul",
    "ViewBaronTimur",
    "ViewSambisari"
]
for idx, a in enumerate(location):
    print(str(idx + 1) + ". " + a)
i = input("Pilih lokasi: ")

print("Opening stream....")
while capturing: 
    vcap = cv2.VideoCapture(
        "https://mam.jogjaprov.go.id:1937/atcs-kota/"
        + location[int(i) - 1]
        + ".stream/playlist.m3u8"
    )
    if vcap.isOpened():
        print("Collected")

        # Create directory based on location
        directory = location[int(i) - 1]
        complete_dir = 'videos/' + directory
        if not os.path.exists(complete_dir):
            os.makedirs(complete_dir)

        # Define video writer
        filename = os.path.join(complete_dir, str(time.time()) + ".mp4")
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Adjust codec if needed (XVID is a common choice)
        writer = cv2.VideoWriter(filename, fourcc, fps, (int(vcap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

        start_time = time.time()
        while (time.time() - start_time) < duration:
            ret, frame = vcap.read()
            if ret:
                writer.write(frame)
                cntr += 1
            else:
                print("Error capturing frame")
                break

        writer.release()
        vcap.release()

        print(f"Finished recording video: {filename}")
        capturing = False

print(f"Successfully captured video for {duration} seconds")
