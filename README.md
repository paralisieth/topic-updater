# GitHub Topics Updater 🏷️

A powerful GUI tool for managing GitHub repository topics with ease. This application allows you to select from a comprehensive list of predefined topics or add custom ones to your GitHub repositories.

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue?style=for-the-badge)

## 🌟 Features

- **Interactive GUI**: User-friendly interface for topic management
- **Real-time Search**: Quickly find topics with instant search functionality
- **200+ Predefined Topics**: Comprehensive list of common GitHub topics
- **Custom Topics**: Add your own custom topics
- **Secure**: GitHub token-based authentication
- **Category Organization**: Topics organized by categories like:
  - Programming Languages
  - Web Development
  - Frameworks & Libraries
  - Cloud & DevOps
  - Data Science & AI
  - And many more!

## 🚀 Quick Start

1. Clone the repository:
   ```bash
   git clone [your-repo-url]
   cd topicsupdater
   ```

2. Run the application:
   ```bash
   python run.py
   ```
   The script will automatically install all required dependencies.

## 🛠️ Usage

1. Launch the application using `python run.py`
2. Enter your GitHub credentials:
   - GitHub Personal Access Token
   - Repository Owner
   - Repository Name
3. Search and select topics:
   - Use the search bar to filter topics
   - Select multiple topics using Ctrl+click
   - Move topics using ">>" and "<<" buttons
4. Add custom topics if needed
5. Click "Update Topics" to apply changes

## 🔑 GitHub Token

To use this tool, you need a GitHub Personal Access Token with the following permissions:
- `repo` scope for private repositories
- `public_repo` scope for public repositories

To create a token:
1. Go to GitHub Settings
2. Navigate to Developer Settings > Personal Access Tokens
3. Generate a new token with required permissions
4. Copy and use the token in the application

## 📚 Available Topic Categories

- Programming Languages
- Web Development
- Frameworks & Libraries
- Mobile Development
- Cloud & DevOps
- Data Science & AI
- Database Technologies
- Security
- Testing
- Game Development
- Desktop Development
- Operating Systems
- Software Engineering
- Tools & Utilities
- Emerging Technologies
- Project Management
- Education & Learning

## ⚙️ Requirements

- Python 3.7+
- Required packages (automatically installed):
  - requests==2.31.0

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Add more predefined topics
- Improve documentation

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔒 Security

- Never commit your GitHub token
- Use environment variables when possible
- Revoke unused tokens from GitHub settings

## 📞 Support

For support, please open an issue in the GitHub repository.
