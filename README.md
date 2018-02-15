Google Search
=============

Search Google for the currently selected text/word, or an input in Sublime Text 2/3.

This package adds: 

* A `Google Search` command to the context menu for the selected 
* A pallete command for the current selection(or word)
* A pallete command that will ask you what to search

## Install

If your using the [Sublime Package Manager][2] hold down Ctrl+Shift+P and type
`Package Control: Install Package`. Then search for `google-search` and hit return.

If your not using the package manager then go to your Sublime packages directory(Sublime Text/Packages) Then run this command `git clone https://github.com/nwjlyons/google-search.git`.

Or you can download the package as a zip file [https://github.com/nwjlyons/google-search/archive/master.zip][3] then copy it into your Sublime packages directory.


## Settings
```js
{
    "suffix": "", // will be after the query
    "prefix": "", // will be added before the query
    "default_browser": "", // chrome, firefox, more valid values here https://docs.python.org/2/library/webbrowser.html#webbrowser.register
    "domain": "https://www.google.com" // google domain to perform the search
}
```
You can edit the settings by going to Preferences -> Package Settings -> Google Search -> Settings - User

## Usage

Place the cursor inside a word or select some text and press `Ctrl+Shift+G`.

Context Menu
![context menu][4]

Command Pallette

![pallete][5]

![pallete][6]

  [1]: http://www.sublimetext.com
  [2]: https://sublime.wbond.net/
  [3]: https://github.com/nwjlyons/google-search/archive/master.zip
  [4]: http://i.stack.imgur.com/MJMC1.png
  [5]: http://puu.sh/9DyUy/b89bbcd3ce.png
  [6]: http://puu.sh/9Dz30/cd502986cd.png
