
create table Person ( PID int, First varchar(15), Last varchar(15), age int, Gender char(1), 
Username varchar(15), Password varchar(15), Favorite_Movie varchar(20), 
Favorite_Director varchar(20), Favorite_Actor varchar(20), Favorite_Genre varchar(15),
primary key (PID) );

create table Location ( LID int, Address varchar(50), Capacity int, Screen varchar(10), Rating int,
primary key(LID) );

create table Location_2 ( LID int references Location(LID), Cooking_Util varchar(20), primary key(LID) );

create table Rate ( PID int references Person(PID), LID int references Location(LID), rating int, Primary key(PID,LID) );

create table Rate_2 ( PID int references Person(PID), MID int references Media(MID), rating int, primary key(PID, MID) );

create table Rate_3 ( PID int references Person(PID), FID int references Food(FID), rating int, primary key(PID,FID) );

create table Event (EID int, Time varchar(5), Name varchar(30), date varchar(20), primary key(EID));

create table Serve (FID int, LID int references Location(LID), Cost int, primary key(FID,LID));

create table Food (FID int, Name varchar(20), Type varchar(20), Temp int, primary key(FID) );

create table Media (MID int, Title varchar(30), Description varchar(150), Release_Date varchar(20), Rating int, primary key(MID) );

create table Media_2 (MID int references Media(MID), Genre varchar(20), primary key(MID,Genre));

create table Movie (MID int references Media(MID), Director varchar(40), Lengh int, primary key(MID));

create table Series (MID int references Media(MID), Episodes int, primary key(MID));

create table Episodes (Name varchar(50), Length int, Season int, primary key(Name));

create table Attend( PID int references Person(PID), EID int references Event(EID));

create table Make_Event(PID int references Person(PID), EID int references Event(EID));

create table Has(FID int references Food(FID),EID int references Event(EID));

create table At(LID int references Location(LID), EID int references Event(EID));

create table Friend(PID int references Person(PID),PID1 int references Person(PID));



insert into Person values (123456789, 'Rick','Bobby',50,'M','Talladega','Knights',
'Ghost Busters', 'Steven Spielberg','Ricky Bobby','Romance');

insert into Person values (987654321,'Johnny','Depp',51,'M','JackSparrow','ivegotajar',
'Edward Scizzorhands','Tim Burton','Johnny Depp','Action');

insert into Person values (456123789,'Will','Ferrel',47,'M','TightPants','Steve',
'Step Brothers','Adam McKay','Will Ferrel','Comedy');

insert into Location values (11111111,'1800 Vic Street, St.Louis, MO',700,'100x100',4);

insert into Location values (22222222,'525 Eisenhower Rd., Rolla, MO',900,'120x110',3);

insert into Location values (33333333,'146 West Street, St.Clair, MO',500,'90x90',5);

insert into Location_2 values (11111111,'Popcorn Machine');

insert into Location_2 values (22222222,'Simple Snacks');

insert into Location_2 values (33333333,'Grill');

insert into Rate values (123456789,11111111,3);
insert into Rate values (123456789,22222222,2);
insert into Rate values (123456789,33333333,4);

insert into Rate values (987654321,11111111,5);
insert into Rate values (987654321,22222222,4);
insert into Rate values (987654321,33333333,5);

insert into Rate values (456123789,11111111,4);
insert into Rate values (456123789,22222222,3);
insert into Rate values (456123789,33333333,5);


insert into Rate_2 values (123456789,44444444,5);
insert into Rate_2 values (123456789,55555555,1);
insert into Rate_2 values (123456789,66666666,4);

insert into Rate_2 values (987654321,44444444,3);
insert into Rate_2 values (987654321,55555555,4);
insert into Rate_2 values (987654321,66666666,5);

insert into Rate_2 values (456123789,44444444,5);
insert into Rate_2 values (456123789,55555555,2);
insert into Rate_2 values (456123789,66666666,3);

insert into Rate_3 values (123456789,005,1);
insert into Rate_3 values (123456789,010,3);
insert into Rate_3 values (123456789,015,2);

insert into Rate_3 values (987654321,005,5);
insert into Rate_3 values (987654321,010,2);
insert into Rate_3 values (987654321,015,3);

insert into Rate_3 values (456123789,005,3);
insert into Rate_3 values (456123789,010,3);
insert into Rate_3 values (456123789,015,4);

insert into Event values (00000001,'5:00','Pirate Marathon',06/21/2015);
insert into Event values (00000002,'4:00','April is Over',05/20/2015);
insert into Event values (00000003,'3:00','Lord of the Rings',07/02/2015);

insert into Serve values (005,11111111,5);
insert into Serve values (010,22222222,2);
insert into Serve values (015,33333333,7);

insert into Food values (005,'Popcorn','Snack',100);
insert into Food values (010,'Candy','Snack',65);
insert into Food values (015,'Hotdogs','Meal',150);

insert into Media values (44444444,'Ballad of Ricky Bobby',
'Racing Comedy Featuring Will Ferrel','08/04/2006',3);

insert into Media values (55555555,'Lord of the Rings','Epic Film Based on the Novel',
'12/19/2001',4);

insert into Media values (66666666,'Pirates of the Caribbean','Action Packed Pirate Film',
'08/09/2003',4);

insert into Media_2 values(44444444,'Comedy');
insert into Media_2 values(55555555,'Action');
insert into Media_2 values(66666666,'Action');


insert into Movie values(44444444,'Adam McKay',108);
insert into Movie values(55555555,'Peter Jackson',178);
insert into Movie values(66666666,'Gore Verbinski',143);

insert into Series values(44444444,1);
insert into Series values(55555555,6);
insert into Series values(66666666,4);

insert into Episodes values('Talladega Knights',108,1);
insert into Episodes values('An Unexpected Journey',169,1);
insert into Episodes values('The Desolation of Smaug',161,2);
insert into Episodes values('The Battle of the Five Armies',144,3);
insert into Episodes values('The Fellowship of the Ring',178,4);
insert into Episodes values('The Two Towers',179,5);
insert into Episodes values('The Return of the King',201,6);
insert into Episodes values('The Curse of the Black Pearl',143,1);
insert into Episodes values('Dead Mans Chest',151,2);
insert into Episodes values('At Worlds End',169,3);
insert into Episodes values('On Stranger Tides',136,4);


drop table Person restrict;
drop table Location restrict;
drop table Location_2 restrict;
drop table Rate restrict;
drop table Rate_2 restrict;
drop table Rate_3 restrict;
drop table Event restrict;
drop table serve restrict;
drop table Food restrict;
drop table Media restrict;
drop table Media_2 restrict;
drop table Movie restrict;
drop table Series restrict;
drop table Episodes restrict;
drop table Attend restrict;
drop table Make_Event restrict;
drop table Has restrict;
drop table At restrict;
drop table Friend restrict;



