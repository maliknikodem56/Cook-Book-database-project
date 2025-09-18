use recipies;


create table dish_types(
id int auto_increment primary key,
name_ varchar(100) not null );

create table cuisines(
id int auto_increment primary key ,
name_ varchar(150) not null);


create table diets ( 
id int auto_increment primary key, 
name_ varchar(150) not null);


create table dishes(
id int auto_increment primary key,
name_ varchar(150),
dish_type_id int,
cuisine_id int,
diet_id int,
kcal_per_100g decimal(10,2),
ingredients text,
preparation_time_minutes int,
foreign key(dish_type_id) references dish_types(id),
foreign key (cuisine_id) references cuisines(id),
foreign key (diet_id) references diets(id));


