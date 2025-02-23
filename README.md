# LexiEase AI Backend

LexiEase AI is an AI-powered dyslexia support system providing personalized learning, dyslexia severity assessment, gamification, document conversion, and chatbot assistance. This backend is built using **Django (FastAPI/Flask for some services)** and powered by **MySQL** for data storage.

## 🚀 Features

### 1️⃣ Dyslexia Severity Assessment
- **AI-Powered Test:** Utilizes the **Groq DeepSeek model** for dyslexia severity assessment.
- **User Input Analysis:** Evaluates reading, writing, and comprehension skills.
- **Automated Scoring:** Provides severity levels and personalized recommendations.
- **Data Storage:** Saves assessment results in **MySQL** for tracking progress.

### 2️⃣ Personalized Learning System
- **User Profile & Learning Path:** Custom-tailored learning based on severity level.
- **Content Adaptation:** Dynamically adjusts reading difficulty.
- **Progress Tracking:** Monitors improvements and suggests new materials.

### 3️⃣ AI-Powered Document Conversion
- **Text Simplification:** Rewrites documents in a dyslexia-friendly format.
- **Text-to-Speech (TTS):** Converts text into speech using **Google STT/Coqui AI**.
- **Mind Map Generation:** Summarizes key ideas using **AI-generated mind maps**.
- **Storage:** Uses **Vultr Block Storage** for document handling.

### 4️⃣ AI Chatbot for Learning Assistance
- **Rephraser:** Provides simpler text versions for better readability.
- **Pronunciation & Spelling Help:** Guides users with phonetic hints.
- **Health-Related Queries:** Offers general health assistance for patients.
- **Personalized AI Responses:** Uses **DeepSeek model** for personalized interactions.

### 5️⃣ Gamification System
- **Interactive Exercises:** AI-generated exercises to reinforce learning.
- **Level Progression:** Users must score **70%+** to unlock the next level.
- **Leaderboard & Achievements:** Tracks progress and rewards users.
- **Backend:** Built with **Django & MySQL**, storing results for analytics.

### 6️⃣ User Management & Authentication
- **JWT Authentication:** Secure login & session management.
- **Role-Based Access:** Different access levels for students, educators, and admins.
- **Data Encryption:** Ensures secure storage of user data.

### 7️⃣ API Endpoints
- **RESTful API:** Built with **Django + FastAPI/Flask** for different modules.
- **Scalability:** Optimized for high performance and quick responses.
- **Documentation:** Auto-generated API docs using **Swagger/OpenAPI**.

## 🛠️ Tech Stack
- **Backend Framework:** Django (FastAPI/Flask for some services)
- **Database:** MySQL (Vultr Managed MySQL)
- **AI Models:** OpenAI/Hugging Face, Google STT/Coqui AI, TensorFlow/Keras, DeepSeek
- **Storage:** Vultr Block Storage
- **Hosting:** Vultr Compute Instances (separate instances for frontend & backend)
- **Authentication:** JWT-based authentication

## 📌 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/LexiEase-Backend.git
cd LexiEase-Backend
```

### 2️⃣ Setup a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file and add:
```env
DJANGO_SECRET_KEY=your_secret_key
DATABASE_URL=mysql://user:password@host/db_name
AI_API_KEY=your_ai_api_key
JWT_SECRET=your_jwt_secret
```

### 5️⃣ Run Migrations
```bash
python manage.py migrate
```

### 6️⃣ Start the Server
```bash
python manage.py runserver
```

## 📖 API Documentation
Swagger UI is available at:
```
http://127.0.0.1:8000/docs
```

## 🤝 Contributing
Feel free to fork and submit pull requests to improve the project.


---

### 🔥 Built with Passion for Accessibility & AI Innovation 🚀
