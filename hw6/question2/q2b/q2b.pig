p = load 'patient.csv' using PigStorage(',');
v = load 'visit.csv' using PigStorage(',');
data = join p by $0, v by $2;
grp = group data by ($0,$1);
result = foreach grp generate group.$0, group.$1, COUNT(data);
dump result;
