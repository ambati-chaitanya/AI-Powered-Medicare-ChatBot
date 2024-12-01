# AI-Powered Medicare Chatbot

## Overview
The **AI-Powered Medicare Chatbot** is designed to assist users with Medicare-related queries. Leveraging advanced technologies like Natural Language Processing (NLP), Machine Learning (ML), and knowledge graphs, this chatbot simplifies user interactions by providing instant and accurate responses. The project also includes features for handling image, PDF, and CSV inputs for enhanced user assistance.

## Features
- **Natural Language Understanding:** Processes user queries in natural language.
- **Document Analysis:** Extracts information from uploaded documents like Medicare cards and receipts.
- **CSV Data Handling:** Analyzes Medicare costs, provider rates, and drug formulary data.
- **PDF Text Summarization:** Extracts and summarizes key information.
- **Image Recognition:** Identifies medical equipment and prescriptions from images.

## Tools and Technologies
- **NLP:** For understanding and responding to user queries.
- **Machine Learning:** Improves responses over time using user interactions.
- **Knowledge Graphs:** Stores structured Medicare policy information.
- **Cloud Computing:** Provides scalability for handling high traffic.
- **Streamlit:** Creates the web interface.
- **LangChain:** Manages chains and vector stores.
- **Google Generative AI:** Powers the conversational model.
- **PandasAI & Matplotlib:** Facilitates CSV-based data analysis and visualization.
- **PyPDF2:** Extracts text from PDF documents.
- **Pillow:** Handles image uploads.

## Repository Structure
```plaintext
├── assets
│   ├── images
│   │   ├── chatbot_demo.png
│   │   ├── pdf_detection_example.png
│   │   ├── image_recognition_example.png
├── src
│   ├── app.py               # Main Streamlit app
│   ├── pdf_processor.py     # Handles PDF extraction
│   ├── image_processor.py   # Handles image recognition
│   ├── chatbot_logic.py     # Core chatbot logic
├── requirements.txt         # Required Python libraries
├── .env                     # Environment variables (e.g., API keys)
├── README.md                # Project description and instructions
```

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-powered-medicare-chatbot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ai-powered-medicare-chatbot
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add API keys and environment variables to `.env`.
5. Run the application:
   ```bash
   streamlit run src/app.py
   ```

## Screenshots

### Chatbot Interface
![WhatsApp Image 2024-10-14 at 15 56 01_70a54796](https://github.com/user-attachments/assets/5c60c550-5f52-4722-ac57-5b219105dbe9)

![WhatsApp Image 2024-10-14 at 15 56 02_879de028](https://github.com/user-attachments/assets/b6522410-ee19-4990-8bb9-bec1744f7aef)

![WhatsApp Image 2024-10-14 at 15 56 02_b1375e8e](https://github.com/user-attachments/assets/5455baf2-237b-4f58-bfd9-c94a8d21c1c9)


### PDF Detection Interface
![WhatsApp Image 2024-10-14 at 15 56 03_a35c1e4e](https://github.com/user-attachments/assets/9eb537f9-8b5c-49c7-b5e9-4cdf0b6493ce)

![WhatsApp Image 2024-10-14 at 15 56 03_91c0e5f6](https://github.com/user-attachments/assets/efa5fd43-9d59-4bc8-9438-497444c44ab3)

### CSV Recognition Interface
![WhatsApp Image 2024-10-14 at 15 56 03_02af4ca0](https://github.com/user-attachments/assets/e0a9e89f-5de3-45d0-a2fe-368322e67074)


### Image Recognition Interface
![WhatsApp Image 2024-10-14 at 15 56 04_125c8482](https://github.com/user-attachments/assets/7332a566-a93f-4cee-bb93-a9b280e78514)

### Example
![WhatsApp Image 2024-11-27 at 16 33 05_9623dd26](https://github.com/user-attachments/assets/d85feb72-82f3-43a6-9d85-3ca7e262093e)

![WhatsApp Image 2024-11-27 at 16 33 05_88b4d165](https://github.com/user-attachments/assets/e2913c13-0f6f-4234-a98f-0a8072374e57)

![WhatsApp Image 2024-11-27 at 16 33 06_58ad5a61](https://github.com/user-attachments/assets/ef9781ec-9df3-4018-9000-bde8096b55a0)

![WhatsApp Image 2024-11-27 at 16 33 06_475b1188](https://github.com/user-attachments/assets/6d4b9d7e-3751-45a6-a3e3-8ed6acfde607)

![WhatsApp Image 2024-11-27 at 16 33 07_50e4eaa5](https://github.com/user-attachments/assets/5674db8c-67b2-4257-b574-cce6893d19c4)


## Team Members
- **Gone Guna Sathwika** (21BCE9510)
- **Chowdam Sreenivasulu** (21BCE9848)
- **Uppada Mahesh Srinivas** (21BCE9465)
- **Ambati Sri Chaitanya** (21BCE9543)

