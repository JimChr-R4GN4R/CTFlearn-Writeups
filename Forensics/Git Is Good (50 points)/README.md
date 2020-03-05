The flag used to be there. But then I redacted it. 

Good Luck. 

https://mega.nz/#!3CwDFZpJ!Jjr55hfJQJ5-jspnyrnVtqBkMHGJrd6Nn_QqM7iXEuc

#############################################################

So downloaded the zip file and extracted it.

It was obvious that it is a git repository.

In there found a file called 'flag.txt' and it's content was <code>flag{REDACTED}</code>

So thinked to check it's logs...

Show first I executed this command when got inside the folder from terminal <code>git log</code> and got this:

///////////////////////////////////////////////////////////////////

commit d10f77c4e766705ab36c7f31dc47b0c5056666bb (HEAD -> master)
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:33:18 2016 -0400

    Edited files

commit 195dd65b9f5130d5f8a435c5995159d4d760741b
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:32:44 2016 -0400

    Edited files

commit 6e824db5ef3b0fa2eb2350f63a9f0fdd9cc7b0bf
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:32:11 2016 -0400

    edited files
    
///////////////////////////////////////////////////////////////////

So I searched on internet how to view the changes for each commit and found this:
https://www.thegeekstuff.com/2014/04/git-log/

Here it says that you can view the changes by writing:
<code>git log -p</code>

Then got this:

///////////////////////////////////////////////////////////////////

Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:33:18 2016 -0400

    Edited files

diff --git a/flag.txt b/flag.txt
index 8684e68..c5250d0 100644
--- a/flag.txt
+++ b/flag.txt
@@ -1 +1 @@
-flag{protect_your_git}
+flag{REDACTED}

commit 195dd65b9f5130d5f8a435c5995159d4d760741b
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:32:44 2016 -0400

    Edited files

diff --git a/flag.txt b/flag.txt
index c5250d0..8684e68 100644
--- a/flag.txt
+++ b/flag.txt
@@ -1 +1 @@
-flag{REDACTED}
+flag{protect_your_git}

///////////////////////////////////////////////////////////////////

Bingo!

Flag: flag{protect_your_git}
