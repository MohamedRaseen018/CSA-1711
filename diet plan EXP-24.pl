% Diet Recommendation System Based on Disease

% Diet recommendations for diabetes
diet(diabetes, oats).
diet(diabetes, vegetables).
diet(diabetes, whole_grains).
diet(diabetes, beans).

% Diet recommendations for hypertension
diet(hypertension, fruits).
diet(hypertension, vegetables).
diet(hypertension, low_salt_food).
diet(hypertension, whole_grains).

% Diet recommendations for anemia
diet(anemia, spinach).
diet(anemia, lentils).
diet(anemia, beans).
diet(anemia, iron_fortified_foods).

% Diet recommendations for obesity
diet(obesity, vegetables).
diet(obesity, fruits).
diet(obesity, whole_grains).
diet(obesity, lean_protein).

% Diet recommendations for heart_disease
diet(heart_disease, oats).
diet(heart_disease, fruits).
diet(heart_disease, vegetables).
diet(heart_disease, fish).

% Rule to suggest diet based on disease
suggest_diet(Disease, Food) :-
    diet(Disease, Food).

% Rule to check whether a disease is available
available_disease(Disease) :-
    diet(Disease, _).
