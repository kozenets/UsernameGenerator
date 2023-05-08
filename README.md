# Usernames for Telegram generator

This repository contains a Python script that generates random nicknames by combining two lists of words. The user can choose the two lists to combine from a selection of predefined combinations. It also checks status (availability, cost) of nicknames on Fragment.com.

## Usage

1. Clone the repository to your local machine.
2. Make sure you have Python 3 installed.
3. Navigate to the repository directory in your terminal.
4. Run the following command: `python3 nickname_generator.py`.
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

## Combinations

The script can combine any two of the word lists above in the following combinations:

- prefixes + nouns
- prefixes + profession
- prefixes + popular
- prefixes + profanity
- prefixes + aggressive
- prefixes + cute
- nouns + prefixes
- nouns + profession
- nouns + popular
- nouns + profanity
- nouns + aggressive
- nouns + cute
- profession + prefixes
- profession + nouns
- profession + popular
- profession + profanity
- profession + aggressive
- profession + cute
- popular + prefixes
- popular + nouns
- popular + profession
- popular + profanity
- popular + aggressive
- popular + cute
- profanity + prefixes
- profanity + nouns
- profanity + profession
- profanity + popular
- profanity + aggressive
- profanity + cute
- aggressive + prefixes
- aggressive + nouns
- aggressive + profession
- aggressive + popular
- aggressive + profanity
- aggressive + cute
- cute + prefixes
- cute + nouns
- cute + profession
- cute + popular
- cute + profanity
- cute + aggressive

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
