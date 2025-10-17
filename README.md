-----
## 🌟 Project Overview

This repository hosts the **Customized User Interface (UI)** for the **AI-GRC Assistant**. The interface is built using the Python library **Chainlit** and heavily customized to deliver a clean, professional, and compliant user experience (UX).

The project adheres to a **Microservices Architecture** by operating as a lightweight frontend client. Its sole responsibility is handling user interaction, sending queries to the designated backend API, and displaying the specialized RAG responses.

-----

## 🚀 Key Features and Customization

This project highlights advanced frontend and integration skills by adapting a standard framework to meet specific professional needs:

  * **Deep UI Customization:** Custom CSS (`stylesheet.css`) and JavaScript (`elements.js`) were implemented to align the chat interface with professional standards.
      * **Branding & Aesthetics:** Custom styling was applied to the assistant's avatar/logo (`emt.png`) and chat elements.
      * **UX Cleanup:** Unnecessary default platform elements, such as the "New Chat" button and system watermarks, were hidden using JavaScript for a distraction-free experience.
  * **Professional Configuration:** The `config.toml` file is precisely configured to manage session timeouts, specify custom assets, and control the display of advanced features.
  * **Decoupled API Integration:** The core application logic (`ui.py`) uses the `requests` library to seamlessly communicate with the external FastAPI backend, ensuring the interface remains fast and independent of the complex RAG processing.

-----

## ⚙️ Tech Stack and Integration

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **UI Framework** | **Chainlit** (Customized) | Core chatbot environment. |
| **Frontend Logic** | Python (`ui.py`) + `requests` | Handles user input and API communication. |
| **Custom Styling** | CSS, JavaScript, TOML Configuration | Defines the professional aesthetic and overrides default behavior. |
| **Backend Dependency** | **FastAPI API** (Hosted on Hugging Face Space) | Source of RAG-grounded, GRC compliance answers. |

### 🔗 Backend Service Link

All user queries are routed to the following live API endpoint:

  * **Target API Endpoint:** `https://grc2025-grc.hf.space/ask`
  * **Backend Repository:** [AI-GRC-Assistant-backend-2025 ([GitHub Link](https://github.com/MQushaym/AI-GRC-Assistant-backend-2025))]

-----

## 🛠️ Local Setup Guide

### 1\. Prerequisites

Ensure you have Python installed and install the required libraries:

```bash
pip install -r requirements.txt
```

### 2\. Execution

To run the custom frontend locally and connect it to the live backend service:

```bash
chainlit run ui.py
```

The application will launch in your browser, ready to query the remote RAG backend for compliance advice.

-----

## 🤝 Contact

| Detail | Information |
| :--- | :--- |
| **Author** | Meshal Qushaym |
| **Email** | meshalqushim@outlook.com |
| **GitHub Username** | MQushaym |

-----
