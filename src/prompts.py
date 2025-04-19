import json

def about_prompt(user_data, job_description):
    return f"""You are a professional CV writer.
Write a concise and compelling ABOUT section (a concise) tailored to this job description,
based on the candidate's profile. Keep it professional and 3-5 sentences max.

=== JOB DESCRIPTION ===
{job_description}

=== CANDIDATE PROFILE ===
{user_data}

For example, this would be a good output, if the job description is for a data analyst, and machine learning is listed as a requirement, and the candidates profile includes experience in data analysis and machine learning:

=== EXAMPLE OUTPUT ===
Business analytics student with proven expertise in data-driven decision-making, predictive modeling, and market analysis. Successfully applied machine learning and analytical skills to optimize customer retention strategies, develop actionable insights, and streamline operations in gaming, entertainment, and NGO sectors. Strong communicator adept at translating complex data into clear, strategic recommendations that drive measurable business impact.

remarks:
Try to match the style and length of the example output. Also, make sure to include the most relevant skills and experiences from the candidate's profile. Please double check that the output is not too long, and that it is not too short. The output should be a good summary of the candidate's profile, and it should be tailored to the job description. The output should be in a professional tone, and it should be easy to read and understand.
Make sure that everything you write is relevant to the job description, and included in the provided candidate's profile. 
"""

def experience_prompt(experience_entry, job_description):
    return f"""You are a CV-writing assistant.
Using the following job description and experience entry, rewrite the experience bullet points to better match the job requirements.
Keep the output in 2 concise and effective bullet points.
please create the bullet points using the CAR Method (Challenge, Action, Result), and starting with an action word.

this is an example of the CAR method, IT IS IMPORTANT TO FOLLOW THIS EXAMPLE, also just use "• " as the bullet point, and do not use any other character nor tabulation:
=== EXAMPLE OUTPUT ===
• Collaborated with an external ONG company, successfully bridging academic expertise and real-world business challenges through data-driven analysis and innovative solutions.

=== JOB DESCRIPTION ===
{job_description}

=== EXPERIENCE ===
{experience_entry}

remarks:
Try to match the style and length of the example output. Also, make sure to include the most relevant skills and experiences from the candidate's profile. please only output the bullet points, and do not include any other text. 
"""

def courses_prompt(courses_list, job_description):
    return f"""You are a CV optimization assistant.
From the following list of academic courses, choose and return the 8 most relevant courses to the job description provided.
Do not explain or comment — just return the course names in a comma-separated list.

=== JOB DESCRIPTION ===
{job_description}

=== COURSES ===
{courses_list}
"""

def skills_prompt(skills_data, job_description):
    skill_type = skills_data
    prompt = f"""You are a CV optimization assistant.
Take the following list of technical skills and tools, choose the most relevant items of the list based on the job description.
Return them in the following format (just a list of words separated by commas, no other text or brackets):
do not just select the ones that are explicitly mentioned in the job description, but also the ones that are related to the job description. 
so it's not a matter of reducing the number of items, but rather selecting the most relevant ones, and ordering them accordingly. remove skills that you feel may hurt the candidate's chances of getting the job.
Do not include any other text, and do not include any other characters or tabulation.
Do not explain or comment — just return the words in a comma-separated list.
Make absolutely sure that the output is only words that are present in the skills data provided, and that the output is not too long, and that it is not too short.

=== JOB DESCRIPTION ===
{job_description}

=== SKILLS DATA ===
{skills_data}
"""
    return prompt

def cover_letter_prompt(user_data, job_description):
    return f"""You are a professional CV writer.
Write a concise and compelling cover letter tailored to this job description, based on the following candidate's profile. Keep it professional and follo the provided structure:

=== STRUCTURE ===
1st Paragraph – Introduction (3/4 lines)
 Answer to: Who are you? What are you doing now? What are you looking to do in the near future?
e.g. “My name is Anna, I am currently in the second year of my Bachelor in Economics at Nova School of Business and Economics, and through my studies I have become increasingly interested in the Sales and Marketing areas, within which I would like to further my knowledge and practical experiences.“

2nd Paragraph – Motivation (5/6 lines)
 Answer to: Why are you interested specifically in this Job Role? And why this particular Organisation?

3rd / 4th Paragraph – Showcase Alignment, focusing on skills (5/6 lines each paragraph)
 Answer to: Why should this Organisation hire you?
e.g. “The teamwork skills I developed as a student at Nova SBE, have allowed me to establish positive and efficient work relationships with people from various backgrounds, which could prove valuable in [OrganisationName]'s worldwide implementation projects.”

Last Paragraph – Conclusion (3/4 lines)
 Answer to: Thank the reader, reaffirm your interest, end with a call to action.
e.g. “Thank you for taking the time to consider my application. The prospect of contributing to [CompanyName] truly excites me, since my passion for [SpecificCharacteristic] aligns seamlessly with [CompanyName]’s vision. In this sense, I would be happy to further discuss my background and relevant achievements with you in an interview.”

Complimentary Close: “Sincerely,” / “Best Regards,” / “Yours Respectfully,”

=== JOB DESCRIPTION ===
{job_description}

=== CANDIDATE PROFILE ===
{user_data}
"""
    
def main():
    with open("data/profile.json", "r") as f:
        profile = json.load(f)

    with open("data/job_description.txt", "r") as f:
        job_description = f.read()
        
    print("about")
    print(about_prompt(profile, job_description))
    print("experience")
    print(experience_prompt(profile["experience"][0], job_description, 1))
    print("courses")
    print(courses_prompt(profile["education"][0]["courses"], job_description))
    print("skills")
    print(skills_prompt(profile["skills"]))
    print("=== END ===")
    

if __name__ == "__main__":
    main()