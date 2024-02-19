 
![pysimplegui_logo](https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png)        
        
![Downloads](http://pepy.tech/badge/pysimpleguiwx)
      
 ![Awesome Meter](https://img.shields.io/badge/Awesome_meter-1000-yellow.svg)  
         
 ![Python Version](https://img.shields.io/badge/Python-3.x-yellow.svg)        
        
      
[![PyPI Version](https://img.shields.io/pypi/v/pysimpleguiwx.svg?style=for-the-badge)](https://pypi.org/project/pysimpleguiwx/)         
                
        
# PySimpleGUIWx        

The WxPython port of PySimpleGUI

## Primary PySimpleGUI Documentation

To get instructions on how use PySimpleGUI's APIs, please reference the [main documentation](http://www.PySimpleGUI.org). 
This Readme is for information ***specific to*** the WxPython port of PySimpleGUI.


## Why Use PySimpleGUIWx Over The Other Ports?

PySimpleGUIWx brings the number of PySimpleGUI ports to 3.

Why use PySimpleGUIWx over PySimpleGUIQt PySimpleGUI (tkinter version)?  

There are a couple of easy reasons to use PySimpleGUIWx over PySimpleGUIQt. One is footprint.  PyInstaller EXE for PySimpleGUIWx is 9 MB, on Qt it's 240 MB.  Another is cool widgets.  

WxPython has some nice advanced widgets that will be offered though PySimpleGUIWx, hopefully sooner than later.

The System Tray feature works well with a feature set identical to PySimpleGUIQt.  If you are looking for a System Tray feature, PySimpleGUIWx is recommended over PySimpleGUIQt ; the primary reason being size of the WxPython framework versus the size of Qt.  They both give you very similar features.  They look and behave in an ***identical*** fashion when using PySimpleGUI.  That's the beauty of the PSG SDK, the function calls are the same for all implementations of PySimpleGUI.  The source code is highly portable between the GUI frameworks.

This simple list is another way of looking at the question....

1.  It's simple and easy to program GUIs
2.  You can move between the GUI frameworks tkinter, Qt and WxPython by changing a single line of code, the import statement.
3.  Get the same custom layout and access to the same widgets but in a simple, easy to use and understand interface.
4.  It's fun to program GUIs again


 ## Engineering Pre-Release   Version 0.13.0
 
 [Announcements of Latest Developments](https://github.com/MikeTheWatchGuy/PySimpleGUI/issues/142)        

Having trouble? Visit the [GitHub site ](http://www.PySimpleGUI.com) and log an Issue.
              
  
## What Works

Remember, these are Engineering Releases.  Not all features are complete, but generally speaking those that are marked as completed and working are working quite well.  It's not an "Engineering Quality".  The completed features are at about a Beta level.

### Ready to use

#### Elements

* Text
* Input Text
* Buttons including file/folder browse
* Input multiline
* Output multiline
* Output
* Columns
* Frames - except cannot set colors yet
* Progress Meters
* Checkbox
* Radio Button
* Combobox
* Spinner
* Vertical and Horizontal Separators


#### Features

* System Tray
* Debug Print
* Invisible/Visible Elements
* All Popups
* Check box
* Keyboard key events
* Mouse wheel events
* Multiple windows
* Read with timeout
* Background images
* One Line Progress Meter (tm)
* Auto-closing windows
* No titlebar windows
* Grab anywhere windows
* Alpha channel
* Window size
* Window disappear/reappear
* Get screen size
* Get window location
* Change window size
* Window move
* Window minimize
* Window maximize
* Window Disable
* Window Enable
* Window Hide
* Window UnHide
* Window Bring to front
* Look and Feel settings
* Default Icon
* Base64 Icons
* PEP8 bindings for all element methods and functions


It won't take long to poke at these and hit errors.  For example, the code to do Button Updates is not complete.  Most of the time you won't be doing this. 

Due to the small size of the development team, features may feel a little "thin" for a while.  The idea is to implement with enough depth that 80% of the uses are covered.  It's a multi-pass, iterative approach.  

If you, the reader, are having problems or have hit a spot where something is not yet implemented, then open an Issue.  They are often completed in a day.  This process of users pushing the boundaries is what drives the priorities for development.  It's "real world" kinds of problems that have made PySimpleGUI what it is today.

  
        
## SystemTray

This was the first fully functioning feature of PySimpleGUIWx.  Previously only the Qt port supported the System Tray.  Why use Wx?  The footprint is much much smaller.  An EXE file created using PyInstaller is 9 MB for PySimpleGUIWx, when using Qt it's 240 MB.

Now it's possible to "tack on" the System Tray to your PySimpleGUI application. 

If you're unable to upgrade to Qt but want the System Tray feature, then adding PySimpleGUIWx to your project may be the way to go.  

You can mix your System Tray's event loop with your normal Window event loop by adding a timeout to both your Window.Read call and your SystemTray.Read call.

### Source code compatibility

PySimpleGUIWx's System Tray feature has been tested against the same PySimpleGUIQt feature.  As long as you don't use features that are not yet supported you'll find your source code will run on either PySimpleGUIQt or PySimpleGUIWx by changing the import statement.  
 

## System Tray Design Pattern

Here is a design pattern you can use to get a jump-start.

This program will create a system tray icon and perform a blocking Read. 

```python
import PySimpleGUIWx as sg

tray = sg.SystemTray(menu= ['menu',['Open', ['&Save::KEY', '---', 'Issues', '!Disabled'], 'E&xit']],
                     filename=r'C:\Python\PycharmProjects\GooeyGUI\default_icon.ico')
tray.ShowMessage('My Message', 'The tray icon is up and runnning!')
while True:
    event = tray.Read()
    print(event)
    if event == 'Exit':
        break
```


## Menu Definitions

See the original, full documentation for PySimpleGUI to get an understanding of how menus are defined.  


## SystemTray Methods

### Read - Read the context menu or check for events

```python
def Read(timeout=None)
    '''  
 Reads the context menu  
 :param timeout: Optional.  Any value other than None indicates a non-blocking read
 :return:   String representing meny item chosen. None if nothing read.  
    '''
```
The `timeout` parameter specifies how long to wait for an event to take place.  If nothing happens within the timeout period, then a "timeout event" is returned.  These types of reads make it possible to run asynchronously.  To run non-blocked, specify `timeout=0`on the Read call (not yet supported).

Read returns the menu text, complete with key, for the menu item chosen.  If you specified `Open::key` as the menu entry, and the user clicked on `Open`, then you will receive the string `Open::key` upon completion of the Read.

#### Read special return values

In addition to Menu Items, the Read call can return several special values.    They include:

EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED - Tray icon was double clicked
EVENT_SYSTEM_TRAY_ICON_ACTIVATED - Tray icon was single clicked
EVENT_SYSTEM_TRAY_MESSAGE_CLICKED - a message balloon was clicked
TIMEOUT_KEY is returned if no events are available if the timeout value is set in the Read call


### ShowMessage

Just like Qt, you can create a pop-up message.  Unlike Qt, you cannot set your own custom icon in the message, at least you can't at the moment.

The preset `messageicon` values are:

    SYSTEM_TRAY_MESSAGE_ICON_INFORMATION 
    SYSTEM_TRAY_MESSAGE_ICON_WARNING
    SYSTEM_TRAY_MESSAGE_ICON_CRITICAL 
    SYSTEM_TRAY_MESSAGE_ICON_NOICON

```python
ShowMessage(title, message, filename=None, data=None, data_base64=None, messageicon=None, time=10000):  
    '''  
 Shows a balloon above icon in system tray  
 :param title:  Title shown in balloon  
 :param message: Message to be displayed  
 :param filename: Optional icon filename  
 :param data: Optional in-ram icon  
 :param data_base64: Optional base64 icon  
 :param time: How long to display message in milliseconds  :return:  
 '''
```

### Update

You can update any of these items within a SystemTray object
* Menu definition
* Icon (not working yet)
* Tooltip

 Change them all or just 1.

```python
Update(menu=None, tooltip=None,filename=None, data=None, data_base64=None,)
    '''  
 Updates the menu, tooltip or icon  
 :param menu: menu defintion  
 :param tooltip: string representing tooltip  
 :param filename:  icon filename  
 :param data:  icon raw image  
 :param data_base64: icon base 64 image  
 :return:  
 '''
```
## Menus with Keys

You can add a key to your menu items.  To do so, you add :: and the key value to the end of your menu definition. 

`menu_def = ['File', ['Hide::key', '&Open::key', '&Save',['1', '2', ['a','b']], '&Properties', 'E&xit']]`

The menu definition adds a key "key" to the menu entries Hide and Open.

If you want to change the separator characters from :: top something else,change the variable `MENU_KEY_SEPARATOR`

When a menu item has a key and it is chosen, then entire string is returned.  If Hide were selected, then Hide::key would be returned from the Read.  Note that the shortcut character & is NOT returned from Reads.


## Popups

Starting with release 0.4.0, most of the Popup functions work.  This means you can do things like show information in a window when there's a choice made in a System Tray menu.  Or if your program finds some event it wishes to inform the user about.  For example, when new Issues are posted on a GitHub project.


# Release Notes:  
  
### 0.1.0   -   25-Dec-2018

* Support for SystemTray
  * Read, with or without a timeout
  * Catch single click, double click events
  * Source code compatiable with Qt

### 0.2.0   -   26-Dec-2018

* Correctly handling base64 images
* Support for clicking message balloon
* Can Hide and  UnHide the  icon


### 0.3.0   -   27-Dec-2018

* Hooked up buttons!
* Browse file button is only file/folder button that works
* Text, Input and Button elements are the only working elements
* SystemTray can take any kind of image as icon
* Read with Timeout (non-zero) works
* Popups


### 0.4.0 PySimpleGUIWx  30-Dec-2018

* Text Element - colors, font work
* Text Update method works
* Button - Close button implemented
* Button - Implemented basic button, correctly presented Values on Read
* Button - Can now set font
* Changed overall "App" variable usage for better mainloop control
* Windows - Timeouts and non-blocking Reads work
* Windows - Autoclose works
* Windows - Non-blocking calls supported (timeout=0)
* Windows - Grab anywhere works
* Windows - No title-bar works
* Windows - Location and Size working correctly
* Correctly adding element padding to Text, Input, Buttons
* Popups - most Popups work (except for the input type that involve folders)

### 0.5.0 PySimpleGUIWx 6-Jan-2019

* New element - Multiline input
* New element - Multiline output
* Borderless Windows
* Grab anywhere windows
* Alpha channel for windows
* Finishing up the Text and Input Text Elements
* Visibility for all Elements
* Input Get / Set focus
* Output element - unable to get stdout to re-route
* Debug window works


### 0.6.0 9-Jan-2019

* Column Element
* Checkbox Element with events
* Output Element
* Background Image (I think works)
* Debug Print
* One Line Progress Meter
* All Popups works

### 0.7.0 PySimpleGUIWx 21-Jan-2019

* Element.Update support for disabled and tooltip
* Combo Element
* Newest Combo parameters
* Radio Element
* Newest Radio parameters (size_px, visible, enable_events)
* Type hints on Wx widgets
* Spinner Element
* Newest Spinner parameters
* Text Element visibility
* Column Element size_px parameter (unclear if works... likely does not)
* Column visibility
* Column Update method added
* System Tray - support for any kind of image format for icons
* Window.Move
* Window.Minimize
* Window.Maximize
* Window.Disable
* Window.Enable
* Window.Hide
* Window.UnHide
* Window.BringToFront
* Popup non_blocking - returns window and button not just button
* More comprehensive test harness when running PySimpleGUIWx.py

### 0.8.0 20-Feb-2019 PySimpleGUIWx

* Big Try/Except block around Update method for multiline in case window closed
* Text - convert incoming text to string right away
* Text.Update - convert incoming value to string
* Completed Button.Update method.  Can now change text, color, etc.
* Added Try around reading multiline input value - not sure why needed
* OneLineProgressMeter - can update text on every call now

### 0.9.0 06-Mar-2019 PySimpleGUIWx

* Addition of Assert Suppression
   * This was needed for a  multi-threaded version of PySimpleGUIWx
   * Complained when exiting a system tray if did not make this change and ran the tray in a thread
* Tray.Close now correctly Hides the icon
* SetGlobalIcon functional
* Can also now set icon using SetOptions call


### 0.10.0 23-Mar-2019 PySimpleGUIWx

* `do_not_clear` is now TRUE by default on Input and Multiline elements!!

  
## 0.11.0 11-Apr-2019 PySimpleGUIWx

* NEW Window parameter layout so can skip calling Layout

## 0.13.0 1-OCT-2019 PySimpleGUIWx

* Version numbering using sg.version string
* PEP8 bindings!
* Improved scaling of character to pixel sizes of elements that are multilined
* Added Metadata variable to all elements
* Renamed element callback functions to start with _
* Removed __del__ methods everywhere except Output Element
* Can "Call" an element which will call its Update method
* InputText element - convert default text and password char to string 
* Removed old code such as tkinter's tooltip and drag and drop from Qt
* Shortcut I for InputText
* Listbox added size_px parm
* Changed type checking to use the comment style types
* Added Element.Widget to all Elements so can access the Wx widgets directly
* Text Element now defaults to '' so no need to specify anything if a blank Text Element (often used for output)
* Button text converted to string when creating button
* New Button shortcuts - B, Btn
* VerticalSeparator - Newly supported Element
* HorizontalSeparator - Newly supported Element
* Slider - added size_px parm
* Fixed leak caused by System Tray not cleaning up the timer
* Window - added finalize paramter so can skip using chained .Finalize()
* Window - AllKeysDict now used like other PySimpleGUI ports. Has all the keys and elements in a window
* Window.FindElement - added silent_on_error parm like other ports have
* Window[key] construct added that calls FindElement
* window() - can "Call" a window you've created. Will call Window.Read()
* Popup buttons no longer use CloseButtons for normal popups.  Calls window.Close manually
* PopupGetFolder changed to use keys, normal button, new window design patterns
* PopupGetFile changed to use keys, normal buttons, new window design patterns
* PopupGetText changed to use keys, normal buttons, new window design patterns
* Default application (PySimpleGUI.main) now shows the version number like other PySimpleGUI ports

## 0.13.0 17-Nov-2019 PySimpleGUIWx

* 105 Look and Feel Themes to choose from!
* New "Fuzzy" look and feel selection
* Preview all look and feels not yet supported due to lack of Frame support

## 0.15.0 PySimpleGUIWx 24-Dec-2019

Themes!

* Picked up the new "theme" APIs like all 4 ports got
* Dark Blue 3 is the new official color theme for PySimpleGUI
* Added "port" string so that your code can detect which port of PySimpleGUI is being executed
* Removed restriction on Macs (totally didn't make sense that it was there as it blocked a tkinter problem, not a Wx one)
* Depricated the TRANSPARENT_BUTTON variable as it was being misunderstood by users and was misleading
* BROWSE_FILES_DELIMITER can be changed to change the default ';' delimeter between filenames in FilesBrowse button
* Frame Element!  BUT, it's only a partial solution as I am unable to set the background color (need to understand how panels work). It's better than nothing


## 0.16.0 PySimpleGUIWx 6-May-2020

* Added constants
    * WIN_CLOSED and WINDOW_CLOSED
    * EVENT_TIMEOUT and TIMEOUT_EVENT
* Added Graph.change_coordinates method
* Added close parameter to Window.read


## 0.17.0 PySimpleGUIWx 6-Jun-2020

Element justification within Window and Containers!  Finally a unified justification

* When any Radio element is updated to be False, the entire GROUP is reset so nothing is selected
* element_jutification added so that all elements inside these will be justified accordingly.
	* For PySimpleGUIQt only, the default is "float" which sets nothing. Buttons will stretch across the window as result
	* Valid values are 'l', 'r', 'c'.  You can spell it out, but only first letter is used.
	* Window
	* Frame
	* Column
	* Tab

## 0.17.1 PySimpleGUIWx 7-Jun-2020

* Quick patch of Multiline.update so that newlines are recognized correctly


# Design        
# Author 
 Mike B.        
        
   
# License        
 GNU Lesser General Public License (LGPL 3) +        
        
# Acknowledgments
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxNDIwNTI0ODQsODg2MzA1Mjk2XX0=
-->