from db import *
import tkinter as tk
from tkinter import *

from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
import pygame


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Login")
        self.root.iconbitmap('./icons/earth.ico')
        self.setup_login_page()
        self.ajout = tk.NORMAL
        self.mod = tk.NORMAL
        self.sup = tk.NORMAL
        self.i=0
        self.current_record_id = None
        # Start the main event loop
        self.root.mainloop()

    def setup_login_page(self):
        # Clear any existing widgets
        self.clear_widgets()
        #Title
        self.title=tk.Label(self.root,text="Choisir la maniere que vous voulez d'authentifier ",font=('Serif',20,'bold'))
        self.title.grid(row=0,columnspan=4, pady=10, sticky="nsew")

        # ----ADMIN-----
        # Load and resize the image
        self.admin = Image.open('./icons/utilisateur.png')
        self.admin_resize = self.admin.resize((180, 120))
        self.admin_pic = ImageTk.PhotoImage(self.admin_resize)
        
        # Create the image label and button for Admin
        self.admin_image_label = tk.Label(self.root, image=self.admin_pic)
        self.admin_image_label.grid(rowspan=2, row=2, column=0, padx=10, pady=10)
        
        self.admin_button = tk.Button(self.root, text='Admin', command=self.admin_button_click)
        self.admin_button.grid(row=4, column=0, padx=10, pady=10)

        # -----UTILISATEUR-----
        self.user = Image.open('./icons/images.png')
        self.user_resize = self.user.resize((180, 120))
        self.user_pic = ImageTk.PhotoImage(self.user_resize)
        
        # Create the image label and button for Utilisateur
        self.user_image_label = tk.Label(self.root, image=self.user_pic)
        self.user_image_label.grid(rowspan=2, row=2, column=3, padx=10, pady=10)
        
        self.user_button = tk.Button(self.root, text='Utilisateur', command=self.user_button_click)
        self.user_button.grid(row=4, column=3, padx=10, pady=10)

        #------Quiter l'interface 
        self.quiter=tk.Button(self.root,text="Quiter l'application",command=self.dec)
        self.quiter.grid(rowspan=2,row=6,column=1)


    def dec(self):
        res=messagebox.askyesno(
             title='Deconnexion',
             message="veux-tu quitter l'application?",
          )
        if  res:
          messagebox.showinfo("Deconnexion","Merci pour votre visite \U0001F600")
          exit()

    def admin_button_click(self):
        # Placeholder function to handle the click event of the Admin button
         # Placeholder labels and entries for username and password
        self.admin_image_label.grid(rowspan=2, row=0, column=0, padx=10, pady=10)
        self.quiter.grid(row=2,column=0)
        self.label_nom = tk.Label(self.root, text="Nom Utilisateur")
        self.nom = tk.Entry(self.root)

        self.label_pdw = tk.Label(self.root, text="Mot de passe")
        self.pdw = tk.Entry(self.root, show="*")

        self.login_button = tk.Button(self.root, text="Authentifier", command=self.authentication_admin)
        self.cache = Image.open('./icons/cache.png')
        self.cache_resize = self.cache.resize((20, 20))
        self.cache_pic = ImageTk.PhotoImage(self.cache_resize) 
        self.show_pdw=tk.Checkbutton(self.root,command=self.show,image=self.cache_pic)

        # Arrange widgets using grid layout
        self.label_nom.grid(row=0, column=1, padx=10, pady=5)
        self.nom.grid(row=0, column=2, padx=10, pady=5)
        self.label_pdw.grid(row=1, column=1, padx=10, pady=5)
        self.pdw.grid(row=1, column=2, padx=10, pady=5)
        self.login_button.grid(row=2, column=3, padx=10, pady=10)
        self.show_pdw.grid(row=1, column=3, padx=10, pady=5)

        self.title.destroy()
        self.admin_button.destroy()
        self.user_image_label.destroy()
        self.user_button.destroy()
        self.back=tk.Button(text='Menu',command=self.setup_login_page)
        self.back.grid(row=2, column=1, padx=10, pady=10)

    def user_button_click(self):
       
        # Placeholder function to handle the click event of the Utilisateur button
         # Placeholder labels and entries for username and password
        self.user_image_label.grid(rowspan=2, row=0, column=0, padx=10, pady=10)
        self.quiter.grid(row=2,column=0)
        self.user_button.grid(row=2, column=0, padx=10, pady=10)
        self.label_nom = tk.Label(self.root, text="Nom Utilisateur")
        self.nom = tk.Entry(self.root)

        self.label_pdw = tk.Label(self.root, text="Mot de passe")
        self.pdw = tk.Entry(self.root, show="*")

        self.login_button = tk.Button(self.root, text="Authentifier", command=self.authentication_user)
        self.show_pdw=tk.Checkbutton(self.root,command=self.show)
        self.cache = Image.open('./icons/cache.png')
        self.cache_resize = self.cache.resize((20, 20))
        self.cache_pic = ImageTk.PhotoImage(self.cache_resize)
        self.show_pdw.config(image=self.cache_pic)

        # Arrange widgets using grid layout
        self.label_nom.grid(row=0, column=1, padx=10, pady=5)
        self.nom.grid(row=0, column=2, padx=10, pady=5)
        self.label_pdw.grid(row=1, column=1, padx=10, pady=5)
        self.pdw.grid(row=1, column=2, padx=10, pady=5)
        self.login_button.grid(row=2, column=3, padx=10, pady=10)
        self.show_pdw.grid(row=1, column=3, padx=10, pady=5)
        
        self.title.destroy()
        self.user_button.destroy()
        self.admin_image_label.destroy()
        self.admin_button.destroy()
        self.back=tk.Button(text='Menu',command=self.setup_login_page)
        self.back.grid(row=2, column=1, padx=10, pady=10)

    def authentication_admin(self):
        global username
        # Placeholder authentication logic
        username = self.nom.get()
        password = self.pdw.get()

        # Replace the following with your actual authentication logic

        mycursor.execute("SELECT * FROM admin WHERE username=%s AND pdw=%s ",(username,password))
        res=mycursor.fetchall()
        if res:
            messagebox.showinfo("Succes",f" Bienvenu  Admin {username} ")
            self.nom.delete(0, tk.END)
            self.pdw.delete(0, tk.END)
            self.clear_widgets()
            self.create_widgets()
            self.lister()
            self.display_record()
             
        elif username=="":
           messagebox.showerror("Erreur","S'il vous plait remplire le champ nom utilisateur")

        elif password=="":
           messagebox.showerror("Erreur","S'il vous plait entrer un mot de passe")

    def authentication_user(self):
        global username
        # Placeholder authentication logic
        username = self.nom.get()
        password = self.pdw.get()

        # Replace the following with your actual authentication logic
        if (username != "" and password != "") :
            messagebox.showinfo("Succes",f" Bienvenu {username} ")
            self.nom.delete(0, tk.END)
            self.pdw.delete(0, tk.END)
            self.clear_widgets()
            self.create_widgets()
            self.ajout.config(state=tk.DISABLED)
            self.val.config(state=tk.DISABLED)
            self.mod.config(state=tk.DISABLED)
            self.sup.config(state=tk.DISABLED)
            self.but_flag.config(state=tk.DISABLED)
            self.load_button.config(state=tk.DISABLED)
            self.lister()  
            self.display_record()
        elif username=="":
           messagebox.showerror("Erreur","S'il vous plait remplire le champ nom utilisateur")

        elif password=="":
           messagebox.showerror("Erreur","S'il vous plait entrer un mot de passe")

    def clear_widgets(self):
        # Clear all widgets on the current page
        for widget in self.root.winfo_children():
            widget.destroy()

    def show(self):
        current_show_state = self.pdw.cget("show")
        if current_show_state == '*':
            self.visible = Image.open('./icons/visible.png')
            self.visible_resize = self.visible.resize((20, 20))
            self.visible_pic = ImageTk.PhotoImage(self.visible_resize)
            # If currently hidden, show the password
            self.pdw.config(show='')
            self.show_pdw.config(text="",image=self.visible_pic)
            
        else:
            self.cache = Image.open('./icons/cache.png')
            self.cache_resize = self.cache.resize((20, 20))
            self.cache_pic = ImageTk.PhotoImage(self.cache_resize)
            # If currently shown, hide the password

            self.pdw.config(show='*')
            self.show_pdw.config(text="",image=self.cache_pic)


    def lister(self):
        global flag
       
        mycursor.execute("SELECT * FROM pay")
        res=mycursor.fetchall()
        if res:
           for i in res:
                 # print(i)
                #   self.pay_input.insert(END,i[0])
                  self.nom_input.delete(0,tk.END)
                  self.nom_input.insert(tk.END,i[1].capitalize())
                  self.capital_input.delete(0,tk.END)
                  self.capital_input.insert(tk.END,i[2].capitalize())
                  self.population_input.delete(0,tk.END)
                  self.population_input.insert(tk.END,i[3])
                  self.continent_input.delete(0,tk.END)
                  self.continent_input.insert(tk.END,i[4].capitalize()) 
                  image_path =i[5]
                  sound_path=i[6]
                  pygame.mixer.init()
                  if image_path and sound_path:
                    # ----- get the flag from data base
                    flag = Image.open(image_path)
                    flag = flag.resize((150, 100))
                    flag = ImageTk.PhotoImage(flag)
                    self.label=tk.Label(image=flag,width=200,height=100)
                    self.label.grid(row=5,column=3)
                    #------get the sound from data base
                    pygame.mixer.music.load(sound_path)
                    name=sound_path.split("/")
                    name=name[-1]
                    self.name_mp3=tk.Label(self.root,text=f"{name}",fg="#c2960f",font=('Serif',20,'bold'))
                    self.name_mp3.grid(row=6,column=3)


    

    def insert_image(self):
        global filename,img
        self.f_types=[('Png files','*.png'),('Jpg files','*.jpg')]
        filename=filedialog.askopenfilename(filetypes=self.f_types)
        if(filename):
                    
                    img=Image.open(filename)
                    img=img.resize((150,100))
                    img=ImageTk.PhotoImage(img)
                    self.but_flag.config(image=img, text="")
                    self.label=tk.Label(image=img,width=220,height=100)
                    self.label.grid(row=5,column=3)
       

    def load_music(self):
        global file_path 
        pygame.mixer.init()
        file_path = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
                
                pygame.mixer.music.load(file_path)
                name=file_path.split("/")
                name=name[-1]
            # print(f"Loaded: {name}")
             
                self.name_mp3=tk.Label(text=f"{name}",fg="#c2960f",font=('Serif',20,'bold'))
                self.name_mp3.grid(row=6,column=3,padx=(2, 0.1), pady=5)


    def ajouter(self):
            
            self.clear()
            self.val.config(state=tk.ACTIVE)
            self.ajout=tk.ACTIVE
           
        
            
    def supprimer(self):
        #if self.check_admin():
           
            self.clear()
            self.val.config(state=tk.ACTIVE)
            self.sup=tk.ACTIVE
                
            
    def modifier(self):
        #if self.check_admin():
            self.clear()
            self.val.config(state=tk.ACTIVE)
            self.mod=tk.ACTIVE
          
            

    def valider(self):
        nom=self.nom_input.get()
        nom_pay=nom.lower()
        mycursor.execute("SELECT * FROM pay WHERE nom=%s",(nom_pay,))
        res=mycursor.fetchall()
        # print("Button States:", self.ajout, self.mod, self.sup)
        if not(res) and self.ajout==tk.ACTIVE:
            nom=self.nom_input.get().lower()
            capitale=self.capital_input.get().lower()
            population=self.population_input.get()
            continent=self.continent_input.get().lower()
            image=filename
            song=file_path
           
            mycursor.execute("INSERT INTO pay (nom,capitale,population,continent,image,audio) VALUES (%s,%s,%s,%s,%s,%s) ",(nom,capitale,population,continent,image,song,))
            conn.commit()

            message=f"La pay {nom} a bien ajouter"
            messagebox.showinfo("Valider",message)
            self.clear()
            self.ajout=tk.NORMAL
            self.val.config(state=tk.DISABLED)

        elif res and  self.ajout==tk.ACTIVE:

            messagebox.showwarning('',f"{nom} est déjà ajouter")

        elif res and self.mod==tk.ACTIVE:

            nom=self.nom_input.get().lower()
            capitale=self.capital_input.get().lower()
            population=int(self.population_input.get())
            continent=self.continent_input.get().lower()
            image=filename
            song=file_path
            mycursor.execute("UPDATE  pay SET nom=%s , capitale=%s , population=%s , continent=%s , image=%s , audio=%s WHERE nom=%s",(nom,capitale,population,continent,image,song,nom,))
            conn.commit()
            message=f"La modification bien fait"
            messagebox.showinfo("Valider",message)
            self.mod=tk.NORMAL
            self.clear()
            self.val.config(state=tk.DISABLED)

        
        elif not(res) and self.mod==tk.ACTIVE:
             messagebox.showwarning('',f" Impossible de fait la modification car {nom} pas encore ajouter  ")

        elif res and self.sup==tk.ACTIVE:
            nom=self.nom_input.get().lower()
            capitale=self.capital_input.get().lower()
            population=int(self.population_input.get())
            continent=self.continent_input.get().lower()
            image=filename
            song=file_path
            mycursor.execute("DELETE FROM  pay WHERE nom=%s AND capitale=%s AND population=%s AND continent=%s AND image=%s AND audio=%s",(nom,capitale,population,continent,image,song,))
            conn.commit()

            message=f"La pay {nom} a ete supprimer"
            messagebox.showinfo("Valider",message)
            self.sup=tk.NORMAL
            self.clear()
            self.val.config(state=tk.DISABLED)

        elif res and self.sup==tk.ACTIVE:
             messagebox.showwarning('',f" Impossible de supprimer {nom} car pas encore ajouter  ")

        else:
            messagebox.showerror("Ereur","Aucune action spécifique à valider")




    def clear(self):
        self.nom_input.delete(0,tk.END)
        self.capital_input.delete(0,tk.END)
        self.population_input.delete(0,tk.END)
        self.continent_input.delete(0,tk.END)
        if hasattr(self, 'label') and self.label is not None:
           self.label.destroy()

        
        self.name_mp3.destroy()
        self.but_flag.config(image=None, text="Insert le drapeau")
        self.but_flag=tk.Button(self.root,text='Insert le drapeau', command=self.insert_image,width=30)
        self.but_flag.grid(row=5,column=3,padx=(1, 0.1), pady=4)

        
        self.load_button =tk.Button(self.root, text="+l'hymne nationale",command=self.load_music,width=30)
        self.load_button.grid(row=6,column=3,padx=(2, 0.1), pady=5)

 
    def search_pay(self):
        global flag
        nom_pay=self.pay_input.get()
        mycursor.execute("SELECT * FROM pay WHERE nom= '"+nom_pay +"'")
        res=mycursor.fetchall()
        if res:
           for i in res:
                 # print(i)
                  self.pay_input.delete(0,tk.END)
                #   self.pay_input.insert(END,i[0])
                  self.nom_input.delete(0,tk.END)
                  self.nom_input.insert(tk.END,i[1].capitalize())
                  self.capital_input.delete(0,tk.END)
                  self.capital_input.insert(tk.END,i[2].capitalize())
                  self.population_input.delete(0,tk.END)
                  self.population_input.insert(tk.END,i[3])
                  self.continent_input.delete(0,tk.END)
                  self.continent_input.insert(tk.END,i[4].capitalize()) 
                  image_path =i[5]
                  sound_path=i[6]
                  pygame.mixer.init()
                  if image_path and sound_path:
                    # ----- get the flag from data base
                    flag = Image.open(image_path)
                    flag = flag.resize((150, 100))
                    flag = ImageTk.PhotoImage(flag)
                    self.label=tk.Label(image=flag,width=200,height=100)
                    self.label.grid(row=5,column=3)
                    #------get the sound from data base
                    pygame.mixer.music.load(sound_path)
                    name=sound_path.split("/")
                    name=name[-1]
                    self.name_mp3=tk.Label(self.root,text=f"{name}",fg="#c2960f",font=('Serif',20,'bold'))
                    self.name_mp3.grid(row=6,column=3)

        else:
           self.pay_input.delete(0,tk.END)
           #self.pay_input.insert(END,"Pays introvable")
           messagebox.showerror("Ereur",f"Pays introuvable \N{angry face}")

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.init()
        pygame.mixer.music.stop()

    def display_record(self, offset=0, pays=None):
      global flag
      self.nom_input.delete(0,tk.END)
      self.capital_input.delete(0,tk.END)
      self.population_input.delete(0,tk.END)
      self.continent_input.delete(0,tk.END)

      if pays:
        print("Débogage : Affichage du tuple pays :", pays)
        self.current_record_id = pays[0]
        self.nom_input.insert(0, pays[1])
        self.capital_input.insert(0, pays[2])
        self.continent_input.insert(0, pays[4])  # Assuming you want the continent, adjust the index here
        self.population_input.insert(0, pays[3])
        image_path =pays[5]
        sound_path=pays[6]
        pygame.mixer.init()
        if image_path and sound_path:
                    # ----- get the flag from data base
            flag = Image.open(image_path)
            flag = flag.resize((150, 100))
            flag = ImageTk.PhotoImage(flag)
            self.label=tk.Label(image=flag,width=200,height=100)
            self.label.grid(row=5,column=3)
            #------get the sound from data base
            pygame.mixer.music.load(sound_path)
            name=sound_path.split("/")
            name=name[-1]
            self.name_mp3=tk.Label(self.root,text=f"{name}",fg="#c2960f",font=('Serif',20,'bold'))
            self.name_mp3.grid(row=6,column=3)

      else:
        if hasattr(self, 'search_results') and self.i < len(self.search_pay):
            # Display the next result from the search
            self.display_record(offset=self.i, pays=self.search_pay[self.i])
            self.btn_b4.config(state=tk.NORMAL)
        else:
            # Display the next result from the database
            mycursor.execute('SELECT * FROM pay LIMIT 1 OFFSET %s', (offset,))
            pays =mycursor.fetchone()
            conn.commit()

            if pays:
                self.current_record_id = pays[0]
                self.nom_input.insert(0, pays[1])
                self.capital_input.insert(0, pays[2])
                self.continent_input.insert(0, pays[4])  # Assuming you want the continent, adjust the index here
                self.population_input.insert(0, pays[3])
                image_path =pays[5]
                sound_path=pays[6]
                pygame.mixer.init()
                if image_path and sound_path:
                    # ----- get the flag from data base
                    flag = Image.open(image_path)
                    flag = flag.resize((150, 100))
                    flag = ImageTk.PhotoImage(flag)
                    self.label=tk.Label(image=flag,width=200,height=100)
                    self.label.grid(row=5,column=3)
                    #------get the sound from data base
                    pygame.mixer.music.load(sound_path)
                    name=sound_path.split("/")
                    name=name[-1]
                    self.name_mp3=tk.Label(self.root,text=f"{name}",fg="#c2960f",font=('Serif',20,'bold'))
                    self.name_mp3.grid(row=6,column=3)

            else:
                # Handle the case when there are no more records
                messagebox.showinfo("Fin", "Tous les pays sans afficher")
    def next_button(self):
      self.i += 1
      self.display_record(offset=self.i)

      mycursor.execute('SELECT * FROM pay LIMIT 1 OFFSET %s', (self.i,))
      next_row =mycursor.fetchone()
    

      if not next_row:
          self.btn_b1.config(state=tk.DISABLED)

      self.btn_b4.config(state=tk.NORMAL)
      conn.commit()


    def previous_button(self):
        if self.i > 0:
            self.i -= 1
            self.display_record(offset=self.i)

        self.btn_b1.config(state=tk.NORMAL)

        if self.i == 0:
            self.btn_b4.config(state=tk.DISABLED)
            conn.commit()



    def first_contry(self):
        global flag
        mycursor.execute("SELECT * FROM pay ORDER BY id ASC LIMIT 1")
        res=mycursor.fetchall()
        for i in res:
                 # print(i)
                #   self.pay_input.insert(END,i[0])
                  self.nom_input.delete(0,tk.END)
                  self.nom_input.insert(tk.END,i[1].capitalize())
                  self.capital_input.delete(0,tk.END)
                  self.capital_input.insert(tk.END,i[2].capitalize())
                  self.population_input.delete(0,tk.END)
                  self.population_input.insert(tk.END,i[3])
                  self.continent_input.delete(0,tk.END)
                  self.continent_input.insert(tk.END,i[4].capitalize()) 
                  image_path =i[5]
                  sound_path=i[6]
                  pygame.mixer.init()
                  if image_path and sound_path:
                    # ----- get the flag from data base
                    flag = Image.open(image_path)
                    flag = flag.resize((150, 100))
                    flag = ImageTk.PhotoImage(flag)
                    self.label=tk.Label(image=flag,width=200,height=100)
                    self.label.grid(row=5,column=3)
                    #------get the sound from data base
                    pygame.mixer.music.load(sound_path)
                    name=sound_path.split("/")
                    name=name[-1]
                    self.name_mp3=tk.Label(self.root,text=f"{name}",fg="#c2960f",font=('Serif',20,'bold'),width=20)
                    self.name_mp3.grid(row=6,column=3)
    def last_contry(self):
        global flag
        mycursor.execute("SELECT * FROM pay ORDER BY id DESC LIMIT 1")
        res=mycursor.fetchall()
        for i in res:
                 # print(i)
                #   self.pay_input.insert(END,i[0])
                  self.nom_input.delete(0,tk.END)
                  self.nom_input.insert(tk.END,i[1].capitalize())
                  self.capital_input.delete(0,tk.END)
                  self.capital_input.insert(tk.END,i[2].capitalize())
                  self.population_input.delete(0,tk.END)
                  self.population_input.insert(tk.END,i[3])
                  self.continent_input.delete(0,tk.END)
                  self.continent_input.insert(tk.END,i[4].capitalize()) 
                  image_path =i[5]
                  sound_path=i[6]
                  pygame.mixer.init()
                  if image_path and sound_path:
                    # ----- get the flag from data base
                    flag = Image.open(image_path)
                    flag = flag.resize((150, 100))
                    flag = ImageTk.PhotoImage(flag)
                    self.label=tk.Label(image=flag,width=200,height=100)
                    self.label.grid(row=5,column=3)
                    #------get the sound from data base
                    pygame.mixer.music.load(sound_path)
                    name=sound_path.split("/")
                    name=name[-1]
                    self.name_mp3=tk.Label(self.root,text=f"{name}",fg="#c2960f",font=('Serif',20,'bold'),width=20)
                    self.name_mp3.grid(row=6,column=3)




    def create_widgets(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        self.text=tk.Label(self.root,text=f"Bienvenu {username.upper()}",font=('Serif',20,'bold'))
        
  # ----ADD
        self.a=Image.open('./icons/add.png')
        self.a_resize=self.a.resize((20,20))
        self.a_pic=ImageTk.PhotoImage(self.a_resize)
        self.ajout=tk.Button(self.root,text='Ajouter',image=self.a_pic,compound=tk.LEFT,width=330,height=50,bg='MediumSeaGreen',fg='white',font=('Arial',12,'bold'),activeforeground='MediumSeaGreen',command=self.ajouter)

    #---- UPDATE
        self.m=Image.open('./icons/update.png')
        self.m_resize=self.m.resize((20,20))
        self.m_pic=ImageTk.PhotoImage(self.m_resize)
        self.mod=tk.Button(self.root,text='Modifier',image=self.m_pic,compound=tk.LEFT,width=330,height=50,bg='Orange',fg='white',font=('Arial',12,'bold'),activeforeground='Orange',command=self.modifier)

    #----VALIDAYE
        self.v=Image.open('./icons/val.png')
        self.v_resize=self.v.resize((20,20))
        self.v_pic=ImageTk.PhotoImage(self.v_resize)
        self.val=tk.Button(self.root,text='Valider',image=self.v_pic,compound=tk.LEFT,width=330,height=50,bg='DodgerBlue',fg='white',font=('Arial',12,'bold'),activeforeground='DodgerBlue',command=self.valider)
        self.val.config(state=tk.DISABLED)
    # ----DELETE
        self.s=Image.open('./icons/delet.png')
        self.s_resize=self.s.resize((20,20))
        self.s_pic=ImageTk.PhotoImage(self.s_resize)
        self.sup=tk.Button(self.root,text='Supprimer',image=self.s_pic,compound=tk.LEFT,width=330,height=50,bg='Tomato',fg='white',font=('Arial',12,'bold'),activeforeground='Tomato',command=self.supprimer)

  #-----Quit
        self.quit=Image.open('./icons/exit.png')
        self.quit_resize=self.quit.resize((20,20))
        self.quit_pic=ImageTk.PhotoImage(self.quit_resize)
        
        self.leave=tk.Button(self.root,text='Quiter',compound=tk.LEFT,image=self.quit_pic,width=200,height=50,  bg='#CBC1AE',fg='white',font=('Arial',12,'bold'),activeforeground='#CBC1AE',command=self.logout)
   #------
        self.nom=tk.Label(self.root,text='Nom',font=('italic',10))
        self.nom_input=tk.Entry(width=50,font=('Helvetica',18))

        self.capital=tk.Label(self.root,text='Capitale',font=('italic',10))
        self.capital_input=tk.Entry(width=50,font=('Helvetica',18))

        self.population=tk.Label(self.root,text='Population',font=('italic',10))
        self.population_input=tk.Entry(width=50,font=('Helvetica',18))

        self.continent=tk.Label(self.root,text='Continent',font=('italic',10))
        self.continent_input=tk.Entry(width=50,font=('Helvetica',18))
        
        #search part 
        self.pay=tk.Label(self.root,text='Nom du pays :',font=('italic',10))

        self.pay_input=tk.Entry(width=45,font=('Helvetica',10))

        self.image=Image.open('./icons/search.png')
        self.resized_image=self.image.resize((20,20))
        self.picture=ImageTk.PhotoImage(self.resized_image)
        #----search button 
        self.pay_but=tk.Button(self.root,text='Rechercher',image=self.picture,compound=tk.RIGHT, command=self.search_pay )

       # insert flag button 
        self.but_flag=tk.Button(self.root,text='Insert le drapeau  ',command=self.insert_image )

     #-------start button
        self.p=Image.open('./icons/start.png')
        self.p_resize=self.p.resize((20,20))
        self.p_pic=ImageTk.PhotoImage(self.p_resize)
        self.play_button =tk.Button(self.root, text="", image=self.p_pic,command=self.play_music)
     #-------stop button 
        self.st=Image.open('./icons/stop.png')
        self.st_resize=self.st.resize((20,20))
        self.st_pic=ImageTk.PhotoImage(self.st_resize)

        self.stop_button =tk.Button(self.root, text="",image=self.st_pic, command=self.stop_music)


        #------next button 
     #----------- insert l'hymne nationale button

        self.load_button =tk.Button(self.root, text="+l'hymne nationale",command=self.load_music)
       # ---footer
        self.btn_b1 = tk.Button(self.root, text='|<', fg='black', bg='LightGray', width=47,command=self.first_contry)
        self.btn_b2 = tk.Button(self.root, text='<<', fg='black', bg='LightGray', width=47,command=self.previous_button)
        self.btn_b3 =tk.Button(self.root, text='>>', fg='black', bg='LightGray', width=47,command=self.next_button)
        self.btn_b4= tk.Button(self.root, text='>|', fg='black', bg='LightGray',width=47,command=self.last_contry)
       

        #---header---
        self.text.grid(row=0,columnspan=4, pady=10, sticky="nsew")
        self.ajout.grid(row=1,column=0)
        self.mod.grid(row=1,column=1)
        self.val.grid(row=1,column=2)
        self.sup.grid(row=1,column=3)
        self.leave.grid(row=1,column=4)


    
        #---body----
        self.nom.grid(row=4,column=0,)
        self.nom_input.grid(row=4,column=1,columnspan=2, pady=1, ipadx=10,ipady=10, sticky="w")
      
        self.capital.grid(row=5,column=0,)
        self.capital_input.grid(row=5,column=1,columnspan=2 ,pady=1,ipadx=10,ipady=10, sticky="w")
        self.population.grid(row=6,column=0,)
        self.population_input.grid(row=6,column=1,columnspan=2, pady=1, ipadx=10,ipady=10, sticky="w")
        self.continent.grid(row=7,column=0,)
        self.continent_input.grid(row=7, column=1, columnspan=2, pady=1, ipadx=10, ipady=10, sticky="w")


        self.pay.grid(row=8,column=0 ,padx=(0, 0.1), pady=5, sticky="e")
        self.pay_input.grid(row=8,column=1, padx=(0, 0), pady=5)
        self.pay_but.grid(row=8,column=2,padx=(0, 0.2), pady=5, sticky="w")
        

        self.play_button.grid(row=7,column=3,padx=(1, 0.1), pady=5,sticky="e")
        self.stop_button.grid(row=7,column=3,padx=(0, 0.2), pady=5)

        

        #--------footer---------
        self.btn_b1.grid(row=9,column=0)
        self.btn_b2.grid(row=9,column=1)
        self.btn_b3.grid(row=9,column=2)
        self.btn_b4.grid(row=9,column=3)

    def logout(self):
        res=messagebox.askyesno(
             title='Deconnexion',
             message="veux-tu quitter l'interface?",
          )
        if  res:
          messagebox.showinfo("Deconnexion","Merci pour votre visite \U0001F600")
         
          self.setup_login_page()

# Instantiate the Login class

l = App()
