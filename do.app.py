
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class TodoApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("To-Do List")
        self.geometry("450x550")
        self.resizable(False, False)

        # Sarlavha
        self.title_label = ctk.CTkLabel(
            self,
            text="Vazifalar Menejeri",
            font=ctk.CTkFont(size=22, weight="bold"),
        )
        self.title_label.pack(pady=(20, 10))

        # Kiritish freymi
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(padx=20, pady=10, fill="x")

        self.entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Yangi vazifa kiriting...",
            width=280,
        )
        self.entry.pack(side="left", padx=(10, 5), pady=10)
        self.entry.bind("<Return>", lambda event: self.add_task())

        self.add_button = ctk.CTkButton(
            self.input_frame, text="Qo'shish", width=90, command=self.add_task
        )
        self.add_button.pack(side="right", padx=(5, 10), pady=10)

        # Vazifalar ro'yxati (Scrollable Frame)
        self.tasks_frame = ctk.CTkScrollableFrame(
            self, width=400, height=350, label_text="Vazifalaringiz"
        )
        self.tasks_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Muallif imzosi
        self.footer_label = ctk.CTkLabel(
            self,
            text="Developed by gafurov",
            font=ctk.CTkFont(size=11, slant="italic"),
            text_color="gray",
        )
        self.footer_label.pack(side="bottom", pady=5)

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            task_item = ctk.CTkFrame(self.tasks_frame)
            task_item.pack(fill="x", pady=4, padx=5)

            checkbox = ctk.CTkCheckBox(task_item, text=task_text)
            checkbox.pack(side="left", padx=10, pady=8, expand=True, fill="x")

            delete_btn = ctk.CTkButton(
                task_item,
                text="✕",
                width=30,
                fg_color="#e74c3c",
                hover_color="#c0392b",
                command=lambda: task_item.destroy(),
            )
            delete_btn.pack(side="right", padx=10, pady=8)

            self.entry.delete(0, "end")


if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
