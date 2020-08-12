# shinyrates scraper
(automatically grabbing Pokemon GO shiny rates data)

## What is this?
Ever since I learned about [Github Actions](https://github.com/features/actions), I've been using it to automate simple workflows. This has included:
 * [CI-doku](https://github.com/tuchandra/sudoku), which gets me Sudoku puzzles to solve daily
 * [My personal website](https://github.com/tuchandra/sitev2), which automatically rebuilds https://tusharc.dev every time I push to the source repo

... and now this! This project makes a GET request to https://shinyrates.com every 6 hours and saves the result to a CSV. The goal is to do Bayesian modeling on these as part of an eventual talk for PyMCon or a PyData conference.


## Repo contents
This repo is pretty simple:
 * `main.py` is the main Python script, which is something like 20 lines of actual code
 * `requirements.txt` says that I need requests and pandas
 * `.github/workflows/main.yml` is the workflow configuration file

And that's it!

