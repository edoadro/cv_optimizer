import json
import os
import google.generativeai as genai
import ollama
from prompts import about_prompt, experience_prompt, courses_prompt, skills_prompt

# Configuration: Choose "gemini" or "ollama"
LLM_BACKEND = os.getenv("LLM_BACKEND", "ollama")  # default is ollama

# === Setup Gemini ===
if LLM_BACKEND == "gemini":
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    gemini_model = genai.GenerativeModel("gemini-2.0-flash-lite")

# === Setup Ollama ===
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1")  

def call_llm(prompt: str):
    if LLM_BACKEND == "gemini":
        response = gemini_model.generate_content(prompt)
        return response.text

    elif LLM_BACKEND == "ollama":
        try:
            response = ollama.chat(model=OLLAMA_MODEL, messages=[{'role': 'user', 'content': prompt}])
            return response['message']['content']
        except Exception as e:
            raise RuntimeError(f"Error calling Ollama: {e}")
    else:   
        raise ValueError("Invalid LLM_BACKEND. Must be 'gemini' or 'ollama'.")

def generate_content(placeholder, user_data, job_description):
    prompt_map = {
        "{{about}}": "about",
        "{{exp1}}": "experience",
        "{{exp2}}": "experience",
        "{{exp3}}": "experience",
        "{{courses1}}": "courses",
        "{{courses2}}": "courses",
        "{{software}}": "skills",
        "{{libraries}}": "skills",
        "{{tech}}": "skills",
    }

    section_type = prompt_map.get(placeholder)

    if section_type == "about":
        prompt = about_prompt(user_data, job_description)
        return call_llm(prompt)

    elif section_type == "experience":
        index = int(placeholder[-3]) - 1
        prompt = experience_prompt(user_data["experience"][index], job_description)
        return call_llm(prompt)

    elif section_type == "courses":
        index = int(placeholder[-3]) - 1
        prompt = courses_prompt(user_data["education"][index]["courses"], job_description)
        return call_llm(prompt)

    elif section_type == "skills":
        prompt = skills_prompt(user_data["skills"][placeholder[2:-2]], job_description)
        return call_llm(prompt)

    else:
        return "error: unknown placeholder"

def main():
    with open("data/profile.json") as f:
        user_data = json.load(f)

    with open("data/job_description.txt") as f:
        job_description = f.read()

    print("Using backend:", LLM_BACKEND)

    print("\nAbout Section:")
    print(generate_content("{{about}}", user_data, job_description))

    print("\nExperience Section:")
    print(generate_content("{{exp1}}", user_data, job_description))

    print("\nCourses Section:")
    print(generate_content("{{courses1}}", user_data, job_description))

    print("\nSkills Section:")
    print(generate_content("{{software}}", user_data, job_description))

if __name__ == "__main__":
    main()