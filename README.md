# Plachutta
Plachutta is an interpreter for [Three-Address Code](https://en.wikipedia.org/wiki/Three-address_code), implemented
with Python and ANTLR. It is intended to be a very simple interpreter for testing the intermediate output of a
multi-pass compiler.

## Regenerating the ANTLR Bits
`antlr4 -visitor -Dlanguage=Python3 TAC.g4`

## Running Tests
Testing is implemented with pytest - just run `pytest tests`. 

## FAQs

### What is a Plachutta?

It is the most interesting chess TACtic I know of. I learned about it from 
[this video from the incomparable Agadmator](https://www.youtube.com/watch?v=AOZTkfCwK_c).
If you prefer text, here's the [Wikipedia article on the Plachutta](https://en.wikipedia.org/wiki/Plachutta).
