create database todo_list
default character set utf8
default collate utf8_general_ci;

use todo_list;

create table lista (
id int auto_increment NOT NULL,
tarefa varchar(50),
stts enum ('C', 'N') default 'N',
primary key (id)
) default charset = utf8;