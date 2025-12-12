# New York Times Spelling Bee Solver (NYTSBS)

## Introduction

A few months ago I got into the habit of completing the New York Times Spelling Bee each day. As a side project for myself, I decided to try and code a solution for it that would provide you with valid words given the required letters for the current day's puzzle.

The project is coded exclusively using python, however I plan on fully porting it over into dart to make a companion app out of it.

## Using the Code

Once you run the program, you will first enter the key letter for the day, that being the one presented in the center of the hexagon on the NYT website. Then, you will enter in the remaining six letters for the day and hit enter. You will then be given the 50 most frequently used words that are solutions to the puzzle.

## Future Plans

Currently, the project uses some downloaded text files that contain all the words that the program can search through, (which was the easiest thing to do when I had first started working on it). My next steps with the project will be to move from that approach into utilizing an api so that the program can work with more up-to-date data, as well as skipping over some of the more arcane words that still manage to float up into the suggested answers.
