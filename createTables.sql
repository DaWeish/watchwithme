use watchWithMe;

create table Person ( PID int NOT NULL AUTO_INCREMENT, First varchar(15), Last varchar(15), age int, Gender char(1), 
Username varchar(15), Password varchar(15), Favorite_Movie varchar(20), 
Favorite_Director varchar(20), Favorite_Actor varchar(20), Favorite_Genre varchar(15),
primary key (PID) );

create table Location ( LID int AUTO_INCREMENT, Address varchar(50), Capacity int, Screen varchar(10), Rating int,
primary key(LID) );

create table Location_2 ( LID int references Location(LID), Cooking_Util varchar(20), primary key(LID) );

create table Rate ( PID int references Person(PID), LID int references Location(LID), rating int, Primary key(PID,LID) );

create table Rate_2 ( PID int references Person(PID), MID int references Media(MID), rating int, primary key(PID, MID) );

create table Rate_3 ( PID int references Person(PID), FID int references Food(FID), rating int, primary key(PID,FID) );

create table Event (EID int AUTO_INCREMENT, Time varchar(5), Name varchar(30), date varchar(20), primary key(EID));

create table Food (FID int AUTO_INCREMENT, Name varchar(20), Type varchar(20), Temp int, primary key(FID) );

create table Serve (FID int references Food(FID), LID int references Location(LID), Cost int, primary key(FID,LID));

create table Media (MID int AUTO_INCREMENT, Title varchar(30), Description varchar(150), Release_Date varchar(20), Rating int, primary key(MID) );

create table Media_2 (MID int references Media(MID), Genre varchar(20), primary key(MID,Genre));

create table Movie (MID int references Media(MID), Director varchar(40), Lengh int, primary key(MID));

create table Series (MID int references Media(MID), Episodes int, primary key(MID));

create table Episodes (Name varchar(50), Length int, Season int, primary key(Name));

create table Attend( PID int references Person(PID), EID int references Event(EID));

create table Make_Event(PID int references Person(PID), EID int references Event(EID));

create table EventHasFood(FID int references Food(FID),EID int references Event(EID));

create table EventAtLocation(LID int references Location(LID), EID int references Event(EID));

create table Friend(PID int references Person(PID),PID1 int references Person(PID));

create table EventHasMedia(EID int references Event(EID), MID int references Media(MID), primary key(EID, MID));