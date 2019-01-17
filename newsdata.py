#!/usr/bin/env python3

import sys
import psycopg2

# define the database connection
try:
    db = psycopg2.connect("dbname=news")
except psycopg2.Error as e:
    print ("Unable to connect to the database")


# Get the 3 most popular posts and return the title and number of views.
# Order highest to lowest
def get_articles():
    q = db.cursor()
    q.execute("select articles.title, count(log.status) as views \
    from articles join log on log.path like '%' || articles.slug || '%' \
    and log.status not like '%404%' \
    group by articles.title \
    order by views desc \
    limit 3;")

    # excecute the query
    articles = q.fetchall()

    # close the connection to the database
    db.close()

    # print the results
    print("\nThe three most popular articles of all time are: \n")
    for article in articles:
        print('"' + article[0] + '" -- ' + str(article[1]) + ' views')


# Get the most popular authors and and number of views.
# Order highest to lowest.
def get_authors():
    q = db.cursor()
    q.execute("select name, count(log.status) as views \
    from \
        (select authors.name, articles.slug \
        from authors join articles \
        on authors.id = articles.author) \
    as author_list join log on log.path \
    like '%' || author_list.slug || '%' \
    and log.status not like '%404%' \
    group by author_list.name \
    order by views desc;")

    # excecute the query
    authors = q.fetchall()

    # close the connection to the database
    db.close()

    # print the results
    print("\nThe most popular article authors of all time are: \n")
    for author in authors:
        print(author[0] + ' -- ' + str(author[1]) + ' views')


def get_404s():
    q = db.cursor()
    q.execute("select to_char(time::date, 'FMMonth DD, YYYY') as date, \
    to_char( \
    (count(*) filter(where status like '%404%') * 100.0 / count(*)), \
    'FM990.00\"%\"') as percent \
    from log \
    group by date \
    having (count(*) filter(where status like '%404%') *100.0 / count(*)) > 1 \
    order by percent desc;")

    # execute the query
    days = q.fetchall()

    # close the connection to the database
    db.close()

    # print the results
    print(" \nThe days on which more than 1% of \
    requests lead to errors are: \n")
    for day in days:
        print(day[0] + ' -- ' + day[1] + ' errors')


# Ask the user which query to run
def get_input():
    user_response = input("\n \
    1. What are the most popular three articles of all time? \n \
    2. Who are the most popular article authors of all time? \n \
    3. On which days did more than 1% of requests lead to errors? \n\n \
    Which query would you like to run? ")

    if user_response == 1:
        get_articles()
    elif user_response == 2:
        get_authors()
    elif user_response == 3:
        get_404s()
    else:
        print("\nPlease make a proper selection \n")
        get_input()


# Run the program
get_input()
