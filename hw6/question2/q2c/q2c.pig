p = load 'patient.csv' using PigStorage(',');
v1 = load 'visit.csv' using PigStorage(',');
v2 = load 'visit.csv' using PigStorage(',');
q1 = FILTER v1 by $3 == 'hypertension';
q2 = FILTER v2 by $3 == 'diabetes';
data = JOIN q1 by $2, q2 by $2;
data2 = JOIN p by $0, data by $2;
result = foreach data2 generate $0, $1;
dump result;
