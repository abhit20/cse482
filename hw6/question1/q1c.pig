s = load 'student.csv' using PigStorage(',');
t = load 'transcript.csv' using PigStorage(',');
data = join s by $0, t by $1;
tmp = foreach data generate $2,$3,$5;
tmp2 = filter tmp by $1 matches 'cse231';
grp = group tmp2 by $0;
result = foreach grp generate group, AVG(tmp2.$2);
dump result;
