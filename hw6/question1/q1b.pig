data = load 'transcript.csv' using PigStorage(',');
grp = group data by $1;
tmp = foreach grp generate group, AVG(data.$2);
result = FILTER tmp by $1 >= 3.5;
dump result;
