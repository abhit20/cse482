SELECT P.id, P.name
FROM Patient P, Visit V
WHERE P.id = V.patientID and P.diagnosis = 'hypertension';
