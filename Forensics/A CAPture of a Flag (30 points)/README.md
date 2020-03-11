This isn't what I had in mind, when I asked someone to capture a flag... can you help? 

You should check out WireShark. 

https://mega.nz/#!3WhAWKwR!1T9cw2srN2CeOQWeuCm0ZVXgwk-E2v-TrPsZ4HUQ_f4

#################################################################################

So I downloaded a .pcap file and opened it with wireshark.

Then I typed in the filter 'http' to check first http packets first.

And I found this unusual packet:

`247	2.270670	10.50.203.75	185.21.216.190	HTTP	504	GET /?msg=ZmxhZ3tBRmxhZ0luUENBUH0= HTTP/1.1`

This `ZmxhZ3tBRmxhZ0luUENBUH0=` is a base64 encoded text

So I used this https://www.base64decode.org/ and decoded it and got the flag!

Flag: flag{AFlagInPCAP}
