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



