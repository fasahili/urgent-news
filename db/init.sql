CREATE TABLE IF NOT EXISTS news (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL
);

INSERT INTO news (title, content) VALUES
('Breaking News 1', 'Content for Breaking News 1'),
('Breaking News 2', 'Content for Breaking News 2'),
('Breaking News 3', 'Content for Breaking News 3'),
('Breaking News 4', 'Content for Breaking News 4'),
('Breaking News 5', 'Content for Breaking News 5'),
('Breaking News 6', 'Content for Breaking News 6'),
('Breaking News 7', 'Content for Breaking News 7'),
('Breaking News 8', 'Content for Breaking News 8'),
('Breaking News 9', 'Content for Breaking News 9'),
('Breaking News 10', 'Content for Breaking News 10');
