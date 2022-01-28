from src.main import start
from openpyxl import load_workbook
import time

book = load_workbook("book.xlsx")
sheet = book["data"]
A = sheet["A"]
B = sheet["B"]
C = sheet["C"]

def main():
    for i in range(len(A)):
        try:
            if B[i].value == None or A[i].value == "":
                continue
            start(username="", password="", description=B[i].value, path=C[i].value)
            if i%2==0:
                time.sleep(60*2)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()