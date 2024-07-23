-- Creates a user with a replication client privilege
CREATE USER IF NOT EXISTS 'alx_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'alx_user'@'localhost';
FLUSH PRIVILEGES;
