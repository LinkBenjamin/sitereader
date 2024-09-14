import requests
import re

from ragmodelapp import RagModelApp

def main():
    while True:
        choice = input("Enter the URL, or Q to quit: ")

        if choice == "Q":
            break
        else:
            response = requests.get(choice)
            if response.status_code == 200:
                rma = RagModelApp(re.sub(r'<.*?>', '', response.text))
                rma.prepare_chain()
                print(rma.invoke("Write a short summary of the content provided in Spanish."))
        
    print("Quit selected.  Closing app.")

if __name__ == "__main__":
    main()