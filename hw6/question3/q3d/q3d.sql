SELECT P.id, P.name
FROM Patient P, Visit V1, Visit V2
WHERE P.id = V1.patientID AND V1.patientID = V2.patientID and V2.diagnosis = 'hypertension' AND V1.diagnosis = 'diabetes';
