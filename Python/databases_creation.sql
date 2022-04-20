CREATE TABLE data_from_news(
    article_id INT PRIMARY KEY,
    article_source VARCHAR(10),
    article_link VARCHAR(200),
    article_title VARCHAR(120),
    article_subtitle VARCHAR(300),
    article_body VARCHAR(20000)
);