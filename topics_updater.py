import requests
import os
from typing import List
import tkinter as tk
from tkinter import ttk, messagebox

class TopicsUpdater:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GitHub Topics Updater")
        self.window.geometry("600x800")
        
        # Default topics list (can be modified)
        self.default_topics = [
            # Programming Languages
            "python", "javascript", "typescript", "java", "cpp", "c-plus-plus", "csharp", "go", "rust", "php", "ruby", "swift",
            "kotlin", "scala", "perl", "r", "matlab", "dart", "lua", "haskell", "assembly", "shell", "powershell", "sql",
            
            # Web Development
            "html", "css", "html5", "css3", "sass", "less", "webpack", "babel", "web-components", "pwa", "spa",
            "responsive-design", "web-development", "frontend", "backend", "full-stack",
            
            # Frameworks & Libraries
            "react", "angular", "vue", "svelte", "nextjs", "nuxtjs", "django", "flask", "fastapi", "spring-boot",
            "express", "nodejs", "deno", "laravel", "symfony", "rails", "jquery", "bootstrap", "tailwind",
            "material-ui", "chakra-ui", "redux", "vuex", "mobx", "rxjs", "graphql", "rest-api",
            
            # Mobile Development
            "android", "ios", "flutter", "react-native", "xamarin", "ionic", "cordova", "mobile-development",
            "android-development", "ios-development", "mobile-app",
            
            # Cloud & DevOps
            "aws", "azure", "gcp", "cloud-computing", "kubernetes", "docker", "containerization", "microservices",
            "serverless", "ci-cd", "devops", "devsecops", "infrastructure-as-code", "terraform", "ansible",
            "jenkins", "github-actions", "gitlab-ci", "cloud-native", "distributed-systems",
            
            # Data Science & AI
            "machine-learning", "deep-learning", "artificial-intelligence", "data-science", "neural-networks",
            "tensorflow", "pytorch", "keras", "scikit-learn", "pandas", "numpy", "jupyter", "data-analysis",
            "data-visualization", "computer-vision", "nlp", "big-data", "data-engineering",
            
            # Database
            "mysql", "postgresql", "mongodb", "redis", "elasticsearch", "cassandra", "sqlite", "oracle",
            "sql-server", "database", "nosql", "database-design", "orm", "database-migration",
            
            # Security
            "cybersecurity", "security", "encryption", "authentication", "oauth", "jwt", "penetration-testing",
            "security-tools", "cryptography", "blockchain", "smart-contracts", "web3", "defi",
            
            # Testing
            "testing", "unit-testing", "integration-testing", "test-automation", "selenium", "cypress",
            "jest", "mocha", "pytest", "tdd", "bdd", "quality-assurance", "continuous-testing",
            
            # Game Development
            "game-development", "unity", "unreal-engine", "godot", "gamedev", "game-engine", "3d-game",
            "2d-game", "game-design", "game-programming",
            
            # Desktop Development
            "electron", "qt", "gtk", "wxwidgets", "desktop-application", "cross-platform", "gui",
            "windows-development", "linux-development", "macos-development",
            
            # Operating Systems
            "linux", "windows", "macos", "ubuntu", "debian", "fedora", "centos", "unix", "bash",
            "operating-system", "kernel", "system-programming",
            
            # Software Engineering Practices
            "clean-code", "design-patterns", "solid-principles", "agile", "scrum", "code-quality",
            "code-review", "pair-programming", "refactoring", "documentation", "api-design",
            
            # Tools & Utilities
            "git", "github", "gitlab", "bitbucket", "vscode", "intellij", "eclipse", "vim", "emacs",
            "developer-tools", "productivity-tools", "debugging", "monitoring", "logging",
            
            # Emerging Technologies
            "iot", "augmented-reality", "virtual-reality", "edge-computing", "5g", "quantum-computing",
            "robotics", "drones", "computer-graphics", "embedded-systems",
            
            # Project Management
            "project-management", "agile-development", "kanban", "jira", "trello", "collaboration",
            "team-management", "workflow-automation",
            
            # Education & Learning
            "education", "tutorial", "learning-resources", "programming-tutorials", "coding-challenges",
            "competitive-programming", "algorithms", "data-structures", "interview-preparation",
            
            # Miscellaneous
            "awesome-list", "boilerplate", "starter-kit", "template", "utilities", "best-practices",
            "performance-optimization", "scalability", "high-availability", "fault-tolerance",
            "internationalization", "accessibility", "seo", "analytics", "open-source"
        ]
        
        self.selected_topics = []
        self.setup_ui()

    def setup_ui(self):
        # GitHub Configuration Frame
        config_frame = ttk.LabelFrame(self.window, text="GitHub Configuration", padding=10)
        config_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(config_frame, text="GitHub Token:").pack()
        self.token_entry = ttk.Entry(config_frame, width=50)
        self.token_entry.pack(pady=5)

        ttk.Label(config_frame, text="Repository Owner:").pack()
        self.owner_entry = ttk.Entry(config_frame, width=50)
        self.owner_entry.pack(pady=5)

        ttk.Label(config_frame, text="Repository Name:").pack()
        self.repo_entry = ttk.Entry(config_frame, width=50)
        self.repo_entry.pack(pady=5)

        # Topics Selection Frame
        topics_frame = ttk.LabelFrame(self.window, text="Topics Selection", padding=10)
        topics_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Available Topics with Search
        available_frame = ttk.LabelFrame(topics_frame, text="Available Topics")
        available_frame.pack(side="left", fill="both", expand=True, padx=5)

        # Add search frame
        search_frame = ttk.Frame(available_frame)
        search_frame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(search_frame, text="Search Topics:").pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace('w', self.filter_topics)
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(5, 0))

        # Create a frame for the listbox and scrollbar
        list_frame = ttk.Frame(available_frame)
        list_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.available_listbox = tk.Listbox(list_frame, selectmode="multiple", width=30)
        self.available_listbox.pack(side="left", fill="both", expand=True)
        
        # Configure scrollbar
        scrollbar.config(command=self.available_listbox.yview)
        self.available_listbox.config(yscrollcommand=scrollbar.set)
        
        # Populate available topics
        for topic in self.default_topics:
            self.available_listbox.insert(tk.END, topic)

        # Buttons Frame
        buttons_frame = ttk.Frame(topics_frame)
        buttons_frame.pack(side="left", padx=5)

        ttk.Button(buttons_frame, text=">>", command=self.add_topics).pack(pady=5)
        ttk.Button(buttons_frame, text="<<", command=self.remove_topics).pack(pady=5)

        # Selected Topics
        selected_frame = ttk.LabelFrame(topics_frame, text="Selected Topics")
        selected_frame.pack(side="right", fill="both", expand=True, padx=5)

        # Create a frame for the selected listbox and scrollbar
        selected_list_frame = ttk.Frame(selected_frame)
        selected_list_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Add scrollbar for selected topics
        selected_scrollbar = ttk.Scrollbar(selected_list_frame)
        selected_scrollbar.pack(side="right", fill="y")

        self.selected_listbox = tk.Listbox(selected_list_frame, selectmode="multiple", width=30)
        self.selected_listbox.pack(side="left", fill="both", expand=True)
        
        # Configure scrollbar for selected topics
        selected_scrollbar.config(command=self.selected_listbox.yview)
        self.selected_listbox.config(yscrollcommand=selected_scrollbar.set)

        # New Topic Entry
        new_topic_frame = ttk.LabelFrame(self.window, text="Add New Topic", padding=10)
        new_topic_frame.pack(fill="x", padx=10, pady=5)

        self.new_topic_entry = ttk.Entry(new_topic_frame, width=40)
        self.new_topic_entry.pack(side="left", padx=5)
        
        ttk.Button(new_topic_frame, text="Add Topic", command=self.add_new_topic).pack(side="left", padx=5)

        # Update Button
        ttk.Button(self.window, text="Update Topics", command=self.update_topics).pack(pady=10)

    def filter_topics(self, *args):
        search_term = self.search_var.get().lower()
        self.available_listbox.delete(0, tk.END)
        
        for topic in self.default_topics:
            if search_term in topic.lower():
                self.available_listbox.insert(tk.END, topic)

    def add_topics(self):
        selections = self.available_listbox.curselection()
        for index in reversed(selections):
            topic = self.available_listbox.get(index)
            self.selected_listbox.insert(tk.END, topic)
            self.available_listbox.delete(index)

    def remove_topics(self):
        selections = self.selected_listbox.curselection()
        for index in reversed(selections):
            topic = self.selected_listbox.get(index)
            self.available_listbox.insert(tk.END, topic)
            self.selected_listbox.delete(index)

    def add_new_topic(self):
        new_topic = self.new_topic_entry.get().strip()
        if new_topic:
            if "-" not in new_topic and " " in new_topic:
                new_topic = new_topic.replace(" ", "-")
            self.available_listbox.insert(tk.END, new_topic)
            self.new_topic_entry.delete(0, tk.END)

    def update_topics(self):
        token = self.token_entry.get().strip()
        owner = self.owner_entry.get().strip()
        repo = self.repo_entry.get().strip()

        if not all([token, owner, repo]):
            messagebox.showerror("Error", "Please fill in all GitHub configuration fields!")
            return

        selected_topics = list(self.selected_listbox.get(0, tk.END))
        
        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }

        url = f'https://api.github.com/repos/{owner}/{repo}/topics'
        
        try:
            response = requests.put(url, json={'names': selected_topics}, headers=headers)
            
            if response.status_code == 200:
                messagebox.showinfo("Success", "Topics successfully updated!")
                print("\nAdded topics:")
                for topic in selected_topics:
                    print(f"- {topic}")
            else:
                messagebox.showerror("Error", f"Error updating topics: {response.status_code}\n{response.json()}")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = TopicsUpdater()
    app.run()
