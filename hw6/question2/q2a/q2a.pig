p = load 'patient.csv' using PigStorage(',');
v = load 'visit.csv' using PigStorage(',');
data = join p by $0, v by $2;
tmp = filter data by $7 matches 'hypertension';
result = foreach tmp generate $0, $1;
dump result;
