# Scripts used to help you count image from the subfolder of /images

import os

def is_image_file(filename):
  """Checks if the filename has a common image extension."""
  extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]
  for ext in extensions:
    if filename.lower().endswith(ext):
      return True
  return False

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
    "SimpangBalaikotaTimur"
]

base_dir = "/media/pram/New Volume/Ikhwan/Lomba/Unity/Data Mining/cctv-crawler/images/"

# Print location options with numbers
for idx, a in enumerate(location):
  print(str(idx + 1) + ". " + a)

while True:
  try:
    i = int(input("Pilih lokasi (angka) atau ketik 'q' untuk keluar: ")) - 1  # Subtract 1 for zero-based indexing
    if 0 <= i < len(location):
      break
    else:
      print("Invalid input. Please choose a number between 1 and", len(location), "or 'q' to quit.")
  except ValueError:
    if input("Invalid input. Quit (q) or try again? ").lower() == 'q':
      exit()

if i == -1:  # Handle 'q' to quit
  exit()

simpang_dir = location[i]

directory = os.path.join(base_dir, simpang_dir)

num_images = 0
for filename in os.listdir(directory):
  if is_image_file(filename):
    num_images += 1

print(f"There are {num_images} images in '{simpang_dir}'.")
