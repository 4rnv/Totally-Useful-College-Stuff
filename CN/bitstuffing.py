def check_5_1(data):
  y = 0
  for i in range(len(data)):
    # print(i)
    if data[i] == "1":
      y += 1
    elif data[i] == "0":
      y = 0
    if y == 6:
      return (True,i)
  return (False,i)

def sender(data):
  flag = "01111110"
  if check_5_1(data)[0]:
    extra = check_5_1(data)[1]
    data = data[:check_5_1(data)[1]] + "0" + data[check_5_1(data)[1]:]
    send = flag + data + flag
    print(f"Transmitted data: {flag + ' ' + data + ' ' + flag}")
    return (send,extra)
  else:
    send = flag + data + flag
    print(f"Transmitted data: {flag + ' ' + data + ' ' + flag}")
    return send

def receiver(data):
  if len(data) == 2:
    extra = data[1]
    data = data[0][8:]
    data = data[:extra] + data[extra+1:-8]
    return data
  else:
    return data[8:-8]

data = input("Enter your data:")
try:
    bin = int(data, 2)
except ValueError:
    print('Please make sure your number contains digits 0-1 only.')
    exit()
print("Received data (decrypted):",receiver(sender(data)))