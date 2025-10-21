import customtkinter as ctk
from tkinter import messagebox

import mysql.connector
from mysql.connector import Error,errorcode

#=========== confugracao do banco de dados ==============
config = {
    "host": "localhost",
    "user":"cadastro_app",
    "password":"amanda123",
    "database":"techsolutions"
}
#=========== FIM confugracao do banco de dados ==============

def get_connection():
    connection = None
   
    try:
        connection = mysql.connector.connect(**config)
        print("Conexão ao MySQL bem-sucedida")
    except Error as e:
        print(f"Ocorreu um erro: {e}")
    return connection



# Inicializa o banco de dados (cria a tabela se não existir)
def  init_db():

    """Garante que a tabela exista (safe para rodar no início do app)."""
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            cpf VARCHAR(14) NOT NULL,
            email VARCHAR(100) NOT NULL,
            telefone VARCHAR(15) NOT NULL,
            endereco VARCHAR(255) NOT NULL,
            estado VARCHAR(2) NOT NULL
        );
    """)
        connection.commit()
    except Error as e:
        messagebox.showerror("Erro de Banco", f"Não foi possível inicializar a tabela.\n\n{e}")    
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass


def cadastrar_cliente():
    nome = entrada_nome.get()
    cpf = entrada_CPF.get()
    email = entrada_Email.get()
    telefone = entrada_Telefone.get()
    endereco = entrada_Endereco.get()
    estado = entrada_estado.get()

    if not (nome and cpf and email and telefone and endereco and estado):
        messagebox.showwarning("Campos Incompletos", "Por favor, preencha todos os campos.")
        return
    if estado and len(estado) != 2:
        messagebox.showwarning("Estado inválido", "Informe a sigla do estado com 2 letras (ex.: SP).")
        return
    
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO clientes (nome, cpf, email, telefone, endereco, estado)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nome, cpf, email, telefone, endereco, estado))
        connection.commit()
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        entrada_nome.delete(0, ctk.END)
        entrada_CPF.delete(0, ctk.END)
        entrada_Email.delete(0, ctk.END)
        entrada_Telefone.delete(0, ctk.END)
        entrada_Endereco.delete(0, ctk.END)
        entrada_estado.delete(0, ctk.END)
    except Error as e:
        if getattr(e, "erro", None) == errorcode.ER_DUP_ENTRY:
            messagebox.showerror("Erro", "Já existe um cliente com esse CPF.")
    finally:           
        try:
                cursor.close()
                connection.close()
        except:
                pass

# Inicializa a estrutura do banco/tabela ao abrir o app
init_db()

#=========== Configuração da interface gráfica ==============
app = ctk.CTk()
app.geometry("600x600")
app.title(" 🔰CADASTRO CLIENTES - techsolutions")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app.minsize(600, 600)

label_nome = ctk.CTkLabel(app, text="Nome:", font=("Arial", 20))
label_nome.place(x=150, y=50)  # posição do texto
entrada_nome = ctk.CTkEntry(app, placeholder_text="Nome Completo", width=300)

entrada_nome.configure(fg_color="white", text_color="black", border_color="black", border_width=2)
entrada_nome.place(x=250, y=50)
entrada_nome.focus()

label_CPT = ctk.CTkLabel(app, text="CPF:", font=("Arial", 20))
label_CPT.place(x=150, y=100)  # posição do texto
entrada_CPF = ctk.CTkEntry(app, placeholder_text="CPF", width=300)

entrada_CPF.configure(fg_color="white", text_color="black", border_color="black", border_width=2)
entrada_CPF.place(x=250, y=100)
entrada_CPF.focus()

label_Email = ctk.CTkLabel(app, text="Email:", font=("Arial", 20))
label_Email.place(x=150, y=150)  # posição do texto
entrada_Email = ctk.CTkEntry(app, placeholder_text="Email", width=300)

entrada_Email.configure(fg_color="white", text_color="black", border_color="black", border_width=2)
entrada_Email.place(x=250, y=150)   
entrada_Email.focus()
entrada_Email.insert(0, "@gmail.com")


label_Telefone = ctk.CTkLabel(app, text="Telefone:", font=("Arial", 20))
label_Telefone.place(x=150, y=200)  # posição do texto
entrada_Telefone = ctk.CTkEntry(app, placeholder_text="Telefone", width=300)
entrada_Telefone.configure(fg_color="white", text_color="black", border_color="black", border_width=2)
entrada_Telefone.place(x=250, y=200)        
entrada_Telefone.focus()
entrada_Telefone.insert(0, "(xx)xxxxx-xxxx")


label_Endereco = ctk.CTkLabel(app, text="Endereço:", font=("Arial", 20))
label_Endereco.place(x=150, y=250)  # posição do texto
entrada_Endereco = ctk.CTkEntry(app, placeholder_text="Endereço", width=300)
entrada_Endereco.configure(fg_color="white", text_color="black", border_color="black", border_width=2)
entrada_Endereco.place(x=250, y=250)
entrada_Endereco.focus()


label_estado = ctk.CTkLabel(app, text="Estado:", font=("Arial", 20))
label_estado.place(x=150, y=300)  # posição do texto
entrada_estado = ctk.CTkEntry(app, placeholder_text="Estado", width=300)
entrada_estado.configure(fg_color="white", text_color="black", border_color="black", border_width=2)
entrada_estado.place(x=250, y=300)
entrada_estado.focus()



button_cadastrar = ctk.CTkButton(app, text="CADASTRAR", width=200, height=50, fg_color="#1f6aa5", hover_color="#367fa9", font=("Arial", 20), command=cadastrar_cliente)
button_cadastrar.place(x=300, y=400)


app.mainloop()



