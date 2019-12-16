# Markdown Cheatsheet (title)
## Table of Contents
1. Headers
2. Simple text formatting
3. Lists
4. Links
5. Images


## 1. Headers
Headers are generated simply by number of hash signs (octothorps) you have before, such as the title or section title.

## 2. Simple Text Formatting

* Regular text can have a lot of things in it. here's a...

* ` single line of code `
* Regular text can even include `inline code`, as shown here.
```
block code (uses 3 backticks surrounding text, like here
new line here
```
* *italics* and _italics_ are nice
* **bold** and __bold__ are also good
* **_combined_** can be great
* ~~strikethrough~~ helps too
* Three dashes  make a nice gray-colored divider, but can't be kept close to text above them

---

## 3. Lists

#### Numbered
1. first
2. second

#### Bulleted
* this character is ok
+ that character is ok
- another that's ok, but all are part of same list

#### Checkboxes
* [ ] not done (note: for some reason, requires a list symbol)
* [x] done

#### sublists:
1. item
 1. subitem (notice that this line has a space before it)
  1. however, you can't have a subsubitem. tragic


* same goes for bullets (notice 2 lines to separate both lists)
 * this is a subitem

## 4. Links
* This [inline, renamed link](https://www.google.com) that looks nice.
* This [inline with hover title](https://www.google.com "google page") that looks nice.
* This [relative reference to repo file](../blob/master/LICENSE). NOTE: not a real link here.
* This [Reference-style link][1], but requires having links at the bottom of your ``*md`` file (links at bottom don't show up)

[1]: http://www.google.com

## 5. Images
Inline is pretty much the only way to include images, but you can at least put them on their own line, like so (with hover text):

![alt text](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png "HoverText")

what about making the image a reference as well?

this is a ![logo]

[logo]: https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png

## 6. Tables
Just remember that every column needs to have at least three dashes for the header cells, and every table MUST have header cells.

**Table 1**

| Tables        | Are           | Cool  |
| ------------- |-------------| -----|
| one | two | three |
| you can be lazy and have a table | that isn't really 100% aligned in text | but still looks good |

**Table 2**

| Name | Value   | Symbol |
| ---  | ---     | ---    |
| Pi   | 3.14    | $\pi$  |
| e    | 2.71828 | e      |
| ---  | ---     | ---    |
| ---  | ---     | ---    |



## 7. Basic Mathematics Concepts
* simple special characters: $\alpha$
* simple formula notation: $f(x) = x^2$
* matrix notation: $\begin{bmatrix}a & b\\c & d\end{bmatrix}$ ()

more information: [stack exchange](https://tex.stackexchange.com/questions/43444/how-to-typeset-a-matrix-with-mathjax)

## 8. Miscellaneous note on HTML tags
Certain things aren't possible in markdown, and thus require html to be achieved. Note, because the below text is centered inside an html tag, you'll need to follow html convention to do conventional markdown tasks
<div style="text-align: center"> <b> Centered, bold text. </b> </div>



### More information:
There's plenty of other things not covered here, so if you want more, just check out the following link:

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
