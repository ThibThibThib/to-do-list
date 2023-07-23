import sqlite3



def todolits():
    try:
        print("● Voir vos tâches (1)\n● Ajouter des tâches (2)\n● Supprimer une/toutes tâche(s) (3)\n")
        reponse_qst_start = input()
        print("")

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        def choix_page():
            print("Voulez vous changer de page pour voir vos autres task (oui / non)")
            reponse_autre = input()
            if reponse_autre == 'oui':
                print("Quelle page voulez vous obtenir ? (Page de base = 0)")
                page_reponse = int(input())
                print("")
                page_reponse = page_reponse * 10  
                req = cursor.execute('SELECT * FROM todolist LIMIT 10 OFFSET ' + str(page_reponse))

                for i in req.fetchall():
                    if i [1]:
                        print(i[1], "         ID :",i[0])
                
                choix_page
            elif reponse_autre == 'non':
                print("")
            else:
                print("Réponse invalide")


        def choix_page_mauvaise_endroit():
            print("Quelle page voulez vous obtenir ? (Page de base = 0)")
            page_reponse = int(input())
            print("")
            page_reponse = page_reponse * 10  
            req = cursor.execute('SELECT * FROM todolist LIMIT 10 OFFSET ' + str(page_reponse))

            for i in req.fetchall():
                if i [1]:
                    print(i[1], "         ID :",i[0])
            supprimer_bonne_page()



        if reponse_qst_start == '1' :
            req = cursor.execute('SELECT * FROM todolist LIMIT 10')

            for i in req.fetchall():
                if i [1]:
                    print(i[1], "         ID :",i[0])

            choix_page()

        elif reponse_qst_start == '2' :
            print("\nQuelle tâche voulez vous rajouter ?\n")
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
                    print("Remarque : Vous devez vous situez dans la page ou votre task est pour pouvoir la supprimer")
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
                    print("Voulez vous vraiment tout supprimer (oui / non)")
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

    except Exception as e:
        print("[ERREUR]", e)
        connection.rollback


    finally:
        connection.close()


todolits()
