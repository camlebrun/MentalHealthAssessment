import streamlit as st
st.title("PCL-5")
st.write("Post-traumatic stress disorder Checlist version DSM-5")
st.write("Consignes : Voici une liste de problèmes que les gens éprouvent parfois suite à une expérience vraiment stressante. Veuillez lire chaque énoncé attentivement et cocher la case pour indiquer dans quelle mesure ce problème vous a affecté dans le dernier mois")
questions = [
    {
        "question": "Des souvenirs répétés, pénibles et involontaires de l’expérience stressante ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Des rêves répétés et pénibles de l’expérience stressante ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Se sentir ou agir soudainement comme si vous viviez à nouveau l’expérience stressante ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Se sentir mal quand quelque chose vous rappelle l’événement ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Avoir de fortes réactions physiques lorsque quelque chose vous rappelle l’événement (accélération cardiaque, difficulté respiratoire, sudation) ?r",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Essayer d’éviter les souvenirs, pensées, et sentiments liés à l’événement ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Essayer d’éviter les personnes et les choses qui vous rappellent l’expérience stressante (lieux, personnes, activités, objets) ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Des croyances négatives sur vous-même, les autres, le monde (des croyances comme : je suis mauvais, j’ai quelque chose qui cloche, je ne peux avoir confiance en personne, le monde est dangereux) ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Vous blâmer ou blâmer quelqu’un d’autre pour l’événement ou ce qui s’est produit ensuite ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Avoir des sentiments négatifs intenses tels que peur, horreur, colère, culpabilité, ou honte ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Perdre de l’intérêt pour des activités que vous aimiez auparavant ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Vous sentir distant ou coupé des autres ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Avoir du mal à éprouver des sentiments positifs (par exemple être incapable de ressentir de la joie ou de l’amour envers vos proches) ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Comportement irritable, explosions de colère, ou agir agressivement ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Prendre des risques inconsidérés ou encore avoir des conduites qui pourraient vous mettre en danger ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Être en état de « super-alerte », hyper vigilant ou sur vos gardes ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Sursauter facilement ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": " Avoir du mal à vous concentrer ?",
        "options": [
            {"option": "Pas du tout", "weight": 0},
            {"option": "Un peu", "weight": 1},
            {"option": "Modérement", "weight": 2},
            {"option": "Beaucoup", "weight": 3},
            {"option": "Extrêmement", "weight": 4}
        ]
    },
    {
        "question": "Avoir du mal à trouver le sommeil ou à rester endormi ?",
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
        response = st.selectbox(
            "Votre réponse :", [
                option["option"] for option in question["options"]], key=f"radio-{i}")
        responses.append(response)
    st.metric("Score:", calculate_score(responses))


if __name__ == '__main__':
    main()
st.write("Hésitez pas à consulter un·e professionnel·le si vous avez besoin d'aide.")
st.warning(" SAMU : 15 ou 112", icon="⚠️")
st.warning(
    " Numéro national de prévention du suicide (24h/24 et 7j/7) 3114",
    icon="📞")
