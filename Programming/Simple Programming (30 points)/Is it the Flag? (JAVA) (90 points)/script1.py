def java_string_hashcode(s):
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000

print(java_string_hashcode("000000"))


final_text = ""

text = "000000"

text = list(text)

for shift_0 in range(0,43):
  
  letter_0 = chr(ord(text[0]) + shift_0)

  if chr(ord(text[0]) + 1) == ":":
    letter_0 = "a"

  for shift_1 in range(0,43):
    letter_1 = chr(ord(text[1]) + shift_1)

    if chr(ord(text[1]) + 1) == ":":
      letter_1 = "a"

    for shift_2 in range(0,43):
      letter_2 = chr(ord(text[2]) + shift_2)

      if chr(ord(text[2]) + 1) == ":":
        letter_2 = "a"

      for shift_3 in range(0,43):
        letter_3 = chr(ord(text[3]) + shift_3)

        if chr(ord(text[3]) + 1) == ":":
          letter_3 = "a"

        for shift_4 in range(0,43):
          letter_4 = chr(ord(text[4]) + shift_4)

          if chr(ord(text[4]) + 1) == ":":
            letter_4 = "a"

          for shift_5 in range(0,43):
            letter_5 = chr(ord(text[5]) + shift_5)

            if chr(ord(text[5]) + 1) == ":":
              letter_5 = "a"
            
            final_text = letter_0+letter_1+letter_2+letter_3+letter_4+letter_5
            
            if int(java_string_hashcode(final_text.lower())) == 1472541258:
                print(final_text)