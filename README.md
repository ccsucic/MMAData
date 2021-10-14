# MMA Data Project

For this project, I chose to focus on sourcing and formatting data from the sport of mixed martial
arts (MMA). The sport of MMA began in the late 1990s, so it does not have a robust amount of
data or data tools like other sports such as basketball or baseball. Given this, I thought it would
be interesting to try and build my own tool so others could easily view and download MMA
statistics. I sourced the MMA statistics from the biggest league in MMA, the UFC. The UFC
keeps data on each fighter. For each fighter, you have statistics such as strikes landed per minute,
strike accuracy, takedown accuracy, etc. I scraped and stored each fighter with these statistics,
but I also made my own statistic called classification.

This projects extracts data using a web scraper made with Scrapy, transforms the data using Python
libraries such as Pandas, and loads the data into an SQLite database that is available for download on a Flask web app.

Below, you will find a screenshot of the homepage of the Flask app. The page contains an explanation of the different
variables present in the database. You will also find a screenshot of the full database within the Flask app.

![Homepage Screenshot](MMAData/MMAData/screenshots/UFCDBHome.PNG)

![Full Database Screenshot](MMAData/MMAData/screenshots/UFCDBFullDB.PNG)


# Future Work

In the future, the Flask web app could be set up on a webserver that is publicly available. That
way, others interested in MMA statistics could easily download the dataset and run their own
analyses on it.
