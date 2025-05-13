# MentalHealth-Agent-Project 🚀

## Project Overview
This Multi-Agentic System is developed to assist people to help in doing automated or scheduling tasks, providing support to feel good while sharing their feelings, emotions, their life experiences, if having some bad thoughts or some positive thoughts, it can provide support in that. Basically, the obejctive behind developing this chatbot was to help people who feel low, or overwhelmed in their lives due to the bad life experiences they had in their life due to which they feel stress, have tensions & depression or anxiety problems.

## Project Members
1. Muhammad Usman - AI Software Enginner

## Project Tech-Stack & Deployment
### 1. Tech Stack
- The Project is developed using 
1. **React.js** & **TailwindCSS**
2. **React SpeechRecognition Library for Voice Input**
2. **MongoDB Atlas for Database**
3. **Python**
4. **CrewAI ** & **OpenAI Model**
5. **LangChain,LangGraph chaining, CrewAI-Tools for Agents inter communication and tool management and memory context for generating reposts and scheduling tasks, etc**, and **chromaDB as Vector Database for embeddings**.
### 2. Deployment
- The frontend is being deployed on [Vercel](https://vercel.com) using default build production.
- The backend is beinf deployed on [Railway](https://railway.com) using Docker containerization tool.

## Project Setup
### Backend
- goto backend folder using command: "**cd backend**"
- create the environment by the following command:
"**python -m venv env**"
- activate the environment using command: "**env\scripts\activate**" if using cmd in windows.
- if using powershell, then try using command: "**env\scripts\activate.ps1**" for activation of environment.
- install the mentioned dependencies mentioned in requirements.txt file by using the command: "**pip install -r requirements.txt**"
- create a file named "**.env**" and add your **OPENAI_API_KEY** & **MONGO_URL** in it.
- run the backend server by using command: "**uvicorn chatbot_api:app**"

### Frontend
- goto frontend folder using command: "**cd frontend**"
- install all the node modules by: "**npm i**"
- run the frontend server using command: "**npm run dev**"

### Database - MongoDB
- install mongoDB, if not installed
- connect mongoDB with the chatbot
- create variable **MONGO_URL** in .env with the mongoDB localhost URL.

#### Note: This Project is under MIT Licence. So, if anyone wants to add features or want to contribute, create a PR for your input and will be then merged if found useful. 
#### If found some issues in current release, please raise in issue and create a PR for it.

### Thank You Everyone! - enjoy 😁
