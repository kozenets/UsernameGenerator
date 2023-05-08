# Usernames for Telegram generator

This repository contains a Python script that generates random nicknames by combining two lists of words. The user can choose the two lists to combine from a selection of predefined combinations. It also checks status (availability, cost) of nicknames on Fragment.com.

## Usage

1. Clone the repository to your local machine.
2. Make sure you have Python 3 installed.
3. Navigate to the repository directory in your terminal.
4. Run the following command: `python3 main.py`.
5. Follow the instructions to choose a combination of word lists.
6. The script will generate a list of nicknames and check their availability on a domain name registrar.

## Word lists

The script uses the following word lists:

- prefixes
- nouns
- profanity
- aggressive
- cute
- profession
- popular
- colors
- hobbies
- simple
- short
- qualities

## Combinations

The script can combine any two of the word lists above in the following combinations:

1. prefixes + nouns
2. prefixes + profanity
3. prefixes + aggressive
4. prefixes + cute
5. prefixes + profession
6. prefixes + popular
7. prefixes + qualities
8. prefixes + short
9. prefixes + hobbies
10. prefixes + simple
11. prefixes + colors
12. nouns + profanity
13. nouns + aggressive
14. nouns + cute
15. nouns + profession
16. nouns + popular
17. nouns + qualities
18. nouns + short
19. nouns + hobbies
20. nouns + simple
21. nouns + colors
22. profession + popular
23. profession + qualities
24. profession + short
25. profession + hobbies
26. profession + simple
27. profession + colors
28. popular + prefixes
29. popular + qualities
30. popular + short
31. popular + hobbies
32. popular + simple
33. popular + colors
34. profanity + aggressive
35. profanity + cute
36. profanity + profession
37. profanity + popular
38. profanity + qualities
39. profanity + short
40. profanity + hobbies
41. profanity + simple
42. profanity + colors
43. aggressive + cute
44. aggressive + profession
45. aggressive + popular
46. aggressive + qualities
47. aggressive + short
48. aggressive + hobbies
49. aggressive + simple
50. aggressive + colors
51. cute + profession
52. cute + popular
53. cute + qualities
54. cute + short
55. cute + hobbies
56. cute + simple
57. cute + colors
58. qualities + short
59. qualities + hobbies
60. qualities + simple
61. qualities + colors
62. short + hobbies
63. short + simple
64. short + colors
65. hobbies + simple
66. hobbies + colors
67. simple + colors

## Dependencies

The script requires the following dependencies:

- requests
- beautifulsoup4

You can install these dependencies using pip. For example, to install requests, run the following command:

```
pip install requests
pip install beautifulsoup4
```

This project is licensed under the MIT License.
