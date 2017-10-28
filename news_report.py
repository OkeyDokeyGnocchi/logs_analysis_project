#!/usr/bin/env python2.7


import psycopg2


def most_popular_article():
    """Function that uses a(n) SQL query to find the top three articles
    based on number of views."""
    db = psycopg2.connect(database="news")
    cursor = db.cursor()
    cursor.execute("""select title, count(*) as Views
                   from articles
                   join log on log.path = '/article/' || articles.slug
                   group by title
                   order by Views desc limit 3;""")
    rows = cursor.fetchall()
    print "The top three articles of all time are: \n"
    for article, views in rows:
        print str(article) + ' **|** ' + str(views)  # remove ()/[] chars

    db.close()


def most_popular_authors():
    """Function that uses a(n) SQL query to parse the logs for the authors
    that have the most combined views across their articles."""
    db = psycopg2.connect(database="news")
    cursor = db.cursor()
    cursor.execute("""select authors.name, count(*) as Views
                   from authors
                   join articles on authors.id = articles.author
                   join log on log.path = '/article/' || articles.slug
                   group by authors.name
                   order by Views desc;""")
    rows = cursor.fetchall()
    print "\n\nThis is the number of views each author has received: \n"
    for author, views in rows:
        print str(author) + ' **|** ' + str(views)  # remove ()/[] chars


def too_many_errors():
    """Function that uses a(n) SQL query to parse the logs and find the dates
    where the error percentage is greater than 1%."""
    db = psycopg2.connect(database="news")
    cursor = db.cursor()
    cursor.execute("""select day, percentage
                   from percentage_view
                   where percentage >= 1;""")
    rows = cursor.fetchall()
    print "\n\nDays with over 1% errors when accessing articles: \n"
    for date, percent in rows:
        print str(date) + ' **|** ' + str(percent) + '%'


if __name__ == "__main__":
    most_popular_article()
    most_popular_authors()
    too_many_errors()
