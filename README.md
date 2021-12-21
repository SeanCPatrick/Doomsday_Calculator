# Overview
The Doomsday method is an algorithm devised by [John Conway](https://en.wikipedia.org/wiki/John_Horton_Conway). It's purpose was, when given a date, to see what day of the week that date falls on.

## The Rules

To start, let's set some rules that are required for this calculation to take place. 

1. Each day of the week must be placed in an index, with Sunday being 0, Saturday being 6, and the days in between having the corresponding numbers as well.
2. Every year, there are certain dates that will always fall on a certain day of the week called Doomsdays. Those dates are the following: 1/3 (1/4 in a leap year), 2/28 (2/29 in a leap year), 3/14, 4/4, 5/9, 6/6, 7/11, 8/8, 9/5, 10/10, 11/7, and 12/12. For the year 2021, those dates are all Sundays. 
3. Each century has an anchor day, determined by what these dates fall on in the first year of the century. In 1800, it was Friday, 1900, it was Wednesday. 2000, it was Tuesday. 2100, it will be Sunday. Remember the index I set out in rule 1? Each century thus has a corresponding number. Additionally, as the Gregorian calendar repeats itself every 400 years, this cycle is true ad infinitum.

## The Math

Let's take John Conway's birthday, December 26th, 1937. As a date in the 1900s, the anchor day was Wednesday, so the counter starts off at 3. Taking the last two digits of the year, 37, we apply the following math.

>37 // 12 = 3

>37 % 12 = 1

>1 // 4 = 0

With the century code of 3 (corresponding to Wednesday) in mind, the sum of these numbers is 7. As one final calculation, 7 % 7 is 0, which means for the year 1937, the doomsdays are Sundays.

Knowing that 12/12 was a Sunday, that means John Conway was born on a Sunday.

![image](https://user-images.githubusercontent.com/86089535/146846364-78d31195-b73e-43d0-a901-bfd2df7099d8.png)

## Shortcomings and Challenges

Personally, there were two challenges with creating this program, regarding the limited range of years this method could be applied to, and the input method for the user.

Keeping in mind that the Gregorian calendar repeats itself every 400 years, I wanted to make it so that the user could get a day of the week for any date from year 0 to the year 9999. My initial solve was to code it like so:

>if fullyear[:2] % 4 == 2
>>counter += 5

>elif fullyear[:2] % 4 == 3
>>counter += 3

>elif fullyear[:2] % 4 == 0
>>counter += 2

>elif fullyear[:2] % 4 == 1
>>counter += 0

This would have replaced the code I wrote in lines 9 through 19, which is for determining the century code of the date input by the user. However, Python would not allow this because of a catch 22: the code "[:2]", in my novice understanding, can only be applied to strings, while the code "% 4" can only be applied to integers.

Another challenge I had was determining the best input method for the user. There was a point where I wanted the date to be one string, then split it into a list separated by slashes or dashes, and pop each item in the list to each be their own objects, but I ultimately decided this was the simpler and more elegant solution. Besides, slash, dash, or enter, it's the same number of keystrokes regardless.

For more information on how to do the Doomsday method, I liked [this video](https://youtu.be/714LTMNJy5M) a lot. If you want to get into the exact details of the math, along with some helpful mnemonics, [the Wikipedia article for the Doomsday Method](https://en.wikipedia.org/wiki/Doomsday_rule) does a great job of that.
