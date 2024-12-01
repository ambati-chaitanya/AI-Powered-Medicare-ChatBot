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
![WhatsApp Image 2024-10-14 at 15 56 01_3465c50d](https://github.com/user-attachments/assets/dda1e113-65ad-4b7f-b895-a50539edcd62)

![WhatsApp Image 2024-10-14 at 15 56 02_17a0e3c7](https://github.com/user-attachments/assets/76f2ca89-0079-4bbd-9e27-6748f8f988b3)

![WhatsApp Image 2024-10-14 at 15 56 02_edbb7a06](https://github.com/user-attachments/assets/691a38b8-d29f-4dee-b996-ed16de5cf171)


### PDF Detection Interface
![WhatsApp Image 2024-10-14 at 15 56 03_aa143bf4](https://github.com/user-attachments/assets/7d6073dd-6418-49cc-92cd-72d8d9f1a954)

![WhatsApp Image 2024-10-14 at 15 56 03_2961561f](https://github.com/user-attachments/assets/36bdf0eb-208f-4cc0-8203-a36b4e874897)


### CSV Recognition Interface
![WhatsApp Image 2024-10-14 at 15 56 03_7105d476](https://github.com/user-attachments/assets/6540b6c9-24eb-4f21-aa93-ca3649c8dfb5)

### Image Recognition Interface
![WhatsApp Image 2024-10-14 at 15 56 04_2b23ad0f](https://github.com/user-attachments/assets/32bae964-58a8-40a0-b0c0-708d6fc72aa3)

### Chat Interface
![WhatsApp Image 2024-10-14 at 15 56 04_81de2103](https://github.com/user-attachments/assets/f69d0256-694d-48ee-8d83-e5fc82531d77)


### Example
![WhatsApp Image 2024-11-27 at 16 33 06_123d76fe](https://github.com/user-attachments/assets/4adbb1b2-0ee3-4391-bd02-2f37910d4cdb)

![WhatsApp Image 2024-11-27 at 16 33 06_3e1549cd](https://github.com/user-attachments/assets/19763ba6-53e9-4c1f-8da6-8923b757710f)

![WhatsApp Image 2024-11-27 at 16 33 06_0ab57df0](https://github.com/user-attachments/assets/7c80e793-a54e-4076-9dd2-12ff31621ccc)

![WhatsApp Image 2024-11-27 at 16 33 05_7b7a1003](https://github.com/user-attachments/assets/e6651d51-e37d-4309-be7a-656938d0813a)

![WhatsApp Image 2024-11-27 at 16 33 05_a1be8900](https://github.com/user-attachments/assets/058a9aa9-924f-43c4-8e20-72ece04528cf)

![WhatsApp Image 2024-11-27 at 16 33 07_8fd628ec](https://github.com/user-attachments/assets/6e68555e-726a-436c-806e-548107ac110b)


## Team Members
- **Gone Guna Sathwika** (21BCE9510)
- **Chowdam Sreenivasulu** (21BCE9848)
- **Uppada Mahesh Srinivas** (21BCE9465)
- **Ambati Sri Chaitanya** (21BCE9543)

