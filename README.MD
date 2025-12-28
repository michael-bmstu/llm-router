# LLM Router

The Admissions Committee for the Master's Program in Artificial Intelligence receives numerous students with similar questions every day.

The questions are divided into four groups (topics):
- document submission (подача документов)
- entrance tests (входные испытания)
- curriculum and courses (учебный план и дисциплины)
- internships (стажировки)
- other (другое)

Each question group can have its own AI agent implemented.

This project is responsible for routing requests to the appropriate parts of the system.

## Project struct
- `main.py` : main program
- `router.py` : LLM router implementation with LangChain 
- `graph.py` :  application graph
- `.env` : enviroment varibales 
- `requirements.txt` : requirements for project launch
- `` : 
- `` : 