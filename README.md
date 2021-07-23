# parsingHLA-cGDM

convert HLA report file to SQL file which has cGDM HLA-TYPE schema 

## download
pip install -i https://test.pypi.org/simple/ parsingHLA-cGDM

## command
parsingHLA-cGDM -i INPUTDIR -o OUTPUT.sql --count identifier number

-i | required 
Input directory 

-o | Default: result_INPUTDIR.sql 
Output file name 

--count | Default: 1
Identifier number
