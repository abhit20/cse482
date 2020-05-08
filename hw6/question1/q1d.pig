s = load 'student.csv' using PigStorage(',');
n = filter s by not($1 matches 'cs');
t = load 'transcript.csv' using PigStorage(',');
t2 = filter t by $0 matches 'cs.*';
tmp = join t2 by $1, n by $0;
result = foreach tmp generate $1;
dump result;
