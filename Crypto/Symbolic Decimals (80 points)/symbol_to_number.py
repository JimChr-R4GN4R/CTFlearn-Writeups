text = "^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%"

text = text.replace('!','1').replace('@','2').replace('#','3').replace('$','4').replace('%','5').replace('^','6').replace('&','7').replace('*','8').replace('(','9').replace(')','0')

print(text)
