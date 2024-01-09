# CYBERSENTINEL
Projet soutenance CDSD

Le but de la future application de détection d'intrusion est de détecter les attaques à "faible empreinte".

Les attaques à "faible empreinte" (ou "low footprint" en anglais) font référence à des méthodes d'attaque où l'attaquant essaie de laisser le moins de traces possibles ou d'avoir un impact minimal sur les ressources du système cible. L'objectif est souvent d'éviter la détection par les systèmes de sécurité traditionnels, tels que les IDS (systèmes de détection d'intrusion) ou les IPS (systèmes de prévention des intrusions).

Voici quelques caractéristiques des attaques à faible empreinte :

Discrétion : Les attaquants utilisent des méthodes qui génèrent peu ou pas de logs ou d'alertes. Par exemple, ils peuvent sonder un réseau très lentement pour éviter les seuils de détection.

Utilisation minimale des ressources : Plutôt que de lancer une attaque DDoS qui consommerait beaucoup de ressources, un attaquant pourrait utiliser une technique nécessitant moins de bande passante, de puissance de calcul ou d'autres ressources.

Éviter les comportements suspects : Les attaquants peuvent éviter d'utiliser des outils ou des techniques bien connus qui sont facilement détectables et opter pour des méthodes moins conventionnelles.

Utilisation d'outils polymorphes : Certains malwares peuvent changer leur signature ou leur comportement pour éviter la détection par des solutions basées sur des signatures.

Attaques ciblées : Plutôt que d'attaquer de nombreux systèmes, un attaquant pourrait cibler un système ou une ressource spécifique pour réduire la probabilité de détection.

L'objectif des attaquants utilisant des méthodes à faible empreinte est d'opérer sous le radar, d'éviter la détection aussi longtemps que possible, et d'atteindre leur objectif (qu'il s'agisse de voler des informations, d'installer un logiciel malveillant ou d'effectuer d'autres actions malveillantes) sans éveiller de soupçons.

Visualisations des attaques à faible empreinte dans les données réseau :

Discrétion : Observer les caractéristiques liées à la génération de logs ou d'alertes, comme la vitesse de sondage du réseau (par exemple, dur, Sload, Dload). Utilisez un graphique de ligne pour visualiser la variation de la durée de la transaction (dur) au fil du temps. Les transactions plus longues pourraient indiquer une discrétion accrue. Utilisez des histogrammes pour représenter la distribution de la bande passante (Sload, Dload). Des valeurs basses pourraient indiquer une discrétion en évitant une utilisation excessive de la bande passante.

Utilisation minimale des ressources : Analyser les caractéristiques liées à la consommation de ressources, telles que la bande passante (Sload, Dload), la puissance de calcul, et d'autres ressources spécifiques à votre système. Créez des diagrammes à barres pour comparer la consommation de ressources telles que la bande passante (Sload, Dload) entre différentes attaques. Recherchez des schémas où les attaques à faible empreinte consomment moins de ressources que d'autres types d'attaques.

Éviter les comportements suspects : Examiner les caractéristiques liées aux outils et techniques utilisés, en évitant ceux bien connus (par exemple, service, ct_flw_http_mthd). Utilisez des diagrammes à secteurs pour visualiser la répartition des services (service). Recherchez des services moins conventionnels qui pourraient indiquer des attaques à faible empreinte. Créez des graphiques en nuage de points pour explorer la relation entre le nombre de flux HTTP avec des méthodes telles que GET et POST (ct_flw_http_mthd) et d'autres caractéristiques.

Utilisation d'outils polymorphes : Rechercher des changements de signature ou de comportement, par exemple, en examinant les caractéristiques liées aux paquets et aux transactions (Spkts, Dpkts, trans_depth). Utilisez des graphiques de dispersion pour visualiser la relation entre le nombre de paquets (Spkts, Dpkts) et la taille moyenne des flux (smeansz, dmeansz). Des variations constantes pourraient indiquer l'utilisation de techniques polymorphes.

Attaques ciblées : Analyser les caractéristiques spécifiques à la cible, telles que les adresses IP (srcip, dstip), les ports (sport, dsport), et les services (service). Utilisez des cartes de chaleur pour représenter les fréquences des paires source-destination IP (srcip, dstip) et des ports (sport, dsport). Identifiez des concentrations élevées qui pourraient indiquer des attaques ciblées.


## MODELES DE MACHINE LEARNING
D'accord, nous allons tester plusieurs algorithmes pour déterminer lequel est le plus performant pour cette tâche de détection d'intrusion. Voici quelques points à considérer :
1.	KNN (k-Nearest Neighbors) : C'est un algorithme de classification basé sur la distance. Il pourrait être utile, mais il peut ne pas être le plus efficace en termes de temps de calcul avec de grands ensembles de données.
2.	DB-SCAN : C'est un algorithme de clustering. Il n'est pas typiquement utilisé pour la classification, mais il pourrait être utilisé pour identifier des groupes d'activités similaires dans les données.
3.	Régression linéaire : C'est généralement utilisé pour la régression (prédiction d'une valeur continue) et non pour la classification. Dans ce cas, nous voulons prédire une étiquette binaire (normal vs. attaque), donc ce n'est pas le meilleur choix.
4.	Arbres de décision, Forêts aléatoires et Machines à gradient boosting : Ce sont de bons choix pour la classification et peuvent gérer à la fois des caractéristiques numériques et catégorielles.
5.	Réseaux de neurones : Ils peuvent être puissants, mais nécessitent une optimisation et un réglage appropriés. Ils pourraient être un bon choix si les autres méthodes ne fonctionnent pas bien.

•	Machine à vecteurs de support (SVM) : Elle peut être efficace pour la classification binaire.
•	XGBoost : Une variante optimisée des machines à gradient boosting.
