# cv_optimizer

An LLM-based cv optimization tool

## Usage

1. Install requirements.txt

    ```bash
    pip install -r requirements.txt
    ```

2. rename the following files removing .profile in the file name:
    - job_description.template.txt (becomes job_description.txt)
    - profile.template.json (becomes profile.json)
    - cv_template.template.docx (becomes.cv_template.template.docx)

3. rewrite the same three files with the desired information: your profile, target job description etc.
    > keep in mind that longer and more detailed prompts tend to generate better results. so it's key to take the time to write as much as possible inside the json

4. run `main.py`

5. the script will create a word file (cv_final.docx) with your cv taylored for the job description. 

6. Make sure to look over the LLM-generated content, you and only you are responsible for misleading and/or information in your CV.

## License

This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.
