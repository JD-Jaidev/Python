''' 
# general syntax

f'{value:format_specifier}'
------------------------------------------------------------------------------------------------------------------------------------------------
# f- strings - formatted string literal

name = 'Jaidev'
marks = 90
print(f'Your name is {name} and your mark is {mark}')
------------------------------------------------------------------------------------------------------------------------------------------------
# format specifiers : 

1. String - f'{num:s}'

2. Integer - f'{num:d}'

3. Binary - f'{num:b}' # converts to binary

4. Octal - f'{num:o}' # converts to octal

5. Hexadecimal lowercase - f'{num:x}' # converts to hexadecimal lower

6. Hexadecimal uppercase - f'{num:X}' # converts to hexadecimal upper

7. Floating point - f'{num:f}' # default upto 6 decimal places

8. Fixed decimal places - f'{num:.2f}' # if suppose num = 499.999 , >>> 500.00

                          f'{num:.3f}' # if suppose num = 499.999 , >>> 499.999

9. Scientific notation (e) - f'{num:e}' # writes in the e form

10. Percentage - f'{num:.1%}' # automatically coverts to percentage

11. Width specifier - f'{num:5}' # gives leading spaces, suppose if num = 25 , >>>_____25

13. Left alignment - f'{num:<}' # left aligned

14. Right alignment - f'{num:>}' # right aligned

15. Center alignment - f'{num:^}' # center aligned

16. Fill character - f'{name:*^10}' # fills specific character in the center with the specified spaces

                    suppose name = 'Jai'
                    print(f'|{name:*^10}|') , >>> |***Jai****|

17. Leading zeros - f'{num:05}' # the total characters should be according to the specified number with leading zeros

                    suppose num = 42
                    print(f'{num:05}') , >>> 00042

18. Thousands separator - f'{num:,}'

                    suppose num = 123456789
                    print(f'{num:,}') , >>> 123,456,789

19. Under score separator - f'{num:_}'

                    suppose num = 123456789
                    print(f'{num:_}') , >>> 123_456_789

20 . Sign specifier - f'{num:+}' # specifies sign according to given number input

21. Combining specifiers - 

                Eg -
                num = 1234.56789
                print(f'{num:>15,.2f}')
                >>>       1,234.57
------------------------------------------------------------------------------------------------------------------------------------------------
'''