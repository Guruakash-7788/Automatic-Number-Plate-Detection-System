import easyocr
import cv2
from datetime import datetime
from datetime import date
import mysql.connector as sql
harcascade = "haarcascade_russian_plate_number.xml"
f_name = ""


cap = cv2.VideoCapture(0)

cap.set(3, 640) # width
cap.set(4, 480) #height
min_area = 500

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y+h, x:x+w]
            cv2.imshow("ROI", img_roi)
    cv2.imshow("Result", img)
    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        now = datetime.now()
        f_name = "plates/" + str(date.today()) + "_" + now.strftime("%H_%M_%S"+".jpg")
        cv2.imwrite(f_name, img_roi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results", img)
cap.release()


reader = easyocr.Reader(['en'])
output = reader.readtext(f_name)
text = output[0][-2]
print(f"License Plate: {text}")

"""
connect = sql.connect(host="localhost", user='root', password="your_password", database = "parking")
if connect.is_connected():
    print("SQL Connection established...")

sql = connect.cursor()
insert_data_query = "INSERT INTO parking (id,parking_code,vechile_cat_id,rate_id,slot_id,in_time) VALUES (%s,%s,%s,%s,%s,%s)"
sql.execute("SELECT id FROM parking ORDER BY id DESC LIMIT 1")
res = sql.fetchone()
g = res[0] + 11

a='1'
num=1701010896
z=0
data = (g,text,a,a,a,num,)
sql.execute(insert_data_query, data)
connect.commit()
sql.close()
connect.close()
print("License plate details stored in the sql database!!")
"""

