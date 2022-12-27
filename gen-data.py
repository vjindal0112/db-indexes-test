import random
# CREATE Table authors
# (
#    author_id int not null primary key,
#    author_name varchar(50),
#    country varchar(50)
# );

# CREATE Table books
# (
#    book_id int not null primary key,
#    author_id int,
#    price int,
#    edition int,
#    foreign key (author_id) references authors(author_id)
# );


NAMES = ["JAMES", "NICK", "JOHN", "ANGELICA", "PIYUSH", "SONA",
         "SUNITA", "KRUTI", "SWASTI", "ELLIOT", "YASH", "SWASHBUCKLER"]
COUNTRIES = ["UNITED STATES", "INDIA", "GERMANY", "MORROCO", "BRAZIL", "JAPAN", "CHINA", "RUSSIA", "CANADA", "AUSTRALIA", "NEW ZEALAND", "MEXICO", "FRANCE", "ITALY",
             "SPAIN", "UK", "IRELAND", "NETHERLANDS", "BELGIUM", "SWEDEN", "DENMARK", "NORWAY", "FINLAND", "ICELAND", "GREECE", "TURKEY", "EGYPT", "SOUTH AFRICA", "NIGERIA", "KENYA"]
PRICES = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
EDITIONS = [1, 2, 3]

# CREATE AUTHORS
# open the file create-data.sql to write to
# with open('create-authors-smaller.sql', 'w') as f:
# # write fake data to the file given the schema in init-db.sql
#   f.write("INSERT INTO authors (author_name, country)\n")
#   f.write("VALUES ")
#   for x in range(100000):
#     f.write("('" + random.choice(NAMES) + "', '" + random.choice(COUNTRIES) + "')")
#     if x != 99999:
#       f.write(",\n")
#   f.write(";")
#   f.write("\n")

# CREATE BOOKS
# for k in range(8):
# with open('create-books-smaller.sql', 'w') as f:
#   f.write("INSERT INTO books (author_id, price, edition)\n")
#   f.write("VALUES ")
#   for x in range(0, 25000):
#     k = random.randint(2, 10)
#     for y in range(k):
#       f.write("('" + str(x) + "', '" + str(random.choice(PRICES)) +
#               "', '" + str(random.choice(EDITIONS)) + "')")
#       if x != 24999 or y != k-1:
#         f.write(", ")
#   f.write(";")

# CREATE POINTS
with open('create-points-smaller.sql', 'w') as f:
  f.write("INSERT INTO points (loc)\n")
  f.write("VALUES ")
  for x in range(100000):
    f.write("(point(" + str(random.randint(0, 10000)) +
            ", " + str(random.randint(0, 10000)) + "))")
    if x != 99999:
      f.write(",\n")
  f.write(";")
