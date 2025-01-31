import requests

username = input("Entrez le nom d\' un utilisateur : ")
url = f"https://api.github.com/users/{username}/events"
urlEvents = "https://raw.githubusercontent.com/shinnn/github-event-types/master/index.json"

#Récupération des informations de l'API
def get_activity():
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            activity = response.json()
            return activity
        else:
            print('Erreur : ', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur : ", e)
        return None

allEvents = requests.get(urlEvents).json()
activity = get_activity()

#Création d'un dictionnaire qui liste toutes les activités. Chaque activité a une liste liée
#qui contiendra d'autres listes pour chaque couple repo / comptage
usersActivity = {activ:[] for activ in allEvents}

#Pour chaque activités sorties de l'API, je récupère le repo, et j'ajoute le nom du répo + le nombre d'actions
#L'idée est d'avoir pour une activité (ex "PushEvent"), une liste de données :
#"PushEvent" : [["Repo 1", 2], ["Repo 2", 4]] ...
for i in range(len(activity)):
    acType = activity[i]["type"]
    
    repository = activity[i]["repo"]
    rep_found = False
                
    for dataRepo in usersActivity[acType]:
        if dataRepo[0] == repository['name']:
            dataRepo[1] += 1
            rep_found = True
            break
                
    if not rep_found:
        usersActivity[acType].append([repository['name'], 1])


#IA Generated
event_messages = {
    "CommitCommentEvent": "L'utilisateur a commenté un commit {x} fois pour le repo {y}.",
    "CreateEvent": "L'utilisateur a créé un référentiel, une branche ou une balise {x} fois pour le repo {y}.",
    "DeleteEvent": "L'utilisateur a supprimé une branche ou une balise {x} fois pour le repo {y}.",
    "PushEvent": "L'utilisateur a poussé des commits {x} fois vers le repo {y}.",
    "DeploymentEvent": "L'utilisateur a créé un déploiement {x} fois pour le repo {y}.",
    "DeploymentStatusEvent": "Un déploiement a changé de statut {x} fois pour le repo {y}.",
    "PageBuildEvent": "Une page GitHub Pages a été générée ou mise à jour {x} fois pour le repo {y}.",
    "ForkEvent": "L'utilisateur a forké le référentiel {y} {x} fois.",
    "ForkApplyEvent": "L'utilisateur a appliqué un patch depuis un fork {x} fois pour le repo {y}.",
    "PublicEvent": "L'utilisateur a rendu un repo public {x} fois.",
    "IssueCommentEvent": "L'utilisateur a commenté une issue {x} fois pour le repo {y}.",
    "IssuesEvent": "L'utilisateur a créé, fermé, rouvert ou modifié une issue {x} fois pour le repo {y}.",
    "PullRequestEvent": "L'utilisateur a ouvert, fermé, fusionné ou rouvert une pull request {x} fois pour le repo {y}.",
    "PullRequestReviewEvent": "L'utilisateur a soumis un examen de pull request {x} fois pour le repo {y}.",
    "PullRequestReviewCommentEvent": "L'utilisateur a commenté une review de pull request {x} fois pour le repo {y}.",
    "LabelEvent": "L'utilisateur a ajouté, modifié ou supprimé un label {x} fois pour le repo {y}.",
    "MilestoneEvent": "L'utilisateur a créé, modifié ou fermé un jalon {x} fois pour le repo {y}.",
    "MemberEvent": "L'utilisateur a ajouté ou retiré un membre {x} fois pour le repo {y}.",
    "MembershipEvent": "L'utilisateur a rejoint ou quitté une organisation ou une équipe {x} fois.",
    "TeamAddEvent": "Un référentiel a été ajouté à une équipe {x} fois.",
    "RepositoryEvent": "Le dépôt a été renommé, archivé, désarchivé ou supprimé {x} fois.",
    "ReleaseEvent": "L'utilisateur a publié, modifié ou supprimé une version {x} fois pour le repo {y}.",
    "FollowEvent": "L'utilisateur a suivi un autre utilisateur {x} fois.",
    "WatchEvent": "L'utilisateur a mis une étoile ⭐ sur un dépôt {x} fois.",
    "GollumEvent": "L'utilisateur a créé ou mis à jour une page wiki {x} fois pour le repo {y}.",
    "GistEvent": "L'utilisateur a créé, modifié ou supprimé un Gist {x} fois.",
    "DownloadEvent": "Un fichier a été téléchargé {x} fois depuis le repo {y}.",
    "StatusEvent": "Le statut d'un commit a changé {x} fois pour le repo {y}.",
}            

#Je crée un fichier txt pour stocker mes evenements
#Pour chaque type d'evenement et de repo dans le dictionnaire usersActivity, si on trouve l'evenement
#Dans le dictionnaire event_mesage, alors pour chaque repo présent dans cet evenement, 
#on écrit le compte et le nom du repo dans le fichier txt
with open(f"tracking/{username}.txt", "w", encoding="utf-8") as file:
    for eventType, repo in usersActivity.items():
        if eventType in event_messages:
            for repo_name, count in repo:
                file.write(f"{event_messages[eventType].format(x=count, y=repo_name)} \n")
                print(event_messages[eventType].format(x=count, y=repo_name))