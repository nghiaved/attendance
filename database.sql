CREATE TABLE `students` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL,
  `last_checked_in` datetime,
  `path` varchar(255)
);

