# Hangman-solver

This tool enables you to easily solve complex hangman puzzles:

## How to use

type the word out with "_" in the place of any unknown words

example: `g _ t _ _ b --> github`

If more than one words have the same letter combinations and length, all possible words will be displayed in a list

## Issues

 - This project uses the OS module to find the filepath of the text file, which relies on the names of the files being the same, this could mean that the program could collide with other text files if they has exactly the same file and directory names.
 - Many words in the text file are not english, so a more relevent text file must be found (possibly with words being ranked by most popular)

see [issues](https://github.com/Ollie-Edwards/Hangman-solver/issues) for any further details
