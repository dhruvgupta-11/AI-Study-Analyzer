# AI Study Analyzer

## Overview

AI Study Analyzer is a terminal-based Python project that helps students
analyze academic topics across multiple subjects. It provides structured
learning guidance by identifying prerequisites, learning paths, and
estimated difficulty levels.

------------------------------------------------------------------------

## Features

-   Multi-subject support (AI/ML, Programming, Electric Circuits,
    Physics, Chemistry, Communication)
-   Topic-wise prerequisite analysis
-   Automatic learning path generation
-   Difficulty prediction using Machine Learning
-   Interactive menu-based terminal interface

------------------------------------------------------------------------

## How It Works

1.  User selects a subject
2.  Selects a topic
3.  System provides:
    -   Prerequisites
    -   Learning Path
    -   Estimated Difficulty (Easy/Medium/Hard)

------------------------------------------------------------------------

## Technologies Used

-   Python
-   Scikit-learn (Decision Tree Classifier)
-   Modular Programming (separate files for logic, ML, data)

------------------------------------------------------------------------

## Project Structure

ai_study_analyzer/

main.py

data/ - topics.py - dependencies.py

core/ - analyzer.py - utils.py

ml/ - train.py - predict.py

README.md

------------------------------------------------------------------------

## Machine Learning

A Decision Tree model is used to estimate topic difficulty based on: -
Length of input - Estimated concept complexity

------------------------------------------------------------------------

## Example Output

Subject: AI_ML Topic: A\* Search

Estimated Difficulty: Hard

Prerequisites: - BFS - DFS

Learning Path: - Search Problems - BFS - DFS - A\* Search

------------------------------------------------------------------------

## Conclusion

This project helps students move from random studying to structured
learning by understanding dependencies between topics.
