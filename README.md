

# AI Recipe Generator

The AI Recipe Generator is a fun and creative tool that generates cooking recipes based on user input. It leverages OpenAI's GPT-3.5-turbo model for text generation and DALL-E-2 for image synthesis. With this application, users can explore unique and imaginative recipes along with visually appealing images.

## Features

- **Recipe Generation**: Enter the name of a dish, and the AI will create a detailed cooking recipe for it.
- **Formatted Output**: The generated recipe follows a specific format, including headings, ingredients, and cooking steps.
- **Image Synthesis**: The application also generates an image related to the dish using DALL-E-2.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/MuhammadSalman-Kamran/AIRecipeGenerator-Deployment.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key by creating a `.env` file with the following content:

    ```
    OPENAI_API_KEY=your_api_key_here
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Enter the name of a dish (e.g., "Chicken Biryani") and click the "Create Recipe" button.
3. The AI will generate a recipe and display it along with an image related to the dish.

## Example Output

**Flavorful Chicken Biryani Recipe**

---

**Table Of Contents**:
- Links to the different sections of the recipe content.

**Introduction**:
- Briefly introduce the dish.

**Ingredients**:
- List of ingredients needed for the recipe.

**Cooking Steps**:
- Detailed instructions on how to prepare the dish.

**FAQ**:
- Answers to frequently asked questions related to the recipe.

---

## Acknowledgments

- This project uses OpenAI's GPT-3.5-turbo and DALL-E-2 models.
- Inspired by the creativity of AI-generated content.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
