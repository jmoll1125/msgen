# msgen
June 9, 2023

msgen (**m**anu**s**cript **gen**erator) converts a series of plain text files into one large text file. To do so, it finds all the plain text files in a specified directory (set as `notes/`) and then writes the contents of each into a new text file (`msYYYYDDMMHHMM.txt`) in order from oldest to newest. It also prepends each file's text with the filename and date last modified. 

msgen is loosely based on the [HTML directory generator](#) I wrote the previous fall (hence the references to 8.15.21 and 9.16.21 in the date comment). I wrote it in September 2022 tp use when I published my notes book, which I did in January of 2023. ios-conv was born out of the same notes book project, but with a slighly different purpose (you can find out more about iosconv here). 
## Example output
Suppose there are three files in the `notes` directory, with the following attributes:

`a.txt` (last modified November 6, 2022 at 12:30 PM)  
`File 1`  
`b.txt` (last modified February 3, 2023 at 4:30 PM)  
`File 2`  
`c.txt` (last modified April 13, 2023 at 8:30 PM)  
`File 3`

If msgen were run as I write this, it would create `ms202306092247.txt` with the following contents:

```
$$$TITLE$$$a$$$TITLE$$$

$$$DATE$$$November 6, 2022 12:30 PM$$$DATE$$$

File 1



$$$TITLE$$$b$$$TITLE$$$

$$$DATE$$$February 3, 2023 4:30 PM$$$DATE$$$

File 2



$$$TITLE$$$c$$$TITLE$$$

$$$DATE$$$April 13, 2023 8:30 PM$$$DATE$$$

File 3
```
## Versions
msgen6 is the main version I developed for work on the notes book. Ny notes were all written in Microsoft Notepad and saved with either the "ANSI" (cp1252) or "Unicode" (UTF-16) encoding. msgen6 will read either and save the output in UTF-8 format. If you want to use msgen6 to read plain text files with a different encoding, you might need to edit the pertinent sections of the script. 
When I wrote ios-conv I updated msgen to msgen7. That version is meant to be used alongside ios-conv and so it is presented in that repository instead.

Previous versions of msgen from its development can be found in this repo's `development` subdirectory.
## Modifications
You can modify any aspect of `msgen` to suit your needs. The `dateformat` function at the very top of the program will change the way the date appears in the output file between the `$$$DATE$$$` blocks. Changing the `search_dir` variable will alter which directory msgen searches. 
