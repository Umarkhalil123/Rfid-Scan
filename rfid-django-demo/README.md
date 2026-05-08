
## 1) What this demo does

- Uses Django to show attendance fields (`Card UID`, `Employee ID`, `Employee Name`, `Department`).
- JavaScript captures scanner input and auto-fills employee data if card mapping exists.
- If scanned UID is new, Save creates that employee-card mapping automatically.
- Saves attendance with `time_in` on first save and `time_out` on next save for same open record.
- Includes optional Python script `detect_reader.py` to list likely RFID devices.

## 2) Prerequisites

- Windows 10/11
- Python 3.10+ installed
- USB RFID reader 

## 3) Setup (first time)

Open terminal in this project folder and run:

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Open browser:

- http://127.0.0.1:8000/

## 4) How scanning works

1. Keep demo webpage active.
2. Tap card on RFID reader.
3. Reader "types" card UID into hidden buffer field.
4. Script copies UID into `Card UID` field automatically.
5. Click **Save Attendance** to store attendance.

## 5) Beginner test checklist

### A) Confirm hardware first

1. Open Notepad.
2. Tap RFID card.
3. Check if UID appears as typed text.
4. If yes, reader is keyboard wedge and demo should work.

### B) Test in web app

1. Open demo page.
2. Tap a card.
3. Confirm `Card UID` gets filled.
4. Add employee details if card is new.
5. Save (first save = Time In).
6. Scan and save again (second save = Time Out).
7. Confirm row appears in **Recent Scans**.

## 6)for daily Use
Open terminal in this project folder and run:

.venv\Scripts\activate
python manage.py runserver 0.0.0.0:8000


paste this command on terminal in project path
