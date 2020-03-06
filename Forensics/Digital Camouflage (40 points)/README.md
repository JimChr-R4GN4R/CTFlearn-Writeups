

We need to gain access to some routers. 

Let's try and see if we can find the password in the captured network data: 

https://mega.nz/#!XDBDRAQD!4jRcJvAhMkaVaZCOT3z3zkyHre2KHfmkbCN5lYpiEoY 

Hint 1: It looks like someone logged in with their password earlier. 

Where would log in data be located in a network capture?

Hint 2: If you think you found the flag, but it doesn't work, consider that the data may be encrypted.

Credit: picoCTF 2017

###############################################################################

So the downloaded file was a .pcap file. So opened it with wireshark.

Then I typed on the filter <code>http</code> and after some packets I found this:

'=G]'8,\E_/q@@÷"
çG}(Ìw«CÉ:
'&Ruserid=hardawayn&<code>pswrd=UEFwZHNqUlRhZQ%3D%3D</code>

And then took the pswrd value and decoded it with url decoder (https://www.urldecoder.org/)

Then I took this result : <code>UEFwZHNqUlRhZQ==</code> 

which is base64

So I used this https://www.base64decode.org/ and decoded it.

It gave me this: <code>PApdsjRTae</code> 

Flag: CTFlearn{PApdsjRTae}
