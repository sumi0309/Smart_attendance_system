import os
import face_recognition as fr
def encode_faces(folder):
list_people_encoding = []
for filename in os.listdir(folder):
if '.jpg' in filename:
known_image = fr.load_image_file(f'{folder}{filename}')
known_encoding = fr.face_encodings(known_image)[0]
list_people_encoding.append((known_encoding, filename.replace(".jpg", "")))
return list_people_encoding
def find_target_face(target_image, target_encoding, currentImageFileName,
attendancePath, att_list):
face_location = fr.face_locations(target_image)
stDbDrivePath = '/content/drive/MyDrive/Student Data'
for person in encode_faces(stDbDrivePath + '/'):
encoded_face = person[0]
filename = person[1]
# tolerance_level depends on particular image
is_target_face = fr.compare_faces(encoded_face, target_encoding, tolerance = 0.51)
if face_location:
face_number = 0
for _ in face_location:
if is_target_face[face_number]:
label = filename
if label.find(".DS_Store"):
att_list.append(label)
face_number += 1
return face_number
