% Facts about symptoms and diseases
symptom(fever, [flu, cold, malaria]).
symptom(cough, [flu, cold]).
symptom(headache, [flu, migraine]).
symptom(rash, [allergy, measles]).
symptom(runny_nose, [flu, cold]).
symptom(fatigue, [flu, malaria]).
symptom(sneezing, [cold, allergy]).
symptom(chills, [malaria, flu]).

% Rule to diagnose a disease based on symptoms
diagnose(Disease, Symptoms) :-
    findall(D, (
        symptom(Symptom, Diseases),
        member(Symptom, Symptoms),
        member(D, Diseases)
    ), PossibleDiseases),
    sort(PossibleDiseases, SortedDiseases),
    member(Disease, SortedDiseases),
    forall(member(Symptom, Symptoms), (symptom(Symptom, Diseases), member(Disease, Diseases))).
