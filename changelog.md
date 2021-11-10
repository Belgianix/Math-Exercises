# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],

## [Unreleased]
- Level of difficulty dependent on grade level
- Login option through MariaDB 

## [2.0.1]  - 2021-11-10
### Added 
- Sound effects
- Method to choose random sound

## [2.0.0] - 2021-10-29

### Added
- Comments to the Gui and other small memo's in code 
- Gui frame for specified exercise + widgets and their locations on the frame
- Counters displaying the amount of correct and wrong answers
- Back button that returns to the main menu
- Display of correct answer when the user inputs the wrong answer
- Prevention of input besides integers
- Handlers class
- return_to_main_menu and check_button_handler methods
- frm_menu to switch between pages easier
- limited docstrings
- counters class
- ability to press the enter key to input answer
- Round btn
- Btn.png

### Changed
- Positioning of code blocks
- global amount_wrong, amount_correct variables to class variables
- Lay-out calculation screen
- Changed the GUI to match the drawing from discord

### Deprecated
- check_for_stop method
- viability_check method
- viability class

### Removed
- While loops inside operations methods
- While loop inside game loop function
- Output to console for user


## [1.0.1] - 2021-10-01

### Changed
- Prevention of decimal numbers in the division method. Better optimized

## [1.0.0] - 2021-9-30
- initial release

<!-- Links -->
[keep a changelog]: https://keepachangelog.com/en/1.0.0/

<!-- Versions -->
[1.0.0]: https://github.com/Belgianix/Math-Exercises
[1.0.1]: https://github.com/Belgianix/Math-Exercises/releases/tag/v1.0.1
[2.0.0]: https://github.com/Belgianix/Math-Exercises/releases/tag/v2.0.0
