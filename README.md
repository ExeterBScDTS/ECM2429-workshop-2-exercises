# ECM2429-workshop-2-exercises

Python programming exercises

## Aims

Learn how to add database capabilities to Python programs.

Use *mocks* to simplify unit testing.

Store and retrieve binary data (blobs).

## Getting started

We're going to use SQLite as our database 'engine' for the exercises.

Important things to know about SQLite

The good stuff

* SQLite reads and writes directly to ordinary disk files.

* SQLite does not have a separate server process. So you don't have to install and manage any database server software.

* SQLite is *transactional* <https://www.sqlite.org/transactional.html>

* SQLite implements most of the queries and other syntax you would expect from a SQL database engine. 

* Python3 includes a built-in version of SQLite <https://docs.python.org/3/library/sqlite3.html>

The not so good stuff

 * SQLite does not have a separate server process. Yes, there could be downsides to this.

 * SQLite files are (almost) plain text, not encrypted.

## Quiz

What do we mean by ACID when talking about databases?

What is the role of a Connection object?

What is the role of a Cursor object?

## Why use a database?

Databases provide many useful features, they allow us to organise data, query it, and also ensure its integrity; however as programmers the most useful
feature is often the simplest - databases provide *persistent storage* in an easy to use manner.

## Alternatives for persistent storage and data exchange in Python

If your only requirement from your database is persistence, then it might be that you don't need a database at all.  Here are some alternatives.

 * pickle <https://docs.python.org/3/library/pickle.html>

 * Text or binary files <https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>  
 
 When using data files pick a well known file format, for example text files formatted as JSON, XML, or YAML are often used to save program configuration. CSV files are typically used to exchange tabular data between applications.

 For the exchange of *media*, such as drawings, photos, videos and audio, it is usual to use one of the widely used portable file formats, i.e. a format that is usable by a variety of software applications.  Examples are SVG, PNG, JPEG, MPEG and MP4. For a much longer list, and links to useful resources see <https://developer.mozilla.org/en-US/docs/Web/Media/Formats> Note that most of these formats are binary and apply data compression algorithms, so to read and write them appropriate software libraries are required.

## SQLite exercises

1. Use the makedb.py program to create a database.

1. Use the addblob.py program to store WAV data in your database.

1. Use the randomplay.py program to play audio from the database.

1. Modify randomplay.py to take two command line arguments loud/quiet music/noise so it can be used like this -

```sh
randomplay.py loud music
```

## Testing exercises

1. Try running the provided tests ```test_addblob.py``` and ```test_randomplay.py``` using pytest.

1. Refactor and write a similar test for ```makedb.py```

1. Can you write a test for ```play.py```?
