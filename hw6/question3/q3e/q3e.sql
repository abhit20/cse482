SELECT V.diagnosis, COUNT(*) as Diagnosis
FROM Patient P, Visit V
WHERE P.id = V.patientID AND P.age >= 40
GROUP BY V.diagnosis
ORDER BY Diagnosis DESC
LIMIT 1;
