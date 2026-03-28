```
int count_letters(string text)
{
    int letters = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            letters += 1;
        }
    }
    return letters;
}
```
- In this code, I wondered why 'n' doesn't need 'int'

Answer
Because int i = 0, n = strlen(word) is one single declaration.
The int at the front applies to everything after it, separated by commas. It's the same as writing:
```
c
int i = 0;
int n = strlen(word);
```
Just written in one line as a shortcut:
```
c
int i = 0, n = strlen(word);
```
The int is declared once and shared across both variables. Writing int 

int i = 0, int n = ... would be wrong — you only declare the type once per statement.

- The problem
```
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);


    // Coleman-Liau index
    double L = (letters / words)*100;
    double S = (sentences / words)*100;
    double index = 0.0588 * L - 0.296 * S - 15.8;

```


`letters`, `words`, and `sentences` are all `int`. So `letters / words` performs **integer division** — the decimal is thrown away **before** being stored as `double`.

For example:
```
letters = 50, words = 20
50 / 20 = 2    ← not 2.5, the .5 is lost
2 * 100 = 200.0  ← already wrong
```


Fix — cast to double before dividing:
```
cdouble L = ((double)letters / words) * 100;
double S = ((double)sentences / words) * 100;
```
Now letters is treated as a decimal number first, so the division keeps the fractional part.

- The final code
```
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt user's input
    string text = get_string("Input: ");

    // Count the number of letters, words, and sentences
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);


    // Coleman-Liau index
    double L = ((double)letters / words)*100;
    double S = ((double)sentences / words)*100;
    double index = 0.0588 * L - 0.296 * S - 15.8;

    // round the number
    int rounded = (int) round(index);
    // Print the grade level
    if (rounded < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (rounded >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", rounded);
    }

}


int count_letters(string text)
{
    int letters = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            letters += 1;
        }
    }
    return letters;
}

int count_words(string text)
{
    int words = 0;
    for (int i=0, n = strlen(text); i<n; i++)
    {
        if (isblank(text[i]))
        {
            words += 1;
        }
    }
    return words + 1;
}

int count_sentences(string text)
{
    int sentences = 0;
    for (int i=0, n=strlen(text); i<n; i++)
    {
        if (text[i] == '!' || text[i] == '?' || text[i] == '.')
        {
            sentences += 1;
        }
    }
    return sentences;
}




```