data = load 'student.csv' using PigStorage(',');
grp = group data by $2;
result = foreach grp generate group, COUNT(data);
dump result;
