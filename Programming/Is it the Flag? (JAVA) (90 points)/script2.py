def java_string_hashcode(s):
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000


text = "0GHZXY"

text = list(text)

target = 1471587914


final_bin = ""


for i in range(0,64):
  final_bin = str(final_bin)
  number = bin(i)
  number = number.replace('0b','')

  final_bin = "{:06d}".format(int(number))
  
  final_bin = list(final_bin)
  
  if int(final_bin[0]) == 1:
    text[0] = text[0].lower()
  else:
    text[0] = text[0].upper()
    
  if int(final_bin[1]) == 1:
    text[1] = text[1].lower()
  else:
    text[1] = text[1].upper()
    
  if int(final_bin[2]) == 1:
    text[2] = text[2].lower()
  else:
    text[2] = text[2].upper()
    
  if int(final_bin[3]) == 1:
    text[3] = text[3].lower()
  else:
    text[3] = text[3].upper()
    
  if int(final_bin[4]) == 1:
    text[4] = text[4].lower()
  else:
    text[4] = text[4].upper()
    
  if int(final_bin[5]) == 1:
    text[5] = text[5].lower()
  else:
    text[5] = text[5].upper()
    
  final_text =  str(text[0]) + str(text[1]) + str(text[2]) + str(text[3]) + str(text[4]) + str(text[5])
  result = java_string_hashcode(final_text)
  
  if int(result) == target:
    print(final_text)
