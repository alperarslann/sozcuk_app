## a basic word application for computational linguistics class
We were introduced to the basics of python in this class. Our instructor wanted us to make use of what we learned in the class.
We were asked to assign a variable that is normally a static one. I turned it into dynamic one where you enter whatever you want and, it returns the result according to what you've entered.
To make it look like more of an app, I used TKinter for basic UI.

## specs:
1. returns whatever text you've entered.
2. returns the number of characters and also number of characters without white spaces.
3. it gets the input down to list, indicating all members of the sentece in double-quotes seperately. Additionally, if there are punctuations in between the words it doesn't count that punctuations as a member of the arguments indicated with double-quotes in the list.
4. and shows the word count and average number of characters per word.
## update V0.1
In Turkish language, it is thought to be two tenses: past and non-past tense. With this update, the app now can determine durative aspects (whether it is included in sentence or not)
Durative aspect in Turkish is -YOR, which is a suffix.

1. tells whether there is a durative verb in the sentence or not. (## Sürerlik görünüşü var / Sürerlik görünüşü yok.)
2. determines the durative verb in the sentence and shows them in a seperate list with "-yor" suffix is uppercased.
