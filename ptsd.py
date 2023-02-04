import streamlit as st

questions = [
    {
        "question": "Tout rappel de l’événement ravivait mes sentiments face à l’événement",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Je me réveillais la nuit",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
        {
        "question": "Différentes choses m’y faisait penser",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
        {
        "question": "Je me sentais irritable et en colère",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
        {
        "question": "Quand j’y repensais ou qu’on me le rappelait, j’évitais de me laisser bouleverser",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
        {
        "question": "Sans le vouloir, j’y repensais",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
        {
        "question": "J’ai eu l’impression que l’événement n’était jamais arrivé ou n’était pas réel",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
         {   
        "question": "Je me suis tenu(e) loin de ce qui m’y faisait penser",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
             {   
        "question": "Des images de l’événement surgissaient dans ma tête",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
             {   
        "question": "J’étais nerveux (nerveuse) et j’ai sursautais facilement",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
             {   
        "question": "J’essayais de ne pas y penser",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
             {   
        "question": "J’étais conscient(e) d’avoir encore beaucoup d’émotions à propos de l’événement, mais je n’y ai pas fait face",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
             {   
        "question": "Mes sentiments à propos de l’événement étaient comme figés",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
             {   
        "question": "Je me sentais et je réagissais comme si j’étais encore dans l’événement",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
             {   
        "question": "J’avais du mal à m’endormir",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
             {   
        "question": "J’ai ressenti des vagues de sentiments intenses à propos de l’événement",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
                 {   
        "question": "J’ai essayé de l’effacer de ma mémoire",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
             {   
        "question": "J’avais du mal à me concentrer",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
             {   
        "question": "Ce qui me rappelait l’événement me causait des réactions physiques telles que des sueurs, des difficultés à respirer, des nausées ou des palpitations",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
             {   
        "question": "J’ai rêvé à l’événement",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
                 {   
        "question": "J’étais aux aguets, sur mes gardes",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    }

]

def calculate_score(responses):
    score = 0
    for i, response in enumerate(responses):
        for option in questions[i]["options"]:
            if option["option"] == response:
                score += option["weight"]
                break
    return score

def main():
    responses = []
    for i, question in enumerate(questions):
        st.write("Question :", question["question"])
        response = st.radio("Votre réponse :", [option["option"] for option in question["options"]], key=f"radio-{i}")
        responses.append(response)
    st.write("Score:", calculate_score(responses))

if __name__ == '__main__':
    main()
