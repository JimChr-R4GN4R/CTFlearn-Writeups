Where do robots find what pages are on a website?

Hint:
What does disallow tell a robot?

###################################################

At first I was trying to put CTFlearn{robots.txt} and other alternatives around it with no luck...

After some minutes I thinked to try it on CTFlearn's page.

https://ctflearn.com/robots.txt

There you will see this:

`Disallow: /70r3hnanldfspufdsoifnlds.html`

So then I visited this page: https://ctflearn.com/70r3hnanldfspufdsoifnlds.html

and found the flag!


Flag: CTFlearn{r0b0ts_4r3_th3_futur3}
