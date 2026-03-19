# CS50 Week 2 


## String Length
A common problem within programming, and perhaps C more specifically, is to discover the length of a string. How could we implement this in code? Type code length.c in the terminal window and code as follows:

```
// Determines the length of a string

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for user's name
    string name = get_string("Name: ");

    // Count number of characters up until '\0' (aka NUL)
    int n = 0;
    while (name[n] != '\0')
    {
        n++;
    }
    printf("%i\n", n);
}
```
Notice that this code loops until the NUL character is found.




## string.c
```
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Input:  ");
    printf("Output ");
    for (int i = 0; i < strlen(s); i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");
}
```
This is not good design
because in the for loop everytime calculate **strlen(s)**

⬇

We can do
```

int main(void)
{
    string s = get_string("Input:  ");
    printf("Output ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");
}

```


## uppercase

```
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After:  ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        // If s[i] is lowercase
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            printf("%c", s[i] - 32);
        }
        //else if not lowercase
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
}

```
Output
``` 
$ ./uppercase
Before: David
After:  DAVID
```
⬇We can just use library
```
int main(void)
{
    string s = get_string("Before: ");
    printf("After:  ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", toupper(s[i]));
    }
    printf("\n");
}
```

## Command-Line Arguments

- We write 'main(void)', so there is no argument.
```
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("hello, %s\n", answer);
}
```
⬇
- We can add arguments
```
#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    printf("hello, %s\n", argv[1]);
}
```
Output:
```
$ ./greet David
hello, David
```
 --> argc: argument count
  == the number of command line arguments

**As a convention, I should add both argc and argv**

```
#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        printf("hello, %s\n", argv[1]);
    }
    else
    {
        printf("hello, world\n");
    }
}
```
- Notice that this program knows both argc, the number of command line arguments, and argv, which is an array of strings passed as arguments at the command line.

- Therefore, using the syntax of this program, executing ./greet David would result in the program saying hello, David.


## Exit Status

- 0: Success
- 1: Error

```
#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Missing command-line argument\n");
        return 1;
    }
    printf("hello, %s\n", argv[1]);
    return 0;
}


```

- If I type 'echo $?', I can see the exit status of the last run command
```
$ ./status David
hello, David
$ echo $
$
$ echo $?
0
```
--> it's success


```
$ ./status
Missing command-line argument
$ echo $?
1
```


## Summing up
In this lesson, you learned more details about compiling and how data is stored within a computer. Specifically, you learned…

Generally, how a compiler works.
How to debug your code using four methods.
How to utilize arrays within your code.
How arrays store data in back-to-back portions of memory.
How strings are simply arrays of characters.
How to interact with arrays in your code.
How command-line arguments can be passed to your programs.