Pedro was disappointed because he didn't speak Python well enough to capture some of the flags on CTFLearn. 

His plan for revenge was to create one in his native language (Java). 

The flag is a String of 6 alphanumeric characters. Capture it. 

https://mega.nz/#!SHp1xCAL!I9-Zy4kwu_JY019MiYZ6CzGey8sJ6UvqE-ML2idmkrs

#################################################################################################

From description we see that the flag has total 6 alphanumeric characters.

So the downloaded file was this java script:
```
public class IsItTheFlag {

public static boolean isFlag(String str) {
	return str.hashCode() == 1471587914 && str.toLowerCase().hashCode() == 1472541258;
}

public static void main(String[] args) {

String flag = "------";

if (isFlag(flag))
	System.out.println("You found it!");
else
	System.out.println("Try again :(");

	}
}
```



If we read cearfully the code, we will see that there is a flag variable which theoritically has our flag.

Then he sends it to `isFlag` function via `str` variable and he does this:
`return str.hashCode() == 1471587914 && str.toLowerCase().hashCode() == 1472541258;`



Flag: CTFlearn{0gHzxY}
