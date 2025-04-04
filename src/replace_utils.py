import re
from llm_interface import generate_content

def replace_placeholders_in_doc(doc, user_data, job_description):
    placeholder_pattern = re.compile(r"{{[^{}]+}}")

    for para in doc.paragraphs:
        matches = placeholder_pattern.findall(para.text)
        if matches:
            new_text = para.text
            for placeholder in matches:
                print(f"🔍 Found placeholder: {placeholder}")
                generated = generate_content(placeholder, user_data, job_description).strip()
                new_text = new_text.replace(placeholder, generated)
            para.text = new_text.rstrip('\\n')  # Ensure no trailing newlines