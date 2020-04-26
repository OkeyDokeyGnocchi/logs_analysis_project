# Markdown File for my Back-End Specialization Project:
## News Report (news_report.py)

### Using Python, psycopg2, and Postgresql to query a database
### and gather information about the logs for the news reports
### contained therein.

program (written in Python) leverages the psycopg2 library
and functions contained within it to query a Postgresql database and gather
information from the logs contained within that database.


### How the program works

* To run the program, simply place it in the /vagrant shared directory
with the News DB and run it via terminal using the command
`python news_report.py`, it's as simple as that!

* This code requires Python2, PostgreSQL,
the psycopg2 library, and the newsdata.sql file.

* The newsdata.sql file can be found either through the direct link,
  or via the Udacity Nanodegree project page.
  __Direct Link:__
  https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

  __Udacity Page:__ https://classroom.udacity.com/nanodegrees/nd000/parts/b910112d-b5c0-4bfe-adca-6425b137ed12/modules/a3a0987f-fc76-4d14-a759-b2652d06ab2b/lessons/0aa64f0e-30be-455e-a30d-4cae963f75ea/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91

* To load the newsdata.sql file into the news database, go to the folder
  where your database will be located (in my case this was the /vagrant
  folder within the vagrant Linux virtual machine) and run the command
  `psql -d news -f newsdata.sql` to create necessary tables and populate
  the database.

The program is built on three (3) functions:

* _most_popular_article()_ queries the database by a count of the
  occurrences of %path% that match up with
  the slugs of articles.  The results are grouped by Title and sorted
  by most views to least.  Finally, the output is limited to the top
  3 articles.

* _most_popular_authors()_ is similar to most_popular_article(), but
  rather than returning the counts for articles, it compares the article's
  author ID to the author table and aggregates the number of views for
  each author as a sum of the article views they are responsible for.

* _too_many_errors()_ takes in the percentage calculated in the
  percentage_view (which itself takes in and divides the number of errors
  for a day by the number of total hits to determine the percentage of errors)
  and returns the days that had a percentage >= 1%.

These three functions are returned at the end of the program by the
`if __name__ == "__main__":` block.





### The following views were entered into the 'News' database `psql news`:

* 'create view comp_errors as
  select a.Day, a.Errors, b.Hits
  from (select date_trunc('day', time) as Day, count(*) as Errors from log where status not like '200%' group by Day) a
  INNER JOIN
  (select date_trunc('day', time) as Date, count(*) as Hits from log group by Date) b on Day = Date;'

* 'create view percentage_view as
  select comp_errors.day, (round((comp_errors.errors::numeric/comp_errors.hits::numeric),4)*100) as Percentage
  FROM comp_errors;'
