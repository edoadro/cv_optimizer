# CV Optimizer

An LLM-based CV optimization tool.

## Make an Informed Decision About Your LLM

To run this script, you will need access to a Large Language Model (LLM).

This tool allows users to choose between two options:

- `Ollama`, which runs local models on your machine.
- Google's `Gemini API`, which interfaces with cloud-based models via Google's servers.

From a privacy-oriented perspective, running a model locally is preferable, as your data never leaves your machine. However, Ollama can be challenging to install for some users, and local LLMs are computationally demanding, which means you may need powerful hardware to get good results. For example the 'lightest' model that I was able to get decent results with was `phi4` (9.1 GB)

For a more accessible alternative, you can use Google's Generative AI framework. If you choose this option, you’ll need a Google account. Visit Google’s [AI Studio](https://aistudio.google.com/welcome) to retrieve your API key.

Refer to the [Usage](#usage) section below for a detailed setup guide.

---

## Usage

> This usage guide is beginner-friendly, with minimal assumptions about Python experience.

### Step-by-step Guide

1. **Clone this repository** to your machine (or [download the zip](https://github.com/your-repo-link)):

    ```bash
    git clone <put-repository-link>
    ```

2. **Create a virtual environment** (optional, but recommended):

    > A [virtual environment](https://python.land/virtual-environments/virtualenv) helps isolate dependencies and keeps your system clean.  
    > It also makes it easier to manage environment variables in the next step.

3. **Create the environment variables**:

    Choose between `ollama` and `gemini`. If you're unsure, review the section above for guidance.

    **Ollama setup**:

    ```bash
    export LLM_BACKEND="ollama"
    export OLLAMA_MODEL="llama3.1"  # Or the local model of your choice
    ```

    **Gemini setup**:

    ```bash
    export LLM_BACKEND="gemini"
    export GEMINI_API_KEY="your-api-key"
    ```

4. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Rename the following template files** by removing `.template` from their filenames:
    - `job_description.template.txt` → `job_description.txt`
    - `profile.template.json` → `profile.json`
    - `cv_template.template.docx` → `cv_template.docx`

6. **Edit the renamed files** with your personal information and target job details:
    > Be as detailed as possible — longer and more informative prompts tend to produce higher-quality LLM outputs.

7. **Run the script**:

    ```bash
    python main.py
    ```

8. **The output** will be a Word document named `cv_final.docx`, customized for the job description you provided.

9. **Review the generated CV carefully**:
    > You, and only you, are responsible for ensuring the accuracy and honesty of the information presented in your CV.

---

## License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.
