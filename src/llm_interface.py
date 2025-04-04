import json
import os
import google.generativeai as genai
from prompts import about_prompt, experience_prompt, courses_prompt, skills_prompt

# Initialize Gemini with API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash-lite")

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
        index = int(placeholder[-3]) - 1  # -2 to get the number inside {{exp1}}, etc.
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

def call_llm(prompt: str):
    response = model.generate_content(prompt)
    return response.text

def main():
    with open("data/profile.json") as f:
        user_data = json.load(f)

    with open("data/job_description.txt") as f:
        job_description = f.read()

    print("About Section:")
    print(generate_content("{{about}}", user_data, job_description))

    print("\nExperience Section:")
    print(generate_content("{{exp1}}", user_data, job_description))

    print("\nCourses Section:")
    print(generate_content("{{courses1}}", user_data, job_description))

    print("\nSkills Section:")
    print(generate_content("{{software}}", user_data, job_description))

if __name__ == "__main__":
    main()