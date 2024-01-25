INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO post (title, body, author_id, created_at)
VALUES
  ('test title 0', 'test 0' || x'0a' || 'body', 1, '2018-01-01 00:00:00'),
  ('test title 1', 'test 1' || x'0a' || 'body', 1, '2018-01-01 00:00:01'),
  ('test title 2', 'test 2' || x'0a' || 'body', 1, '2018-01-01 00:00:02'),
  ('test title 3', 'test 3' || x'0a' || 'body', 1, '2018-01-01 00:00:03'),
  ('test title 4', 'test 4' || x'0a' || 'body', 1, '2018-01-01 00:00:04'),
  ('test title 5', 'test 5' || x'0a' || 'body', 2, '2018-01-01 00:00:05'),
  ('test title 6', 'test 6' || x'0a' || 'body', 2, '2018-01-01 00:00:06'),
  ('test title 7', 'test 7' || x'0a' || 'body', 2, '2018-01-01 00:00:07'),
  ('test title 8', 'test 8' || x'0a' || 'body', 2, '2018-01-01 00:00:08'),
  ('test title 9', 'test 9' || x'0a' || 'body', 2, '2018-01-01 00:00:09');

INSERT INTO todo (title, body, author_id, created_at)
VALUES
  ('test todo 0', 'todo 0' || x'0a' || 'body', 1, '2018-01-01 00:00:00'),
  ('test todo 1', 'todo 1' || x'0a' || 'body', 1, '2018-01-01 00:00:02'),
  ('test todo 2', 'todo 2' || x'0a' || 'body', 1, '2018-01-01 00:00:04'),
  ('test todo 3', 'todo 3' || x'0a' || 'body', 1, '2018-01-01 00:00:06'),
  ('test todo 4', 'todo 4' || x'0a' || 'body', 1, '2018-01-01 00:00:08'),
  ('test todo 5', 'todo 5' || x'0a' || 'body', 2, '2018-01-01 00:00:10'),
  ('test todo 6', 'todo 6' || x'0a' || 'body', 2, '2018-01-01 00:00:12'),
  ('test todo 7', 'todo 7' || x'0a' || 'body', 2, '2018-01-01 00:00:14'),
  ('test todo 8', 'todo 8' || x'0a' || 'body', 2, '2018-01-01 00:00:16'),
  ('test todo 9', 'todo 9' || x'0a' || 'body', 2, '2018-01-01 00:00:18');
