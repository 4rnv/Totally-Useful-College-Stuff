import random

def sender():
  bin_data = input("Enter the Binary Data to be sent : ")
  try:
    bin_check = int(bin_data,2)
  except ValueError:
    print('Please make sure your number contains digits 0-1 only.')
    exit()
  data_size = len(bin_data)
  crc_temp = crc_generator()
  print(f"CRC Generator : {crc_temp}")
  len_crc = len(crc_temp)
  for i in range(len_crc -1):
    bin_data += '0'
  crc_data = xor(bin_data,crc_temp)
  print(f"CRC bits : {crc_data}")
  final_data = bin_data[:data_size] + crc_data
  print("Message to be transmitted :",final_data)
  print("How do you want to transmit the data. \n1. With Error.\n2. Without Error.")
  user = input("Select your choice : ")
  if (user == "1"):
    return twe(final_data,crc_temp)
  else :
    return twoe(final_data,crc_temp)

#CRC Gen
def crc_generator():
  degree = int(input("Enter the degree of Generator Polynomial : "))
  coefficient = []
  for i in range(degree,-1,-1):
    coeff = input(f"Enter the coefficients in Binary for x^{i} : ")
    coefficient.append(coeff)
  crc_gen = ''.join(coefficient)
  print(crc_gen)
  return crc_gen

#Binary X-OR
def xor(a,b):
  if len(a) < len(b):
    return a
  crc_size = len(b)
  temp = []
  for i in range(crc_size):
    if (a[i] == b[i]):
      temp.append('0')
    else:
      temp.append('1')
  ans = ''.join(temp)
  result = ans +a[crc_size:]
  result = result.lstrip('0')
  result = xor(result,b)
  result = result.zfill(crc_size - 1)
  return result

def twoe(wo_error,crc):
  return receiver(wo_error,crc)

def twe(w_error,crc):
  index = random.randint(0,len(w_error)-1)
  bit = '1' if w_error[index] == '0' else '0'
  corrupted_data = w_error[:index] + bit + w_error[index + 1:]
  print(f"Corrupted Data : {corrupted_data}")
  return receiver(corrupted_data,crc)
  
def receiver(data,crc):
  print(f"Transmitted message is : {data}")
  answer = xor(data,crc)
  answer = answer.zfill(len(crc))
  print(f"Answer = {answer}")
  if (answer == '0000'):
    print("Data is Transmitted without Error.")
  else :
    print("Data is Transmitted with Error.")
    
sender()