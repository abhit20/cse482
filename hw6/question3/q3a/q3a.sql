CREATE EXTERNAL Patient (
	id int,
	name string,
	gender string,
	age int)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;
LOCATION '/user/hadoop/patient';

CREATE EXTERNAL Visit (
	visitID int,
	vDate string,
	patientID int,
	diagnosis string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;
LOCATION '/user/hadoop/visit';
