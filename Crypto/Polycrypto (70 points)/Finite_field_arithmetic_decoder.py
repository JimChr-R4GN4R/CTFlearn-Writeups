import binascii


Polynomial = 'x^206 + x^205 + x^202 + x^201 + x^198 + x^197 + x^195 + x^194 + x^190 + x^189 + x^184 + x^182 + x^181 + x^178 + x^177 + x^176 + x^174 + x^173 + x^172 + x^171 + x^169 + x^168 + x^166 + x^165 + x^164 + x^157 + x^156 + x^150 + x^149 + x^147 + x^146 + x^142 + x^141 + x^140 + x^139 + x^136 + x^134 + x^133 + x^131 + x^130 + x^129 + x^126 + x^125 + x^123 + x^122 + x^121 + x^120 + x^118 + x^117 + x^115 + x^114 + x^112 + x^109 + x^108 + x^104 + x^102 + x^101 + x^96 + x^94 + x^93 + x^91 + x^90 + x^86 + x^85 + x^84 + x^81 + x^80 + x^78 + x^76 + x^75 + x^74 + x^73 + x^72 + x^69 + x^68 + x^66 + x^62 + x^61 + x^60 + x^57 + x^53 + x^52 + x^49 + x^48 + x^46 + x^44 + x^43 + x^42 + x^41 + x^40 + x^38 + x^37 + x^35 + x^33 + x^32 + x^29 + x^28 + x^21 + x^20 + x^14 + x^13 + x^11 + x^10 + x^6 + x^5 + x^4 + x^3 + x^2 + 1'.replace('+ 1','').replace('x^','').replace(' + ',',').split(',')



full_binary = '' # create full_binary variable
plus_one = '' # create plus_one variable

for i in range(0,int(Polynomial[0])): # Polynomial[0] is the highest number (in this example, the highest number is 206),                   #
                                      # so we want all the calculations with those binaries to have this amount of digits #

  full_binary += '0' # make full_binary the beginning binary number 000000000.... (256 digits)
  plus_one += '0' # make the beginning binary number for the +1 (cause we removed it from $Polymial)


full_binary = int(full_binary) # make the full_binary an integer (to add j's values in the next loop)

for j in Polynomial: # j = 206 , j = 205 , j = 202 , ....
  full_binary += pow(10,int(j)) # full_binary = full_binary + 10^206 + 10^205 + .... to add the ones at their right place

plus_one = int(plus_one) # Now the number is 0000000000... (256 digits)
plus_one += 1 # Now we will make it to be the number 1 in binary with the 256 digits


plus_one = str(plus_one)        # We need to make it string for the next command
full_binary = str(full_binary)  # We need to make it string for the next command

Final_Binary_Text = bin(int(full_binary,2) + int(plus_one,2)) # full_binary + 1 (with binary way)

print("Final Binary is : ",Final_Binary_Text) # The final binary text


Binary2Text = int(str(Final_Binary_Text), 2)           ## Convert Binary to text
Binary2Text = binascii.unhexlify('%x' % Binary2Text)   #

Binary2Text = str(Binary2Text) # Make it a string so I can remove b' and ' at the final result

print(Binary2Text.replace("b'","").replace("'","")) # Flag!
  
########## Useful sources for the script ##########
# https://beginnersbook.com/2018/03/python-program-to-add-two-binary-numbers/
# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
# https://en.wikipedia.org/wiki/Finite_field_arithmetic
