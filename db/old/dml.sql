-- USE my_database;
INSERT INTO
    users_table (name, email)
VALUES
    ('shuhei', 'a@shushushu.jp');

INSERT INTO
    users_table (name, email)
VALUES
    ('shuhei2', 'b@shushushu.jp');

INSERT INTO
    users_table (name, email)
VALUES
    ('shuhei3', 'c@shushushu.jp');

UPDATE
    users_table
SET
    name = 'shuheiiii'
WHERE
    id = 2;

DELETE FROM
    users_table;
