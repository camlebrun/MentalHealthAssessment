import streamlit as st
st.title("BDI-2 - Inventaire de dépression de Beck")
questions = [
    {
        "question": "Tristesse",
        "options": [
            {"option": "Je ne me sens pas triste", "weight": 0},
            {"option": "Je me sens très souvent triste", "weight": 1},
            {"option": "Je suis tout le temps triste", "weight": 2},
            {"option": "Je suis si triste ou si malheureux(se) que ce n'est pas supportable", "weight": 3}
        ]
    },
    {
        "question": "Pessimisme",
        "options": [
            {"option": "Je ne suis pas découragé·e face à mon avenir", "weight": 0},
            {"option": "Je me sens plus découragé·e qu'avant face à mon avenir", "weight": 1},
            {"option": "Je ne m'attends pas à ce que les choses s'arrangent pour moi", "weight": 2},
            {"option": "J'ai le sentiment que mon avenir est sans espoir et qu'il ne peut qu'empirer", "weight": 3}
        ]
    },
        {
        "question": "Échecs dans le passé",
        "options": [
            {"option": "Je n'ai pas le sentiment d'avoir échoué dans la vie, d'être un·e raté·e", "weight": 0},
            {"option": "UJ'ai échoué plus souvent que je n'aurais dû", "weight": 1},
            {"option": "Quand je pense à mon passé, je constate un grand nombre d'échecs", "weight": 2},
            {"option": "J'ai le sentiment d'avoir complètement raté ma vie", "weight": 3}
        ]
    },
        {
        "question": "Perte de plaisir",
        "options": [
            {"option": "J'éprouve toujours autant de plaisir qu'avant aux choses qui me plaisent", "weight": 0},
            {"option": "Je n'éprouve pas autant de plaisir aux choses qu'avant", "weight": 1},
            {"option": "J'éprouve très peu de plaisir aux choses qui me plaisaient habituellement", "weight": 2},
            {"option": "Je n'éprouve aucun plaisir aux choses qui me plaisaient habituellement", "weight": 3}
        ]
    },
        {
        "question": "Sentiments de culpabilité",
        "options": [
            {"option": "Je ne me sens pas particulièrement coupable", "weight": 0},
            {"option": "Je me sens coupable pour bien des choses que j'ai faites ou que j'aurais dû faire", "weight": 1},
            {"option": "Je me sens coupable la plupart du temps", "weight": 2},
            {"option": "Je me sens tout le temps coupable", "weight": 3}
        ]
    },
        {
        "question": "Sentiment d'être puni·e",
        "options": [
            {"option": "Je n'ai pas le sentiment d'être puni·e", "weight": 0},
            {"option": "Je sens que je pourrais être puni·e", "weight": 1},
            {"option": "Je m'attends à être puni·e", "weight": 2},
            {"option": "Je ne m'aime pas du tout", "weight": 3}
        ]
    },
        {
        "question": "Sentiments négatifs envers soi-même",
        "options": [
            {"option": "Mes sentiments envers moi-même n'ont pas changé", "weight": 0},
            {"option": "J'ai perdu confiance en moi", "weight": 1},
            {"option": "Je suis déçu·e par moi-même", "weight": 2},
            {"option": "Je ne m'aime pas du tout", "weight": 3}
        ]
    },
         {   
        "question": "Attitude critique envers soi",
        "options": [
            {"option": "Je ne me blâme pas ou ne me critique pas plus que d'habitude", "weight": 0},
            {"option": "Je suis plus critique envers moi-même que je ne l'étais", "weight": 1},
            {"option": "Je me reproche tous mes défauts", "weight": 2},
            {"option": "Je me reproche tous les malheurs qui arrivent", "weight": 3}
        ]
    },
             {   
        "question": "Pensées ou désirs de suicide",
        "options": [
            {"option": "Je ne pense pas du tout à me suicider", "weight": 0},
            {"option": "Il m'arrive de penser à me suicider, mais je ne le ferai pas", "weight": 1},
            {"option": "J'aimerais me suicider", "weight": 2},
            {"option": "Je me suiciderais si l'occasion se présentait", "weight": 3}
        ]
    },
             {   
        "question": "Pleurs",
        "options": [
            {"option": "Je ne pleure pas plus qu'avant", "weight": 0},
            {"option": "Je pleure plus qu'avant", "weight": 1},
            {"option": "Je pleure pour la moindre petite chose", "weight": 2},
            {"option": "Je voudrais pleurer mais je ne suis pas capable", "weight": 3}
        ]
    },
             {   
        "question": "Agitation",
        "options": [
            {"option": "Je ne suis pas plus agité·e ou plus tendu·e que d'habitude", "weight": 0},
            {"option": "Je me sens plus agité·e ou plus tendu·e que d'habitude", "weight": 1},
            {"option": "Je suis si agité·e ou tendu·e que j'ai du mal à rester tranquille", "weight": 2},
            {"option": "Je suis si agité·e ou tendu·e que je dois continuellement bouger ou faire quelque chose", "weight": 3}
        ]
    },
             {   
        "question": "Perte d'intérêt",
        "options": [
            {"option": "Je n'ai pas perdu d'intérêt pour les gens ou pour les activités", "weight": 0},
            {"option": "Je m'intéresse moins qu'avant aux gens et aux choses", "weight": 1},
            {"option": "Je ne m'intéresse presque plus aux gens et aux choses", "weight": 2},
            {"option": "J'ai du mal à m'intéresser à quoique ce soit", "weight": 3}
        ]
    },
        {   
        "question": "Indécision",
        "options": [
            {"option": "Je prends des décisions toujours aussi bien qu'avant", "weight": 0},
            {"option": "Il m'est plus difficile que d'habitude de prendre des décisions", "weight": 1},
            {"option": "J'ai beaucoup plus de mal qu'avant à prendre des décisions", "weight": 2},
            {"option": "J'ai du mal à prendre n'importe quelle décision", "weight": 3}
        ]
    },
             {   
        "question": "Dévalorisation",
        "options": [
            {"option": "Je pense être quelqu'un de valable", "weight": 0},
            {"option": "Je ne crois pas avoir autant de valeur ni être aussi utile qu'avant", "weight": 1},
            {"option": "Je me sens moins valable que les autres", "weight": 2},
            {"option": "Je sens que je ne vaux absolument rien", "weight": 3}
        ]
    },
             {   
        "question": "Perte d'énergie",
        "options": [
            {"option": "J'ai toujours autant d'énergie qu'avant", "weight": 0},
            {"option": "J'ai moins d'énergie qu'avant", "weight": 1},
            {"option": "Je n'ai pas assez d'énergie pour pouvoir faire grand-chose", "weight": 2},
            {"option": "J'ai trop peu d'énergie pour faire quoi que ce soit", "weight": 3}
        ]
    },
             {   
        "question": "Modifications dans les habitudes de sommeil",
        "options": [
            {"option": "Mes habitudes de sommeil n'ont pas changé", "weight": 0},
            {"option": "Je dors un peu plus que d'habitude", "weight": 1},
            {"option": "Je dors un peu moins que d'habitude", "weight": 1},
            {"option": "Je dors beaucoup plus que d'habitude", "weight": 2},
            {"option": "Je dors beaucoup moins que d'habitude", "weight": 2},
            {"option": "Je dors presque toute la journée", "weight": 3},
            {"option": "Je me réveille une ou deux heures plus tôt et je suis incapable de me rendormir", "weight": 3}
        ]
    },
                 {   
        "question": "Irritabilité",
        "options": [
            {"option": "Je ne suis pas plus irritable que d'habitude", "weight": 0},
            {"option": "Je suis plus irritable que d'habitude", "weight": 1},
            {"option": "Je suis beaucoup plus irritable que d'habitude", "weight": 2},
            {"option": "Je suis constamment irritable", "weight": 3}
        ]
    },
             {   
        "question": "Modifications de l'appétit",
        "options": [
            {"option": " Mon appétit n'a pas changé", "weight": 0},
            {"option": "J'ai un peu moins d'appétit que d'habitude", "weight": 1},
            {"option": "J'ai un peu plus d'appétit que d'habitude", "weight": 1},
            {"option": "J'ai beaucoup moins d'appétit que d'habitude", "weight": 2},
            {"option": "J'ai beaucoup plus d'appétit que d'habitude", "weight": 2},
            {"option": "Je n'ai pas d'appétit du tout", "weight": 3},
            {"option": "J'ai constamment envie de manger", "weight": 3}
        ]
    },
             {   
        "question": "Difficulté à se concentrer",
        "options": [
            {"option": "Je parviens à me concentrer toujours aussi bien qu'avant", "weight": 0},
            {"option": " Je ne parviens pas à me concentrer aussi bien que d'habitude", "weight": 1},
            {"option": "J'ai du mal à me concentrer longtemps sur quoi que ce soit", "weight": 2},
            {"option": "Je me trouve incapable de me concentrer sur quoi que ce soit", "weight": 3}
        ]
    },
             {   
        "question": "Fatigue",
        "options": [
            {"option": "Je ne suis pas plus fatiqué·e que d'habitude", "weight": 0},
            {"option": "Je me fatigue plus facilement que d'habitude", "weight": 1},
            {"option": "Je suis trop fatigué·e pour faire un grand nombre de choses que je faisais avant", "weight": 2},
            {"option": "Je suis trop fatigué·e pour faire la plupart des choses que je faisais avant", "weight": 3}
        ]
    },
                 {   
        "question": "Perte d'intérêt pour le sexe",
        "options": [
            {"option": "Je n'ai pas noté de changement récent dans mon intérêt pour le sexe", "weight": 0},
            {"option": "Le sexe m'intéresse moins qu'avant", "weight": 1},
            {"option": "Le sexe m'intéresse beaucoup moins maintenant", "weight": 2},
            {"option":"J'ai perdu tout intérêt pour le sexe", "weight": 3}
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
    st.metric("Score:", calculate_score(responses))
    if calculate_score(responses) <= 9:
        st.write("Score normal")
    elif calculate_score(responses) in range(10, 19):
        st.write("Dépression légère, consulter un·e professionnel·e de santé ")
    elif calculate_score(responses) in range(11, 30):
        st.write("Dépression modérée, consulter un·e professionnel·e de santé ")
    else :
        st.write("Dépression sévère, consulter un·e professionnel·e de santé ")


if __name__ == '__main__':
    main()