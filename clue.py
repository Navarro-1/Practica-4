import tkinter as tk
from tkinter import ttk, messagebox
import random, os
from PIL import Image, ImageTk

# --- Colores y estilos ---
FONDO_COLOR = "#1e1e1e"
FONDO_ACUSACION = "#333333"
BOTON_COLOR = "#8B4513"
BOTON_TEXT_COLOR = "white"

# --- Fuentes ---
FONT_TITLE = ("Arial", 34, "bold")
FONT_NORMAL = ("Arial", 18)
FONT_COLUMN = ("Arial", 20, "bold")
FONT_BUTTON = ("Arial", 12, "bold")
FONT_START_TITLE = ("Arial", 32, "bold")
FONT_START_BUTTON = ("Arial", 28, "bold")

class ClueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("¡CLUE: ¡Encuentra al sospechoso!")

        # Datos
        self.suspects = ['Colonel Mustard', 'Professor Plum', 'Mr. Green',
                         'Miss Scarlet', 'Mrs. White', 'Mrs. Peacock']
        self.rooms = ['Vestíbulo', 'Comedor', 'Cocina', 'Salón',
                      'Conservatorio', 'Biblioteca', 'Estudio',
                      'Salón de Baile', 'Sala de Billar']
        self.weapons = ['Llave inglesa', 'Cuerda', 'Candelabro',
                        'Cuchillo', 'Tubería', 'Revólver']

        # 5 historias con diferentes combinaciones de sospechoso, arma y locación
        self.stories = [
            {'suspect': 'Mr. Green', 'weapon': 'Revólver', 'room': 'Biblioteca'},
            {'suspect': 'Mrs. White', 'weapon': 'Cuchillo', 'room': 'Cocina'},
            {'suspect': 'Professor Plum', 'weapon': 'Llave inglesa', 'room': 'Comedor'},
            {'suspect': 'Colonel Mustard', 'weapon': 'Candelabro', 'room': 'Salón'},
            {'suspect': 'Miss Scarlet', 'weapon': 'Tubería', 'room': 'Sala de Billar'}
        ]

        self.file_map = {
            'suspect': {
                'Colonel Mustard': 'Sospechoso_Colonel.png',
                'Professor Plum': 'Sospechoso_ProfessorPlum.png',
                'Mr. Green': 'Sospechoso_MrGreen.png',
                'Miss Scarlet': 'Sospechoso_MissScarlet.png',
                'Mrs. White': 'Sospechoso_MrsWhite.png',
                'Mrs. Peacock': 'Sospechoso_MrsPeacock.png'
            },
            'weapon': {
                'Llave inglesa': 'Arma_Llave.png',
                'Cuerda': 'Arma_Cuerda.png',
                'Candelabro': 'Arma_Candelabro.png',
                'Cuchillo': 'Arma_Cuchillo.png',
                'Tubería': 'Arma_Tuberia.png',
                'Revólver': 'Arma_Revolver.png'
            },
            'room': {
                'Vestíbulo': 'Habitacion_Vestibulo.png',
                'Comedor': 'Habitacion_Comedor.png',
                'Cocina': 'Habitacion_Cocina.png',
                'Salón': 'Habitacion_Salon.png',
                'Conservatorio': 'Habitacion_Conservatorio.png',
                'Biblioteca': 'Habitacion_Biblioteca.png',
                'Estudio': 'Habitacion_Estudio.png',
                'Salón de Baile': 'Habitacion_SalonBaile.png',
                'Sala de Billar': 'Habitacion_SalaBillar.png'
            }
        }

        self.image_labels = {}
        self.show_start_screen()

    def show_start_screen(self):
        """Ventana 1: Pantalla de inicio"""
        self.start_frame = tk.Frame(self.root)
        self.start_frame.pack(fill="both", expand=True)

        portada = os.path.join('imagenes', 'portada.jpg')
        if os.path.exists(portada):
            img = Image.open(portada)
            self.w, self.h = img.size
            self.port_img = ImageTk.PhotoImage(img)
            tk.Label(self.start_frame, image=self.port_img).place(x=0, y=0)
        else:
            self.w, self.h = 800, 600

        self.root.geometry(f"{self.w}x{self.h}")
        self.root.resizable(False, False)

        frase_lbl = tk.Label(self.start_frame,
                             text="¡CLUE: ¡Encuentra al sospechoso!",
                             font=FONT_START_TITLE,
                             fg="white", bg=BOTON_COLOR)
        frase_lbl.place(relx=0.5, rely=0.2, anchor="center")

        tk.Button(self.start_frame, text="Jugar",
                  font=FONT_START_BUTTON,
                  bg=BOTON_COLOR, fg="white",
                  padx=30, pady=15,
                  command=self.show_narrative_window).place(relx=0.5, rely=0.5, anchor="center")

    def show_narrative_window(self):
        """Ventana 2: Ventana nueva con la narrativa y fondo"""
        self.start_frame.destroy()  # Elimina la ventana de inicio

        narrative_window = tk.Frame(self.root)
        narrative_window.pack(fill="both", expand=True)

        # Establecer fondo de la ventana de narrativa (puede ser una imagen)
        fondo_narrativa = os.path.join('imagenes', 'Portada.jpg')  # Ajusta el nombre del archivo si es necesario
        if os.path.exists(fondo_narrativa):
            img = Image.open(fondo_narrativa)
            self.w, self.h = img.size
            self.bg_img = ImageTk.PhotoImage(img)
            tk.Label(narrative_window, image=self.bg_img).place(x=0, y=0)
        else:
            narrative_window.config(bg=FONDO_ACUSACION)

        # Seleccionar una historia aleatoria
        self.selected_story = random.choice(self.stories)

        # Texto de la narrativa (sin fondo, solo texto en negro)
        story_text = (
            f"Esta noche, el cuerpo sin vida de Mr. Black fue encontrado en la mansión.\n"
            f"Las evidencias son escasas y el tiempo apremia.\n"
            f"¿Podrás descubrir quién es el asesino antes de que sea demasiado tarde?"
        )

        # Ajusta el texto para que tenga un fondo transparente (o sin fondo)
        tk.Label(narrative_window, text=story_text,
                 font=("Arial", 20, "italic"), fg="black", bg="white",  # Texto en negro
                 justify="center", wraplength=600).pack(pady=80)

        # Botón Continuar para cerrar la ventana de narrativa y cargar la siguiente
        tk.Button(narrative_window, text="Continuar", font=FONT_BUTTON,
                  bg=BOTON_COLOR, fg="white", padx=30, pady=15,
                  command=lambda: self.show_game_interface(narrative_window)).pack(pady=20)

    def show_game_interface(self, narrative_window):
        """Ventana 3: Inicia el juego de selección de sospechoso, habitación y arma"""
        narrative_window.destroy()  # Elimina la ventana de narrativa

        self.start_game_frame = tk.Frame(self.root)  # Crear una nueva ventana en la misma ventana principal
        self.start_game_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.start_game_frame, width=self.w, height=self.h, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        fondo = os.path.join('imagenes', 'fondo.png')
        if os.path.exists(fondo):
            bg = Image.open(fondo).resize((self.w, self.h), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg)
            self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)

        style = ttk.Style()
        style.configure("Large.TMenubutton", font=("Arial", 16))

        self.secret = self.selected_story  # Usar la historia seleccionada previamente
        self.attempts = 5

        self.canvas.create_text(self.w//2, 40, text="¡Encuentra al asesino!",
                                font=FONT_TITLE, fill="white")
        self.attempts_text = self.canvas.create_text(
            self.w//2, 100, text=f"Oportunidades restantes: {self.attempts}",
            font=FONT_NORMAL, fill="white")

        xs = [self.w/6, self.w/2, 5*self.w/6]

        for idx, (label, options, key) in enumerate([ 
            ("Sospechoso", self.suspects, "suspect"),
            ("Habitación", self.rooms, "room"),
            ("Arma", self.weapons, "weapon")
        ]):
            self.canvas.create_text(xs[idx], 160, text=label,
                                    font=FONT_COLUMN, fill="white")

            var = tk.StringVar(value=options[0])
            om = ttk.OptionMenu(self.start_game_frame, var, options[0], *options,
                                command=lambda val, k=key: self.update_image(k, val),
                                style="Large.TMenubutton")
            om.config(width=20)
            self.canvas.create_window(xs[idx], 210, window=om)
            setattr(self, f"{key}_var", var)

            img_lbl = tk.Label(self.start_game_frame, bd=0)
            self.canvas.create_window(xs[idx], 370, window=img_lbl)
            self.image_labels[key] = img_lbl
            self.update_image(key, options[0])

            btn = tk.Button(self.start_game_frame, text=f"Consultar {label}",
                            font=FONT_BUTTON, bg=BOTON_COLOR, fg="white",
                            command=lambda k=key, v=var: self.consult(k, v.get()))
            self.canvas.create_window(xs[idx], 550, window=btn)

        self.evidence_lbl = tk.Label(self.start_game_frame, text="", fg="white", bg=FONDO_COLOR,
                                     font=FONT_NORMAL, wraplength=700, justify="center")
        self.canvas.create_window(self.w//2, int(self.h*0.86), window=self.evidence_lbl)

        self.accuse_btn = tk.Button(self.start_game_frame, text="Ir a Acusar",
                                    font=FONT_BUTTON, bg=BOTON_COLOR, fg="white",
                                    command=self.show_accusation)

    def update_image(self, category, selection):
        filename = self.file_map[category].get(selection)
        lbl = self.image_labels[category]
        if filename:
            path = os.path.join('imagenes', filename)
            if os.path.exists(path):
                img = Image.open(path)
                img.thumbnail((180, 260), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                lbl.config(image=photo)
                lbl.image = photo
            else:
                lbl.config(text="[Imagen no encontrada]")
        else:
            lbl.config(text="[Sin archivo]")

    def consult(self, category, choice):
        if self.attempts <= 0:
            return

        # Aquí puedes mostrar testimonios específicos
        testimony_map = {
            'suspect': {
                'Mr. Green': "Mr. Green, parece estar nervioso cuando se le pregunta sobre su paradero esa noche.",
                'Mrs. White': "Mrs. White, ha sido vista en la cocina, pero nadie sabe qué hacía allí a esa hora.",
                'Professor Plum': "Profesor Plum, conocido por su afición al vino, estuvo muy cerca de la escena del crimen.",
                'Colonel Mustard': "El Coronel Mustard tiene un historial de peleas violentas, y esa noche estaba en el salón.",
                'Miss Scarlet': "Miss Scarlet, elegante como siempre, fue vista cerca del vestíbulo antes de que comenzara el caos."
            },
            'weapon': {
                'Revólver': "El revólver parece ser el arma definitiva, aunque no se ha encontrado una huella clara.",
                'Cuchillo': "El cuchillo estaba empapado en sangre, pero no es claro si pertenece al asesino.",
                'Llave inglesa': "La llave inglesa, extraña pero letal, fue encontrada cerca de la víctima.",
                'Candelabro': "El candelabro, con su peso, pudo haber sido el arma del crimen, aunque nadie lo vio caer.",
                'Tubería': "La tubería fue encontrada con manchas de sangre, pero no está claro si fue utilizada."
            },
            'room': {
                'Vestíbulo': "En el vestíbulo se escucharon ruidos extraños, tal vez de alguien moviéndose sigilosamente.",
                'Comedor': "Se encontró una copa rota en el comedor, quizás relacionada con lo que ocurrió allí.",
                'Cocina': "La cocina estaba en completo desorden, con huellas de alguien que se apresuraba.",
                'Salón': "El salón fue el lugar de muchas discusiones durante la noche, pero nadie sabía lo que realmente sucedió.",
                'Biblioteca': "La biblioteca estaba muy tranquila, pero hay evidencia de que alguien estaba husmeando allí."
            }
        }

        testimony = testimony_map[category].get(choice, "No se encontró testimonio disponible.")

        # Mostrar el testimonio adicional
        self.evidence_lbl.config(text=f"Testimonio: {testimony}")

        # Restar oportunidades
        self.attempts -= 1

        # Actualizar el texto de oportunidades restantes
        self.canvas.itemconfig(self.attempts_text,
                               text=f"Oportunidades restantes: {self.attempts}")

        # Cuando las oportunidades lleguen a 0, mostrar el botón de acusación
        if self.attempts == 0:
            self.canvas.create_window(self.w//2, int(self.h*0.93), window=self.accuse_btn)

    def show_accusation(self):
        win = tk.Toplevel(self.root)
        win.title("Acusación Final")
        win.config(bg=FONDO_ACUSACION)
        win.geometry("450x500")

        tk.Label(win, text="¡Haz tu acusación final!", font=("Arial", 16, "bold"),
                 fg="white", bg=FONDO_ACUSACION).pack(pady=20)

        self.acc_vars = {}
        for lbl, options, key in [
            ("Sospechoso", self.suspects, "suspect"),
            ("Habitación", self.rooms, "room"),
            ("Arma", self.weapons, "weapon")
        ]:
            frame = tk.Frame(win, bg=FONDO_ACUSACION)
            frame.pack(pady=10)

            tk.Label(frame, text=lbl, font=("Arial", 20, "bold"),
                     fg="white", bg=FONDO_ACUSACION).pack()
            var = tk.StringVar(value=options[0])
            menu = ttk.OptionMenu(frame, var, options[0], *options)
            menu.config(width=20)
            menu.pack()
            self.acc_vars[key] = var

        tk.Button(win, text="¡Acusar!", font=("Arial", 14, "bold"),
                  bg=BOTON_COLOR, fg="white",
                  padx=10, pady=5,
                  command=lambda: self.check_accusation(win)).pack(pady=20)

        tk.Button(win, text="Salir", font=("Arial", 14, "bold"),
                  bg=BOTON_COLOR, fg="white",
                  padx=10, pady=5,
                  command=self.root.quit).pack(pady=10)

    def check_accusation(self, win):
        guess = {k: v.get() for k, v in self.acc_vars.items()}
        correct = all(guess[k] == self.secret[k] for k in guess)
        title = "¡Caso resuelto!" if correct else "Acusación incorrecta"
        detail = (f"Sospechoso: {self.secret['suspect']}\n"
                  f"Habitación: {self.secret['room']}\n"
                  f"Arma: {self.secret['weapon']}")
        messagebox.showinfo(title, detail)
        win.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = ClueApp(root)
    root.mainloop()
