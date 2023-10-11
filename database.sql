CREATE TABLE `students` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL,
  `last_checked_in` datetime,
  `path` varchar(255)
);

INSERT INTO `students` (`code`, `name`) VALUES
('B123', 'Nguyễn Văn A'),
('B234', 'Trần Thị B'),
('B345', 'Ngô Thanh C'),
('B456', 'Lê Thị D');
