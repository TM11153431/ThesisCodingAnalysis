# ThesisCodingAnalysis

Uses [CAT](https://cat.texifter.com/) (Coding Analysis Toolkit) generated CSV files to generate a visual representation of frequency of codes, with an option to see quotes related to that code.

The folder "Python" hosts `csvProcess.py`, which transforms a CAT CSV to a JSON which the visualisation uses
"Data" folder hosts `input.txt`, the input given to CAT (Lorem Ipsum text) and `LoremIpsum_1.csv`, the CSV output of CAT given random codes to lines in the input.
`index.html` incorporates `main.css` and `main.js`, which visualises code frequency through the colour of the button (with the exception of the code "none", which is black by default). onclick of the button `console.log`s the quotes given that code to the console.

[Click here for a demo of the output](https://tm11153431.github.io/ThesisCodingAnalysis/)
