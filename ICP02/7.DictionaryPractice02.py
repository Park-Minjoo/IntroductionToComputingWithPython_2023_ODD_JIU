info = {'Name': 'Jessica', 'Age': 18, 'Address': 'Cikarang', 'Major': 'Information Technology'}
print("The following information is stored for", info['Name'], ":")
print(info.keys())
key = input("Enter the information you want to know: ")
print("The requested information:", info.get(key))
