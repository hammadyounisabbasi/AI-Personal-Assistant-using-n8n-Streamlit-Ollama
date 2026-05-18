# AI-Personal-Assistant-using-n8n-Streamlit-Ollama
AI-powered Personal Assistant built using n8n, Streamlit, and Ollama. It automates tasks like email management, calendar scheduling, note-taking, task handling, expense tracking, and web search through an interactive chat interface with workflow automation and local AI models.
# 🚀 Features

- 💬 AI Chat Assistant
- 📧 Read, summarize, and send emails
- 📅 Create and manage calendar events
- 📝 Notes management
- ✅ Task management
- 💰 Expense tracking
- 🌐 Web search integration
- 🧠 Local AI model using Ollama
- 🔄 Workflow automation with n8n
- 🎨 Interactive Streamlit frontend

---

# 🛠️ Technologies Used

- Python
- Streamlit
- n8n
- Ollama
- Gmail API
- Google Calendar API
- SerpAPI
- HTTP Webhooks

---

# 📂 Project Structure

```bash
AI-Personal-Assistant/
│
├── app.py
├── webhook_test.py
├── requirements.txt
├── README.md
├── screenshots/
├── n8n_workflow/
└── report/
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/AI-Personal-Assistant.git
cd AI-Personal-Assistant
2️⃣ Create Virtual Environment
python -m venv venv

Activate virtual environment:

Windows
venv\\Scripts\\activate
Linux/Mac
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run Streamlit Application
streamlit run app.py
🔄 Run n8n

If using Docker:

docker run -it --rm \
--name n8n \
-p 5678:5678 \
-e GENERIC_TIMEZONE=\"Asia/Karachi\" \
-e TZ=\"Asia/Karachi\" \
-v n8n_data:/home/node/.n8n \
docker.n8n.io/n8nio/n8n
🧠 Ollama Setup

Install Ollama and download your preferred model.

Example:

ollama run llama3
📸 Screenshots
n8n Workflow

(Add workflow screenshot here)

Streamlit Interface

(Add Streamlit screenshot here)

Email Automation

(Add email demo screenshot here)

🧪 Sample Prompts
Show my latest received email
Create a meeting tomorrow at 5 PM
Add expense of 2000 PKR for internet bill
Create a task for project submission
⚠️ Limitations
Local Ollama models can be slow on low-end hardware
OpenAI APIs are expensive for large-scale usage
SerpAPI free plan has limited search tokens
Performance depends on local system resources
Some features require internet connectivity
🔮 Future Improvements
Voice Assistant Integration
WhatsApp Automation
Cloud Deployment
GPU Acceleration
Multi-user Authentication
Long-term Memory Database
📄 Project Report

Detailed project documentation is available in the report/ folder.

👨‍💻 Author

Hammad Younis Abbasi

⭐ Support

If you found this project helpful, consider giving it a star ⭐ on GitHub.
