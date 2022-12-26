CREATE Table authors 
(
   author_id SERIAL PRIMARY KEY,
   author_name varchar(50),
   country varchar(50)
);

CREATE Table books 
(
   book_id SERIAL PRIMARY KEY,
   author_id int, 
   price int,
   edition int,
   foreign key (author_id) references authors(author_id)
);

CREATE TABLE points
(
  point_id SERIAL PRIMARY KEY,
  loc POINT
)