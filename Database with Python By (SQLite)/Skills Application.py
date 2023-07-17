# Skill App
import sqlite3
db=sqlite3.connect("app.db")
uid=1
cr=db.cursor()

def save_close():
    db.commit()
    db.close()
    print("Connection is Closed")


input_mess="""
Enter char for The Option you want:
"S" => Show All Skills 
"A" => Add New Skill
"D" => Delete A Skill
"U" => Update A Skill
"Q" => Quit The App
"""
user_input=input(input_mess).strip().upper()
command_list=['S','A','D','U','Q']
def show_Skills():
    cr.execute(f"SELECT * FROM skills where user_id='{uid}'")
    results=cr.fetchall()
    print(f"You have {len(results)} Skills")
    if len(results) > 0 :
        print("Showing Skills with Progress :")
        for row in results:
            print(f"Skill = > {row[0]}",end=" ")
            print(f"Progress => {row[1]} %")
    save_close()
def Add_Skill():
    sk_name=input("Write Skill name").strip().capitalize()
    cr.execute(f"SELECT name From skills where name='{sk_name}' and user_id='{uid}'")
    results=cr.fetchone()
    if results == None:
        prog=input("Write Skill Prigress").strip()
        cr.execute(f"INSERT INTO skills (name,progress,user_id) values('{sk_name}',{prog},{uid})")
        print(f"Skill {sk_name} Added Successfully")
    else:
        ans=input("Skill is exist If you want to update it enter Yes else enter No").strip().capitalize()
        if ans=="Yes":
            sub_update(sk_name)

    save_close()
def delete_Skill():
    sk_name = input("Write Skill name You want to delete").strip().capitalize()
    cr.execute(f"DELETE FROM skills where name='{sk_name}' and user_id={uid}")
    print(f"Skill {sk_name} Deleted Successfully")
    save_close()
def update_Skill():
    skill_name=input("Enter Skill you want to update").strip().capitalize()
    sub_update(skill_name)
    save_close()
def sub_update(skill_name):
    prog = input("Enter the new Skill Progress ").strip()
    cr.execute(f"UPDATE skills SET progress='{prog}' where name='{skill_name}' and user_id='{uid}'")
    print(f"Skill {skill_name} Updated Successfully")

if user_input in command_list:
    print(f"Command {user_input} Found")
    if user_input=="S":
        show_Skills()
    elif user_input=="A":
        Add_Skill()
    elif user_input=="D":
        delete_Skill()
    elif user_input=="U":
        update_Skill()
    else:
        print("App is closed ")
        save_close()
        exit(0)
else :
    print(f"This Command {user_input} is Not Found")
