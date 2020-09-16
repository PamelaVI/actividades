
    CREATE  DATABASE cinema;
    USE cinema;
    CREATE TABLE actor(
        id_actor  int auto_increment primary key,
        nombre varchar(50) not null,
        apellido varchar(50) not null,
        fecha_nacimiento date not null);

    CREATE TABLE peliculas (
        id_pelicula int auto_increment primary key,
        nombre varchar(50) not null,
        fecha_estreno date not null,
        foreign key(id_actor) references actor(id_actor),
        foreign key(id_director) references director(id_director));

    CREATE TABLE director(
        id_director int auto_increment primary key,
        nombre varchar(50) not null,
        apellido varchar(50) not null,
        fecha_nacimiento date not null);
