CREATE DATABASE IF NOT EXISTS django_emarket_cms_auth
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;

CREATE DATABASE IF NOT EXISTS django_emarket_cms
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;


GRANT ALL PRIVILEGES ON django_emarket_cms.* TO root@''
IDENTIFIED BY '123456';
FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON django_emarket_cms_auth.* TO root@''
IDENTIFIED BY '123456';
FLUSH PRIVILEGES;

#图书
CREATE TABLE `book` (
  `id`           INT(11)      NOT NULL AUTO_INCREMENT,
  `name`         VARCHAR(512) NOT NULL,
  `created_time` BIGINT(20)   NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 1
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_general_ci;