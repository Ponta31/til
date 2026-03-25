Problem to Solve
In the game of Scrabble, players create words to score points, and the number of points is the sum of the point values of each letter in the word.

![alt text](image.png)
For example, if we wanted to score the word “CODE”, we would note that the ‘C’ is worth 3 points, the ‘O’ is worth 1 point, the ‘D’ is worth 2 points, and the ‘E’ is worth 1 point. Summing these, we get that “CODE” is worth 7 points.

In a file called scrabble.c in a folder called scrabble, implement a program in C that determines the winner of a short Scrabble-like game. Your program should prompt for input twice: once for “Player 1” to input their word and once for “Player 2” to input their word. Then, depending on which player scores the most points, your program should either print “Player 1 wins!”, “Player 2 wins!”, or “Tie!” (in the event the two players score equal points).


I was writing like this first
```
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};


int compute_score(string word);

``` 
Why the prototype needs ;
In C, there are two different things that look similar:

```
c
int compute_score(string word);   // prototype (declaration)
int compute_score(string word)    // start of the actual definition
{
    ...
}
```
The semicolon tells C "I'm just announcing this function exists — the body comes later." Without it, C expects { to follow immediately, meaning you're trying to define the function right there.
Think of it like the difference between:

"I will give a speech tomorrow." ← just an announcement (;)
Actually standing up and giving the speech ← the real definition ({ ... })

```
int main(void)
{
    // Prompt the user for two words
    string word1 = get_string("Player1: ");
    string word2 = get_string("Player2: ");


    // Compute the score of each word
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Compare
    if (score1 > score2)
    {
        printf("Player 1 win\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 win\n");
    }
    else
    {
        printf("Tie\n");
    }

}

int compute_score(string word)
{

    // for i in string -> get score
    for (int i = 0; n = strlen(word); i < n; i++)
    {
        int score += POINTS[toupper(word[i]) - 64];
    }
    // return score
    return score;
}



```
Bug 5 — Wrong for loop syntax
```
c
for (int i = 0; n = strlen(word); i < n; i++)
//              ^^^^^^^^^^^^^^^^^ 
```
this is the condition slot, not init
A for loop has exactly 3 slots: init ; condition ; update. 

You've accidentally put 4 things. n must be declared in the init slot alongside i.
```
c
for (int i = 0, n = strlen(word); i < n; i++)
```


Bug 6 — Wrong variable declaration inside the loop

```
c
for (...)
{
    int score += POINTS[...];  // ← can't declare AND += at the same time
}
```
Two problems here:

- You can't use += on a variable at the moment you declare it with int
- Declaring score inside the loop means it resets every iteration and vanishes after the loop, so return score would fail


Bug 7 — Off-by-one in index calculation
```
c
POINTS[toupper(word[i]) - 64]
```

'A' in ASCII is 65, so 'A' - 64 = 1, but POINTS[0] is the score for A. You're always reading one slot too far.

Always use the character literal 'A' instead of a magic number — it's clearer and correct:
```
c
POINTS[toupper(word[i]) - 'A']   // 'A' - 'A' = 0 ✓
```
You also need a guard so non-letter characters (spaces, numbers, etc.) don't cause an out-of-bounds access:

```
if (isalpha(word[i]))
{
    score += POINTS[toupper(word[i]) - 'A'];
}
```
- ___isalpha()___ returns true only for a-z and A-Z. So the dangerous index calculation is never reached for anything else.

