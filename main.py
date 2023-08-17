import sqlite3

#Création de la to do list
def todolits():
    try:
        #Connexion à la db
        connection = sqlite3.connect("Saisir l'emplacement de votre fichier database.db")
        cursor = connection.cursor()

        #Choix de l'utilisateur parmit les 3 propositions
        print("● Voir vos tâches (1)\n● Ajouter des tâches (2)\n● Supprimer une/toutes tâche(s) (3)\n")
        reponse_qst_start = input()

        # Demande du choix de la page à l'utilisateur en fin de réponse (1)
        def choix_page():
            print("\nVoulez vous changer de page pour voir vos autres task (oui / non)")
            reponse_autre = input()
            if reponse_autre == 'oui':
                print("\nQuelle page voulez vous obtenir ? (Page de base = 0)")
                page_reponse = int(input())
                print("")
                page_reponse = page_reponse * 10  
                req = cursor.execute('SELECT * FROM todolist LIMIT 10 OFFSET ' + str(page_reponse))

                for i in req.fetchall():
                    if i [1]:
                        print(i[1], "         ID :",i[0])
                choix_page()

            elif reponse_autre == 'non':
                print("")
            else:
                print("Réponse invalide")

        #Demande du choix de page quand nous souhaitons supprimer un tache et quelle n'est pas dans la bonne page
        def choix_page_mauvaise_endroit():
            print("\nQuelle page voulez vous obtenir ? (Page de base = 0)")
            page_reponse = int(input())
            print("")
            page_reponse = page_reponse * 10  
            req = cursor.execute('SELECT * FROM todolist LIMIT 10 OFFSET ' + str(page_reponse))

            for i in req.fetchall():
                if i [1]:
                    print(i[1], "         ID :",i[0])
            supprimer_bonne_page()

        def ajout_autre_task_def():
            print("\nVeuillez écrire la task que vous souhaitez ajouter")
            name_task = input()
            cursor.execute(
                """
                INSERT INTO todolist (name_task)
                VALUES (?)
                """,
                (name_task,)
            )
            connection.commit()
            print("\nVotre tâche à été ajouté.")
            print("\nVoulez vous voir vos task ? (oui / non)")
            ajout_autre_task = input()
            if ajout_autre_task == 'oui':
                ajout_autre_task_def()
            elif ajout_autre_task == 'non':
                pass

        #Voir les tâches
        if reponse_qst_start == '1' :
            req = cursor.execute('SELECT * FROM todolist LIMIT 10')

            for i in req.fetchall():
                if i [1]:
                    print(i[1], "         ID :",i[0])
            choix_page()

        #Ajouter des tâches
        elif reponse_qst_start == '2' :
            print("\nVeuillez écrire la task que vous souhaitez ajouter")
            name_task = input()
            cursor.execute(
                """
                INSERT INTO todolist (name_task)
                VALUES (?)
                """,
                (name_task,)
            )
            connection.commit()
            print("\nVotre tâche à été ajouté.")
            print("\nSouhaitez vous rajouter une autre task ? (oui / non)")
            ajout_autre_task = input()
            if ajout_autre_task == 'oui':
                ajout_autre_task_def()
            elif ajout_autre_task == 'non':
                pass
            print("\nVoulez vous voir vos task ? (oui / non)")
            reponse_task_ajout = input()
            if reponse_task_ajout == 'oui':
                req = cursor.execute('SELECT * FROM todolist LIMIT 10')

                for i in req.fetchall():
                    if i [1]:
                        print(i[1], "         ID :",i[0])
                choix_page()
            elif reponse_task_ajout == 'non ':
                pass

        #Supprimer des tâches (une ou toute)            
        elif reponse_qst_start == '3' :
            print("")
            req = cursor.execute('SELECT * FROM todolist LIMIT 10')
            for i in req.fetchall():
                if i [1]:
                    print(i[1], "         ID :",i[0])
            print("")
            print("Voulez vous supprimer une task (1) ou toute (2) ?")
            reponse_1_2 = input()
            
            def supprimer_bonne_page() :
                if reponse_1_2 == '1' :
                    print("Remarque : Vous devez vous situez dans la page ou votre task est situé pour pouvoir la supprimer")
                    print("êtes vous dans la bonne page de votre task? (oui / non)")
                    reponse_mauvaise_endroit = input()
                    if reponse_mauvaise_endroit == 'oui':
                        print("Veuillez saisir l'ID de la task que vous voulez supprimier")
                        choix_task = int(input(""))
                        cursor.execute('DELETE FROM todolist WHERE id_task = '+ str(choix_task))
                        connection.commit()
                        print("Votre task a été supprimer")
                    elif reponse_mauvaise_endroit == 'non' :
                        choix_page_mauvaise_endroit()
                elif reponse_1_2 == '2' :
                    print("\nVoulez vous vraiment tout supprimer (oui / non)")
                    qst_sur = input()
                    if qst_sur=='oui':
                        cursor.execute('DELETE FROM todolist')
                        connection.commit()
                        print("Toute vos task on été supprimer")
                    elif qst_sur == 'non' :
                        print("Rien n'a était supprimer")
                    else :
                        print("Votre réponse est invalide rien n'a été supprimer")
                else :
                    print("Votre réponse est invalide")
            supprimer_bonne_page()
        else:
            print("Votre réponse est invalide")

    #Si erreur
    except Exception as e:
        print("[ERREUR]", e)
        connection.rollback

    #Fin du programme fermeture de la db
    finally:
        connection.close()

todolits()
