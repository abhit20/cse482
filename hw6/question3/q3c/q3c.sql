SELECT P.id, P.name, COUNT(*) as Number of Visits
FROM Patient P, Visit V
WHERE P.id = V.patientID
GROUP BY P.id, P.name;
