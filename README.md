# msgen
[//]: #written June 9, 2023

msgen (**m**anu**s**cript **gen**erator) converts a series of plain text files into one large text file. To do so, it finds all the plain text files in a specified directory (set as `notes/`) and then writes the contents of each into a new text file (`msYYYYDDMMHHMM.txt`) in order from oldest to newest. It also prepends each file's text with the filename and date last modified. 

## Example output
Suppose there are three files in the `notes` directory, with the following attributes:

`a.txt` (last modified November 6, 2022 at 12:30 PM)
`File 1`
`b.txt` (last modified February 3, 2023 at 4:30 PM)
`File 2`
`b.txt` (last modified April 13, 2023 at 8:30 PM)
`File 3`

If msgen were run as I write this, it would create `ms202306092247.txt` with the following contents:

```$$$TITLE$$$a$$$TITLE$$$

$$$DATE$$$November 6, 2022 12:30 PM$$$DATE$$$

File 1



$$$TITLE$$$b$$$TITLE$$$

$$$DATE$$$February 3, 2023 4:30 PM$$$DATE$$$

File 2



$$$TITLE$$$b$$$TITLE$$$

$$$DATE$$$April 13, 2023 8:30 PM$$$DATE$$$

File 3```


See `development` subdirectory for prerelease versions of msgen.
