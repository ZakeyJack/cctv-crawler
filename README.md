# CCTV Crawler

Simple CCTV Crawler for Jogja ATCS CCTV

## Installation

To install this crawler, follow the required steps below:

1. Clone the repository:

```
git clone https://github.com/prammmoe/cctv-crawler.git
```

2. Install cv2

```
pip install opencv-python
```

3. Run the script using (run from src)

```
python main.py
```

or when running from parent directory:

```
python src/main.py
```

## Documentations

### Locations

For the locations code below:

```
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
    "Warungboto1",
    "Simpang_KolSugiono2",
    "SimpangPasarTeloUtara",
    "KMNol",
    "BPK",
    "ViewSimpangTugu",
    "ViewBukitKlangon",
    "ViewAlunAlunKidul",
    "ViewBaronTimur",
    "ViewSambisari",
    "Juadi",
    "SimpangAtmosukarto",
    "SimpangDeBritto",
    "Sajiono",
    "SimpangMandalakrida",
    "SimpangBasen",
    "Warungboto2",
    "Simpang_MenteriSupeno2",
    "MargoUtomo_SelatanOlive",
    "MargoUtomo_GowonganLor",
    "MargoUtomo_WismaRatih",
    "SimpangGambiranBarat",
    "SimpangRejowinangunTimur",
    "Simpang_SugengJeroni2",
    "MargoUtomo_TokoCatWahyu",
    "SimpangBalaikota",
    "AhmadJazuli",
    "FMNoto",
    "SimpangAmongrogoTimur",
    "ParkiranNgabean",
    "SimpangGambiranTimur",
    "Jlagran",
    "SimpangPatangpuluhan",
    "SimpangBorobudurPlaza",
    "SimpangMelia",
    "Simpang_MenteriSupeno1",
    "Simpang_SugengJeroni1",
    "YosSudarso",
    "Terban",
    "SimpangBausasran",
    "Pingit",
    "MargoUtomo_WijayaBaruTravel",
    "Simpang_PasarGading2",
    "SimpangJatikencana",
    "KyaiMojo1",
    "SimpangGaleriaTImurSelatan"
]
```

Locations above is related from where you used the endpoint, so always refers to these sites:

1. https://mam.jogjaprov.go.id
2. https://cctvjss.jogjakota.go.id

The naming convention of the location can be random, you can try it by using snake case or camel case as shown above.

You can add more specific location by adding it into the list. Some locations are disabled for crawling, but you can try your luck.

### Pathing

Image directory will automatically made when the code finish running and collecting image. The directory saving the file is in images folder and the location selected will be the subfolder.

Complete structure:

    .
    ├── images
    │   ├──
    │   {location}              # Image folder
    │   └──
    │   {image files}
    ├── src                     # Source files
    │   └──
    │   main.py                 # main script
    ├── .gitignore
    └── README.md

### Endpoint

1. MAM Jogjaprov Endpoint

```
https://mam.jogjaprov.go.id:1937/{cctv-category}
```

For the CCTV Category, you can change based what shown on the website https://mam.jogjaprov.go.id/cctvs

We suggest just using two endpoint: /atcs/ and /atcs-kota/

2. CCTV Jogjakota Endpoint

```
https://cctvjss.jogjakota.go.id/atcs/
```

For the CCTV endpoint, we only used /atcs/ as referred from https://cctv.jogjakota.go.id/
